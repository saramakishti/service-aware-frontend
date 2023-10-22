{
  # Use this path to our repo root e.g. for UI test
  # inputs.clan-core.url = "../../../../.";

  # this placeholder is replaced by the path to clan-core
  inputs.clan-core.url = "__CLAN_CORE__";

  outputs = { self, clan-core }:
    let
      clan = clan-core.lib.buildClan {
        directory = self;
        clanName = "test_with_core_and_pass_clan";
        machines = {
          vm1 = { lib, ... }: {
            clan.networking.deploymentAddress = "__CLAN_DEPLOYMENT_ADDRESS__";
            system.stateVersion = lib.version;
            clanCore.secretStore = "password-store";
            clanCore.secretsUploadDirectory = lib.mkForce "__CLAN_SOPS_KEY_DIR__/secrets";

            clan.networking.zerotier.controller.enable = true;

            systemd.services.shutdown-after-boot = {
              enable = true;
              wantedBy = [ "multi-user.target" ];
              after = [ "multi-user.target" ];
              script = ''
                #!/usr/bin/env bash
                shutdown -h now
              '';
            };
          };
        };
      };
    in
    {
      inherit (clan) nixosConfigurations clanInternals;
    };
}
