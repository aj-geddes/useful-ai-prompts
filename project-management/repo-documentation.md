Temperature: 0

Review the entire codebase in this repository and generate factual, evidence-based documentation. Generate ONLY documentation that can be directly supported by evidence in the code. This is a deterministic task where creativity and variation are NOT desired.

1. README.md - Based EXCLUSIVELY on actual repository contents:
   
   ## Header Section
   - Project name (extract directly from package.json, setup.py, pom.xml, or similar manifest files)
   - Status badges - Include ONLY for CI/CD systems with configuration files present:
     * GitHub Actions badges: Only if .github/workflows/*.yml exists
     * CircleCI badges: Only if .circleci/config.yml exists
     * Jenkins badges: Only if Jenkinsfile exists
     * Test coverage badge: Only if coverage configuration exists
     * Release version: Only if version is explicitly defined in the codebase
     * Dependency status: Only if dependabot.yml or similar exists
   
   ## Core Content
   - Project description: Use EXACT description from manifest files or main module docstrings
   - Features list: ONLY features with corresponding implemented code
   - Installation instructions: Based SOLELY on actual setup scripts and declared dependencies
   - Configuration: Document ONLY environment variables and options actually referenced in code
   
   ## Project Structure
   - Provide exact directory structure with file counts
   - List main modules with their exact functions/classes count
   - Document actual, current dependencies with precise versions

2. Additional Documentation - Create ONLY if substantial relevant code exists:
   - API.md: Document ONLY endpoints with actual implementations
   - ARCHITECTURE.md: Describe ONLY patterns and components explicitly in the code
   - DEVELOPMENT.md: Document ONLY workflows configured in the repository

3. For all documentation:
   - If a fact cannot be verified in the code, DO NOT include it
   - Use precise language that reflects certainty based on evidence
   - Include exact file paths as references for all documented features
   - Do not speculate about intended functionality - document only what exists

Before generating content:
1. Create an inventory of all files in the repository
2. Identify configurations for build systems, testing frameworks, and CI/CD pipelines
3. Extract metadata from manifest files and build configurations
4. Document only what is objectively present in the code

This task requires zero creativity - document exactly what exists in a clear, organized format.
