#!/bin/bash

set -euxo pipefail

WorkspaceRoot=$(realpath "$(dirname "$0")")

pushd "$WorkspaceRoot"
"python" -m venv .venv
".venv/bin/pip" install -r "./requirements.txt"
".venv/bin/pip" install --editable "./editable"
