#!/bin/bash
################################################################################
# Session Setup Hook for Claude Code
# Initializes development environment on session start
################################################################################

set -euo pipefail

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || echo "$PWD")"
SESSION_CONFIG="${PROJECT_ROOT}/.session-config"

# Default settings
ENV_FILE="${ENV_FILE:-.env}"
CHECK_DEPENDENCIES="${CHECK_DEPENDENCIES:-true}"
REQUIRED_COMMANDS="${REQUIRED_COMMANDS:-node,npm,git}"
CHECK_DATABASE="${CHECK_DATABASE:-false}"
SHOW_GIT_STATUS="${SHOW_GIT_STATUS:-true}"
SHOW_SCRIPTS="${SHOW_SCRIPTS:-true}"
AUTO_START_SERVICES="${AUTO_START_SERVICES:-false}"
SHOW_TODOS="${SHOW_TODOS:-false}"
TODO_FILE="${TODO_FILE:-TODO.md}"
WELCOME_MESSAGE="${WELCOME_MESSAGE:-}"

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
    if [[ -f "$SESSION_CONFIG" ]]; then
        # shellcheck source=/dev/null
        source "$SESSION_CONFIG"
    fi
}

print_header() {
    local project_name
    project_name=$(basename "$PROJECT_ROOT")

    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${BLUE}${BOLD}🚀 Session Setup - ${project_name}${NC}"
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""
}

print_footer() {
    echo ""
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${GREEN}${BOLD}✨ Session initialized successfully!${NC}"
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""
}

load_environment() {
    local env_path="${PROJECT_ROOT}/${ENV_FILE}"

    if [[ ! -f "$env_path" ]]; then
        echo -e "${YELLOW}⚠️  Environment Variables${NC}"
        echo -e "   No ${ENV_FILE} file found"
        echo -e "   ${CYAN}Tip: Create ${ENV_FILE} from ${ENV_FILE}.example${NC}"
        echo ""
        return 1
    fi

    # Load .env file
    set -a
    # shellcheck source=/dev/null
    source "$env_path"
    set +a

    local var_count
    var_count=$(grep -c "^[^#]" "$env_path" 2>/dev/null || echo "0")

    echo -e "${GREEN}${BOLD}✅ Environment Variables Loaded${NC}"
    echo -e "   Loaded ${BOLD}${var_count}${NC} variables from ${ENV_FILE}"
    echo ""
}

check_dependencies() {
    echo -e "${BLUE}${BOLD}📦 Dependencies Check${NC}"

    local has_issues=false
    IFS=',' read -ra commands <<< "$REQUIRED_COMMANDS"

    for cmd in "${commands[@]}"; do
        cmd=$(echo "$cmd" | xargs)  # Trim whitespace

        if command -v "$cmd" &>/dev/null; then
            local version=""

            # Get version based on command
            case "$cmd" in
                node)
                    version=$(node --version 2>/dev/null || echo "")
                    if [[ -n "${MIN_NODE_VERSION:-}" ]]; then
                        check_version "$cmd" "$version" "$MIN_NODE_VERSION"
                    fi
                    ;;
                npm)
                    version=$(npm --version 2>/dev/null || echo "")
                    if [[ -n "${MIN_NPM_VERSION:-}" ]]; then
                        check_version "$cmd" "$version" "$MIN_NPM_VERSION"
                    fi
                    ;;
                python|python3)
                    version=$(python3 --version 2>/dev/null | cut -d' ' -f2 || echo "")
                    if [[ -n "${MIN_PYTHON_VERSION:-}" ]]; then
                        check_version "$cmd" "$version" "$MIN_PYTHON_VERSION"
                    fi
                    ;;
                ruby)
                    version=$(ruby --version 2>/dev/null | cut -d' ' -f2 || echo "")
                    if [[ -n "${MIN_RUBY_VERSION:-}" ]]; then
                        check_version "$cmd" "$version" "$MIN_RUBY_VERSION"
                    fi
                    ;;
                git)
                    version=$(git --version 2>/dev/null | cut -d' ' -f3 || echo "")
                    ;;
                docker)
                    version=$(docker --version 2>/dev/null | cut -d' ' -f3 | tr -d ',' || echo "")
                    if [[ -n "${MIN_DOCKER_VERSION:-}" ]]; then
                        check_version "$cmd" "$version" "$MIN_DOCKER_VERSION"
                    fi
                    ;;
                *)
                    version="installed"
                    ;;
            esac

            if [[ -n "$version" ]]; then
                echo -e "   ${GREEN}✓${NC} $cmd ${CYAN}($version)${NC}"
            else
                echo -e "   ${GREEN}✓${NC} $cmd"
            fi
        else
            echo -e "   ${RED}✗${NC} $cmd ${RED}(not found)${NC}"
            has_issues=true
        fi
    done

    echo ""

    if [[ "$has_issues" == true ]]; then
        echo -e "${YELLOW}⚠️  Some dependencies are missing${NC}"
        echo -e "   ${CYAN}Install missing dependencies and restart session${NC}"
        echo ""
    fi
}

check_version() {
    local cmd=$1
    local current=$2
    local required=$3

    # Remove 'v' prefix if present
    current="${current#v}"
    required="${required#v}"

    if ! version_ge "$current" "$required"; then
        echo -e "   ${YELLOW}⚠️  $cmd version $current is below minimum $required${NC}"
    fi
}

version_ge() {
    # Returns 0 if $1 >= $2
    printf '%s\n%s' "$2" "$1" | sort -V -C
}

check_database() {
    if [[ "$CHECK_DATABASE" != "true" ]]; then
        return 0
    fi

    echo -e "${BLUE}${BOLD}🗄️  Database Connection${NC}"

    local has_issues=false

    # Check PostgreSQL
    if [[ -n "${DATABASE_URL:-}" ]] || [[ -n "${POSTGRES_URL:-}" ]]; then
        local db_url="${DATABASE_URL:-${POSTGRES_URL:-}}"
        if check_postgres_connection "$db_url"; then
            local db_name
            db_name=$(echo "$db_url" | sed -E 's|.*://[^/]+/([^?]+).*|\1|')
            echo -e "   ${GREEN}✓${NC} PostgreSQL connected ${CYAN}($db_name)${NC}"
        else
            echo -e "   ${RED}✗${NC} PostgreSQL connection failed"
            has_issues=true
        fi
    fi

    # Check Redis
    if [[ -n "${REDIS_URL:-}" ]]; then
        if check_redis_connection "$REDIS_URL"; then
            echo -e "   ${GREEN}✓${NC} Redis connected"
        else
            echo -e "   ${RED}✗${NC} Redis connection failed"
            has_issues=true
        fi
    fi

    # Check MongoDB
    if [[ -n "${MONGODB_URL:-}" ]]; then
        if check_mongodb_connection "$MONGODB_URL"; then
            echo -e "   ${GREEN}✓${NC} MongoDB connected"
        else
            echo -e "   ${RED}✗${NC} MongoDB connection failed"
            has_issues=true
        fi
    fi

    echo ""

    if [[ "$has_issues" == true ]]; then
        echo -e "${YELLOW}⚠️  Some database connections failed${NC}"
        echo -e "   ${CYAN}Check database services and connection strings${NC}"
        echo ""
    fi
}

check_postgres_connection() {
    local db_url=$1
    if command -v psql &>/dev/null; then
        psql "$db_url" -c "SELECT 1;" &>/dev/null
        return $?
    elif command -v pg_isready &>/dev/null; then
        # Extract host and port
        local host port
        host=$(echo "$db_url" | sed -E 's|.*://[^@]+@([^:/]+).*|\1|')
        port=$(echo "$db_url" | sed -E 's|.*:([0-9]+)/.*|\1|')
        pg_isready -h "$host" -p "${port:-5432}" &>/dev/null
        return $?
    fi
    return 1
}

check_redis_connection() {
    local redis_url=$1
    if command -v redis-cli &>/dev/null; then
        # Extract host and port
        local host port
        host=$(echo "$redis_url" | sed -E 's|redis://([^:]+).*|\1|')
        port=$(echo "$redis_url" | sed -E 's|.*:([0-9]+).*|\1|')
        redis-cli -h "${host:-localhost}" -p "${port:-6379}" ping &>/dev/null
        return $?
    fi
    return 1
}

check_mongodb_connection() {
    local mongo_url=$1
    if command -v mongosh &>/dev/null; then
        mongosh "$mongo_url" --eval "db.adminCommand('ping')" &>/dev/null
        return $?
    elif command -v mongo &>/dev/null; then
        mongo "$mongo_url" --eval "db.adminCommand('ping')" &>/dev/null
        return $?
    fi
    return 1
}

show_git_status() {
    if [[ "$SHOW_GIT_STATUS" != "true" ]]; then
        return 0
    fi

    if ! git rev-parse --git-dir &>/dev/null; then
        return 0
    fi

    echo -e "${BLUE}${BOLD}📊 Git Status${NC}"

    # Current branch
    local branch
    branch=$(git branch --show-current 2>/dev/null || echo "detached HEAD")
    echo -e "   Branch: ${BOLD}${branch}${NC}"

    # Changes
    local changed unstaged staged
    changed=$(git diff --shortstat 2>/dev/null || echo "")
    unstaged=$(git diff --name-only 2>/dev/null | wc -l | xargs)
    staged=$(git diff --cached --name-only 2>/dev/null | wc -l | xargs)

    if [[ $unstaged -gt 0 ]] || [[ $staged -gt 0 ]]; then
        echo -e "   Status: ${YELLOW}${unstaged} files changed, ${staged} files staged${NC}"
    else
        echo -e "   Status: ${GREEN}Working tree clean${NC}"
    fi

    # Commits ahead/behind
    local ahead behind
    ahead=$(git rev-list @{u}..HEAD 2>/dev/null | wc -l | xargs || echo "0")
    behind=$(git rev-list HEAD..@{u} 2>/dev/null | wc -l | xargs || echo "0")

    if [[ $ahead -gt 0 ]]; then
        echo -e "   Commits ahead: ${CYAN}${ahead}${NC}"
    fi
    if [[ $behind -gt 0 ]]; then
        echo -e "   Commits behind: ${YELLOW}${behind}${NC}"
    fi

    echo ""
}

show_available_scripts() {
    if [[ "$SHOW_SCRIPTS" != "true" ]]; then
        return 0
    fi

    local has_scripts=false

    # Check for package.json scripts
    if [[ -f "${PROJECT_ROOT}/package.json" ]]; then
        echo -e "${BLUE}${BOLD}📝 Available Scripts${NC}"

        local scripts
        scripts=$(node -pe "try { const p=require('./package.json'); Object.keys(p.scripts || {}).map(k => '   ' + k.padEnd(20) + ' - ' + p.scripts[k]).join('\n') } catch(e) { '' }" 2>/dev/null)

        if [[ -n "$scripts" ]]; then
            echo "$scripts"
            has_scripts=true
        fi
    fi

    # Check for Makefile
    if [[ -f "${PROJECT_ROOT}/Makefile" ]]; then
        if [[ "$has_scripts" != true ]]; then
            echo -e "${BLUE}${BOLD}📝 Available Make Targets${NC}"
        fi

        local targets
        targets=$(grep -E '^[a-zA-Z0-9_-]+:.*?##' "${PROJECT_ROOT}/Makefile" 2>/dev/null | awk 'BEGIN {FS = ":.*?## "}; {printf "   %-20s - %s\n", $1, $2}')

        if [[ -n "$targets" ]]; then
            echo "$targets"
            has_scripts=true
        fi
    fi

    [[ "$has_scripts" == true ]] && echo ""
}

show_todos() {
    if [[ "$SHOW_TODOS" != "true" ]]; then
        return 0
    fi

    local todo_path="${PROJECT_ROOT}/${TODO_FILE}"

    if [[ ! -f "$todo_path" ]]; then
        return 0
    fi

    echo -e "${BLUE}${BOLD}📌 TODO Reminders${NC}"

    # Extract TODO items (lines starting with - or * or numbers)
    local todos
    todos=$(grep -E '^\s*[-*]|\s*[0-9]+\.' "$todo_path" | head -n 10 2>/dev/null || echo "")

    if [[ -n "$todos" ]]; then
        local count
        count=$(echo "$todos" | wc -l | xargs)
        echo "$todos" | head -n 5 | sed 's/^/   /'

        if [[ $count -gt 5 ]]; then
            echo -e "   ${CYAN}... and $((count - 5)) more${NC}"
        fi
    fi

    echo ""
}

start_services() {
    if [[ "$AUTO_START_SERVICES" != "true" ]]; then
        return 0
    fi

    if [[ -z "${SERVICES:-}" ]]; then
        return 0
    fi

    echo -e "${BLUE}${BOLD}🔧 Starting Services${NC}"

    # Check for docker-compose
    if [[ -f "${PROJECT_ROOT}/docker-compose.yml" ]] && command -v docker-compose &>/dev/null; then
        echo "   Starting services with docker-compose..."
        docker-compose up -d &>/dev/null
        echo -e "   ${GREEN}✓${NC} Services started"
    else
        # Start individual services
        IFS=',' read -ra service_list <<< "$SERVICES"
        for service in "${service_list[@]}"; do
            service=$(echo "$service" | xargs)  # Trim whitespace

            if systemctl is-active "$service" &>/dev/null; then
                echo -e "   ${GREEN}✓${NC} $service already running"
            else
                if systemctl start "$service" &>/dev/null; then
                    echo -e "   ${GREEN}✓${NC} Started $service"
                else
                    echo -e "   ${RED}✗${NC} Failed to start $service"
                fi
            fi
        done
    fi

    echo ""
}

show_welcome_message() {
    if [[ -n "$WELCOME_MESSAGE" ]]; then
        echo -e "${CYAN}${BOLD}💡 ${WELCOME_MESSAGE}${NC}"
        echo ""
    fi
}

main() {
    # Load configuration
    load_config

    print_header

    # Load environment variables
    load_environment

    # Check dependencies
    if [[ "$CHECK_DEPENDENCIES" == "true" ]]; then
        check_dependencies
    fi

    # Check database connections
    check_database

    # Show git status
    show_git_status

    # Show available scripts
    show_available_scripts

    # Show TODO reminders
    show_todos

    # Start services
    start_services

    # Show welcome message
    show_welcome_message

    print_footer
}

# Run main function
main "$@"
