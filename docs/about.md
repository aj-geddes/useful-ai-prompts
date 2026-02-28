---
layout: default
title: "About Useful AI Prompts"
description: "Free, open-source library of 679 expert AI prompts across 47 categories, structured with role+context+task for genuinely expert output."
permalink: /about/
---

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "AboutPage",
  "name": "About Useful AI Prompts",
  "url": "https://aj-geddes.github.io/useful-ai-prompts/about/",
  "description": "Useful AI Prompts is a free, open-source library of 679 expert AI prompts organized by profession and use case, designed to produce genuinely expert AI output.",
  "mainEntity": {
    "@type": "WebSite",
    "name": "Useful AI Prompts",
    "url": "https://aj-geddes.github.io/useful-ai-prompts/",
    "description": "679 expert AI prompts across 47 categories for professionals",
    "license": "https://opensource.org/licenses/MIT"
  }
}
</script>

<div class="about-page">
  <div class="container">

    <div class="page-header">
      <h1>About Useful AI Prompts</h1>
      <p class="page-subtitle">A free, open-source library of structured AI prompts built for professionals who need AI to actually do the work — not just sound like it could.</p>
    </div>

    <div class="about-content">

      <h2>What This Library Is</h2>

      <p>Useful AI Prompts is a collection of 679 expert-grade prompts organized across 47 categories covering 14 professional domains. Every prompt is free, open-source under the MIT license, and available without an account, paywall, or signup.</p>

      <p>The prompts are designed for use with ChatGPT, Claude, Gemini, and any other capable large language model. They work by establishing a precise expert persona, gathering the specific context needed for your situation, then producing structured, professional-grade output.</p>

      <h2>Why This Exists</h2>

      <p>Most AI prompts circulating online fall into one of two categories: vague single-liners that produce generic output, or over-hyped "mega-prompts" that are long but structurally empty. Neither produces the kind of output a professional can use directly.</p>

      <p>This library takes a different approach. Each prompt is built around a specific professional role with defined expertise, structured to gather the right inputs before producing output, and designed to apply real professional frameworks to your specific situation. The goal is prompts that make AI genuinely useful at work — not just impressive in a demo.</p>

      <h2>How Prompts Are Structured</h2>

      <p>Every prompt in this library follows a standardized XML tag format with seven components:</p>

      <ul>
        <li><strong>role</strong> — Defines the specific expert persona the AI adopts, including domain expertise, professional background, and decision-making frameworks</li>
        <li><strong>context</strong> — Establishes the professional situation and constraints the AI operates within</li>
        <li><strong>input_handling</strong> — Specifies what information the AI needs to gather from you before proceeding</li>
        <li><strong>task</strong> — Defines the 3–7 specific steps the AI follows to complete the work</li>
        <li><strong>output_specification</strong> — Sets the required format, length, and structure of the deliverable</li>
        <li><strong>quality_criteria</strong> — Establishes measurable standards the output must meet</li>
        <li><strong>constraints</strong> — Defines what the AI should not do, what assumptions to avoid, and where to flag uncertainty</li>
      </ul>

      <p>This structure produces different behavior from a typical prompt. Instead of generating plausible-sounding text, the AI gathers your specific context, applies professional frameworks, and delivers output with defined quality standards — closer to working with a knowledgeable colleague than querying a search engine.</p>

      <h2>The Numbers</h2>

      <ul>
        <li><strong>679 prompts</strong> across 47 categories</li>
        <li><strong>14 professional domains</strong> covered in depth: Development, Security, Finance, Human Resources, Healthcare, Education, Project Management, Operations, Engineering, Customer Service, Creative, Research, Administrative, and Academic</li>
        <li>Each domain includes 10–50 prompts targeting specific roles and workflows within that field</li>
      </ul>

      <h2>How to Contribute</h2>

      <p>This project is open source and contributions are welcome. You can contribute new prompts, improve existing ones, report issues, or suggest new categories. All contributions follow the same structured format and quality standards as the existing library.</p>

      <p>See the <a href="https://github.com/aj-geddes/useful-ai-prompts/blob/main/CONTRIBUTING.md" target="_blank" rel="noopener">contributing guide on GitHub</a> for full instructions on how to submit prompts, what quality criteria they need to meet, and how the review process works.</p>

      <h2>License</h2>

      <p>All prompts in this library are released under the <a href="https://opensource.org/licenses/MIT" target="_blank" rel="noopener">MIT License</a>. You can use, copy, modify, and distribute them freely — for personal or commercial use — with no restrictions beyond attribution.</p>

      <div class="about-actions">
        <a href="{{ '/' | relative_url }}" class="btn-primary">Browse All Prompts</a>
        <a href="https://github.com/aj-geddes/useful-ai-prompts" class="btn-secondary" target="_blank" rel="noopener">View on GitHub</a>
      </div>

    </div>
  </div>
</div>

<style>
.about-page {
  padding: 3rem 0 4rem;
}

.page-header {
  text-align: center;
  margin-bottom: 3rem;
  max-width: 800px;
  margin-left: auto;
  margin-right: auto;
}

.page-header h1 {
  font-size: 2.5rem;
  font-weight: 700;
  color: #1a202c;
  margin: 0 0 1rem;
}

.page-subtitle {
  font-size: 1.125rem;
  color: #4a5568;
  line-height: 1.7;
  margin: 0;
}

.about-content {
  max-width: 800px;
  margin: 0 auto;
}

.about-content h2 {
  font-size: 1.5rem;
  font-weight: 700;
  color: #2d3748;
  margin: 2.5rem 0 1rem;
  padding-bottom: 0.5rem;
  border-bottom: 2px solid #e2e8f0;
}

.about-content p {
  font-size: 1rem;
  color: #4a5568;
  line-height: 1.75;
  margin: 0 0 1.25rem;
}

.about-content ul {
  margin: 0 0 1.25rem;
  padding-left: 1.5rem;
}

.about-content ul li {
  font-size: 1rem;
  color: #4a5568;
  line-height: 1.75;
  margin-bottom: 0.5rem;
}

.about-content a {
  color: #4299e1;
  text-decoration: none;
}

.about-content a:hover {
  color: #3182ce;
  text-decoration: underline;
}

.about-actions {
  display: flex;
  gap: 1rem;
  margin-top: 3rem;
  flex-wrap: wrap;
}

.btn-primary,
.btn-secondary {
  padding: 0.875rem 1.75rem;
  border-radius: 6px;
  font-weight: 600;
  font-size: 1rem;
  text-decoration: none;
  transition: all 0.2s;
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
}

.btn-primary {
  background: #4299e1;
  color: white;
}

.btn-primary:hover {
  background: #3182ce;
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(66, 153, 225, 0.3);
  color: white;
  text-decoration: none;
}

.btn-secondary {
  background: white;
  color: #4a5568;
  border: 2px solid #e2e8f0;
}

.btn-secondary:hover {
  border-color: #cbd5e0;
  background: #f7fafc;
  text-decoration: none;
}

@media (max-width: 768px) {
  .page-header h1 {
    font-size: 2rem;
  }

  .about-content h2 {
    font-size: 1.375rem;
  }

  .about-actions {
    flex-direction: column;
  }

  .btn-primary,
  .btn-secondary {
    text-align: center;
    justify-content: center;
  }
}
</style>
