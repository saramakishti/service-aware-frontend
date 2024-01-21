{ inputs, ... }:
{
  perSystem = { self', pkgs, system, ... }: {
    devShells.clan-cli = pkgs.callPackage ./shell.nix {
      inherit (self'.packages) clan-cli ui-assets nix-unit;
    };
    packages = {
      clan-cli = pkgs.python3.pkgs.callPackage ./default.nix {
        inherit (self'.packages) ui-assets;
        inherit (inputs) nixpkgs;
        inherit (inputs.nixpkgs-for-iosl.legacyPackages.${system}.python3Packages) broadcaster;
      };
      inherit (self'.packages.clan-cli) clan-openapi;
      default = self'.packages.clan-cli;


      clan-docker = pkgs.dockerTools.buildImage {
        name = "clan-docker";
        tag = "latest";
        created = "now";
        config = {
          Cmd = [ "${self'.packages.clan-cli}/bin/clan" "webui" "--no-open" "--host" "0.0.0.0" ];
          ExposedPorts = {
            "2979/tcp" = { };
          };
        };
      };
    };

    checks = self'.packages.clan-cli.tests;
  };

}
