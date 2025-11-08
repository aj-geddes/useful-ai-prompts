#!/bin/bash
################################################################################
# Security Scan Hook for Claude Code
# Scans for secrets, API keys, and sensitive data before commits
################################################################################

set -euo pipefail

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || echo "$PWD")"
SECRETS_IGNORE="${PROJECT_ROOT}/.secretsignore"
SCAN_MODE="${SCAN_MODE:-normal}"  # strict, normal, permissive
MAX_FILE_SIZE="${MAX_FILE_SIZE:-1048576}"  # 1MB
EXCLUDED_DIRS="${EXCLUDED_DIRS:-node_modules|vendor|.git|dist|build}"

# Colors and formatting
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
BOLD='\033[1m'
NC='\033[0m' # No Color

# Secret patterns
declare -A PATTERNS=(
    # AWS
    ["AWS Access Key"]='(A3T[A-Z0-9]|AKIA|AGPA|AIDA|AROA|AIPA|ANPA|ANVA|ASIA)[A-Z0-9]{16}'
    ["AWS Secret Key"]='aws_secret_access_key\s*=\s*['\''"][A-Za-z0-9/+=]{40}['\''"]'
    ["AWS Session Token"]='aws_session_token\s*=\s*['\''"][A-Za-z0-9/+=]{100,}['\''"]'

    # GitHub
    ["GitHub Token"]='gh[pousr]_[0-9a-zA-Z]{36,}'
    ["GitHub PAT"]='github_pat_[0-9a-zA-Z]{22}_[0-9a-zA-Z]{59}'

    # Generic API Keys
    ["API Key"]='api[_-]?key\s*[=:]\s*['\''"][a-zA-Z0-9_\-]{20,}['\''"]'
    ["Bearer Token"]='[Bb]earer\s+[a-zA-Z0-9_\-\.]{20,}'

    # Private Keys
    ["RSA Private Key"]='-----BEGIN RSA PRIVATE KEY-----'
    ["SSH Private Key"]='-----BEGIN OPENSSH PRIVATE KEY-----'
    ["PEM Private Key"]='-----BEGIN PRIVATE KEY-----'
    ["EC Private Key"]='-----BEGIN EC PRIVATE KEY-----'

    # OAuth
    ["OAuth Token"]='[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}'

    # JWT
    ["JWT Token"]='eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}'

    # Database
    ["Database URL"]='[a-zA-Z]+://[^:]+:[^@]+@[^/]+/[a-zA-Z0-9_]+'
    ["PostgreSQL Password"]='postgres://[^:]+:[^@]{8,}@'
    ["MySQL Password"]='mysql://[^:]+:[^@]{8,}@'

    # Passwords
    ["Password Assignment"]='password\s*[=:]\s*['\''"][^'\''"\s]{8,}['\''"]'
    ["Secret Assignment"]='secret\s*[=:]\s*['\''"][^'\''"\s]{16,}['\''"]'

    # Cloud Services
    ["Slack Token"]='xox[baprs]-[0-9a-zA-Z]{10,}'
    ["Stripe Key"]='sk_live_[0-9a-zA-Z]{24,}'
    ["Google API Key"]='AIza[0-9A-Za-z_-]{35}'
    ["Azure Key"]='[a-zA-Z0-9/+=]{88}=='
    ["Twilio API Key"]='SK[0-9a-fA-F]{32}'

    # Generic Secrets
    ["Base64 Secret"]='['\''"][A-Za-z0-9+/]{40,}={0,2}['\''"]'
    ["Hex Secret"]='['\''"][a-fA-F0-9]{32,}['\''"]'
)

# Exit codes
EXIT_SUCCESS=0
EXIT_SECRETS_FOUND=1
EXIT_ERROR=2

################################################################################
# Functions
################################################################################

print_header() {
    echo -e "${BLUE}${BOLD}🔒 Security Scan Starting...${NC}"
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""
}

print_footer() {
    echo ""
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
}

print_success() {
    echo -e "${GREEN}${BOLD}✅ Security Scan Passed${NC}"
    echo -e "${GREEN}No secrets detected in staged files${NC}"
}

print_error() {
    local count=$1
    echo -e "${RED}${BOLD}❌ SECURITY ISSUE DETECTED${NC}"
    echo ""
    echo -e "${RED}Found ${BOLD}${count}${NC}${RED} potential secret(s) in staged files:${NC}"
    echo ""
}

print_remediation() {
    echo ""
    echo -e "${YELLOW}${BOLD}⚠️  COMMIT BLOCKED - Remove secrets before committing${NC}"
    echo ""
    echo -e "${YELLOW}Remediation steps:${NC}"
    echo -e "  1. Remove the secrets from your code"
    echo -e "  2. Use environment variables instead: process.env.API_KEY"
    echo -e "  3. Add secrets to .env file (ensure .env is in .gitignore)"
    echo -e "  4. Update .secretsignore if these are false positives"
    echo -e "  5. Rotate any exposed credentials immediately"
    echo ""
}

load_whitelist() {
    local whitelist=()
    if [[ -f "$SECRETS_IGNORE" ]]; then
        while IFS= read -r line; do
            # Skip comments and empty lines
            [[ "$line" =~ ^#.*$ || -z "$line" ]] && continue
            whitelist+=("$line")
        done < "$SECRETS_IGNORE"
    fi
    printf '%s\n' "${whitelist[@]}"
}

is_whitelisted() {
    local content="$1"
    local whitelist
    whitelist=$(load_whitelist)

    if [[ -z "$whitelist" ]]; then
        return 1
    fi

    while IFS= read -r pattern; do
        if [[ "$content" =~ $pattern ]]; then
            return 0
        fi
    done <<< "$whitelist"

    return 1
}

check_git_command() {
    local args="$1"

    # Check if this is a git commit command
    if [[ "$args" =~ git[[:space:]]+commit ]]; then
        return 0
    fi

    return 1
}

get_staged_files() {
    if git rev-parse --git-dir > /dev/null 2>&1; then
        git diff --cached --name-only --diff-filter=ACMR 2>/dev/null || true
    else
        # Not in a git repo, return empty
        echo ""
    fi
}

scan_file() {
    local file="$1"
    local findings=0

    # Skip if file doesn't exist
    [[ ! -f "$file" ]] && return 0

    # Skip if file is too large
    local size
    size=$(stat -f%z "$file" 2>/dev/null || stat -c%s "$file" 2>/dev/null || echo 0)
    if [[ $size -gt $MAX_FILE_SIZE ]]; then
        return 0
    fi

    # Skip binary files
    if file "$file" | grep -q "binary"; then
        return 0
    fi

    # Scan for each pattern
    for pattern_name in "${!PATTERNS[@]}"; do
        local pattern="${PATTERNS[$pattern_name]}"

        # Search for pattern
        local matches
        matches=$(grep -nE "$pattern" "$file" 2>/dev/null || true)

        if [[ -n "$matches" ]]; then
            # Check each match against whitelist
            while IFS=: read -r line_num line_content; do
                if ! is_whitelisted "$line_content"; then
                    echo -e "  ${YELLOW}📄 ${file}${NC}"
                    echo -e "     Line ${line_num}: ${line_content:0:80}"
                    echo -e "     Pattern: ${BOLD}${pattern_name}${NC}"
                    echo ""
                    ((findings++))
                fi
            done <<< "$matches"
        fi
    done

    return $findings
}

scan_files() {
    local files=("$@")
    local total_findings=0

    for file in "${files[@]}"; do
        # Skip excluded directories
        if [[ "$file" =~ ($EXCLUDED_DIRS) ]]; then
            continue
        fi

        scan_file "$file"
        total_findings=$((total_findings + $?))
    done

    return $total_findings
}

main() {
    # Parse input - Claude Code passes the command as argument
    local command="${1:-}"

    # Only run for git commit commands
    if ! check_git_command "$command"; then
        exit $EXIT_SUCCESS
    fi

    print_header

    # Get staged files
    local staged_files
    mapfile -t staged_files < <(get_staged_files)

    if [[ ${#staged_files[@]} -eq 0 ]]; then
        echo -e "${YELLOW}⚠️  No staged files to scan${NC}"
        print_footer
        exit $EXIT_SUCCESS
    fi

    echo -e "${BLUE}Scanning ${#staged_files[@]} staged file(s)...${NC}"
    echo ""

    # Scan files
    local findings
    scan_files "${staged_files[@]}"
    findings=$?

    if [[ $findings -eq 0 ]]; then
        print_success
        print_footer
        exit $EXIT_SUCCESS
    else
        print_error "$findings"
        # Findings were already printed by scan_files
        print_remediation
        print_footer

        if [[ "$SCAN_MODE" == "permissive" ]]; then
            echo -e "${YELLOW}⚠️  Running in permissive mode - allowing commit${NC}"
            exit $EXIT_SUCCESS
        else
            exit $EXIT_SECRETS_FOUND
        fi
    fi
}

# Run main function
main "$@"
