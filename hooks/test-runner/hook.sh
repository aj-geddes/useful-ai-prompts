#!/bin/bash
################################################################################
# Test Runner Hook for Claude Code
# Automatically runs tests before commits
################################################################################

set -euo pipefail

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || echo "$PWD")"
TEST_CONFIG="${PROJECT_ROOT}/.testconfig"

# Default settings
TEST_SCOPE="${TEST_SCOPE:-changed}"  # all, changed, affected
PARALLEL_TESTS="${PARALLEL_TESTS:-true}"
MAX_PARALLEL="${MAX_PARALLEL:-4}"
TEST_TIMEOUT="${TEST_TIMEOUT:-300}"
FAIL_FAST="${FAIL_FAST:-false}"
VERBOSE="${VERBOSE:-false}"
CACHE_TESTS="${CACHE_TESTS:-true}"
MIN_COVERAGE="${MIN_COVERAGE:-0}"
SKIP_TEST_HOOK="${SKIP_TEST_HOOK:-false}"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
BOLD='\033[1m'
NC='\033[0m'

# Exit codes
EXIT_SUCCESS=0
EXIT_TESTS_FAILED=1
EXIT_ERROR=2

################################################################################
# Functions
################################################################################

load_config() {
    if [[ -f "$TEST_CONFIG" ]]; then
        # shellcheck source=/dev/null
        source "$TEST_CONFIG"
    fi
}

print_header() {
    echo -e "${BLUE}${BOLD}🧪 Test Runner Starting...${NC}"
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""
}

print_footer() {
    echo ""
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
}

print_success() {
    local total=$1
    local duration=$2
    echo -e "${GREEN}${BOLD}✅ All Tests Passed${NC}"
    echo ""
    echo -e "${GREEN}Summary:${NC}"
    echo -e "  Total: ${BOLD}${total}${NC} tests"
    echo -e "  Passed: ${BOLD}${total}${NC} (100%)"
    echo -e "  Duration: ${BOLD}${duration}${NC}s"
}

print_failure() {
    local total=$1
    local passed=$2
    local failed=$3
    local duration=$4

    echo -e "${RED}${BOLD}❌ TEST FAILURES DETECTED${NC}"
    echo ""
    echo -e "${RED}Summary:${NC}"
    echo -e "  Total: ${total} tests"
    echo -e "  Passed: ${passed} ($(( passed * 100 / total ))%)"
    echo -e "  Failed: ${BOLD}${failed}${NC} ($(( failed * 100 / total ))%)"
    echo -e "  Duration: ${duration}s"
    echo ""
    echo -e "${YELLOW}${BOLD}⚠️  COMMIT BLOCKED - Fix failing tests before committing${NC}"
    echo ""
    echo -e "${YELLOW}Next steps:${NC}"
    echo -e "  1. Review failing test output above"
    echo -e "  2. Fix the failing test(s)"
    echo -e "  3. Run tests manually to verify"
    echo -e "  4. Try committing again"
    echo ""
}

check_git_command() {
    local args="$1"
    [[ "$args" =~ git[[:space:]]+commit ]] && return 0 || return 1
}

detect_test_framework() {
    local framework=""

    # JavaScript/TypeScript
    if [[ -f "${PROJECT_ROOT}/package.json" ]]; then
        if grep -q '"jest"' "${PROJECT_ROOT}/package.json" 2>/dev/null; then
            framework="jest"
        elif grep -q '"mocha"' "${PROJECT_ROOT}/package.json" 2>/dev/null; then
            framework="mocha"
        elif grep -q '"vitest"' "${PROJECT_ROOT}/package.json" 2>/dev/null; then
            framework="vitest"
        elif grep -q '"ava"' "${PROJECT_ROOT}/package.json" 2>/dev/null; then
            framework="ava"
        fi
    fi

    # Python
    if [[ -f "${PROJECT_ROOT}/pytest.ini" ]] || [[ -f "${PROJECT_ROOT}/setup.cfg" ]] || command -v pytest &>/dev/null; then
        framework="pytest"
    elif [[ -f "${PROJECT_ROOT}/setup.py" ]] && grep -q "unittest" "${PROJECT_ROOT}/setup.py" 2>/dev/null; then
        framework="unittest"
    fi

    # Ruby
    if [[ -f "${PROJECT_ROOT}/.rspec" ]] || [[ -f "${PROJECT_ROOT}/spec/spec_helper.rb" ]]; then
        framework="rspec"
    elif [[ -f "${PROJECT_ROOT}/Rakefile" ]] && grep -q "Minitest" "${PROJECT_ROOT}/Rakefile" 2>/dev/null; then
        framework="minitest"
    fi

    # Go
    if [[ -f "${PROJECT_ROOT}/go.mod" ]]; then
        framework="go"
    fi

    # Rust
    if [[ -f "${PROJECT_ROOT}/Cargo.toml" ]]; then
        framework="rust"
    fi

    # PHP
    if [[ -f "${PROJECT_ROOT}/phpunit.xml" ]]; then
        framework="phpunit"
    fi

    echo "$framework"
}

get_changed_files() {
    if git rev-parse --git-dir > /dev/null 2>&1; then
        git diff --cached --name-only --diff-filter=ACMR 2>/dev/null || true
    else
        echo ""
    fi
}

get_test_files() {
    local framework=$1
    local scope=$2
    local changed_files=("${@:3}")

    case "$framework" in
        jest|mocha|vitest|ava)
            if [[ "$scope" == "all" ]]; then
                find "$PROJECT_ROOT" -type f \( -name "*.test.js" -o -name "*.test.ts" -o -name "*.spec.js" -o -name "*.spec.ts" \) | grep -v node_modules
            else
                # Find test files for changed files
                for file in "${changed_files[@]}"; do
                    local base="${file%.*}"
                    find "$PROJECT_ROOT" -type f \( -name "${base}.test.*" -o -name "${base}.spec.*" \) 2>/dev/null
                done
            fi
            ;;
        pytest)
            if [[ "$scope" == "all" ]]; then
                find "$PROJECT_ROOT" -type f \( -name "test_*.py" -o -name "*_test.py" \) | grep -v __pycache__
            else
                for file in "${changed_files[@]}"; do
                    [[ "$file" =~ test_.*\.py$ || "$file" =~ .*_test\.py$ ]] && echo "$file"
                done
            fi
            ;;
        rspec)
            if [[ "$scope" == "all" ]]; then
                find "$PROJECT_ROOT/spec" -type f -name "*_spec.rb" 2>/dev/null
            else
                for file in "${changed_files[@]}"; do
                    [[ "$file" =~ _spec\.rb$ ]] && echo "$file"
                done
            fi
            ;;
        *)
            echo ""
            ;;
    esac
}

run_tests() {
    local framework=$1
    local scope=$2
    shift 2
    local changed_files=("$@")

    local start_time
    start_time=$(date +%s)

    local test_cmd=""
    local test_output=""
    local exit_code=0

    case "$framework" in
        jest)
            if [[ "$scope" == "changed" ]]; then
                test_cmd="npx jest --onlyChanged --passWithNoTests"
            else
                test_cmd="npx jest"
            fi

            [[ "$PARALLEL_TESTS" == "true" ]] && test_cmd="$test_cmd --maxWorkers=$MAX_PARALLEL"
            [[ "$CACHE_TESTS" == "true" ]] && test_cmd="$test_cmd --cache"
            [[ "$FAIL_FAST" == "true" ]] && test_cmd="$test_cmd --bail"
            [[ "$VERBOSE" == "true" ]] && test_cmd="$test_cmd --verbose"
            [[ $MIN_COVERAGE -gt 0 ]] && test_cmd="$test_cmd --coverage"
            ;;

        mocha)
            test_cmd="npx mocha"
            [[ "$PARALLEL_TESTS" == "true" ]] && test_cmd="$test_cmd --parallel"
            [[ "$FAIL_FAST" == "true" ]] && test_cmd="$test_cmd --bail"
            ;;

        vitest)
            test_cmd="npx vitest run"
            [[ "$scope" == "changed" ]] && test_cmd="$test_cmd --changed"
            ;;

        pytest)
            test_cmd="pytest"
            [[ "$PARALLEL_TESTS" == "true" ]] && test_cmd="$test_cmd -n $MAX_PARALLEL"
            [[ "$FAIL_FAST" == "true" ]] && test_cmd="$test_cmd -x"
            [[ "$VERBOSE" == "true" ]] && test_cmd="$test_cmd -v"
            [[ $MIN_COVERAGE -gt 0 ]] && test_cmd="$test_cmd --cov --cov-fail-under=$MIN_COVERAGE"

            if [[ "$scope" == "changed" ]]; then
                test_files=$(get_test_files "$framework" "$scope" "${changed_files[@]}")
                [[ -n "$test_files" ]] && test_cmd="$test_cmd $test_files"
            fi
            ;;

        rspec)
            test_cmd="bundle exec rspec"
            [[ "$PARALLEL_TESTS" == "true" ]] && test_cmd="parallel_rspec"
            [[ "$FAIL_FAST" == "true" ]] && test_cmd="$test_cmd --fail-fast"
            [[ "$VERBOSE" == "true" ]] && test_cmd="$test_cmd --format documentation"

            if [[ "$scope" == "changed" ]]; then
                test_files=$(get_test_files "$framework" "$scope" "${changed_files[@]}")
                [[ -n "$test_files" ]] && test_cmd="$test_cmd $test_files"
            fi
            ;;

        go)
            test_cmd="go test ./..."
            [[ "$PARALLEL_TESTS" == "true" ]] && test_cmd="$test_cmd -parallel $MAX_PARALLEL"
            [[ "$VERBOSE" == "true" ]] && test_cmd="$test_cmd -v"
            [[ $MIN_COVERAGE -gt 0 ]] && test_cmd="$test_cmd -cover"
            ;;

        rust)
            test_cmd="cargo test"
            [[ "$PARALLEL_TESTS" == "true" ]] && test_cmd="$test_cmd --jobs $MAX_PARALLEL"
            [[ "$VERBOSE" == "true" ]] && test_cmd="$test_cmd --verbose"
            ;;

        phpunit)
            test_cmd="./vendor/bin/phpunit"
            [[ "$FAIL_FAST" == "true" ]] && test_cmd="$test_cmd --stop-on-failure"
            [[ $MIN_COVERAGE -gt 0 ]] && test_cmd="$test_cmd --coverage-text"
            ;;

        *)
            echo -e "${RED}❌ Unknown test framework${NC}"
            return $EXIT_ERROR
            ;;
    esac

    echo -e "${BLUE}Running tests...${NC}"
    [[ "$VERBOSE" == "true" ]] && echo -e "${BLUE}Command: ${test_cmd}${NC}"
    echo ""

    # Run tests with timeout
    if ! test_output=$(timeout "$TEST_TIMEOUT" $test_cmd 2>&1); then
        exit_code=$?
    fi

    local end_time
    end_time=$(date +%s)
    local duration=$((end_time - start_time))

    # Parse test results based on framework
    parse_test_results "$framework" "$test_output" "$exit_code" "$duration"
}

parse_test_results() {
    local framework=$1
    local output=$2
    local exit_code=$3
    local duration=$4

    local total=0
    local passed=0
    local failed=0

    case "$framework" in
        jest|vitest)
            # Parse Jest/Vitest output
            total=$(echo "$output" | grep -oP 'Tests:\s+\K\d+(?= total)' || echo "0")
            passed=$(echo "$output" | grep -oP 'Tests:\s+\K\d+(?= passed)' || echo "0")
            failed=$(echo "$output" | grep -oP '\K\d+(?= failed)' || echo "0")

            if [[ $total -eq 0 ]]; then
                # Alternative parsing
                passed=$(echo "$output" | grep -c "PASS" || echo "0")
                failed=$(echo "$output" | grep -c "FAIL" || echo "0")
                total=$((passed + failed))
            fi
            ;;

        pytest)
            # Parse pytest output
            passed=$(echo "$output" | grep -oP '\K\d+(?= passed)' || echo "0")
            failed=$(echo "$output" | grep -oP '\K\d+(?= failed)' || echo "0")
            total=$((passed + failed))
            ;;

        rspec)
            # Parse RSpec output
            total=$(echo "$output" | grep -oP '\K\d+(?= examples?)' || echo "0")
            failed=$(echo "$output" | grep -oP '\K\d+(?= failures?)' || echo "0")
            passed=$((total - failed))
            ;;

        go)
            # Parse go test output
            passed=$(echo "$output" | grep -c "^PASS" || echo "0")
            failed=$(echo "$output" | grep -c "^FAIL" || echo "0")
            total=$((passed + failed))
            ;;

        rust)
            # Parse cargo test output
            passed=$(echo "$output" | grep -oP 'test result: ok\. \K\d+(?= passed)' || echo "0")
            failed=$(echo "$output" | grep -oP '\K\d+(?= failed)' || echo "0")
            total=$((passed + failed))
            ;;
    esac

    # Show test output if verbose or if tests failed
    if [[ "$VERBOSE" == "true" ]] || [[ $exit_code -ne 0 ]]; then
        echo "$output"
        echo ""
    fi

    if [[ $exit_code -eq 0 ]]; then
        print_success "$total" "$duration"
        print_footer
        return $EXIT_SUCCESS
    else
        print_failure "$total" "$passed" "$failed" "$duration"
        print_footer
        return $EXIT_TESTS_FAILED
    fi
}

main() {
    # Load configuration
    load_config

    # Check for skip flag
    if [[ "$SKIP_TEST_HOOK" == "true" ]]; then
        echo -e "${YELLOW}⚠️  Test hook skipped (SKIP_TEST_HOOK=true)${NC}"
        exit $EXIT_SUCCESS
    fi

    # Parse input
    local command="${1:-}"

    # Only run for git commit commands
    if ! check_git_command "$command"; then
        exit $EXIT_SUCCESS
    fi

    print_header

    # Detect test framework
    local framework
    framework=$(detect_test_framework)

    if [[ -z "$framework" ]]; then
        echo -e "${YELLOW}⚠️  No test framework detected${NC}"
        echo -e "${YELLOW}Skipping test execution${NC}"
        print_footer
        exit $EXIT_SUCCESS
    fi

    echo -e "${BLUE}📦 Detected Test Framework: ${BOLD}${framework}${NC}"

    # Get changed files
    local changed_files
    mapfile -t changed_files < <(get_changed_files)

    if [[ ${#changed_files[@]} -eq 0 ]] && [[ "$TEST_SCOPE" == "changed" ]]; then
        echo -e "${YELLOW}⚠️  No changed files to test${NC}"
        print_footer
        exit $EXIT_SUCCESS
    fi

    if [[ "$TEST_SCOPE" == "changed" ]]; then
        echo -e "${BLUE}📝 Running tests for ${#changed_files[@]} changed file(s)${NC}"
    else
        echo -e "${BLUE}📝 Running all tests${NC}"
    fi
    echo ""

    # Run tests
    run_tests "$framework" "$TEST_SCOPE" "${changed_files[@]}"
    exit $?
}

# Run main function
main "$@"
