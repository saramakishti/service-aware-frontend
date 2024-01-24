#!/usr/bin/env bash

# shellcheck shell=bash
set -euo pipefail

# GITLAB_TOKEN
if [[ -z "${GITLAB_TOKEN:-}" ]]; then
cat <<EOF
GITLAB_TOKEN environment var is not set. Please generate a new token under
https://git.tu-berlin.de/internet-of-services-lab/service-aware-network-front-end/-/settings/access_tokens
EOF
  exit 1
fi

tmpdir=$(mktemp -d)
cleanup() { rm -rf "$tmpdir"; }
trap cleanup EXIT

# Create a new ui build
nix build '.#ui' --out-link "$tmpdir/result"


tar --transform 's,^\.,assets,' -czvf "$tmpdir/assets.tar.gz" -C "$tmpdir"/result/lib/node_modules/*/out .
# upload ui assets to gitlab
gitlab_base="https://git.tu-berlin.de/api/v4/projects/internet-of-services-lab%2Fservice-aware-network-front-end"
curl --header "PRIVATE-TOKEN: $GITLAB_TOKEN" \
     --upload-file "$tmpdir/assets.tar.gz" \
     "$gitlab_base/packages/generic/ui-assets/1.0.0/ui-assets.tar.gz"


# write url and hash to ui-assets.nix
url="$gitlab_base/packages/generic/ui-assets/1.0.0/ui-assets.tar.gz"
PROJECT_DIR=$(git rev-parse --show-toplevel)
cat > "$PROJECT_DIR/pkgs/ui/nix/ui-assets.nix" <<EOF
{ fetchzip }:
fetchzip {
  url = "$url";
  sha256 = "$(nix-prefetch-url --unpack $url)";
}
EOF


cat <<EOF
Please commit the changes to ui-assets.nix and push them to the repository.
If you want clan webui to use the new ui assets.
$ git commit -m "Update ui-assets.nix" "$PROJECT_DIR/pkgs/ui/nix/ui-assets.nix"
$ git push
EOF