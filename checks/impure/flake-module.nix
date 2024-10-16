{ ... }: {
  perSystem = { pkgs, lib, ... }: {
    packages = {
      # a script that executes all other checks
      impure-checks = pkgs.writeShellScriptBin "impure-checks" ''
        #!${pkgs.bash}/bin/bash
        set -euo pipefail

        export PATH="${lib.makeBinPath [
          pkgs.gitMinimal
          pkgs.nix
          pkgs.rsync # needed to have rsync installed on the dummy ssh server
        ]}"
        ROOT=$(git rev-parse --show-toplevel)
        cd "$ROOT/pkgs/clan-cli"
        nix develop "$ROOT#clan-cli" -c bash -c 'TMPDIR=/tmp python -m pytest -m impure -s ./tests'
      '';
    };
  };
}
