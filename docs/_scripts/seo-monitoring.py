#!/usr/bin/env python3
"""
SEO Monitoring and Optimization Script
Monitors site performance and provides ongoing SEO recommendations.
"""

import requests
import json
import time
import csv
from datetime import datetime, timedelta
from pathlib import Path
import urllib.parse
import re
from collections import defaultdict

class SEOMonitor:
    def __init__(self, site_url="https://aj-geddes.github.io/useful-ai-prompts"):
        self.site_url = site_url
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'SEO-Monitor/1.0 (SEO monitoring script)'
        })
        
    def check_page_speed(self, url):
        """Check page loading speed"""
        try:
            start_time = time.time()
            response = self.session.get(url, timeout=30)
            load_time = time.time() - start_time
            
            return {
                'url': url,
                'status_code': response.status_code,
                'load_time': round(load_time, 2),
                'content_length': len(response.content),
                'compressed': 'gzip' in response.headers.get('content-encoding', ''),
                'cache_control': response.headers.get('cache-control', 'none'),
                'timestamp': datetime.now().isoformat()
            }
        except Exception as e:
            return {
                'url': url,
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }
    
    def analyze_meta_tags(self, url):
        """Analyze meta tags of a page"""
        try:
            response = self.session.get(url)
            content = response.text
            
            # Extract meta tags
            meta_tags = {}
            
            # Title
            title_match = re.search(r'<title[^>]*>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
            if title_match:
                meta_tags['title'] = title_match.group(1).strip()
                meta_tags['title_length'] = len(meta_tags['title'])
            
            # Meta description
            desc_match = re.search(r'<meta[^>]*name=["\']description["\'][^>]*content=["\']([^"\']*)["\']', content, re.IGNORECASE)
            if desc_match:
                meta_tags['description'] = desc_match.group(1).strip()
                meta_tags['description_length'] = len(meta_tags['description'])
            
            # Open Graph tags
            og_tags = re.findall(r'<meta[^>]*property=["\']og:([^"\']*)["\'][^>]*content=["\']([^"\']*)["\']', content, re.IGNORECASE)
            for prop, content_val in og_tags:
                meta_tags[f'og_{prop}'] = content_val
            
            # Twitter Cards
            twitter_tags = re.findall(r'<meta[^>]*name=["\']twitter:([^"\']*)["\'][^>]*content=["\']([^"\']*)["\']', content, re.IGNORECASE)
            for prop, content_val in twitter_tags:
                meta_tags[f'twitter_{prop}'] = content_val
            
            # Canonical URL
            canonical_match = re.search(r'<link[^>]*rel=["\']canonical["\'][^>]*href=["\']([^"\']*)["\']', content, re.IGNORECASE)
            if canonical_match:
                meta_tags['canonical'] = canonical_match.group(1)
            
            return meta_tags
            
        except Exception as e:
            return {'error': str(e)}
    
    def check_structured_data(self, url):
        """Check for structured data implementation"""
        try:
            response = self.session.get(url)
            content = response.text
            
            # Find JSON-LD blocks
            json_ld_pattern = r'<script[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>'
            json_ld_blocks = re.findall(json_ld_pattern, content, re.DOTALL | re.IGNORECASE)
            
            structured_data = []
            for block in json_ld_blocks:
                try:
                    # Clean up the JSON (remove Liquid templating for analysis)
                    cleaned_block = re.sub(r'\{\{.*?\}\}', '""', block)
                    cleaned_block = re.sub(r'\{%.*?%\}', '', cleaned_block)
                    
                    data = json.loads(cleaned_block)
                    
                    if isinstance(data, dict):
                        if '@graph' in data:
                            for item in data['@graph']:
                                if '@type' in item:
                                    structured_data.append(item['@type'])
                        elif '@type' in data:
                            structured_data.append(data['@type'])
                    
                except json.JSONDecodeError:
                    structured_data.append('Invalid JSON-LD')
            
            return {
                'url': url,
                'json_ld_blocks': len(json_ld_blocks),
                'schema_types': structured_data,
                'timestamp': datetime.now().isoformat()
            }
            
        except Exception as e:
            return {'url': url, 'error': str(e)}
    
    def monitor_sitemap(self, sitemap_url=None):
        """Monitor sitemap accessibility and structure"""
        if not sitemap_url:
            sitemap_url = f"{self.site_url}/sitemap.xml"
        
        try:
            response = self.session.get(sitemap_url)
            
            if response.status_code == 200:
                # Count URLs in sitemap
                url_count = response.text.count('<loc>')
                
                return {
                    'sitemap_url': sitemap_url,
                    'status': 'accessible',
                    'url_count': url_count,
                    'size_bytes': len(response.content),
                    'last_checked': datetime.now().isoformat()
                }
            else:
                return {
                    'sitemap_url': sitemap_url,
                    'status': 'error',
                    'status_code': response.status_code,
                    'last_checked': datetime.now().isoformat()
                }
                
        except Exception as e:
            return {
                'sitemap_url': sitemap_url,
                'status': 'error',
                'error': str(e),
                'last_checked': datetime.now().isoformat()
            }
    
    def analyze_content_seo(self, url):
        """Analyze content SEO factors"""
        try:
            response = self.session.get(url)
            content = response.text
            
            # Remove HTML tags for text analysis
            text_content = re.sub(r'<[^>]+>', ' ', content)
            text_content = re.sub(r'\s+', ' ', text_content).strip()
            
            # Word count
            word_count = len(text_content.split())
            
            # Heading analysis
            h1_count = len(re.findall(r'<h1[^>]*>', content, re.IGNORECASE))
            h2_count = len(re.findall(r'<h2[^>]*>', content, re.IGNORECASE))
            h3_count = len(re.findall(r'<h3[^>]*>', content, re.IGNORECASE))
            
            # Image analysis
            images = re.findall(r'<img[^>]*>', content, re.IGNORECASE)
            images_with_alt = len([img for img in images if 'alt=' in img])
            
            # Link analysis
            internal_links = len(re.findall(r'<a[^>]*href=["\'][^"\']*' + re.escape(self.site_url), content, re.IGNORECASE))
            external_links = len(re.findall(r'<a[^>]*href=["\']https?://(?!' + re.escape(self.site_url), content, re.IGNORECASE))
            
            return {
                'url': url,
                'word_count': word_count,
                'headings': {
                    'h1': h1_count,
                    'h2': h2_count,
                    'h3': h3_count
                },
                'images': {
                    'total': len(images),
                    'with_alt': images_with_alt,
                    'alt_percentage': (images_with_alt / max(len(images), 1)) * 100
                },
                'links': {
                    'internal': internal_links,
                    'external': external_links
                },
                'timestamp': datetime.now().isoformat()
            }
            
        except Exception as e:
            return {'url': url, 'error': str(e)}
    
    def run_comprehensive_audit(self, sample_urls=None):
        """Run comprehensive SEO audit"""
        if not sample_urls:
            sample_urls = [
                self.site_url,
                f"{self.site_url}/categories/",
                f"{self.site_url}/search/",
                f"{self.site_url}/prompts/strategic-roadmap-generator/",
                f"{self.site_url}/prompts/business-analyst-strategic-excellence/"
            ]
        
        audit_results = {
            'audit_timestamp': datetime.now().isoformat(),
            'site_url': self.site_url,
            'pages_audited': len(sample_urls),
            'results': []
        }
        
        print(f"🔍 Running SEO audit for {len(sample_urls)} pages...")
        
        for url in sample_urls:
            print(f"  📄 Auditing: {url}")
            
            page_result = {
                'url': url,
                'performance': self.check_page_speed(url),
                'meta_tags': self.analyze_meta_tags(url),
                'structured_data': self.check_structured_data(url),
                'content_seo': self.analyze_content_seo(url)
            }
            
            audit_results['results'].append(page_result)
            time.sleep(1)  # Be respectful to the server
        
        # Check sitemap
        print("  🗺️ Checking sitemap...")
        audit_results['sitemap'] = self.monitor_sitemap()
        
        return audit_results
    
    def generate_seo_report(self, audit_results):
        """Generate human-readable SEO report"""
        report = []
        report.append("=" * 60)
        report.append("🔍 SEO MONITORING REPORT")
        report.append("=" * 60)
        report.append(f"Site: {audit_results['site_url']}")
        report.append(f"Audit Time: {audit_results['audit_timestamp']}")
        report.append(f"Pages Audited: {audit_results['pages_audited']}")
        report.append("")
        
        # Performance Summary
        load_times = []
        for result in audit_results['results']:
            if 'load_time' in result['performance']:
                load_times.append(result['performance']['load_time'])
        
        if load_times:
            avg_load_time = sum(load_times) / len(load_times)
            report.append(f"📊 PERFORMANCE SUMMARY")
            report.append(f"  Average Load Time: {avg_load_time:.2f}s")
            report.append(f"  Fastest Page: {min(load_times):.2f}s")
            report.append(f"  Slowest Page: {max(load_times):.2f}s")
            
            if avg_load_time < 2.0:
                report.append("  ✅ Excellent loading performance!")
            elif avg_load_time < 3.0:
                report.append("  👍 Good loading performance")
            else:
                report.append("  ⚠️ Loading performance needs improvement")
            report.append("")
        
        # SEO Issues
        issues = []
        recommendations = []
        
        for result in audit_results['results']:
            url = result['url']
            meta = result['meta_tags']
            
            # Check title lengths
            if 'title_length' in meta:
                if meta['title_length'] > 60:
                    issues.append(f"⚠️ Title too long ({meta['title_length']} chars): {url}")
                elif meta['title_length'] < 30:
                    issues.append(f"⚠️ Title too short ({meta['title_length']} chars): {url}")
            
            # Check description lengths
            if 'description_length' in meta:
                if meta['description_length'] > 160:
                    issues.append(f"⚠️ Description too long ({meta['description_length']} chars): {url}")
                elif meta['description_length'] < 120:
                    issues.append(f"⚠️ Description too short ({meta['description_length']} chars): {url}")
            
            # Check for missing meta tags
            if 'description' not in meta:
                issues.append(f"❌ Missing meta description: {url}")
            
            if 'og_title' not in meta:
                issues.append(f"❌ Missing Open Graph title: {url}")
            
            # Content analysis
            content = result['content_seo']
            if 'word_count' in content:
                if content['word_count'] < 300:
                    issues.append(f"⚠️ Low word count ({content['word_count']} words): {url}")
                
                if content['headings']['h1'] != 1:
                    issues.append(f"⚠️ Should have exactly 1 H1 tag (found {content['headings']['h1']}): {url}")
        
        if issues:
            report.append("🚨 ISSUES FOUND:")
            for issue in issues[:10]:  # Show top 10 issues
                report.append(f"  {issue}")
            if len(issues) > 10:
                report.append(f"  ... and {len(issues) - 10} more issues")
            report.append("")
        
        # Recommendations
        recommendations = [
            "💡 RECOMMENDATIONS:",
            "  🎯 Optimize page titles to 30-60 characters",
            "  📝 Ensure meta descriptions are 120-160 characters",
            "  🖼️ Add alt text to all images",
            "  🔗 Improve internal linking between related prompts",
            "  📱 Test mobile performance regularly",
            "  📊 Monitor Core Web Vitals in Google Search Console",
            "  🔍 Submit updated sitemaps to search engines",
            "  📈 Track organic search traffic growth"
        ]
        
        report.extend(recommendations)
        report.append("")
        
        # Sitemap status
        sitemap = audit_results.get('sitemap', {})
        if sitemap.get('status') == 'accessible':
            report.append(f"✅ Sitemap accessible with {sitemap.get('url_count', 0)} URLs")
        else:
            report.append("❌ Sitemap accessibility issues detected")
        
        report.append("")
        report.append("=" * 60)
        
        return "\n".join(report)
    
    def save_results(self, audit_results, filename=None):
        """Save audit results to file"""
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"seo_audit_{timestamp}.json"
        
        with open(filename, 'w') as f:
            json.dump(audit_results, f, indent=2)
        
        return filename

def main():
    """Main monitoring function"""
    print("🚀 Starting SEO monitoring...")
    
    monitor = SEOMonitor()
    
    # Run comprehensive audit
    results = monitor.run_comprehensive_audit()
    
    # Generate and print report
    report = monitor.generate_seo_report(results)
    print("\n" + report)
    
    # Save results
    filename = monitor.save_results(results)
    print(f"\n💾 Detailed results saved to: {filename}")
    
    # Quick CSV export for tracking
    csv_filename = f"seo_summary_{datetime.now().strftime('%Y%m%d')}.csv"
    with open(csv_filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['URL', 'Load Time (s)', 'Title Length', 'Description Length', 'Word Count', 'Issues'])
        
        for result in results['results']:
            url = result['url']
            load_time = result['performance'].get('load_time', 'N/A')
            title_len = result['meta_tags'].get('title_length', 'N/A')
            desc_len = result['meta_tags'].get('description_length', 'N/A')
            word_count = result['content_seo'].get('word_count', 'N/A')
            issues = 0
            
            # Count issues for this page
            if isinstance(title_len, int) and (title_len > 60 or title_len < 30):
                issues += 1
            if isinstance(desc_len, int) and (desc_len > 160 or desc_len < 120):
                issues += 1
            if 'description' not in result['meta_tags']:
                issues += 1
            
            writer.writerow([url, load_time, title_len, desc_len, word_count, issues])
    
    print(f"📊 Summary saved to: {csv_filename}")

if __name__ == "__main__":
    main()