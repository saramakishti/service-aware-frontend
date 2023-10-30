# Website Template

This repository is a template to build high quality websites as a team.
The frontend uses [React NextJS
](https://nextjs.org/) and the backend uses Python with the [Fastapi framework](https://fastapi.tiangolo.com/). To ensure API compatibility between frontend and backend an `openapi.json` file is generated from the Python backend code, which defines the REST API. This `openapi.json` file is then fed into [Orval](https://orval.dev/), which generates Typescript bindings for the Rest API. To ensure code correctness, we use [mypy](https://mypy-lang.org/) to ensure the Python code is correctly statically typed, and [pytest](https://docs.pytest.org/en/7.4.x/) for backend tests. A Continuos Integration (CI) Bot, verifies the code with previously mentioned Quality Assurance (QA) tools and blocks Pull requests if any errors arise.
For dependency management we use the [Nix package manager](https://nixos.org/) to ensure reproducibility.

## Getting Started: Development Environment

1. Install the Nix package manager by [downloading the nix installer](https://github.com/DeterminateSystems/nix-installer/releases) or executing this command:

```bash
curl --proto '=https' --tlsv1.2 -sSf -L https://install.determinate.systems/nix | sh -s -- install
```

2. Install direnv by [downloading the direnv package](https://direnv.net/docs/installation.html) or executing this command:

```bash
curl -sfL https://direnv.net/install.sh | bash
```

3. Clone the repository and cd into it
4. You should see an error message reading like this:

```bash
direnv: error .envrc is blocked. Run `direnv allow` to approve its content
```

5. Execute `direnv allow` to allow automatically executing the shell script `.envrc` on entering the directory
6. Go to `pkgs/clan-cli` and execute

```bash
direnv allow
```

Then wait for the backend to build  
7. To start the backend server then execute:

```
clan webui --reload --no-open --log-level debug
```

The server will automatically restart if any Python file changes.  
8. In a different shell go to `pkgs/ui` and execute

```bash
direnv allow
```

Then wait for the frontend to build.  
9. To start the frontend, execute:

```bash
npm run dev
```

Visit the website by going to [http://localhost:3000](http://localhost:3000)

## Getting started: Setup Git Workflow

1. Register your Gitea account locally by executing

```bash
tea login add
```

You will then see a prompt, please fill it out like outlined below:

```
? URL of Gitea instance:  https://gitea.gchq.icu
? Name of new Login [gitea.gchq.icu]:  gitea.gchq.icu:7171
? Do you have an access token? No
? Username:  MyUserName
? Password:  **********
? Set Optional settings: No
```

2. First add your changes to git:
   1. `git add <file1> <file2>` your changes
   2. Execute `nix fmt` to lint your files
   3. `git commit -a -m "My descriptive commit message"`
3. To automatically open up a pull request, that gets merged if all tests pass execute:

```bash
merge-after-ci
```

4. Go to https://gitea.gchq.icu to the project page, and look under "Pull Requests" if there are any issues with it.
5. If there are issues, fix them and redo step 2. Afterwards execute

```
git push origin HEAD:MyUserName-main
```

to directly push to your open pull request
