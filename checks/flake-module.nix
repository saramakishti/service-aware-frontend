{ self, ... }: {
  imports = [
    ./impure/flake-module.nix
  ];
  perSystem = { pkgs, lib, self', ... }: {
    checks =
      let


        flakeOutputs = lib.mapAttrs' (name: config: lib.nameValuePair "nixos-${name}" config.config.system.build.toplevel) self.nixosConfigurations
          // lib.mapAttrs' (n: lib.nameValuePair "package-${n}") self'.packages
          // lib.mapAttrs' (n: lib.nameValuePair "devShell-${n}") self'.devShells
          // lib.mapAttrs' (name: config: lib.nameValuePair "home-manager-${name}" config.activation-script) (self'.legacyPackages.homeConfigurations or { });
      in
      flakeOutputs;
  };
}
