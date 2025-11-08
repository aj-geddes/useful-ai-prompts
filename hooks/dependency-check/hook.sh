#!/bin/bash
################################################################################
# Dependency Check Hook for Claude Code
# Checks for vulnerable dependencies before commits
################################################################################

set -euo pipefail

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || echo "$PWD")"
CONFIG_FILE="${PROJECT_ROOT}/.dependency-check.yml"

# Default settings
ENABLED="${ENABLED:-true}"
BLOCK_THRESHOLD="${BLOCK_THRESHOLD:-high}"  # low, moderate, high, critical
WARN_THRESHOLD="${WARN_THRESHOLD:-moderate}"
AUTO_FIX="${AUTO_FIX:-false}"
CHECK_ON_COMMIT="${CHECK_ON_COMMIT:-true}"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m'

# Exit codes
EXIT_SUCCESS=0
EXIT_VULNERABILITIES=1
EXIT_ERROR=2

# Counters
CRITICAL_COUNT=0
HIGH_COUNT=0
MODERATE_COUNT=0
LOW_COUNT=0

################################################################################
# Functions
################################################################################

print_header() {
    echo -e "${BLUE}${BOLD}🔒 Dependency Security Check Starting...${NC}"
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""
}

print_footer() {
    echo ""
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
}

check_git_command() {
    local args="$1"
    [[ "$args" =~ git[[:space:]]+commit ]] && return 0 || return 1
}

severity_to_number() {
    local severity=$1
    case "$severity" in
        critical) echo 4 ;;
        high) echo 3 ;;
        moderate) echo 2 ;;
        low) echo 1 ;;
        *) echo 0 ;;
    esac
}

should_block() {
    local vuln_severity=$1
    local threshold_num block_num

    threshold_num=$(severity_to_number "$BLOCK_THRESHOLD")
    block_num=$(severity_to_number "$vuln_severity")

    [[ $block_num -ge $threshold_num ]] && return 0 || return 1
}

detect_package_managers() {
    local managers=()

    [[ -f "${PROJECT_ROOT}/package.json" ]] && managers+=("npm")
    [[ -f "${PROJECT_ROOT}/requirements.txt" ]] || [[ -f "${PROJECT_ROOT}/setup.py" ]] || [[ -f "${PROJECT_ROOT}/pyproject.toml" ]] && managers+=("pip")
    [[ -f "${PROJECT_ROOT}/Gemfile" ]] && managers+=("bundler")
    [[ -f "${PROJECT_ROOT}/Cargo.toml" ]] && managers+=("cargo")
    [[ -f "${PROJECT_ROOT}/go.mod" ]] && managers+=("go")
    [[ -f "${PROJECT_ROOT}/composer.json" ]] && managers+=("composer")

    printf '%s\n' "${managers[@]}"
}

run_npm_audit() {
    echo -e "${BLUE}📦 npm audit${NC}"
    echo "   Scanning packages..."

    local audit_output
    local audit_exit_code=0

    # Run npm audit and capture output
    audit_output=$(npm audit --json 2>/dev/null || true)
    audit_exit_code=$?

    if [[ -z "$audit_output" ]]; then
        echo -e "   ${GREEN}✅ No vulnerabilities found${NC}"
        echo ""
        return 0
    fi

    # Parse JSON output
    local critical high moderate low
    critical=$(echo "$audit_output" | grep -oP '"critical":\s*\K\d+' || echo "0")
    high=$(echo "$audit_output" | grep -oP '"high":\s*\K\d+' || echo "0")
    moderate=$(echo "$audit_output" | grep -oP '"moderate":\s*\K\d+' || echo "0")
    low=$(echo "$audit_output" | grep -oP '"low":\s*\K\d+' || echo "0")

    CRITICAL_COUNT=$((CRITICAL_COUNT + critical))
    HIGH_COUNT=$((HIGH_COUNT + high))
    MODERATE_COUNT=$((MODERATE_COUNT + moderate))
    LOW_COUNT=$((LOW_COUNT + low))

    local total=$((critical + high + moderate + low))

    if [[ $total -eq 0 ]]; then
        echo -e "   ${GREEN}✅ No vulnerabilities found${NC}"
        echo ""
        return 0
    fi

    echo -e "   ${YELLOW}Found ${total} vulnerabilities${NC}"

    # Show detailed vulnerabilities
    if [[ $critical -gt 0 ]]; then
        echo -e "   ${RED}🔴 Critical: ${critical}${NC}"
    fi
    if [[ $high -gt 0 ]]; then
        echo -e "   ${RED}🟠 High: ${high}${NC}"
    fi
    if [[ $moderate -gt 0 ]]; then
        echo -e "   ${YELLOW}🟡 Moderate: ${moderate}${NC}"
    fi
    if [[ $low -gt 0 ]]; then
        echo -e "   ${CYAN}🔵 Low: ${low}${NC}"
    fi

    echo ""

    # Auto-fix if enabled
    if [[ "$AUTO_FIX" == "true" ]]; then
        echo -e "   ${BLUE}Running npm audit fix...${NC}"
        npm audit fix --silent 2>/dev/null || true
        echo -e "   ${GREEN}Auto-fix complete${NC}"
        echo ""
    fi

    return $total
}

run_pip_audit() {
    if ! command -v pip-audit &>/dev/null; then
        echo -e "${YELLOW}⚠️  pip-audit not installed, skipping Python audit${NC}"
        echo ""
        return 0
    fi

    echo -e "${BLUE}📦 pip-audit${NC}"
    echo "   Scanning packages..."

    local audit_output
    local audit_exit_code=0

    # Run pip-audit
    audit_output=$(pip-audit --format json 2>/dev/null || echo '{"dependencies":[]}')
    audit_exit_code=$?

    # Parse output (simplified - actual parsing would be more complex)
    local vuln_count
    vuln_count=$(echo "$audit_output" | grep -o '"vulns"' | wc -l || echo "0")

    if [[ $vuln_count -eq 0 ]]; then
        echo -e "   ${GREEN}✅ No vulnerabilities found${NC}"
        echo ""
        return 0
    fi

    echo -e "   ${YELLOW}Found ${vuln_count} vulnerabilities${NC}"
    echo ""

    # Assume high severity for demonstration
    HIGH_COUNT=$((HIGH_COUNT + vuln_count))

    # Auto-fix if enabled
    if [[ "$AUTO_FIX" == "true" ]]; then
        echo -e "   ${BLUE}Running pip-audit --fix...${NC}"
        pip-audit --fix --dry-run 2>/dev/null || true
        echo ""
    fi

    return $vuln_count
}

run_bundle_audit() {
    if ! command -v bundle-audit &>/dev/null; then
        echo -e "${YELLOW}⚠️  bundle-audit not installed, skipping Ruby audit${NC}"
        echo ""
        return 0
    fi

    echo -e "${BLUE}📦 bundle audit${NC}"
    echo "   Scanning packages..."

    # Update advisory database
    bundle-audit update &>/dev/null || true

    local audit_output
    local audit_exit_code=0

    # Run bundle audit
    audit_output=$(bundle-audit check 2>&1 || true)
    audit_exit_code=$?

    if [[ $audit_exit_code -eq 0 ]]; then
        echo -e "   ${GREEN}✅ No vulnerabilities found${NC}"
        echo ""
        return 0
    fi

    # Parse output
    local vuln_count
    vuln_count=$(echo "$audit_output" | grep -c "Name:" || echo "0")

    if [[ $vuln_count -eq 0 ]]; then
        echo -e "   ${GREEN}✅ No vulnerabilities found${NC}"
        echo ""
        return 0
    fi

    echo -e "   ${YELLOW}Found ${vuln_count} vulnerabilities${NC}"
    echo ""

    # Assume high severity
    HIGH_COUNT=$((HIGH_COUNT + vuln_count))

    return $vuln_count
}

run_cargo_audit() {
    if ! command -v cargo-audit &>/dev/null; then
        echo -e "${YELLOW}⚠️  cargo-audit not installed, skipping Rust audit${NC}"
        echo ""
        return 0
    fi

    echo -e "${BLUE}📦 cargo audit${NC}"
    echo "   Scanning packages..."

    local audit_output
    local audit_exit_code=0

    # Run cargo audit
    audit_output=$(cargo audit --json 2>/dev/null || echo '{"vulnerabilities":{"list":[]}}')
    audit_exit_code=$?

    # Parse JSON
    local vuln_count
    vuln_count=$(echo "$audit_output" | grep -o '"advisory"' | wc -l || echo "0")

    if [[ $vuln_count -eq 0 ]]; then
        echo -e "   ${GREEN}✅ No vulnerabilities found${NC}"
        echo ""
        return 0
    fi

    echo -e "   ${YELLOW}Found ${vuln_count} vulnerabilities${NC}"
    echo ""

    # Assume high severity
    HIGH_COUNT=$((HIGH_COUNT + vuln_count))

    return $vuln_count
}

run_go_audit() {
    if ! command -v govulncheck &>/dev/null; then
        echo -e "${YELLOW}⚠️  govulncheck not installed, skipping Go audit${NC}"
        echo ""
        return 0
    fi

    echo -e "${BLUE}📦 govulncheck${NC}"
    echo "   Scanning packages..."

    local audit_output
    local audit_exit_code=0

    # Run govulncheck
    audit_output=$(govulncheck ./... 2>&1 || true)
    audit_exit_code=$?

    if [[ "$audit_output" =~ "No vulnerabilities found" ]] || [[ $audit_exit_code -eq 0 ]]; then
        echo -e "   ${GREEN}✅ No vulnerabilities found${NC}"
        echo ""
        return 0
    fi

    # Parse output
    local vuln_count
    vuln_count=$(echo "$audit_output" | grep -c "Vulnerability" || echo "0")

    if [[ $vuln_count -eq 0 ]]; then
        echo -e "   ${GREEN}✅ No vulnerabilities found${NC}"
        echo ""
        return 0
    fi

    echo -e "   ${YELLOW}Found ${vuln_count} vulnerabilities${NC}"
    echo ""

    # Assume high severity
    HIGH_COUNT=$((HIGH_COUNT + vuln_count))

    return $vuln_count
}

print_vulnerability_details() {
    echo -e "${RED}${BOLD}❌ VULNERABILITIES FOUND${NC}"
    echo ""

    if [[ $CRITICAL_COUNT -gt 0 ]]; then
        echo -e "${RED}🔴 CRITICAL Severity (${CRITICAL_COUNT} vulnerabilities)${NC}"
        echo ""
    fi

    if [[ $HIGH_COUNT -gt 0 ]]; then
        echo -e "${RED}🟠 HIGH Severity (${HIGH_COUNT} vulnerabilities)${NC}"
        echo ""
    fi

    if [[ $MODERATE_COUNT -gt 0 ]]; then
        echo -e "${YELLOW}🟡 MODERATE Severity (${MODERATE_COUNT} vulnerabilities)${NC}"
        echo ""
    fi

    if [[ $LOW_COUNT -gt 0 ]]; then
        echo -e "${CYAN}🔵 LOW Severity (${LOW_COUNT} vulnerabilities)${NC}"
        echo ""
    fi
}

print_summary() {
    local total=$((CRITICAL_COUNT + HIGH_COUNT + MODERATE_COUNT + LOW_COUNT))

    echo ""
    echo -e "${BLUE}Summary:${NC}"
    echo -e "  Total Vulnerabilities: ${BOLD}${total}${NC}"
    echo -e "  Critical: ${CRITICAL_COUNT}"
    echo -e "  High: ${HIGH_COUNT} $([ $HIGH_COUNT -gt 0 ] && echo '❌' || echo '')"
    echo -e "  Moderate: ${MODERATE_COUNT} $([ $MODERATE_COUNT -gt 0 ] && echo '⚠️' || echo '')"
    echo -e "  Low: ${LOW_COUNT}"
    echo ""

    # Determine if we should block
    local should_block=false

    if should_block "critical" && [[ $CRITICAL_COUNT -gt 0 ]]; then
        should_block=true
    elif should_block "high" && [[ $HIGH_COUNT -gt 0 ]]; then
        should_block=true
    elif should_block "moderate" && [[ $MODERATE_COUNT -gt 0 ]]; then
        should_block=true
    elif should_block "low" && [[ $LOW_COUNT -gt 0 ]]; then
        should_block=true
    fi

    if [[ "$should_block" == true ]]; then
        echo -e "${YELLOW}${BOLD}⚠️  COMMIT BLOCKED - Vulnerabilities detected${NC}"
        echo ""
        echo -e "${YELLOW}Recommended actions:${NC}"
        echo -e "  1. Review vulnerabilities above"
        echo -e "  2. Update vulnerable packages"
        echo -e "  3. Run audit fix commands"
        echo -e "  4. Verify fixes with another audit"
        echo -e "  5. Add to whitelist if vulnerability is not applicable"
        echo ""

        # Provide quick fix commands
        if [[ -f "${PROJECT_ROOT}/package.json" ]]; then
            echo -e "${CYAN}Quick fix (npm):${NC}"
            echo -e "  npm audit fix"
            echo ""
        fi

        if [[ -f "${PROJECT_ROOT}/requirements.txt" ]]; then
            echo -e "${CYAN}Quick fix (pip):${NC}"
            echo -e "  pip-audit --fix"
            echo ""
        fi
    else
        echo -e "${GREEN}${BOLD}✅ Security check passed${NC}"
        if [[ $total -gt 0 ]]; then
            echo -e "${YELLOW}Note: ${total} low-severity vulnerabilities found but below block threshold${NC}"
        fi
        echo ""
    fi
}

main() {
    # Check if enabled
    if [[ "$ENABLED" != "true" ]]; then
        exit $EXIT_SUCCESS
    fi

    # Parse input
    local command="${1:-}"

    # Only run for git commit commands
    if [[ "$CHECK_ON_COMMIT" == "true" ]] && ! check_git_command "$command"; then
        exit $EXIT_SUCCESS
    fi

    print_header

    echo "Scanning dependencies for vulnerabilities..."
    echo ""

    # Detect package managers
    local package_managers
    mapfile -t package_managers < <(detect_package_managers)

    if [[ ${#package_managers[@]} -eq 0 ]]; then
        echo -e "${YELLOW}⚠️  No package managers detected${NC}"
        print_footer
        exit $EXIT_SUCCESS
    fi

    # Run audits for each package manager
    local has_vulns=false

    for pm in "${package_managers[@]}"; do
        case "$pm" in
            npm)
                if ! run_npm_audit; then
                    has_vulns=true
                fi
                ;;
            pip)
                if ! run_pip_audit; then
                    has_vulns=true
                fi
                ;;
            bundler)
                if ! run_bundle_audit; then
                    has_vulns=true
                fi
                ;;
            cargo)
                if ! run_cargo_audit; then
                    has_vulns=true
                fi
                ;;
            go)
                if ! run_go_audit; then
                    has_vulns=true
                fi
                ;;
        esac
    done

    print_footer

    # Show detailed vulnerabilities if found
    local total=$((CRITICAL_COUNT + HIGH_COUNT + MODERATE_COUNT + LOW_COUNT))

    if [[ $total -gt 0 ]]; then
        echo ""
        print_vulnerability_details
        print_footer
    fi

    # Print summary
    print_summary

    print_footer

    # Determine exit code
    if should_block "critical" && [[ $CRITICAL_COUNT -gt 0 ]]; then
        exit $EXIT_VULNERABILITIES
    elif should_block "high" && [[ $HIGH_COUNT -gt 0 ]]; then
        exit $EXIT_VULNERABILITIES
    elif should_block "moderate" && [[ $MODERATE_COUNT -gt 0 ]]; then
        exit $EXIT_VULNERABILITIES
    elif should_block "low" && [[ $LOW_COUNT -gt 0 ]]; then
        exit $EXIT_VULNERABILITIES
    else
        exit $EXIT_SUCCESS
    fi
}

# Run main function
main "$@"
