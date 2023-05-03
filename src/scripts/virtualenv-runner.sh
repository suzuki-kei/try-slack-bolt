#!/bin/bash

set -eu

declare -r ROOT_DIR="$(cd "$(dirname "$0")/../.." && pwd)"
declare -r VIRTUALENV_DIR="${ROOT_DIR}/virtualenv"

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
        setup | repl | run)
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

    exit ${EXIT_STATUS_SUCCESS}
}

function command:repl
{
    source "${VIRTUALENV_DIR}/bin/activate"
    python
}

function command:run
{
    source "${VIRTUALENV_DIR}/bin/activate"
    python "${ROOT_DIR}/src/main/main.py"
}

main "$@"
