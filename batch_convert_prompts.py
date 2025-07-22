#!/usr/bin/env python3
"""
Batch convert old dual-persona prompts to new conversational format
"""

import os
import re
from datetime import datetime

def extract_key_info(content):
    """Extract key information from old format prompt"""
    info = {
        'title': '',
        'category': '',
        'tags': [],
        'description': '',
        'use_cases': [],
        'version': '3.0.0',  # New version for converted prompts
    }
    
    # Extract title
    title_match = re.search(r"^# (.+)$", content, re.MULTILINE)
    if title_match:
        # Simplify title - remove "and X Expert" pattern
        title = title_match.group(1)
        title = re.sub(r" and .+ Expert$", " Expert", title)
        info['title'] = title
    
    # Extract metadata
    cat_match = re.search(r"- \*\*Category\*\*: (.+)$", content, re.MULTILINE)
    if cat_match:
        info['category'] = cat_match.group(1)
        
    tags_match = re.search(r"- \*\*Tags\*\*: (.+)$", content, re.MULTILINE)
    if tags_match:
        info['tags'] = [t.strip() for t in tags_match.group(1).split(',')]
        
    use_match = re.search(r"- \*\*Use Cases\*\*: (.+)$", content, re.MULTILINE)
    if use_match:
        info['use_cases'] = [u.strip() for u in use_match.group(1).split(',')]
    
    # Extract description
    desc_match = re.search(r"## Description\s*\n\s*(.+?)(?=\n##|\n###)", content, re.DOTALL)
    if desc_match:
        desc = desc_match.group(1).strip()
        # Simplify description - remove complex language
        desc = desc.split('.')[0] + '.'  # Just keep first sentence
        info['description'] = desc
    
    return info

def create_conversational_prompt(info, old_content):
    """Create a new conversational format prompt"""
    
    # Extract any context variables from old format
    context_vars = []
    context_match = re.search(r"### .* Context\s*\n(.*?)(?=###|##)", old_content, re.DOTALL)
    if context_match:
        lines = context_match.group(1).strip().split('\n')
        for line in lines:
            if '{{' in line:
                # Extract variable descriptions
                var_match = re.search(r"- \*\*(.+?)\*\*: {{.+?}}", line)
                if var_match:
                    context_vars.append(var_match.group(1))
    
    # Create conversational questions based on context
    questions = []
    if context_vars:
        questions = [f"What is your {var.lower()}?" for var in context_vars[:6]]
    else:
        # Default questions based on category
        if 'analysis' in info['category'].lower():
            questions = [
                "What type of analysis do you need?",
                "What data or information do you have?",
                "What decisions will this analysis inform?",
                "Who is the audience for this analysis?",
                "What's your timeline?",
                "What format should the output be in?"
            ]
        elif 'communication' in info['category'].lower():
            questions = [
                "What's the purpose of this communication?",
                "Who is your audience?",
                "What key message do you need to convey?",
                "What tone should be used?",
                "Are there any sensitive topics to handle?",
                "What format do you need?"
            ]
        else:
            questions = [
                "What specific task do you need help with?",
                "What's your current situation or context?",
                "What are your main goals or objectives?",
                "What constraints or requirements do you have?",
                "Who will be using the output?",
                "What's your timeline?"
            ]
    
    # Extract deliverables from old format
    deliverables = []
    deliv_match = re.search(r"### Deliverables\s*\n(.*?)(?=##|$)", old_content, re.DOTALL)
    if deliv_match:
        deliv_text = deliv_match.group(1)
        # Extract numbered items
        items = re.findall(r"\d+\.\s*\*\*(.+?)\*\*", deliv_text)
        deliverables = items[:5]  # Keep top 5
    
    if not deliverables:
        # Default deliverables based on category
        deliverables = [
            "Analysis Summary",
            "Key Findings",
            "Recommendations",
            "Action Plan",
            "Next Steps"
        ]
    
    # Build the new prompt
    new_content = f"""# {info['title']}

## Metadata

- **Category**: {info['category']}
- **Tags**: {', '.join(info['tags'])}
- **Created**: {datetime.now().strftime('%Y-%m-%d')}
- **Version**: {info['version']}
- **Use Cases**: {', '.join(info['use_cases']) if info['use_cases'] else 'general assistance'}
- **Compatible Models**: GPT-4, Claude 3, Gemini Pro, GPT-3.5

## Description

{info['description']}

## Prompt

```
I'll help you with {info['title'].lower().replace(' expert', '')}. Let me understand your needs:

"""
    
    # Add questions in groups
    new_content += f"**About your situation:**\n"
    for i, q in enumerate(questions[:len(questions)//2], 1):
        new_content += f"{i}. {q}\n"
    
    new_content += f"\n**Specific requirements:**\n"
    for i, q in enumerate(questions[len(questions)//2:], len(questions)//2 + 1):
        new_content += f"{i}. {q}\n"
    
    new_content += f"\nBased on your answers, I'll provide:\n\n"
    
    for deliv in deliverables:
        new_content += f"**{deliv.upper()}** - "
        # Add brief description
        if 'analysis' in deliv.lower():
            new_content += "Comprehensive analysis of your situation\n"
        elif 'recommendation' in deliv.lower():
            new_content += "Actionable recommendations based on findings\n"
        elif 'plan' in deliv.lower():
            new_content += "Step-by-step implementation plan\n"
        elif 'finding' in deliv.lower():
            new_content += "Key insights and discoveries\n"
        else:
            new_content += "Detailed guidance and solutions\n"
    
    new_content += "\nPlease provide the information above so I can assist you effectively.\n```\n\n"
    
    # Add a simple example
    new_content += """## Example Usage

**User Input:**
```
[Provide context based on the questions above]
```

**Assistant Output:**
```
[Comprehensive response addressing all deliverables]
```

## Related Prompts

- [Add related prompts here]
"""
    
    return new_content

def convert_prompt_file(filepath):
    """Convert a single prompt file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        old_content = f.read()
    
    # Extract key information
    info = extract_key_info(old_content)
    
    # Create new conversational format
    new_content = create_conversational_prompt(info, old_content)
    
    # Calculate size reduction
    old_lines = len(old_content.split('\n'))
    new_lines = len(new_content.split('\n'))
    
    print(f"Converting {os.path.basename(filepath)}:")
    print(f"  Old: {old_lines} lines → New: {new_lines} lines")
    print(f"  Reduction: {old_lines - new_lines} lines ({100 - (new_lines/old_lines*100):.1f}%)")
    
    return new_content

def main():
    # Test with one file first
    test_file = "/home/aj-geddes/dev/claude-projects/useful-ai-prompts/prompts/business/administrative/calendar-optimization.md"
    
    print(f"Testing conversion with: {os.path.basename(test_file)}\n")
    
    new_content = convert_prompt_file(test_file)
    
    # Save to a test file
    test_output = "test_converted_prompt.md"
    with open(test_output, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"\nTest conversion saved to: {test_output}")
    print("Review the output and adjust the conversion logic if needed.")

if __name__ == "__main__":
    main()