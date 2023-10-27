# shellcheck shell=bash
set -xeuo pipefail

# GITEA_TOKEN
if [[ -z "${GITEA_TOKEN:-}" ]]; then
  echo "GITEA_TOKEN is not set"
  echo "Go to https://gitea.gchq.icu/user/settings/applications and generate a token"
  exit 1
fi

DEPS=$(nix shell --inputs-from '.#' "nixpkgs#gnutar" "nixpkgs#curl" "nixpkgs#gzip" -c bash -c "echo \$PATH")
export PATH=$PATH:$DEPS


PROJECT_DIR=$(git rev-parse --show-toplevel)
tmpdir=$(mktemp -d)
cleanup() { rm -rf "$tmpdir"; }
trap cleanup EXIT

nix build '.#ui' --out-link "$tmpdir/result"

tar --transform 's,^\.,assets,' -czvf "$tmpdir/assets.tar.gz" -C "$tmpdir"/result/lib/node_modules/*/out .
NAR_HASH=$(nix-prefetch-url --unpack file://<(cat "$tmpdir/assets.tar.gz"))

owner=ui-asset-bot
package_name=ui
package_version=$NAR_HASH

url="https://gitea.gchq.icu/api/packages/$owner/generic/$package_name/$package_version/assets.tar.gz"
set +x
curl --upload-file "$tmpdir/assets.tar.gz" -X PUT "$url?token=$GITEA_TOKEN"
set -x

TEST_URL=$(nix-prefetch-url --unpack "$url")
if [[ $TEST_URL != "$NAR_HASH" ]]; then
  echo "Prefetch failed. Expected $NAR_HASH, got $TEST_URL"
  exit 1
fi


cat > "$PROJECT_DIR/pkgs/ui/nix/ui-assets.nix" <<EOF
{ fetchzip }:
fetchzip {
  url = "$url";
  sha256 = "$NAR_HASH";
}
EOF

