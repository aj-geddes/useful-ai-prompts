#!/bin/bash
################################################################################
# Breaking Change Detection Hook for Claude Code
# Detects breaking API changes before commits
################################################################################

set -euo pipefail

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || echo "$PWD")"
CONFIG_FILE="${PROJECT_ROOT}/.breaking-changes.yml"

# Default settings
ENABLED="${ENABLED:-true}"
STRICTNESS="${STRICTNESS:-normal}"  # strict, normal, permissive
ALLOW_BREAKING_CHANGES="${ALLOW_BREAKING_CHANGES:-false}"

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
EXIT_BREAKING_CHANGES=1
EXIT_ERROR=2

# Counters
BREAKING_COUNT=0
WARNING_COUNT=0

################################################################################
# Functions
################################################################################

print_header() {
    echo -e "${BLUE}${BOLD}🔍 Breaking Change Detection Starting...${NC}"
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

get_staged_files() {
    if git rev-parse --git-dir > /dev/null 2>&1; then
        git diff --cached --name-only --diff-filter=ACMR 2>/dev/null || true
    else
        echo ""
    fi
}

should_check_file() {
    local file=$1

    # Only check source code files
    case "$file" in
        *.js|*.ts|*.jsx|*.tsx|*.py|*.rb|*.go|*.rs|*.java|*.php)
            # Exclude test files
            if [[ "$file" =~ \.(test|spec)\. ]]; then
                return 1
            fi
            # Exclude internal directories
            if [[ "$file" =~ /internal/ ]]; then
                return 1
            fi
            return 0
            ;;
        *)
            return 1
            ;;
    esac
}

extract_exports_js() {
    local file=$1

    # Extract exported functions, classes, and variables
    {
        # Named exports: export function foo() / export class Foo / export const foo
        grep -oP '^\s*export\s+(function|class|const|let|var)\s+\K\w+' "$file" 2>/dev/null || true

        # Default exports (harder to track)
        grep -oP '^\s*export\s+default\s+(function\s+)?\K\w+' "$file" 2>/dev/null || true

        # export { foo, bar }
        grep -oP '^\s*export\s*\{[^}]+\}' "$file" 2>/dev/null | \
            grep -oP '\w+' || true
    } | sort -u
}

extract_exports_py() {
    local file=$1

    # Extract functions and classes (Python has implicit exports)
    {
        # Functions: def foo():
        grep -oP '^\s*def\s+\K\w+' "$file" 2>/dev/null | \
            grep -v '^_' || true  # Exclude private functions

        # Classes: class Foo:
        grep -oP '^\s*class\s+\K\w+' "$file" 2>/dev/null | \
            grep -v '^_' || true  # Exclude private classes

        # Explicit exports in __all__
        grep -oP '__all__\s*=\s*\[([^\]]+)\]' "$file" 2>/dev/null | \
            grep -oP '["'"'"']\K\w+(?=["'"'"'])' || true
    } | sort -u
}

extract_exports_rb() {
    local file=$1

    # Extract Ruby methods and classes
    {
        # Methods: def foo
        grep -oP '^\s*def\s+\K\w+' "$file" 2>/dev/null || true

        # Classes: class Foo
        grep -oP '^\s*class\s+\K\w+' "$file" 2>/dev/null || true

        # Modules: module Foo
        grep -oP '^\s*module\s+\K\w+' "$file" 2>/dev/null || true
    } | sort -u
}

extract_exports_go() {
    local file=$1

    # Extract exported functions and types (capitalized in Go)
    {
        # Functions: func Foo()
        grep -oP '^\s*func\s+\K[A-Z]\w+' "$file" 2>/dev/null || true

        # Types: type Foo
        grep -oP '^\s*type\s+\K[A-Z]\w+' "$file" 2>/dev/null || true
    } | sort -u
}

extract_function_signature_js() {
    local file=$1
    local func_name=$2

    # Extract function signature
    grep -A 1 "export.*function\s\+$func_name\s*(" "$file" 2>/dev/null | \
        grep -oP '\([^)]*\)' | head -n 1 || echo ""
}

extract_function_signature_py() {
    local file=$1
    local func_name=$2

    # Extract function signature
    grep "def\s\+$func_name\s*(" "$file" 2>/dev/null | \
        grep -oP '\([^)]*\)' | head -n 1 || echo ""
}

get_file_exports() {
    local file=$1
    local extension="${file##*.}"

    case "$extension" in
        js|jsx|ts|tsx)
            extract_exports_js "$file"
            ;;
        py)
            extract_exports_py "$file"
            ;;
        rb)
            extract_exports_rb "$file"
            ;;
        go)
            extract_exports_go "$file"
            ;;
        *)
            echo ""
            ;;
    esac
}

get_old_file_content() {
    local file=$1

    # Get file content from HEAD (before changes)
    git show HEAD:"$file" 2>/dev/null || echo ""
}

detect_removed_exports() {
    local file=$1
    local old_content=$2

    # Create temp files for comparison
    local old_file="/tmp/breaking-old-$$"
    local new_file="/tmp/breaking-new-$$"

    echo "$old_content" > "$old_file"

    # Get exports from old and new versions
    local old_exports
    local new_exports

    old_exports=$(get_file_exports "$old_file")
    new_exports=$(get_file_exports "$file")

    # Find removed exports
    local removed
    removed=$(comm -23 <(echo "$old_exports" | sort) <(echo "$new_exports" | sort))

    # Clean up
    rm -f "$old_file" "$new_file"

    if [[ -n "$removed" ]]; then
        while IFS= read -r export_name; do
            [[ -z "$export_name" ]] && continue

            echo -e "  ${RED}❌ BREAKING: Export removed${NC}"
            echo -e "     Export: ${BOLD}${export_name}${NC}"
            echo -e "     Impact: Function/class no longer available to consumers"
            echo ""

            ((BREAKING_COUNT++))
        done <<< "$removed"
    fi
}

detect_signature_changes() {
    local file=$1
    local old_content=$2

    local extension="${file##*.}"

    # Create temp file for old content
    local old_file="/tmp/breaking-old-$$"
    echo "$old_content" > "$old_file"

    # Get common exports (not removed)
    local old_exports new_exports common_exports
    old_exports=$(get_file_exports "$old_file")
    new_exports=$(get_file_exports "$file")
    common_exports=$(comm -12 <(echo "$old_exports" | sort) <(echo "$new_exports" | sort))

    # Check signature changes for common exports
    while IFS= read -r export_name; do
        [[ -z "$export_name" ]] && continue

        local old_sig new_sig

        case "$extension" in
            js|jsx|ts|tsx)
                old_sig=$(extract_function_signature_js "$old_file" "$export_name")
                new_sig=$(extract_function_signature_js "$file" "$export_name")
                ;;
            py)
                old_sig=$(extract_function_signature_py "$old_file" "$export_name")
                new_sig=$(extract_function_signature_py "$file" "$export_name")
                ;;
            *)
                continue
                ;;
        esac

        if [[ -n "$old_sig" ]] && [[ -n "$new_sig" ]] && [[ "$old_sig" != "$new_sig" ]]; then
            echo -e "  ${RED}❌ BREAKING: Function signature changed${NC}"
            echo -e "     Function: ${BOLD}${export_name}${NC}"
            echo -e "     Before: ${CYAN}${export_name}${old_sig}${NC}"
            echo -e "     After:  ${CYAN}${export_name}${new_sig}${NC}"
            echo -e "     Impact: All callers must be updated"
            echo ""

            ((BREAKING_COUNT++))
        fi
    done <<< "$common_exports"

    # Clean up
    rm -f "$old_file"
}

check_file_changes() {
    local file=$1

    echo -e "${BLUE}📄 ${file}${NC}"
    echo ""

    # Get old file content
    local old_content
    old_content=$(get_old_file_content "$file")

    if [[ -z "$old_content" ]]; then
        # New file - no breaking changes
        return 0
    fi

    # Detect removed exports
    detect_removed_exports "$file" "$old_content"

    # Detect signature changes
    detect_signature_changes "$file" "$old_content"
}

print_summary() {
    local breaking=$1
    local warnings=$2

    echo ""
    echo -e "${BLUE}Summary:${NC}"
    echo -e "  Breaking Changes: ${BOLD}${breaking}${NC}"
    echo -e "  Warnings: ${warnings}"
    echo ""

    if [[ $breaking -gt 0 ]]; then
        echo -e "${YELLOW}${BOLD}⚠️  COMMIT BLOCKED - Breaking changes detected${NC}"
        echo ""
        echo -e "${YELLOW}Recommended actions:${NC}"
        echo -e "  1. Review breaking changes above"
        echo -e "  2. Update version to next major (e.g., 2.0.0)"
        echo -e "  3. Document breaking changes in CHANGELOG.md"
        echo -e "  4. Update migration guide"
        echo -e "  5. Add to .breaking-changes.yml whitelist if intentional"
        echo ""
        echo -e "${CYAN}To bypass (not recommended):${NC}"
        echo -e "  export ALLOW_BREAKING_CHANGES=true"
        echo ""
    else
        echo -e "${GREEN}${BOLD}✅ No breaking changes detected${NC}"
        echo ""
    fi
}

main() {
    # Check if enabled
    if [[ "$ENABLED" != "true" ]]; then
        exit $EXIT_SUCCESS
    fi

    # Check if breaking changes are allowed
    if [[ "$ALLOW_BREAKING_CHANGES" == "true" ]]; then
        echo -e "${YELLOW}⚠️  Breaking change detection bypassed${NC}"
        exit $EXIT_SUCCESS
    fi

    # Parse input
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
        echo -e "${YELLOW}⚠️  No staged files to check${NC}"
        print_footer
        exit $EXIT_SUCCESS
    fi

    # Filter files to check
    local files_to_check=()
    for file in "${staged_files[@]}"; do
        if should_check_file "$file"; then
            files_to_check+=("$file")
        fi
    done

    if [[ ${#files_to_check[@]} -eq 0 ]]; then
        echo -e "${YELLOW}⚠️  No relevant files to check${NC}"
        print_footer
        exit $EXIT_SUCCESS
    fi

    echo -e "Analyzing changes in ${BOLD}${#files_to_check[@]}${NC} file(s)..."
    echo ""

    print_footer
    echo ""

    # Check each file for breaking changes
    for file in "${files_to_check[@]}"; do
        check_file_changes "$file"
    done

    print_footer

    # Print summary
    print_summary "$BREAKING_COUNT" "$WARNING_COUNT"

    print_footer

    # Exit with error if breaking changes found
    if [[ $BREAKING_COUNT -gt 0 ]]; then
        exit $EXIT_BREAKING_CHANGES
    else
        exit $EXIT_SUCCESS
    fi
}

# Run main function
main "$@"
