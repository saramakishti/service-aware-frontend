# clan-cli

The clan-cli contains the command line interface as well as the graphical webui through the `clan webui` command.

Start the web ui with

```bash
clan webui --reload --no-open --log-level debug --populate --emulate
```

- The `--populate` flag will automatically populate the database with dummy data
  - To look into the endpoints open up a swagger instance by visiting: http://localhost:2979/docs
- The `--emulate` flag will automatically run servers the database with dummy data for the fronted to communicate with (ap, dlg, c1 and c2)
  - To look into the emulated endpoints go to http://localhost:2979/emulate

# Building a Docker Image

To build a docker image of the frontend and backend be inside the `pkgs/clan-cli` folder and execute:

```bash
nix build .#clan-docker
```

This will create a symlink directory called `result` to a tar.gz docker file. Import it by executing:

```bash
docker load < result
```

And then run the docker file by executing:

```bash
docker run -p 127.0.0.1:2979:2979 clan-docker:latest
```

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

Pull the image

```bash
docker pull git.tu-berlin.de:5000/internet-of-services-lab/service-aware-network-front-end:latest
```

Run the image

```bash
docker run -p 127.0.0.1:2979:2979 git.tu-berlin.de:5000/internet-of-services-lab/service-aware-network-front-end:latest
```

# Auto Generating a Python Client

For the tests we automatically generate a python client for the API endpoints. To do this execute while inside the `pkgs/clan-cli` folder:

```bash
./bin/gen-python-client
```

This will replace the folder
`tests/openapi_client`.

# API Documentation

Api documentation can be found in the folder `pkgs/clan-cli/tests/openapi_client/docs/`
For Entity object go to [tests/openapi_client/docs/EntityCreate.md](tests/openapi_client/docs/EntityCreate.md)

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
