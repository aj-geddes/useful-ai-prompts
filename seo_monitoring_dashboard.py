#!/usr/bin/env python3
"""
SEO Monitoring Dashboard for Useful AI Prompts
Tracks search engine submission progress and performance metrics
"""

import json
import requests
import time
from datetime import datetime, timedelta
from typing import Dict, List, Tuple
import csv
from pathlib import Path

class SEOMonitoringDashboard:
    def __init__(self):
        self.site_url = "https://aj-geddes.github.io/useful-ai-prompts/"
        self.target_keywords = [
            "AI prompts",
            "ChatGPT prompts", 
            "AI prompt library",
            "professional AI prompts",
            "business AI prompts",
            "prompt engineering templates",
            "AI workflow prompts",
            "ChatGPT business prompts"
        ]
        self.submission_targets = {
            "directories": [
                {"name": "There's An AI For That", "status": "pending", "submitted": None, "approved": None},
                {"name": "AI Tools Directory", "status": "pending", "submitted": None, "approved": None},
                {"name": "Future Tools", "status": "pending", "submitted": None, "approved": None},
                {"name": "Product Hunt", "status": "pending", "submitted": None, "approved": None},
                {"name": "AI Tool Kit", "status": "pending", "submitted": None, "approved": None}
            ],
            "communities": [
                {"name": "r/ChatGPT", "status": "pending", "submitted": None, "engagement": 0},
                {"name": "r/artificial", "status": "pending", "submitted": None, "engagement": 0},
                {"name": "r/productivity", "status": "pending", "submitted": None, "engagement": 0},
                {"name": "r/entrepreneur", "status": "pending", "submitted": None, "engagement": 0},
                {"name": "r/webdev", "status": "pending", "submitted": None, "engagement": 0}
            ],
            "github": [
                {"name": "awesome-chatgpt-prompts", "status": "pending", "pr_url": None, "merged": None},
                {"name": "awesome-ai-tools", "status": "pending", "pr_url": None, "merged": None},
                {"name": "awesome-productivity", "status": "pending", "pr_url": None, "merged": None}
            ]
        }
        
    def check_site_health(self) -> Dict:
        """Check basic site health metrics"""
        try:
            start_time = time.time()
            response = requests.get(self.site_url, timeout=10)
            load_time = time.time() - start_time
            
            return {
                "status_code": response.status_code,
                "load_time": round(load_time, 2),
                "content_length": len(response.content),
                "timestamp": datetime.now().isoformat()
            }
        except Exception as e:
            return {
                "status_code": None,
                "load_time": None,
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            }
    
    def check_sitemap_accessibility(self) -> Dict:
        """Verify sitemap is accessible"""
        sitemap_url = f"{self.site_url}sitemap.xml"
        try:
            response = requests.get(sitemap_url, timeout=10)
            return {
                "accessible": response.status_code == 200,
                "status_code": response.status_code,
                "content_type": response.headers.get('content-type', ''),
                "timestamp": datetime.now().isoformat()
            }
        except Exception as e:
            return {
                "accessible": False,
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            }
    
    def check_robots_txt(self) -> Dict:
        """Verify robots.txt is accessible"""
        robots_url = f"{self.site_url}robots.txt"
        try:
            response = requests.get(robots_url, timeout=10)
            return {
                "accessible": response.status_code == 200,
                "status_code": response.status_code,
                "content": response.text[:500] if response.status_code == 200 else None,
                "timestamp": datetime.now().isoformat()
            }
        except Exception as e:
            return {
                "accessible": False,
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            }
    
    def check_search_console_setup(self) -> Dict:
        """Check if Google Search Console meta tag is present"""
        try:
            response = requests.get(self.site_url, timeout=10)
            content = response.text
            
            # Look for Google Search Console verification
            gsc_meta = 'google-site-verification' in content
            
            # Look for Google Analytics
            ga_tag = 'gtag' in content or 'google-analytics' in content
            
            return {
                "gsc_meta_tag": gsc_meta,
                "google_analytics": ga_tag,
                "timestamp": datetime.now().isoformat()
            }
        except Exception as e:
            return {
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            }
    
    def test_page_speed(self) -> Dict:
        """Basic page speed test"""
        try:
            # Test multiple requests to get average
            times = []
            for _ in range(3):
                start_time = time.time()
                response = requests.get(self.site_url, timeout=10)
                if response.status_code == 200:
                    times.append(time.time() - start_time)
                time.sleep(1)
            
            if times:
                avg_time = sum(times) / len(times)
                return {
                    "average_load_time": round(avg_time, 2),
                    "fastest": round(min(times), 2),
                    "slowest": round(max(times), 2),
                    "tests_completed": len(times),
                    "timestamp": datetime.now().isoformat()
                }
            else:
                return {"error": "No successful requests", "timestamp": datetime.now().isoformat()}
                
        except Exception as e:
            return {"error": str(e), "timestamp": datetime.now().isoformat()}
    
    def update_submission_status(self, category: str, name: str, status: str, **kwargs):
        """Update submission status for tracking"""
        if category in self.submission_targets:
            for item in self.submission_targets[category]:
                if item["name"] == name:
                    item["status"] = status
                    item.update(kwargs)
                    break
    
    def generate_weekly_report(self) -> str:
        """Generate weekly progress report"""
        report = f"""
# Weekly SEO Progress Report - {datetime.now().strftime('%Y-%m-%d')}

## Site Health Check
"""
        
        # Site health
        health = self.check_site_health()
        if health.get("status_code") == 200:
            report += f"✅ Site accessible (Load time: {health.get('load_time', 'N/A')}s)\n"
        else:
            report += f"❌ Site issues detected: {health.get('error', 'Unknown error')}\n"
        
        # Sitemap check
        sitemap = self.check_sitemap_accessibility()
        if sitemap.get("accessible"):
            report += "✅ Sitemap accessible\n"
        else:
            report += "❌ Sitemap issues detected\n"
        
        # Robots.txt check
        robots = self.check_robots_txt()
        if robots.get("accessible"):
            report += "✅ Robots.txt accessible\n"
        else:
            report += "❌ Robots.txt issues detected\n"
        
        # Search Console setup
        sc_setup = self.check_search_console_setup()
        if sc_setup.get("gsc_meta_tag"):
            report += "✅ Google Search Console meta tag detected\n"
        else:
            report += "⚠️ Google Search Console meta tag not found\n"
        
        if sc_setup.get("google_analytics"):
            report += "✅ Google Analytics detected\n"
        else:
            report += "⚠️ Google Analytics not detected\n"
        
        # Page speed
        speed = self.test_page_speed()
        if speed.get("average_load_time"):
            avg_time = speed["average_load_time"]
            if avg_time < 2:
                report += f"✅ Excellent page speed: {avg_time}s average\n"
            elif avg_time < 3:
                report += f"⚠️ Good page speed: {avg_time}s average\n"
            else:
                report += f"❌ Slow page speed: {avg_time}s average - needs optimization\n"
        
        # Submission status
        report += "\n## Submission Progress\n\n"
        
        for category, items in self.submission_targets.items():
            report += f"### {category.title()}\n"
            for item in items:
                status_emoji = {
                    "pending": "⏳",
                    "submitted": "📤", 
                    "approved": "✅",
                    "rejected": "❌",
                    "live": "🚀"
                }.get(item["status"], "❓")
                
                report += f"- {status_emoji} {item['name']}: {item['status']}\n"
            report += "\n"
        
        # Next steps
        report += """
## Next Week Action Items
- [ ] Complete any pending submissions
- [ ] Monitor approved submissions for traffic impact
- [ ] Address any technical issues identified
- [ ] Continue content creation and outreach

## Notes
Add any specific observations or concerns here.
"""
        
        return report
    
    def save_report(self, report: str, filename: str = None):
        """Save report to file"""
        if not filename:
            filename = f"seo_report_{datetime.now().strftime('%Y%m%d')}.md"
        
        with open(filename, 'w') as f:
            f.write(report)
        
        print(f"Report saved to {filename}")
    
    def export_submission_tracker(self, filename: str = "submission_tracker.csv"):
        """Export submission status to CSV for tracking"""
        rows = []
        for category, items in self.submission_targets.items():
            for item in items:
                row = {
                    "Category": category,
                    "Name": item["name"],
                    "Status": item["status"],
                    "Submitted": item.get("submitted", ""),
                    "Additional_Info": ""
                }
                
                # Add category-specific info
                if category == "directories":
                    row["Additional_Info"] = item.get("approved", "")
                elif category == "communities":
                    row["Additional_Info"] = f"Engagement: {item.get('engagement', 0)}"
                elif category == "github":
                    row["Additional_Info"] = item.get("pr_url", "")
                
                rows.append(row)
        
        with open(filename, 'w', newline='') as f:
            if rows:
                writer = csv.DictWriter(f, fieldnames=rows[0].keys())
                writer.writeheader()
                writer.writerows(rows)
        
        print(f"Submission tracker exported to {filename}")
    
    def run_full_audit(self):
        """Run complete SEO audit and generate report"""
        print("Running SEO audit...")
        
        # Generate and save report
        report = self.generate_weekly_report()
        self.save_report(report)
        
        # Export submission tracker
        self.export_submission_tracker()
        
        print("Audit complete! Check the generated files for details.")
        
        return report

def main():
    """Main function to run SEO monitoring"""
    dashboard = SEOMonitoringDashboard()
    
    print("=== Useful AI Prompts SEO Monitoring Dashboard ===\n")
    
    while True:
        print("\nOptions:")
        print("1. Run full audit")
        print("2. Check site health")
        print("3. Generate weekly report")
        print("4. Update submission status")
        print("5. Export submission tracker")
        print("6. Exit")
        
        choice = input("\nSelect option (1-6): ").strip()
        
        if choice == "1":
            dashboard.run_full_audit()
            
        elif choice == "2":
            health = dashboard.check_site_health()
            print(f"\nSite Health: {json.dumps(health, indent=2)}")
            
        elif choice == "3":
            report = dashboard.generate_weekly_report()
            print("\n" + report)
            save = input("\nSave report to file? (y/n): ").strip().lower()
            if save == "y":
                dashboard.save_report(report)
                
        elif choice == "4":
            print("\nCategories: directories, communities, github")
            category = input("Category: ").strip()
            
            if category in dashboard.submission_targets:
                print(f"\nItems in {category}:")
                for i, item in enumerate(dashboard.submission_targets[category]):
                    print(f"{i+1}. {item['name']} (current: {item['status']})")
                
                try:
                    idx = int(input("Select item number: ")) - 1
                    new_status = input("New status: ").strip()
                    item_name = dashboard.submission_targets[category][idx]["name"]
                    dashboard.update_submission_status(category, item_name, new_status)
                    print(f"Updated {item_name} to {new_status}")
                except (ValueError, IndexError):
                    print("Invalid selection")
            else:
                print("Invalid category")
                
        elif choice == "5":
            dashboard.export_submission_tracker()
            
        elif choice == "6":
            print("Goodbye!")
            break
            
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()