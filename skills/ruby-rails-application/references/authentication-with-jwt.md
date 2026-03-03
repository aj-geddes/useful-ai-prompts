# Authentication with JWT

## Authentication with JWT

```ruby
# app/controllers/application_controller.rb
class ApplicationController < ActionController::API
  include ActionController::Cookies

  SECRET_KEY = Rails.application.secrets.secret_key_base

  def encode_token(user_id)
    payload = { user_id: user_id, exp: 24.hours.from_now.to_i }
    JWT.encode(payload, SECRET_KEY, 'HS256')
  end

  def decode_token(token)
    begin
      JWT.decode(token, SECRET_KEY, true, { algorithm: 'HS256' })
    rescue JWT::ExpiredSignature, JWT::DecodeError
      nil
    end
  end

  def authenticate_request
    header = request.headers['Authorization']
    token = header.split(' ').last if header.present?

    decoded = decode_token(token)
    if decoded
      @current_user_id = decoded[0]['user_id']
      @current_user = User.find(@current_user_id)
    else
      render json: { error: 'Unauthorized' }, status: :unauthorized
    end
  end

  def current_user
    @current_user
  end

  def logged_in?
    current_user.present?
  end
end

# config/routes.rb
Rails.application.routes.draw do
  namespace :api do
    namespace :v1 do
      post 'auth/login', to: 'auth#login'
      post 'auth/register', to: 'auth#register'

      resources :users
      resources :posts do
        member do
          patch :publish
        end
        resources :comments, only: [:index, :create, :destroy]
      end
    end
  end
end
```
