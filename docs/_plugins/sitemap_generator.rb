# Enhanced Sitemap Generator for Jekyll
# Generates comprehensive XML sitemaps with priority and frequency settings

module Jekyll
  class SitemapGenerator < Generator
    safe true
    priority :high

    def generate(site)
      # Main sitemap
      generate_main_sitemap(site)
      
      # Category-specific sitemaps
      generate_category_sitemaps(site)
      
      # Sitemap index
      generate_sitemap_index(site)
    end

    private

    def generate_main_sitemap(site)
      sitemap = SitemapFile.new(site, site.source, '', 'sitemap.xml')
      sitemap.data = {
        'layout' => nil,
        'entries' => []
      }

      # Add home page
      sitemap.data['entries'] << {
        'url' => site.config['url'] + site.config['baseurl'] + '/',
        'lastmod' => Time.now.strftime('%Y-%m-%d'),
        'changefreq' => 'weekly',
        'priority' => '1.0'
      }

      # Add category pages
      site.collections['categories'].docs.each do |category|
        sitemap.data['entries'] << {
          'url' => site.config['url'] + category.url,
          'lastmod' => category.data['date'] ? category.data['date'].strftime('%Y-%m-%d') : Time.now.strftime('%Y-%m-%d'),
          'changefreq' => 'weekly',
          'priority' => '0.8'
        }
      end

      # Add prompt pages with dynamic priority
      site.collections['prompts'].docs.each do |prompt|
        # Calculate priority based on prompt metadata
        priority = calculate_prompt_priority(prompt)
        
        sitemap.data['entries'] << {
          'url' => site.config['url'] + prompt.url,
          'lastmod' => prompt.data['date'] ? prompt.data['date'].strftime('%Y-%m-%d') : Time.now.strftime('%Y-%m-%d'),
          'changefreq' => 'monthly',
          'priority' => priority.to_s
        }
      end

      # Add static pages
      site.pages.each do |page|
        next if page.name == 'sitemap.xml'
        next if page.name.start_with?('404')
        next if page.data['sitemap'] == false
        
        sitemap.data['entries'] << {
          'url' => site.config['url'] + page.url,
          'lastmod' => page.data['date'] ? page.data['date'].strftime('%Y-%m-%d') : Time.now.strftime('%Y-%m-%d'),
          'changefreq' => page.data['changefreq'] || 'monthly',
          'priority' => page.data['priority'] || '0.6'
        }
      end

      site.pages << sitemap
    end

    def generate_category_sitemaps(site)
      # Group prompts by category
      categories = site.collections['prompts'].docs.group_by { |prompt| prompt.data['category'] }
      
      categories.each do |category_name, prompts|
        sitemap = SitemapFile.new(site, site.source, '', "sitemap-#{category_name}.xml")
        sitemap.data = {
          'layout' => nil,
          'category' => category_name,
          'entries' => []
        }

        prompts.each do |prompt|
          priority = calculate_prompt_priority(prompt)
          
          sitemap.data['entries'] << {
            'url' => site.config['url'] + prompt.url,
            'lastmod' => prompt.data['date'] ? prompt.data['date'].strftime('%Y-%m-%d') : Time.now.strftime('%Y-%m-%d'),
            'changefreq' => 'monthly',
            'priority' => priority.to_s,
            'category' => category_name,
            'tags' => prompt.data['tags'] || []
          }
        end

        site.pages << sitemap
      end
    end

    def generate_sitemap_index(site)
      index = SitemapIndexFile.new(site, site.source, '', 'sitemap-index.xml')
      index.data = {
        'layout' => nil,
        'sitemaps' => []
      }

      # Add main sitemap
      index.data['sitemaps'] << {
        'url' => site.config['url'] + site.config['baseurl'] + '/sitemap.xml',
        'lastmod' => Time.now.strftime('%Y-%m-%d')
      }

      # Add category sitemaps
      categories = site.collections['prompts'].docs.map { |prompt| prompt.data['category'] }.uniq
      categories.each do |category|
        index.data['sitemaps'] << {
          'url' => site.config['url'] + site.config['baseurl'] + "/sitemap-#{category}.xml",
          'lastmod' => Time.now.strftime('%Y-%m-%d')
        }
      end

      site.pages << index
    end

    def calculate_prompt_priority(prompt)
      base_priority = 0.7
      
      # Boost priority for prompts with more metadata
      boost = 0.0
      boost += 0.1 if prompt.data['tags'] && prompt.data['tags'].length > 3
      boost += 0.1 if prompt.data['compatible_models'] && prompt.data['compatible_models'].length > 2
      boost += 0.1 if prompt.data['use_cases'] && prompt.data['use_cases'].length > 2
      boost += 0.05 if prompt.data['examples']
      boost += 0.05 if prompt.data['tips']
      
      # Popular categories get slight boost
      popular_categories = ['technical-workflows', 'management-leadership', 'business-workflows']
      boost += 0.05 if popular_categories.include?(prompt.data['category'])
      
      [base_priority + boost, 0.9].min.round(1)
    end
  end

  class SitemapFile < Page
    def initialize(site, base, dir, name)
      @site = site
      @base = base
      @dir = dir
      @name = name

      self.process(@name)
      self.read_yaml(File.join(base, '_layouts'), 'sitemap.xml')
    end
  end

  class SitemapIndexFile < Page
    def initialize(site, base, dir, name)
      @site = site
      @base = base
      @dir = dir
      @name = name

      self.process(@name)
      self.read_yaml(File.join(base, '_layouts'), 'sitemap-index.xml')
    end
  end
end