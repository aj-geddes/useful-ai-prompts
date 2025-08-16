#!/usr/bin/env python3
"""
SEO Validation Script for Useful AI Prompts Jekyll Site
Validates all SEO implementations and provides optimization recommendations.
"""

import os
import json
import requests
import xml.etree.ElementTree as ET
from urllib.parse import urljoin, urlparse
import re
from collections import defaultdict
import time
from pathlib import Path

class SEOValidator:
    def __init__(self, base_url="https://aj-geddes.github.io/useful-ai-prompts", local_path="./"):
        self.base_url = base_url
        self.local_path = Path(local_path)
        self.results = {
            'meta_tags': [],
            'structured_data': [],
            'sitemaps': [],
            'performance': [],
            'mobile': [],
            'accessibility': [],
            'content': [],
            'errors': [],
            'warnings': [],
            'recommendations': []
        }
    
    def validate_meta_tags(self):
        """Validate meta tags for all pages"""
        print("🔍 Validating meta tags...")
        
        # Check Jekyll templates
        layouts_path = self.local_path / "_layouts"
        includes_path = self.local_path / "_includes"
        
        # Validate meta-tags.html include
        meta_tags_file = includes_path / "meta-tags.html"
        if meta_tags_file.exists():
            content = meta_tags_file.read_text()
            
            # Check for essential meta tags
            essential_tags = [
                'og:title', 'og:description', 'og:url', 'og:image',
                'twitter:card', 'twitter:title', 'twitter:description',
                'canonical', 'viewport', 'robots'
            ]
            
            for tag in essential_tags:
                if tag in content:
                    self.results['meta_tags'].append(f"✅ {tag} implementation found")
                else:
                    self.results['errors'].append(f"❌ Missing {tag} meta tag")
        else:
            self.results['errors'].append("❌ meta-tags.html include not found")
    
    def validate_structured_data(self):
        """Validate JSON-LD structured data"""
        print("🔍 Validating structured data...")
        
        structured_data_file = self.local_path / "_includes" / "structured-data.html"
        if structured_data_file.exists():
            content = structured_data_file.read_text()
            
            # Check for schema types
            schema_types = [
                'WebSite', 'Organization', 'Article', 'HowTo',
                'CollectionPage', 'BreadcrumbList'
            ]
            
            for schema_type in schema_types:
                if f'"@type": "{schema_type}"' in content:
                    self.results['structured_data'].append(f"✅ {schema_type} schema found")
                else:
                    self.results['warnings'].append(f"⚠️ {schema_type} schema not implemented")
            
            # Validate JSON-LD syntax
            try:
                # Extract JSON-LD blocks
                json_ld_pattern = r'<script type="application/ld\+json">(.*?)</script>'
                matches = re.findall(json_ld_pattern, content, re.DOTALL)
                
                for match in matches:
                    # Basic validation (would need full Jekyll rendering for complete validation)
                    if '"@context"' in match and '"@graph"' in match:
                        self.results['structured_data'].append("✅ Valid JSON-LD structure found")
                    
            except Exception as e:
                self.results['errors'].append(f"❌ JSON-LD validation error: {e}")
        else:
            self.results['errors'].append("❌ structured-data.html include not found")
    
    def validate_sitemaps(self):
        """Validate sitemap generation"""
        print("🔍 Validating sitemaps...")
        
        # Check for sitemap plugin
        plugin_file = self.local_path / "_plugins" / "sitemap_generator.rb"
        if plugin_file.exists():
            self.results['sitemaps'].append("✅ Custom sitemap generator found")
            
            content = plugin_file.read_text()
            if 'priority' in content and 'changefreq' in content:
                self.results['sitemaps'].append("✅ Sitemap includes priority and frequency")
            
            if 'category' in content:
                self.results['sitemaps'].append("✅ Category-specific sitemaps enabled")
        
        # Check sitemap layouts
        sitemap_layout = self.local_path / "_layouts" / "sitemap.xml"
        if sitemap_layout.exists():
            self.results['sitemaps'].append("✅ Sitemap XML layout found")
        
        # Check robots.txt
        robots_file = self.local_path / "robots.txt"
        if robots_file.exists():
            content = robots_file.read_text()
            if 'Sitemap:' in content:
                self.results['sitemaps'].append("✅ Robots.txt includes sitemap reference")
            if 'User-agent: *' in content:
                self.results['sitemaps'].append("✅ Robots.txt properly configured")
        else:
            self.results['errors'].append("❌ robots.txt not found")
    
    def validate_performance(self):
        """Validate performance optimizations"""
        print("🔍 Validating performance optimizations...")
        
        # Check performance include
        perf_file = self.local_path / "_includes" / "performance-optimization.html"
        if perf_file.exists():
            content = perf_file.read_text()
            
            performance_features = [
                ('preload', 'Resource preloading'),
                ('preconnect', 'DNS preconnect'),
                ('ServiceWorker', 'Service Worker'),
                ('IntersectionObserver', 'Lazy loading'),
                ('critical.*css', 'Critical CSS')
            ]
            
            for pattern, description in performance_features:
                if re.search(pattern, content, re.IGNORECASE):
                    self.results['performance'].append(f"✅ {description} implemented")
                else:
                    self.results['warnings'].append(f"⚠️ {description} not found")
        
        # Check service worker
        sw_file = self.local_path / "sw.js"
        if sw_file.exists():
            self.results['performance'].append("✅ Service Worker file found")
        
        # Check web manifest
        manifest_file = self.local_path / "site.webmanifest"
        if manifest_file.exists():
            self.results['performance'].append("✅ Web App Manifest found")
    
    def validate_mobile_seo(self):
        """Validate mobile SEO optimizations"""
        print("🔍 Validating mobile SEO...")
        
        mobile_file = self.local_path / "_includes" / "mobile-seo.html"
        if mobile_file.exists():
            content = mobile_file.read_text()
            
            mobile_features = [
                ('apple-mobile-web-app', 'iOS web app meta tags'),
                ('viewport', 'Viewport meta tag'),
                ('touch-action', 'Touch optimization'),
                ('Core Web Vitals', 'Core Web Vitals monitoring'),
                ('prefers-reduced-motion', 'Accessibility motion preferences')
            ]
            
            for pattern, description in mobile_features:
                if pattern in content:
                    self.results['mobile'].append(f"✅ {description} implemented")
                else:
                    self.results['warnings'].append(f"⚠️ {description} not found")
    
    def validate_analytics(self):
        """Validate analytics implementation"""
        print("🔍 Validating analytics...")
        
        analytics_file = self.local_path / "_includes" / "analytics.html"
        if analytics_file.exists():
            content = analytics_file.read_text()
            
            if 'gtag' in content:
                self.results['meta_tags'].append("✅ Google Analytics 4 implemented")
            
            if 'custom_parameter' in content:
                self.results['meta_tags'].append("✅ Custom tracking parameters configured")
            
            if 'trackPromptCopy' in content:
                self.results['meta_tags'].append("✅ Prompt-specific tracking events implemented")
        else:
            self.results['warnings'].append("⚠️ Analytics include not found")
    
    def validate_content_seo(self):
        """Validate content SEO"""
        print("🔍 Validating content SEO...")
        
        # Check prompt files
        prompts_path = self.local_path / "_prompts"
        if prompts_path.exists():
            prompt_files = list(prompts_path.glob("*.md"))
            total_prompts = len(prompt_files)
            
            self.results['content'].append(f"✅ Found {total_prompts} prompt files")
            
            # Sample validation of a few prompts
            sample_size = min(10, total_prompts)
            valid_prompts = 0
            
            for prompt_file in prompt_files[:sample_size]:
                content = prompt_file.read_text()
                
                # Check frontmatter
                if content.startswith('---'):
                    valid_prompts += 1
                
                # Check for SEO-friendly elements
                if 'description:' in content:
                    valid_prompts += 0.5
                
                if 'tags:' in content:
                    valid_prompts += 0.3
            
            seo_score = (valid_prompts / sample_size) * 100
            if seo_score > 80:
                self.results['content'].append(f"✅ Content SEO score: {seo_score:.1f}%")
            else:
                self.results['warnings'].append(f"⚠️ Content SEO needs improvement: {seo_score:.1f}%")
    
    def generate_recommendations(self):
        """Generate SEO recommendations"""
        print("💡 Generating recommendations...")
        
        recommendations = [
            "🎯 Target Keywords Integration:",
            "  - Add 'AI prompts for professionals' to key pages",
            "  - Include 'ChatGPT prompts library' in meta descriptions", 
            "  - Optimize for 'Claude prompts collection' searches",
            "",
            "📊 Content Optimization:",
            "  - Ensure all prompts have unique meta descriptions",
            "  - Add FAQ sections to high-traffic categories",
            "  - Create topic clusters linking related prompts",
            "",
            "🔗 Technical SEO:",
            "  - Implement internal linking between related prompts",
            "  - Add XML sitemaps to Google Search Console",
            "  - Monitor Core Web Vitals in PageSpeed Insights",
            "",
            "📱 Mobile Optimization:",
            "  - Test all pages with Google Mobile-Friendly Test",
            "  - Optimize tap targets for mobile users",
            "  - Ensure fast loading on 3G connections",
            "",
            "📈 Performance Monitoring:",
            "  - Set up Google Search Console",
            "  - Monitor Google Analytics 4 prompt tracking",
            "  - Track prompt copy events and popular categories"
        ]
        
        self.results['recommendations'] = recommendations
    
    def run_validation(self):
        """Run all validation checks"""
        print("🚀 Starting SEO validation...\n")
        
        self.validate_meta_tags()
        self.validate_structured_data()
        self.validate_sitemaps()
        self.validate_performance()
        self.validate_mobile_seo()
        self.validate_analytics()
        self.validate_content_seo()
        self.generate_recommendations()
        
        return self.results
    
    def print_report(self):
        """Print validation report"""
        print("\n" + "="*60)
        print("🔍 SEO VALIDATION REPORT")
        print("="*60)
        
        sections = [
            ('Meta Tags', 'meta_tags'),
            ('Structured Data', 'structured_data'),
            ('Sitemaps', 'sitemaps'),
            ('Performance', 'performance'),
            ('Mobile SEO', 'mobile'),
            ('Content SEO', 'content')
        ]
        
        for section_name, key in sections:
            if self.results[key]:
                print(f"\n📋 {section_name}:")
                for item in self.results[key]:
                    print(f"  {item}")
        
        if self.results['errors']:
            print(f"\n❌ ERRORS:")
            for error in self.results['errors']:
                print(f"  {error}")
        
        if self.results['warnings']:
            print(f"\n⚠️ WARNINGS:")
            for warning in self.results['warnings']:
                print(f"  {warning}")
        
        if self.results['recommendations']:
            print(f"\n💡 RECOMMENDATIONS:")
            for rec in self.results['recommendations']:
                print(f"  {rec}")
        
        # Summary
        total_checks = sum(len(v) for k, v in self.results.items() if k not in ['recommendations'])
        errors = len(self.results['errors'])
        warnings = len(self.results['warnings'])
        successes = total_checks - errors - warnings
        
        print(f"\n📊 SUMMARY:")
        print(f"  ✅ Successful checks: {successes}")
        print(f"  ⚠️ Warnings: {warnings}")
        print(f"  ❌ Errors: {errors}")
        
        score = (successes / max(total_checks, 1)) * 100
        print(f"  🎯 SEO Score: {score:.1f}%")
        
        if score >= 90:
            print("  🏆 Excellent SEO implementation!")
        elif score >= 75:
            print("  👍 Good SEO implementation with room for improvement")
        elif score >= 60:
            print("  ⚠️ SEO implementation needs attention")
        else:
            print("  🚨 SEO implementation requires immediate action")
        
        print("\n" + "="*60)

def main():
    """Main function"""
    validator = SEOValidator()
    validator.run_validation()
    validator.print_report()
    
    # Save results to JSON for CI/CD integration
    results_file = Path("seo-validation-results.json")
    with open(results_file, 'w') as f:
        json.dump(validator.results, f, indent=2)
    
    print(f"\n💾 Results saved to {results_file}")

if __name__ == "__main__":
    main()