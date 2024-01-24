#!/usr/bin/env bash

set -euo pipefail

PROJECT_DIR=$(git rev-parse --show-toplevel)
"$PROJECT_DIR"/pkgs/clan-cli/upload_ui_assets.sh

nix build .#clan-docker

cat <<EOF
==============================
Please commit the changes to ui-assets.nix and push them to the repository.
If you want clan webui to use the new ui assets.
$ git commit -m "Update ui-assets.nix" "$PROJECT_DIR/pkgs/ui/nix/ui-assets.nix"
$ git push
EOF