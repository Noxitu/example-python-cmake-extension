#!/bin/bash

set -euxo pipefail

WorkspaceRoot=$(realpath "$(dirname "$0")")

tar -tvf "$WorkspaceRoot/my_package/dist/my_package-0.tar.gz"
