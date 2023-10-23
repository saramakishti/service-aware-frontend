{ ... }: {
  imports = [
    ./clan-cli/flake-module.nix

    ./ui/flake-module.nix
    ./theme/flake-module.nix
  ];

  perSystem = { pkgs, config, ... }: {
    packages = {
      tea-create-pr = pkgs.callPackage ./tea-create-pr { };

      #theme = pkgs.callPackage ./theme { inherit (self.inputs) floco; clanPkgs = self'.packages; };

      merge-after-ci = pkgs.callPackage ./merge-after-ci {
        inherit (config.packages) tea-create-pr;
      };
      nix-unit = pkgs.callPackage ./nix-unit { };
      inherit (pkgs.callPackages ./node-packages { }) prettier-plugin-tailwindcss;
    };
  };
}
