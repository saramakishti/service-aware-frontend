{
  perSystem = { pkgs, ... }:
    let
      pyproject = builtins.fromTOML (builtins.readFile ./pyproject.toml);
      name = pyproject.project.name;
      package = pkgs.callPackage ./default.nix { };
    in
    {
      packages.${name} = package;
      packages.default = package;
      checks = package.tests;
    };
}
