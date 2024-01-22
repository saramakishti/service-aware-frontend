{ fmod
, pkg
, pkgs
, clanPkgs
}:
pkgs.mkShell {
  buildInputs = [
    fmod.config.floco.settings.nodePackage
  ];
  shellHook = ''
    export ID=${pkg.built.tree}
    currID=$(cat .floco/.node_modules_id 2> /dev/null)

    mkdir -p .floco
    if [[ "$ID" != "$currID" || ! -d "node_modules"  ]];
    then
      ${pkgs.rsync}/bin/rsync -a  --checksum  --chmod=ug+w  --delete ${pkg.built.tree}/node_modules/ ./node_modules/
      echo -n $ID > .floco/.node_modules_id
      echo "floco ok: node_modules updated"
    fi

    ln -sf ${pkgs.roboto}/share/fonts ./src

    export PATH="$PATH:$(realpath ./node_modules)/.bin"
    export NEXT_BUILD_ID=$(git log -1 --pretty=format:"%H")

    # re-generate the api code
    rm -f openapi.json
    rm -rf src/api
    cp ${clanPkgs.clan-openapi}/openapi.json .
    orval
  '';
}
