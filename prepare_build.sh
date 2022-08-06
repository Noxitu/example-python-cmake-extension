#!/bin/bash

set -euxo pipefail

WorkspaceRoot=$(realpath "$(dirname "$0")")

mkdir -p "$WorkspaceRoot/.conan"
pushd "$WorkspaceRoot/.conan"

"conan" install "$WorkspaceRoot/my_package/src"
