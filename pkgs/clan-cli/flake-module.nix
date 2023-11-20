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
        inherit (inputs.nixpkgs-for-iosl.legacyPackages.${system}.python3Packages) deal;
        inherit (inputs.nixpkgs-for-iosl.legacyPackages.${system}.python3Packages) broadcaster;
      };
      inherit (self'.packages.clan-cli) clan-openapi;
      default = self'.packages.clan-cli;
    };

    checks = self'.packages.clan-cli.tests;
  };

}
