{
  description = "Consulting Website";

  inputs = {
    #nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    # https://github.com/NixOS/nixpkgs/pull/257462
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
    floco.url = "github:aakropotkin/floco";
    floco.inputs.nixpkgs.follows = "nixpkgs";
    nixpkgs-for-iosl.url = "github:Luis-Hebendanz/nixpkgs/iosl";
    flake-parts.url = "github:hercules-ci/flake-parts";
    flake-parts.inputs.nixpkgs-lib.follows = "nixpkgs";
    treefmt-nix.url = "github:numtide/treefmt-nix";
    treefmt-nix.inputs.nixpkgs.follows = "nixpkgs";
  };

  outputs = inputs @ { flake-parts, ... }:
    flake-parts.lib.mkFlake { inherit inputs; } ({ ... }: {
      systems = [
        "x86_64-linux"
        "aarch64-linux"
        "aarch64-darwin"
      ];
      imports = [
        ./checks/flake-module.nix
        ./devShell.nix
        ./formatter.nix
        ./pkgs/flake-module.nix
      ];
    });
}
