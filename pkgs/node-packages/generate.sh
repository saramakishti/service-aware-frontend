#!/usr/bin/env nix-shell
#! nix-shell -i bash -p nodePackages.node2nix
# shellcheck shell=bash

rm -f node-env.nix
node2nix -18 -i node-packages.json -o node-packages.nix -c composition.nix
