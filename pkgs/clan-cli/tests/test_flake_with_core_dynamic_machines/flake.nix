{
  # Use this path to our repo root e.g. for UI test
  # inputs.clan-core.url = "../../../../.";

  # this placeholder is replaced by the path to nixpkgs
  inputs.clan-core.url = "__CLAN_CORE__";

  outputs = { self, clan-core }:
    let
      clan = clan-core.lib.buildClan {
        directory = self;
        clanName = "core_dynamic_machine_clan";
        machines =
          let
            machineModules = builtins.readDir (self + "/machines");
          in
          builtins.mapAttrs
            (name: _type: import (self + "/machines/${name}"))
            machineModules;
      };
    in
    {
      inherit (clan) nixosConfigurations clanInternals;
    };
}
