{ self, ... }:
{
  perSystem = { self', pkgs, ... }:
    let
      inherit (self.inputs) floco;
      base = pkgs.callPackage ./default.nix { inherit floco; clanPkgs = self'.packages; };
    in
    {
      packages = {
        ui = base.pkg.global;
        theme = base.pkg.theme;
        ui-assets = pkgs.callPackage ./nix/ui-assets.nix { };
        # EXAMPLE: GITEA_TOKEN=$(rbw get -f GITEA_TOKEN git.clan.lol) nix run .#update-ui-assets
        update-ui-assets = pkgs.callPackage ./nix/update-ui-assets.nix { };
      };
      devShells.ui = pkgs.callPackage ./shell.nix {
        inherit pkgs;
        inherit (base) fmod pkg;
        clanPkgs = self'.packages;
      };
    };
}
