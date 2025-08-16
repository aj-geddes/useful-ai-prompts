# Search Engine Submission Checklists
## Ready-to-Execute Action Items

---

## 🚀 WEEK 1: FOUNDATION SETUP

### Google Search Console Setup ✅
**Priority**: CRITICAL - Complete First

#### Verification Steps:
- [ ] Go to [Google Search Console](https://search.google.com/search-console/)
- [ ] Add property: `https://aj-geddes.github.io/useful-ai-prompts/`
- [ ] Choose verification method:
  - [ ] **HTML Meta Tag** (Recommended)
    - Copy meta tag: `<meta name="google-site-verification" content="[CODE]" />`
    - Add to `/docs/_includes/header.html`
    - Verify after deployment
  - [ ] **HTML File Upload**
    - Download verification file
    - Upload to `/docs/` directory
    - Verify after deployment

#### Post-Verification Actions:
- [ ] Submit sitemap: `https://aj-geddes.github.io/useful-ai-prompts/sitemap.xml`
- [ ] Request indexing for homepage
- [ ] Request indexing for `/categories/` page
- [ ] Set up email notifications
- [ ] Enable data sharing with Google Analytics

#### URLs to Submit for Priority Indexing:
```
https://aj-geddes.github.io/useful-ai-prompts/
https://aj-geddes.github.io/useful-ai-prompts/categories/
https://aj-geddes.github.io/useful-ai-prompts/search/
https://aj-geddes.github.io/useful-ai-prompts/categories/management-leadership/
https://aj-geddes.github.io/useful-ai-prompts/categories/technical-workflows/
https://aj-geddes.github.io/useful-ai-prompts/categories/blockchain/
https://aj-geddes.github.io/useful-ai-prompts/categories/biotechnology/
https://aj-geddes.github.io/useful-ai-prompts/categories/quantum-computing/
```

### Bing Webmaster Tools Setup ✅
**Priority**: HIGH

#### Setup Steps:
- [ ] Go to [Bing Webmaster Tools](https://www.bing.com/webmasters/)
- [ ] Add site: `https://aj-geddes.github.io/useful-ai-prompts/`
- [ ] Choose verification:
  - [ ] **Import from Google Search Console** (easiest if GSC linked)
  - [ ] **XML file method** (download and upload to `/docs/`)
  - [ ] **Meta tag method** (same as Google)

#### Configuration:
- [ ] Submit sitemap: `https://aj-geddes.github.io/useful-ai-prompts/sitemap.xml`
- [ ] Enable crawl rate optimization
- [ ] Set up email alerts for crawl issues
- [ ] Configure geographic targeting (if applicable)

### Technical Implementation ✅

#### 1. Enhanced Schema Markup
**File**: `/docs/_includes/structured-data.html`
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": "Useful AI Prompts",
  "description": "Professional AI prompts for every workflow. 278+ expert prompts across 18 specialized categories.",
  "url": "https://aj-geddes.github.io/useful-ai-prompts/",
  "potentialAction": {
    "@type": "SearchAction",
    "target": {
      "@type": "EntryPoint",
      "urlTemplate": "https://aj-geddes.github.io/useful-ai-prompts/search/?q={search_term_string}"
    },
    "query-input": "required name=search_term_string"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Useful AI Prompts",
    "url": "https://aj-geddes.github.io/useful-ai-prompts/"
  },
  "mainEntity": {
    "@type": "CreativeWork",
    "name": "AI Prompt Library",
    "description": "Comprehensive collection of professional AI prompts for business workflows",
    "genre": ["Artificial Intelligence", "Productivity", "Business Tools"],
    "keywords": "AI prompts, ChatGPT prompts, AI tools, business prompts, professional prompts"
  }
}
</script>
```

#### 2. Google Analytics 4 Setup
- [ ] Create GA4 property at [Google Analytics](https://analytics.google.com/)
- [ ] Copy Measurement ID (G-XXXXXXXXXX)
- [ ] Add to `/docs/_config.yml`:
```yaml
google_analytics: G-XXXXXXXXXX
```
- [ ] Create `/docs/_includes/google-analytics.html`:
```html
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id={{ site.google_analytics }}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', '{{ site.google_analytics }}');
</script>
```
- [ ] Include in `_layouts/default.html` before `</head>`

#### 3. Performance Optimization Check
- [ ] Test site speed: [PageSpeed Insights](https://pagespeed.web.dev/)
- [ ] Ensure mobile-friendly: [Mobile-Friendly Test](https://search.google.com/test/mobile-friendly)
- [ ] Validate structured data: [Rich Results Test](https://search.google.com/test/rich-results)
- [ ] Check sitemap: [XML Sitemap Validator](https://www.xml-sitemaps.com/validate-xml-sitemap.html)

---

## 📊 WEEK 2: DIRECTORY SUBMISSIONS

### AI Tool Directories ✅

#### 1. There's An AI For That
- [ ] **URL**: [theresanaiforthat.com/submit](https://theresanaiforthat.com/submit)
- [ ] **Category**: Productivity/Writing Tools
- [ ] **Required Info**:
  - Tool Name: Useful AI Prompts
  - URL: https://aj-geddes.github.io/useful-ai-prompts/
  - Description: "Searchable library of 278+ professional AI prompts for business workflows. Dual-persona architecture with instant search and copy-to-clipboard functionality."
  - Tags: AI, Prompts, Productivity, Business, ChatGPT
  - Screenshots: Homepage + search functionality
- [ ] **Status**: Submitted ___/___/___

#### 2. AI Tools Directory
- [ ] **URL**: [aitool.directory](https://aitool.directory/)
- [ ] **Submission**: Look for "Submit Tool" or contact form
- [ ] **Required Info**:
  - Name: Useful AI Prompts
  - Category: Productivity & Writing
  - Description: "Professional AI prompt library with 278+ expert prompts across 18 categories. Features instant search, category filtering, and one-click copying."
  - Free/Paid: Free
  - Key Features: Search, Categorization, Mobile-friendly, Copy functionality
- [ ] **Status**: Submitted ___/___/___

#### 3. Future Tools
- [ ] **URL**: [futuretools.io](https://futuretools.io/)
- [ ] **Submission**: Contact form or email
- [ ] **Pitch**: "Premium AI prompt library with professional focus - built for business workflows rather than creative writing"
- [ ] **Status**: Submitted ___/___/___

#### 4. AI Tool Kit
- [ ] **URL**: [aitoolkit.org](https://aitoolkit.org/)
- [ ] **Focus**: Professional/business angle
- [ ] **Description**: "Comprehensive collection of AI prompts designed for business professionals, featuring dual-persona architecture and workflow-specific categorization."
- [ ] **Status**: Submitted ___/___/___

### Developer/Tech Directories ✅

#### 1. Product Hunt Launch
**Preparation Required - Schedule Launch**

**Pre-Launch (1 week before):**
- [ ] Create Product Hunt account
- [ ] Prepare assets:
  - [ ] Logo (high resolution)
  - [ ] Gallery images (5-10 screenshots)
  - [ ] GIF demo of search functionality
  - [ ] Product description (detailed)
- [ ] Build launch list (email contacts)
- [ ] Schedule for Tuesday-Thursday launch
- [ ] Notify networks 24hrs in advance

**Launch Day Materials:**
```
Product Name: Useful AI Prompts
Tagline: Professional AI prompt library with instant search
Description: Searchable collection of 278+ professional AI prompts designed for business workflows. Features dual-persona architecture, instant search, category filtering, and one-click copying. Built for professionals who need reliable AI prompts for their daily work.

Key Features:
• 278+ expert-level prompts across 18 categories
• Instant search with keyword, category, and tag filtering
• Dual-persona architecture combining multiple expert perspectives
• One-click copy-to-clipboard functionality
• Mobile-responsive design
• Completely free, no signup required

Categories: Productivity, Artificial Intelligence, Business Tools
```

- [ ] **Launch Date**: ___/___/___
- [ ] **Status**: Live/Scheduled/Planning

#### 2. Indie Hackers
- [ ] **URL**: [indiehackers.com](https://indiehackers.com/)
- [ ] **Section**: "Show IH" forum
- [ ] **Post Title**: "Built a searchable AI prompt library - 278+ professional prompts"
- [ ] **Content**: Share building process, technical challenges, user feedback
- [ ] **Include**: Metrics, lessons learned, tech stack details
- [ ] **Status**: Posted ___/___/___

#### 3. Hacker News
**Timing Critical - Best Results Tuesday-Thursday, 8-10 AM PST**

- [ ] **URL**: [news.ycombinator.com](https://news.ycombinator.com/submit)
- [ ] **Title**: "Show HN: Useful AI Prompts – 278+ Professional Prompts for Every Workflow"
- [ ] **URL**: https://aj-geddes.github.io/useful-ai-prompts/
- [ ] **Optimal Time**: Tuesday-Thursday, 8-10 AM PST
- [ ] **Follow-up**: Monitor comments, respond promptly
- [ ] **Status**: Posted ___/___/___ at ___:___ PST

### GitHub Awesome Lists ✅

#### 1. Awesome ChatGPT Prompts
- [ ] **Repository**: [f/awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts)
- [ ] **Method**: Fork → Edit README.md → Submit PR
- [ ] **Addition**:
```markdown
## [Useful AI Prompts](https://aj-geddes.github.io/useful-ai-prompts/)
Searchable library of 278+ professional AI prompts organized by workflow and industry. Features dual-persona architecture and instant search functionality.
```
- [ ] **PR Status**: Submitted ___/___/___

#### 2. Awesome AI Tools
- [ ] **Repository**: Search for "awesome-ai-tools" repositories
- [ ] **Target**: Repositories with 500+ stars
- [ ] **Method**: Submit PR to multiple relevant lists
- [ ] **Status**: 
  - Repo 1: ___/___/___
  - Repo 2: ___/___/___
  - Repo 3: ___/___/___

#### 3. Awesome Productivity
- [ ] **Search**: "awesome-productivity" repositories
- [ ] **Category**: AI/Automation tools
- [ ] **Status**: Submitted ___/___/___

---

## 🌐 WEEK 3: COMMUNITY SUBMISSIONS

### Reddit Strategy ✅

#### High-Priority Subreddits:

#### 1. r/ChatGPT (1.5M members)
- [ ] **Best Time**: 9-11 AM EST, weekdays
- [ ] **Title**: "I built a searchable library of 278+ professional AI prompts"
- [ ] **Content**: Use template from strategy document
- [ ] **Focus**: Problem-solving, practical value
- [ ] **Status**: Posted ___/___/___ at ___:___

#### 2. r/artificial (150k members)
- [ ] **Best Time**: 10 AM - 2 PM EST, Tuesday-Thursday
- [ ] **Title**: "Curated collection of AI prompts for professional workflows"
- [ ] **Focus**: Tool utility, organization methodology
- [ ] **Status**: Posted ___/___/___ at ___:___

#### 3. r/productivity (900k members)
- [ ] **Best Time**: 8-10 AM EST, Monday-Wednesday
- [ ] **Title**: "How I organized 278 AI prompts to boost workflow efficiency"
- [ ] **Focus**: Productivity gains, real examples, time savings
- [ ] **Status**: Posted ___/___/___ at ___:___

#### 4. r/entrepreneur (1M members)
- [ ] **Best Time**: 9 AM - 12 PM EST, weekdays
- [ ] **Title**: "Free AI prompt library for business workflows - 278 expert prompts"
- [ ] **Focus**: Business value, ROI, professional applications
- [ ] **Status**: Posted ___/___/___ at ___:___

#### 5. r/webdev (800k members)
- [ ] **Best Time**: 10 AM - 3 PM EST, Tuesday-Thursday
- [ ] **Title**: "Built a Jekyll-powered AI prompt search engine"
- [ ] **Focus**: Technical implementation, search functionality
- [ ] **Include**: Code snippets, architecture decisions
- [ ] **Status**: Posted ___/___/___ at ___:___

### Discord Communities ✅

#### AI-Focused Servers:

#### 1. OpenAI Discord
- [ ] **Channel**: #show-and-tell
- [ ] **Message**: "Built a searchable library for professional AI prompts: [URL]. 278+ prompts with instant search and dual-persona architecture. Thoughts?"
- [ ] **Follow-up**: Engage with feedback, answer questions
- [ ] **Status**: Shared ___/___/___

#### 2. AI/ML Research Communities
- [ ] **Target**: University and research community servers
- [ ] **Angle**: Academic perspective on prompt engineering
- [ ] **Servers Found**: 
  - Server 1: ____________
  - Server 2: ____________
  - Server 3: ____________

### Social Media Execution ✅

#### LinkedIn Strategy:
- [ ] **Personal Post**: Share library with professional network
- [ ] **Company Page**: If applicable
- [ ] **Groups**: AI Professionals, Productivity Hacks, Digital Marketing
- [ ] **Article**: "How I Built a Comprehensive AI Prompt Library"
- [ ] **Status**: 
  - Personal: ___/___/___
  - Groups: ___/___/___
  - Article: ___/___/___

#### Twitter/X Strategy:
- [ ] **Launch Thread**: Multi-tweet thread introducing library
- [ ] **Daily Features**: Tweet different prompts with site links
- [ ] **Hashtags**: #AI #ChatGPT #Prompts #Productivity #AITools
- [ ] **Engage**: Reply to AI/prompt discussions with relevant links
- [ ] **Status**:
  - Launch Thread: ___/___/___
  - Daily Features: Started ___/___/___

---

## 📝 WEEK 4: CONTENT CREATION

### Blog Articles ✅

#### 1. Medium Article
- [ ] **Publication**: Better Programming, The Startup, or AI in Plain English
- [ ] **Title**: "How to Build an AI Prompt Library That Actually Gets Used"
- [ ] **Length**: 1,500-2,000 words
- [ ] **Include**: Technical details, user research, usage analytics
- [ ] **CTA**: Link to library, encourage feedback
- [ ] **Status**: 
  - Draft: ___/___/___
  - Published: ___/___/___

#### 2. Dev.to Article
- [ ] **Title**: "Building a Search-Powered Static Site with Jekyll"
- [ ] **Tags**: #ai, #productivity, #javascript, #jekyll, #searchengine
- [ ] **Focus**: Technical implementation, code examples
- [ ] **Length**: 1,000-1,500 words
- [ ] **Status**: 
  - Draft: ___/___/___
  - Published: ___/___/___

#### 3. LinkedIn Article
- [ ] **Title**: "How AI Prompts Are Transforming Professional Workflows"
- [ ] **Audience**: Business professionals, consultants
- [ ] **Length**: 800-1,200 words
- [ ] **Include**: ROI examples, case studies, practical tips
- [ ] **Status**: 
  - Draft: ___/___/___
  - Published: ___/___/___

### Outreach Campaigns ✅

#### Blogger Outreach:
- [ ] **Target 1**: [Blog name] - [Contact] - Status: ___________
- [ ] **Target 2**: [Blog name] - [Contact] - Status: ___________
- [ ] **Target 3**: [Blog name] - [Contact] - Status: ___________
- [ ] **Target 4**: [Blog name] - [Contact] - Status: ___________
- [ ] **Target 5**: [Blog name] - [Contact] - Status: ___________

#### Template Used:
```
Subject: AI Prompt Library Resource for [Blog Name] Readers

Hi [Name],

I've been following [Blog Name] and really enjoyed your recent post on [specific post]. Your insights on [specific topic] really resonated with me.

I recently built something that might be valuable for your readers: a searchable library of 278+ professional AI prompts organized by workflow and industry.

The site (https://aj-geddes.github.io/useful-ai-prompts/) focuses specifically on business and professional use cases rather than creative writing. Each prompt uses a "dual-persona" approach combining multiple expert perspectives.

Key features your readers might find useful:
• Instant search across all prompts
• 18 specialized categories (Technical, Leadership, Analysis, etc.)
• Copy-to-clipboard functionality
• Mobile-responsive design
• Completely free, no signup required

Would this be something you'd consider mentioning in a future post about AI productivity tools? I'd be happy to provide additional context or answer any questions.

Best regards,
[Your name]
```

---

## 📈 MONITORING & TRACKING

### Weekly Check-ins ✅

#### Week 1 Metrics:
- [ ] Google Search Console: Property verified? ___/___/___
- [ ] Bing Webmaster: Site submitted? ___/___/___
- [ ] Analytics: Tracking code working? ___/___/___
- [ ] Performance: Page speed score: _____
- [ ] Mobile: Mobile-friendly test passed? ___/___/___

#### Week 2 Metrics:
- [ ] Directory submissions completed: ___/5
- [ ] Product Hunt: Launch scheduled? ___/___/___
- [ ] GitHub PRs: Submitted count: ___
- [ ] Initial traffic: Baseline sessions: _____

#### Week 3 Metrics:
- [ ] Reddit posts: Successful submissions: ___/5
- [ ] Discord shares: Communities reached: ___
- [ ] Social media: Posts published: ___
- [ ] Engagement: Comments/replies: ___

#### Week 4 Metrics:
- [ ] Articles published: ___/3
- [ ] Outreach emails sent: ___/5
- [ ] Responses received: ___
- [ ] Backlinks acquired: ___

### Monthly Review Template ✅

```markdown
# Monthly Performance Review - [Month/Year]

## Submission Status
### Directories:
- [ ] There's An AI For That: ________
- [ ] AI Tools Directory: ________
- [ ] Future Tools: ________
- [ ] Product Hunt: ________

### Communities:
- [ ] Reddit (5 subreddits): ___/5 successful
- [ ] Discord (3+ servers): ___/3 active
- [ ] GitHub (awesome lists): ___/3 merged

### Content:
- [ ] Blog articles: ___/3 published
- [ ] Outreach emails: ___/5 sent
- [ ] Responses: ___/5 received

## Traffic Results
- Organic sessions: _____ (+/-___% vs baseline)
- Referral traffic: _____ sessions
- Direct traffic: _____ sessions
- Social traffic: _____ sessions

## Search Performance
- Search Console impressions: _____
- Search Console clicks: _____
- Average position: _____
- Top performing keywords: ________

## Next Month Priorities
1. [Priority action 1]
2. [Priority action 2]
3. [Priority action 3]
```

---

## 🚨 EMERGENCY ACTIONS (If Slow Progress)

### 30-Day Acceleration Plan ✅

#### If minimal traffic after 2 weeks:
- [ ] **Paid promotion**: Reddit promoted posts ($50-100)
- [ ] **Influencer outreach**: Contact 10 AI Twitter influencers
- [ ] **Newsletter pitches**: AI/productivity newsletter mentions
- [ ] **Podcast blitz**: Rapid outreach to 20+ relevant podcasts

#### If submissions rejected:
- [ ] **Analyze feedback**: Common rejection reasons
- [ ] **Site improvements**: Address presentation issues
- [ ] **Alternative directories**: Find niche-specific listings
- [ ] **Direct outreach**: Personal connections in AI community

#### Technical issues:
- [ ] **Site speed**: Optimize to sub-2 seconds
- [ ] **Mobile experience**: Perfect mobile functionality
- [ ] **Search functionality**: Ensure flawless operation
- [ ] **Content quality**: Review and enhance top pages

### Success Multipliers ✅

#### If gaining traction:
- [ ] **Double down**: Increase frequency of successful channels
- [ ] **Expand scope**: More categories, more prompts
- [ ] **Community building**: Start newsletter/email list
- [ ] **Partnerships**: Collaborate with complementary tools
- [ ] **Premium features**: Consider advanced functionality

---

This checklist provides a clear execution path with specific deadlines, metrics tracking, and contingency plans. Each action item can be checked off as completed, providing clear progress visibility and accountability.

**Start with Week 1 foundation items immediately, then maintain momentum with 3-5 submissions per week while building content and community engagement.**