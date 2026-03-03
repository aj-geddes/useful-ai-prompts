# Ruby with Sidekiq

## Ruby with Sidekiq

```ruby
# Gemfile
gem 'sidekiq', '~> 7.0'
gem 'redis'
gem 'sidekiq-scheduler'

# config/sidekiq.yml
---
:redis:
  :url: redis://localhost:6379/0
:concurrency: 5
:timeout: 25
:max_retries: 3
:dead_letter_queue:
  :enabled: true
  :queue_name: dead_letter_queue

# app/workers/email_worker.rb
class EmailWorker
  include Sidekiq::Worker
  sidekiq_options queue: 'emails', retry: 3, lock: :until_executed

  def perform(user_id, subject)
    user = User.find(user_id)
    UserMailer.send_email(user, subject).deliver_now

    logger.info "Email sent to user #{user_id}"
  rescue StandardError => e
    logger.error "Failed to send email: #{e.message}"
    raise
  end
end

# app/workers/report_worker.rb
class ReportWorker
  include Sidekiq::Worker
  sidekiq_options queue: 'reports', retry: 2

  def perform(report_type, filters)
    total_records = Record.filter_by(filters).count
    processed = 0

    Record.filter_by(filters).find_in_batches(batch_size: 1000) do |batch|
      process_batch(batch, report_type)
      processed += batch.size

      # Update progress
      Sidekiq.redis { |conn|
        conn.hset("job:#{jid}", 'progress', (processed.to_f / total_records * 100).round(2))
      }
    end

    logger.info "Report #{report_type} generated"
    { status: 'success', total_records: total_records }
  end
end

# app/controllers/tasks_controller.rb
class TasksController < ApplicationController
  def send_email
    user_id = params[:user_id]
    subject = params[:subject]

    job_id = EmailWorker.perform_async(user_id, subject)
    render json: { job_id: job_id }, status: :accepted
  end

  def job_status
    job_id = params[:job_id]
    status = Sidekiq::Status.get(job_id)

    render json: {
      job_id: job_id,
      status: status || 'not_found'
    }
  end
end

# Scheduled jobs (lib/tasks/scheduler.rake or config/sidekiq.yml)
sidekiq_scheduler:
  cleanup_expired_sessions:
    cron: '0 */6 * * *'
    class: CleanupSessionsWorker
  generate_daily_report:
    cron: '0 0 * * *'
    class: DailyReportWorker
```
