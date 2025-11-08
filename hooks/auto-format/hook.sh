#!/bin/bash
################################################################################
# Auto-Format Hook for Claude Code
# Automatically formats code after file edits
################################################################################

set -euo pipefail

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || echo "$PWD")"
FORMAT_CONFIG="${PROJECT_ROOT}/.formatconfig"

# Default settings
AUTO_FORMAT="${AUTO_FORMAT:-true}"
AUTO_COMMIT_FORMAT="${AUTO_COMMIT_FORMAT:-false}"
SHOW_CHANGES="${SHOW_CHANGES:-true}"
FORMATTERS="${FORMATTERS:-}"
FORMAT_PATTERNS="${FORMAT_PATTERNS:-}"
EXCLUDE_PATTERNS="${EXCLUDE_PATTERNS:-*.min.js,*.bundle.js,dist/*,build/*,node_modules/*}"
VERBOSE="${VERBOSE:-false}"
PARALLEL_FORMAT="${PARALLEL_FORMAT:-false}"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m'

################################################################################
# Functions
################################################################################

load_config() {
    if [[ -f "$FORMAT_CONFIG" ]]; then
        # shellcheck source=/dev/null
        source "$FORMAT_CONFIG"
    fi
}

print_header() {
    echo -e "${BLUE}${BOLD}🎨 Auto-Format Running...${NC}"
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""
}

print_footer() {
    echo ""
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${GREEN}${BOLD}✨ Formatting complete!${NC}"
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""
}

should_format() {
    local file=$1

    # Check if auto-format is enabled
    if [[ "$AUTO_FORMAT" != "true" ]]; then
        return 1
    fi

    # Check if file exists
    if [[ ! -f "$file" ]]; then
        return 1
    fi

    # Check exclude patterns
    IFS=',' read -ra patterns <<< "$EXCLUDE_PATTERNS"
    for pattern in "${patterns[@]}"; do
        pattern=$(echo "$pattern" | xargs)  # Trim whitespace
        if [[ "$file" == $pattern ]]; then
            [[ "$VERBOSE" == "true" ]] && echo "Skipping excluded file: $file"
            return 1
        fi
    done

    # Check format patterns (if specified)
    if [[ -n "$FORMAT_PATTERNS" ]]; then
        local matches=false
        IFS=',' read -ra patterns <<< "$FORMAT_PATTERNS"
        for pattern in "${patterns[@]}"; do
            pattern=$(echo "$pattern" | xargs)
            if [[ "$file" == $pattern ]]; then
                matches=true
                break
            fi
        done

        if [[ "$matches" != true ]]; then
            return 1
        fi
    fi

    return 0
}

detect_formatter() {
    local file=$1
    local extension="${file##*.}"

    # If formatters are explicitly specified, use those
    if [[ -n "$FORMATTERS" ]]; then
        echo "$FORMATTERS" | tr ',' '\n' | head -n 1
        return 0
    fi

    # Detect formatter based on file extension
    case "$extension" in
        js|jsx|ts|tsx|mjs|cjs)
            if command -v prettier &>/dev/null; then
                echo "prettier"
            elif command -v eslint &>/dev/null; then
                echo "eslint"
            fi
            ;;
        py)
            if command -v black &>/dev/null; then
                echo "black"
            elif command -v autopep8 &>/dev/null; then
                echo "autopep8"
            elif command -v yapf &>/dev/null; then
                echo "yapf"
            fi
            ;;
        rb)
            if command -v rubocop &>/dev/null; then
                echo "rubocop"
            fi
            ;;
        go)
            if command -v gofmt &>/dev/null; then
                echo "gofmt"
            elif command -v goimports &>/dev/null; then
                echo "goimports"
            fi
            ;;
        rs)
            if command -v rustfmt &>/dev/null; then
                echo "rustfmt"
            fi
            ;;
        php)
            if command -v php-cs-fixer &>/dev/null; then
                echo "php-cs-fixer"
            fi
            ;;
        java)
            if command -v google-java-format &>/dev/null; then
                echo "google-java-format"
            fi
            ;;
        c|cpp|cc|h|hpp)
            if command -v clang-format &>/dev/null; then
                echo "clang-format"
            fi
            ;;
        css|scss|less|json|yaml|yml|md|html)
            if command -v prettier &>/dev/null; then
                echo "prettier"
            fi
            ;;
        *)
            echo ""
            ;;
    esac
}

format_with_prettier() {
    local file=$1
    local before_hash after_hash

    before_hash=$(md5sum "$file" 2>/dev/null || md5 "$file" 2>/dev/null || echo "")

    if npx prettier --write "$file" &>/dev/null; then
        after_hash=$(md5sum "$file" 2>/dev/null || md5 "$file" 2>/dev/null || echo "")

        if [[ "$before_hash" != "$after_hash" ]]; then
            echo -e "${GREEN}✅ Formatted with Prettier${NC}"
            return 0
        else
            [[ "$VERBOSE" == "true" ]] && echo "No changes needed"
            return 1
        fi
    else
        echo -e "${RED}❌ Prettier formatting failed${NC}"
        return 2
    fi
}

format_with_eslint() {
    local file=$1

    if npx eslint --fix "$file" &>/dev/null; then
        echo -e "${GREEN}✅ Formatted with ESLint${NC}"
        return 0
    else
        echo -e "${RED}❌ ESLint formatting failed${NC}"
        return 2
    fi
}

format_with_black() {
    local file=$1
    local before_hash after_hash

    before_hash=$(md5sum "$file" 2>/dev/null || md5 "$file" 2>/dev/null || echo "")

    if black "$file" &>/dev/null; then
        after_hash=$(md5sum "$file" 2>/dev/null || md5 "$file" 2>/dev/null || echo "")

        if [[ "$before_hash" != "$after_hash" ]]; then
            echo -e "${GREEN}✅ Formatted with Black${NC}"

            # Also run isort if available
            if command -v isort &>/dev/null; then
                isort "$file" &>/dev/null
                echo -e "${GREEN}   Sorted imports with isort${NC}"
            fi
            return 0
        else
            [[ "$VERBOSE" == "true" ]] && echo "No changes needed"
            return 1
        fi
    else
        echo -e "${RED}❌ Black formatting failed${NC}"
        return 2
    fi
}

format_with_autopep8() {
    local file=$1

    if autopep8 --in-place --aggressive --aggressive "$file" &>/dev/null; then
        echo -e "${GREEN}✅ Formatted with autopep8${NC}"
        return 0
    else
        echo -e "${RED}❌ autopep8 formatting failed${NC}"
        return 2
    fi
}

format_with_rubocop() {
    local file=$1

    if rubocop -a "$file" &>/dev/null; then
        echo -e "${GREEN}✅ Formatted with RuboCop${NC}"
        return 0
    else
        echo -e "${RED}❌ RuboCop formatting failed${NC}"
        return 2
    fi
}

format_with_gofmt() {
    local file=$1

    if gofmt -w "$file" &>/dev/null; then
        echo -e "${GREEN}✅ Formatted with gofmt${NC}"
        return 0
    else
        echo -e "${RED}❌ gofmt formatting failed${NC}"
        return 2
    fi
}

format_with_goimports() {
    local file=$1

    if goimports -w "$file" &>/dev/null; then
        echo -e "${GREEN}✅ Formatted with goimports${NC}"
        return 0
    else
        echo -e "${RED}❌ goimports formatting failed${NC}"
        return 2
    fi
}

format_with_rustfmt() {
    local file=$1

    if rustfmt "$file" &>/dev/null; then
        echo -e "${GREEN}✅ Formatted with rustfmt${NC}"
        return 0
    else
        echo -e "${RED}❌ rustfmt formatting failed${NC}"
        return 2
    fi
}

format_with_php_cs_fixer() {
    local file=$1

    if php-cs-fixer fix "$file" &>/dev/null; then
        echo -e "${GREEN}✅ Formatted with PHP-CS-Fixer${NC}"
        return 0
    else
        echo -e "${RED}❌ PHP-CS-Fixer formatting failed${NC}"
        return 2
    fi
}

format_with_clang_format() {
    local file=$1

    if clang-format -i "$file" &>/dev/null; then
        echo -e "${GREEN}✅ Formatted with clang-format${NC}"
        return 0
    else
        echo -e "${RED}❌ clang-format formatting failed${NC}"
        return 2
    fi
}

format_file() {
    local file=$1

    # Make file path absolute if relative
    if [[ ! "$file" =~ ^/ ]]; then
        file="${PROJECT_ROOT}/${file}"
    fi

    # Check if we should format this file
    if ! should_format "$file"; then
        return 0
    fi

    echo -e "${BLUE}📝 Formatting file: ${BOLD}${file}${NC}"
    echo ""

    # Store original content for diff
    local original_content=""
    if [[ "$SHOW_CHANGES" == "true" ]] && [[ -f "$file" ]]; then
        original_content=$(cat "$file")
    fi

    # Detect and run formatter
    local formatter
    formatter=$(detect_formatter "$file")

    if [[ -z "$formatter" ]]; then
        [[ "$VERBOSE" == "true" ]] && echo -e "${YELLOW}⚠️  No formatter found for this file type${NC}"
        return 0
    fi

    local format_result=0

    case "$formatter" in
        prettier)
            format_with_prettier "$file" || format_result=$?
            ;;
        eslint)
            format_with_eslint "$file" || format_result=$?
            ;;
        black)
            format_with_black "$file" || format_result=$?
            ;;
        autopep8)
            format_with_autopep8 "$file" || format_result=$?
            ;;
        rubocop)
            format_with_rubocop "$file" || format_result=$?
            ;;
        gofmt)
            format_with_gofmt "$file" || format_result=$?
            ;;
        goimports)
            format_with_goimports "$file" || format_result=$?
            ;;
        rustfmt)
            format_with_rustfmt "$file" || format_result=$?
            ;;
        php-cs-fixer)
            format_with_php_cs_fixer "$file" || format_result=$?
            ;;
        clang-format)
            format_with_clang_format "$file" || format_result=$?
            ;;
        *)
            echo -e "${YELLOW}⚠️  Unknown formatter: $formatter${NC}"
            return 0
            ;;
    esac

    # Show changes if requested and file was modified
    if [[ "$SHOW_CHANGES" == "true" ]] && [[ $format_result -eq 0 ]] && [[ -f "$file" ]]; then
        local new_content
        new_content=$(cat "$file")

        if [[ "$original_content" != "$new_content" ]]; then
            echo ""
            echo -e "${CYAN}Changes:${NC}"
            # Show simplified diff
            diff <(echo "$original_content") <(echo "$new_content") | grep -E "^[<>]" | head -n 10 | sed 's/^</  -/' | sed 's/^>/  +/' || true
            echo ""
        fi
    fi

    # Auto-commit if requested
    if [[ "$AUTO_COMMIT_FORMAT" == "true" ]] && [[ $format_result -eq 0 ]]; then
        auto_commit_changes "$file"
    fi

    return $format_result
}

auto_commit_changes() {
    local file=$1

    if ! git rev-parse --git-dir &>/dev/null; then
        return 0
    fi

    # Check if file has changes
    if git diff --quiet "$file" 2>/dev/null; then
        return 0
    fi

    # Stage and commit
    git add "$file" 2>/dev/null || true
    git commit -m "chore: auto-format $(basename "$file")" --no-verify &>/dev/null || true

    echo -e "${GREEN}📝 Auto-committed formatting changes${NC}"
}

parse_tool_output() {
    local tool_name=$1
    local tool_output=$2

    # Extract file path from Edit or Write tool output
    # This is Claude Code specific - adjust based on actual output format

    # Try to extract file_path from JSON-like output
    local file_path
    file_path=$(echo "$tool_output" | grep -oP '"file_path":\s*"\K[^"]+' || echo "")

    if [[ -z "$file_path" ]]; then
        # Try alternative patterns
        file_path=$(echo "$tool_output" | grep -oP 'file_path=\K[^\s]+' || echo "")
    fi

    echo "$file_path"
}

main() {
    # Load configuration
    load_config

    # Parse input - Claude Code passes tool name and output
    local tool_name="${1:-}"
    local tool_output="${2:-}"

    # Only run for Edit or Write tools
    if [[ ! "$tool_name" =~ ^(Edit|Write)$ ]]; then
        exit 0
    fi

    # Extract file path from tool output
    local file_path
    file_path=$(parse_tool_output "$tool_name" "$tool_output")

    # If we couldn't parse the file path, try to get it from arguments
    if [[ -z "$file_path" ]] && [[ $# -gt 2 ]]; then
        file_path="${3}"
    fi

    if [[ -z "$file_path" ]]; then
        [[ "$VERBOSE" == "true" ]] && echo "Could not determine file path, skipping format"
        exit 0
    fi

    print_header

    # Format the file
    format_file "$file_path"

    print_footer
}

# Run main function
main "$@"
