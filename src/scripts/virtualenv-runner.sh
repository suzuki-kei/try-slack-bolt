#!/bin/bash

set -eu

declare -r ROOT_DIR="$(cd "$(dirname "$0")/../.." && pwd)"
declare -r VIRTUALENV_DIR="${ROOT_DIR}/virtualenv"

export PYTHONPATH="${ROOT_DIR}/src/main"
export PYTHONPYCACHEPREFIX="${ROOT_DIR}/target/__pycache__"

declare -r EXIT_STATUS_SUCCESS=0
declare -r EXIT_STATUS_INVALID_ARGUMENTS=1

declare -r USAGE=`cat <<EOS | sed 's/^    //'
    NAME
        $(basename "$0")

    SYNOPSIS
        $(basename "$0") -h
        $(basename "$0") COMMAND

    DESCRIPTION
        setup virtualenv environment or execute in virtualenv environment.

    OPTIONS
        -h | --help
            Show usage and exit.

    COMMAND
        ...

    EXIT STATUS
        ${EXIT_STATUS_SUCCESS} if successfully.
        ${EXIT_STATUS_INVALID_ARGUMENTS} if invalid argument passed.
EOS`

function main
{
    declare -r COMMAND="$@"

    case "${COMMAND}" in
        -h | --help)
            echo "${USAGE}"
            exit ${EXIT_STATUS_SUCCESS}
            ;;
        setup | repl | run | test | coverage)
            command:${COMMAND}
            exit ${EXIT_STATUS_SUCCESS}
            ;;
        *)
            echo -e "invalid arguments: [${COMMAND}]\n\n${USAGE}" >&2
            exit ${EXIT_STATUS_INVALID_ARGUMENTS}
            ;;
    esac
}

function command:setup
{
    if [[ -d "${VIRTUALENV_DIR}" ]]; then
        echo "SKIP: virtualenv environment already exists."
    else
        virtualenv --python=python3 "${VIRTUALENV_DIR}"
    fi

    source "${VIRTUALENV_DIR}/bin/activate"
    pip install -r requirements.txt
}

function command:repl
{
    source "${VIRTUALENV_DIR}/bin/activate"
    python
}

function command:run
{
    if [[ -f "${ROOT_DIR}/config/export.sh" ]]; then
        source "${ROOT_DIR}/config/export.sh"
    fi

    source "${VIRTUALENV_DIR}/bin/activate"
    python "${ROOT_DIR}/src/main/myapp/main.py"
}

function command:test
{
    source "${VIRTUALENV_DIR}/bin/activate"
    python -m unittest discover -t "${ROOT_DIR}" -s "${ROOT_DIR}/src/test/myapp"
}

function command:coverage
{
    source "${VIRTUALENV_DIR}/bin/activate"
    export COVERAGE_FILE="${ROOT_DIR}/target/coverage"
    coverage erase
    coverage run --branch --omit 'src/test/*' -m unittest discover -t "${ROOT_DIR}" -s "${ROOT_DIR}/src/test/myapp"
    coverage report
    coverage html --directory=./target/docs/coverage/
}

main "$@"

