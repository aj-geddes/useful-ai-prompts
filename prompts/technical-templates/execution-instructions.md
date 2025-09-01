# Execution Instructions for AI Prompt Research Assistant

The following instructions guide the continuous research and development of useful AI prompts for the GitHub repository at https://github.com/aj-geddes/useful-ai-prompts.

## Initialization Process

1. Begin by creating a project research index:
   - Read the job categories, workflow categories, thinking approaches, and persona profiles
   - Create a prioritization matrix based on potential impact and utility
   - Establish initial research focus areas

2. For each research cycle:
   ```
   CYCLE_ID="PROMPT-$(date +%Y%m%d-%H%M%S)"
   TARGET_DOMAIN=[Select from job categories]
   TARGET_WORKFLOW=[Select from workflow categories]
   THINKING_APPROACH=[Select 1-2 from thinking approaches]
   PRIMARY_PERSONA=[Select from persona profiles]
   SECONDARY_PERSONA=[Optional: Select complementary persona]
   ```

## Research Loop

For each prompt development cycle, execute this research loop:

1. **Domain & Workflow Analysis**

   ```
   Research current best practices for $TARGET_DOMAIN in $TARGET_WORKFLOW
   Identify key challenges and pain points
   Document workflow steps and decision points
   Research existing prompt approaches for similar tasks
   ```

2. **Persona & Thinking Layer Integration**

   ```
   Apply $PRIMARY_PERSONA perspective to workflow challenges
   Layer with $THINKING_APPROACH methodology
   If $SECONDARY_PERSONA defined, integrate complementary viewpoint
   Create initial prompt structure with layered instructions
   ```

3. **Prompt Development**

   ```
   Draft prompt with:
    - Clear context setting
    - Persona-specific instruction layer
    - Thinking methodology guidance
    - Output format specifications
    - Examples where appropriate
   Add customization variables using {{placeholder}} syntax
   Include safeguards and guardrails
   ```

4. **Testing & Refinement**

   ```
   Test prompt against sample scenarios
   Identify edge cases and limitations
   Refine language for clarity and effectiveness
   Add usage instructions and examples
   Document research findings
   ```

5. **Documentation & Commit**

   ```
   Create prompt file following repository structure:
     prompts/$CATEGORY/$SUBCATEGORY/$PROMPT_NAME.md

   Complete all metadata fields
   Add comprehensive usage instructions
   Include concrete examples
   Document research findings

   Commit with message:
   "Add $PROMPT_NAME: $BRIEF_DESCRIPTION"
   ```

6. **Cross-Reference & Index Update**
   ```
   Update related prompts with cross-references
   Add to appropriate index files
   Tag with relevant categories for searchability
   ```

## Selection Criteria

When selecting job and workflow combinations to prioritize:

1. **High-Impact Areas**:
   - Frequently performed workflows with significant time investment
   - Tasks requiring complex cognitive processes
   - Areas where AI assistance can provide substantial value
   - Workflows with clear inputs and outputs

2. **Layering Strategy**:
   - Pair analytical personas with creative workflows
   - Layer strategic thinking with tactical execution
   - Combine domain expertise with methodological frameworks
   - Create unexpected but valuable combinations

3. **Progressive Development**:
   - Start with foundational prompts for common workflows
   - Build toward specialized, niche applications
   - Develop prompt chains for complex processes
   - Create meta-prompts that help develop other prompts

## Continuous Research Focuses

Maintain ongoing research in these key areas:

1. **Prompt Effectiveness**:
   - Techniques for improving response quality
   - Methods for handling edge cases
   - Approaches for maintaining context in complex workflows
   - Strategies for optimizing different thinking layers

2. **Taxonomy Development**:
   - Refine categorization system
   - Develop cross-cutting tags for better discoverability
   - Identify emerging workflow patterns
   - Create relationship maps between prompts

3. **Use Case Expansion**:
   - Identify new professional domains
   - Discover emerging workflow needs
   - Research novel applications of AI assistance
   - Document real-world implementation examples

## Output Standards

Every prompt must meet these standards:

1. **Utility**: Solves a specific, practical problem
2. **Clarity**: Instructions clear enough for consistent results
3. **Adaptability**: Includes customization points
4. **Documentation**: Complete usage instructions and examples
5. **Layering**: Incorporates multiple thinking approaches
6. **Personalization**: Leverages relevant persona perspectives
7. **Reproducibility**: Produces consistent results when used as directed
8. **Originality**: Offers unique value not found in existing prompts

## Commit Cycle

For each new prompt:

1. Create file following naming convention:

   ```
   prompts/<domain>/<workflow>/<approach>-<persona>-<task>.md
   ```

2. Complete prompt template with all required sections:

   ```markdown
   # [Prompt Title]

   ## Metadata
- **Created**: 2025-01-15

   - **Category**: [Primary Category]
   - **Tags**: [comma, separated, relevant, tags]
   - **Version**: [X.Y.Z]
   - **Personas**: [Primary persona, Secondary persona]
   - **Use Cases**: [comma separated use cases]
   - **Compatible Models**: [list of compatible models]

   ## Description

   [Clear explanation of the prompt's purpose and context]

   ## Prompt Template
   ```

   [Actual prompt text with {{placeholders}} for customization]

   ```

   ## Usage Instructions
   [Step-by-step guidance on effective use]

   ## Examples
   ### Example 1: [Brief description]
   **Input**: [Sample input]
   **Output**: [Example of expected output]

   ## Related Prompts
   [Links to related prompts]

   ## Research Notes
   [Insights from testing and development]
   ```

3. Commit with descriptive message

4. Continue to next prompt in the development cycle

## Weekly Progress Report

Generate a weekly summary including:

- Number of new prompts created
- Domains and workflows covered
- Emerging patterns and insights
- Recommendations for next focus areas
- Statistics on prompt categories and distributions
