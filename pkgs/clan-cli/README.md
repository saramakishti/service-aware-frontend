# Starting The Backend

The clan-cli contains the command line interface as well as the graphical webui through the `clan webui` command.

Start the web ui with

```bash
clan webui --reload --no-open --log-level debug --populate --emulate
```

- The `--populate` flag will automatically populate the database with dummy data
  - To look into the endpoints open up a swagger instance by visiting: http://localhost:2979/docs
- The `--emulate` flag will automatically run servers the database with dummy data for the fronted to communicate with (ap, dlg, c1 and c2)
  - To look into the emulated endpoints go to http://localhost:2979/emulate

# Using the Uploaded Docker Image

Pull the image

```bash
docker pull git.tu-berlin.de:5000/internet-of-services-lab/service-aware-network-front-end:latest
```

Run the image

```bash
docker run -p 127.0.0.1:2979:2979 git.tu-berlin.de:5000/internet-of-services-lab/service-aware-network-front-end:latest
```

# API Documentation

Api documentation can be found in the folder `pkgs/clan-cli/tests/openapi_client/docs/`
For Entity object go to

- [tests/openapi_client/docs/EntitiesApi.md](tests/openapi_client/docs/EntitiesApi.md)
- [tests/openapi_client/docs/EventmessagesApi.md](tests/openapi_client/docs/EventmessagesApi.md)
- [tests/openapi_client/docs/ServicesApi.md](tests/openapi_client/docs/ServicesApi.md)
- [tests/openapi_client/docs/ResolutionApi.md](tests/openapi_client/docs/ResolutionApi.md)
- [tests/openapi_client/docs/RepositoriesApi.md](tests/openapi_client/docs/RepositoriesApi.md)

# Building a Docker Image if the Frontend Changed

To build a new docker image when the frontend code and/or backend code changed you first need
to get the `GITLAB_TOKEN` go to [repo access tokens](https://git.tu-berlin.de/internet-of-services-lab/service-aware-network-front-end/-/settings/access_tokens) and generate one.

- Make sure the Gitlab token has access to package registry.

Then execute

```bash
export GITLAB_TOKEN="<your-access-token>"
```

Afterwards you can execute:

```bash
./build_docker.sh
```

This will create a symlink directory called `result` to a tar.gz docker file. Import it by executing:

```bash
docker load < result
```

And then run the docker file by executing:

```bash
docker run -p 127.0.0.1:2979:2979 clan-docker:latest
```

# Uploading a Docker Image

You can use the script:

```bash
./push_docker.sh
```

### The Script Explained

Login to the tu docker image server

```bash
docker login git.tu-berlin.de:5000
```

Tag the imported image

```bash
docker image tag clan-docker:latest git.tu-berlin.de:5000/internet-of-services-lab/service-aware-network-front-end:latest
```

Push the image to the git registry

```bash
docker image push git.tu-berlin.de:5000/internet-of-services-lab/service-aware-network-front-end:latest
```

# Upload UI assets as a package

To upload the release build UI assets to gitlab as a package
first get the `GITLAB_TOKEN`. Go to [repo access tokens](https://git.tu-berlin.de/internet-of-services-lab/service-aware-network-front-end/-/settings/access_tokens) and generate one.

- Make sure the Gitlab token has access to package registry.

To upload the UI assets as a package then execute:

```bash
./upload_ui_assets.sh
```

Please commit the changes to ui-assets.nix and push them to the repository.
If you want clan webui to use the new ui assets.

```bash
$ git commit -m "Update ui-assets.nix" "$PROJECT_DIR/pkgs/ui/nix/ui-assets.nix"
$ git push
```

If you execute `clan webui` the page you will see is a precompiled release version of the UI. This above script will update said precompiled release version. The `./build_docker.sh` script execute this to make sure that the included UI in the docker is up to date.

### The Script Explained

If changes to the UI have been made, and you want them to propagate to the docker container and the `clan webui` command edit the file: [../ui/nix/ui-assets.nix](../ui/nix/ui-assets.nix).
This is where a release version of the frontend is downloaded and integrated into the cli and the docker build. To do this first execute

```bash
nix build .#ui --out-link ui-release
```

Make a tarball out of it called `ui-assets.tar.gz`

```bash
tar --transform 's,^\.,assets,' -czvf "ui-assets.tar.gz" -C ui-release/result/lib/node_modules/*/out .
```

Upload ui-assets.tar.gz to gitlab.

```bash
curl --header "PRIVATE-TOKEN: $GITLAB_TOKEN" \
     --upload-file ./ui-assets.tar.gz \
     "https://git.tu-berlin.de/api/v4/projects/internet-of-services-lab%2Fservice-aware-network-front-end/packages/generic/ui-assets/1.0.0/ui-assets.tar.gz"
```

You can find your uploaded package at the [package registry](https://git.tu-berlin.de/internet-of-services-lab/service-aware-network-front-end/-/packages)

And export the download url into a variable:

```
export url="https://git.tu-berlin.de/api/v4/projects/internet-of-services-lab%2Fservice-aware-network-front-end/packages/generic/ui-assets/1.0.0/ui-assets.tar.gz"
```

Now execute the command:

```bash
cat > "../ui/nix/ui-assets.nix" <<EOF
{ fetchzip }:
fetchzip {
  url = "$url";
  sha256 = "$(nix-prefetch-url --unpack $url)";
}
EOF
```

And now build the docker image:

```bash
nix build .#clan-docker
```

# Building a Docker Image if only the Backend Changed

To build a new docker image only when the backend code changed execute:

```bash
nix build .#clan-docker
```

This is much faster then the `./build_docker.sh` script as it needs not to build the frontend and again.
This will create a symlink directory called `result` to a tar.gz docker file. Import it by executing:

```bash
docker load < result
```

And then run the docker file by executing:

```bash
docker run -p 127.0.0.1:2979:2979 clan-docker:latest
```

- To change parameters in the generated docker image edit the file :
  [flake-module.nix at line 22](flake-module.nix)
- Documentation on `dockerTools.buildImage` you can find here: https://nix.dev/tutorials/nixos/building-and-running-docker-images.html

# Auto Generating a Python Client

For the tests we automatically generate a python client for the API endpoints. To do this execute while inside the `pkgs/clan-cli` folder:

```bash
./bin/gen-python-client
```

This will replace the folder
`tests/openapi_client`.

# Adding dependencies

**Dependency Management**: We use the [Nix package manager](https://nixos.org/) to manage dependencies and ensure reproducibility, making your development process more robust.

To add dependencies edit the file [default.nix](default.nix)

To search for a python dependency named "request" execute:

```bash
nix search nixpkgs#pythonPackages request
```

Add the depdendency at the top of the file

```nix
{
, mydep # <--- Add here
, websockets
, broadcaster
, aenum
, dateutil
, urllib3
}:
let
[...]
```

Add them into this array if they are a python dependency

```nix
dependencies = [
    argcomplete
    fastapi
    uvicorn
    sqlalchemy
    websockets
    broadcaster
    mydep # <--- Add here
  ];
```

To search for a binary dependency named "firefox" execute:

```bash
nix search nixpkgs firefox
```

Runtime dependency add them into this array:

```nix
  runtimeDependencies = [
    bash
    nix
    fakeroot
    zbar
    git
    mypy
  ];
```

# Development environment

The development environment created by `nix develop` or automatically by `direnv` is located at [shell.nix](shell.nix). The `shellHook` variable execute bash code.

# Debugging

When working on the backend of your project, debugging is an essential part of the development process. Here are some methods for debugging and testing the backend of your application:

## Test Backend Locally in Devshell with Breakpoints

To test the backend locally in a development environment and set breakpoints for debugging, follow these steps:

1. Run the following command to execute your tests and allow for debugging with breakpoints:
   ```bash
   rm -f sql_app.db && pytest -s
   ```
   You can place `breakpoint()` in your Python code where you want to trigger a breakpoint for debugging.

## Test Backend Locally in a Nix Sandbox

To run your backend tests in a Nix sandbox, you have two options depending on whether your test functions have been marked as impure or not:

### Running Tests Marked as Impure

If your test functions need to execute `nix build` and have been marked as impure because you can't execute `nix build` inside a Nix sandbox, use the following command:

```bash
nix run .#impure-checks
```

This command will run the impure test functions.

### Running Pure Tests

For test functions that have not been marked as impure and don't require executing `nix build`, you can use the following command:

```bash
nix build .#checks.x86_64-linux.clan-pytest --rebuild
```

This command will run all pure test functions.

### Inspecting the Nix Sandbox

If you need to inspect the Nix sandbox while running tests, follow these steps:

1. Insert an endless sleep into your test code where you want to pause the execution. For example:

   ```python
   import time
   time.sleep(3600)  # Sleep for one hour
   ```

2. Use `cntr` and `psgrep` to attach to the Nix sandbox. This allows you to interactively debug your code while it's paused. For example:

   ```bash
   psgrep -a -x your_python_process_name
   cntr attach <pid>
   ```

These debugging and testing methods will help you identify and fix issues in your backend code efficiently, ensuring the reliability and robustness of your application.

## Run Web UI in VSCode

Useful for vscode run and debug option

```bash
python -m clan_cli.webui --reload --no-open
```

Add this `launch.json` to your .vscode directory to have working breakpoints in your vscode editor.

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Clan Webui",
      "type": "python",
      "request": "launch",
      "module": "clan_cli.webui",
      "justMyCode": true,
      "args": ["--reload", "--no-open", "--log-level", "debug"]
    }
  ]
}
```
