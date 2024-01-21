# Service Aware Network Project Repo

Welcome to our website repository! This repo is designed to build high-quality websites efficiently. We've carefully chosen the technologies to make development smooth and enjoyable.

**Frontend**: Our frontend is powered by [React NextJS](https://nextjs.org/), a popular and versatile framework for building web applications.

**Backend**: For the backend, we use Python along with the [FastAPI framework](https://fastapi.tiangolo.com/). To ensure seamless communication between the frontend and backend, we generate an `openapi.json` file from the Python code, which defines the REST API. This file is then used with [Orval](https://orval.dev/) to generate TypeScript bindings for the REST API. We're committed to code correctness, so we use [mypy](https://mypy-lang.org/) to ensure that our Python code is statically typed correctly. For backend testing, we rely on [pytest](https://docs.pytest.org/en/7.4.x/).

**Continuous Integration (CI)**: We've set up a CI bot that rigorously checks your code using the quality assurance (QA) tools mentioned above. If any errors are detected, it will block pull requests until they're resolved.

**Dependency Management**: We use the [Nix package manager](https://nixos.org/) to manage dependencies and ensure reproducibility, making your development process more robust.

## Supported Operating Systems

- Linux
- macOS

# Getting Started with the Development Environment

Let's get your development environment up and running:

1. **Install Nix Package Manager**:

   - You can install the Nix package manager by running this command:
     ```bash
     curl --proto '=https' --tlsv1.2 -sSf -L https://install.determinate.systems/nix | sh -s -- install
     ```

On Windows Subsystem for Linux (WSL) the installer will fail and tell you what to do. Execute the command from the error message and then afterwards execute:

```bash
sudo echo "experimental-features = nix-command flakes" > '/etc/nix/nix.conf'
```

2. **Install direnv**:

   - Install the direnv package by running the following command:
     ```bash
     curl -sfL https://direnv.net/install.sh | bash
     ```

3. **Add direnv to your shell**:

   - Direnv needs to [hook into your shell](https://direnv.net/docs/hook.html) to work.
     You can do this by executing following command:

   ```bash
   echo 'eval "$(direnv hook zsh)"' >> ~/.zshrc && echo 'eval "$(direnv hook bash)"' >> ~/.bashrc && eval "$SHELL"
   ```

4. **Clone the Repository and Navigate**:

   - Clone this repository and navigate to it.
   - If you are under Windows Subystem For Linux (WSL) please clone the repository to the home folder of your Linux. Do NOT clone it onto your Windows machine!

5. **Allow .envrc**:

   - When you enter the directory, you'll receive an error message like this:
     ```bash
     direnv: error .envrc is blocked. Run `direnv allow` to approve its content
     ```
   - Execute `direnv allow` to automatically execute the shell script `.envrc` when entering the directory.

6. **Build the Backend**:

   - Go to the `pkgs/clan-cli` directory and execute:
     ```bash
     direnv allow
     ```
   - Wait for the backend to build.

7. **Start the Backend Server**:

   - To start the backend server, execute:
     ```bash
     clan webui --reload --no-open --log-level debug --populate --emulate
     ```
   - The server will automatically restart if any Python files change. Emulated services however will not.
   - The `--populate` flag will automatically populate the database with dummy data
     - To look into the endpoints open up a swagger instance by visiting: http://localhost:2979/docs
   - The `--emulate` flag will automatically run servers the database with dummy data for the fronted to communicate with (ap, dlg, c1 and c2)
     - To look into the emulated endpoints go to http://localhost:2979/emulate

8. **Detailed Backend Documentation**

   - For detailed backend documentation go to [pkgs/clan-cli/README.md](pkgs/clan-cli/README.md)
   - We explain:
     - How to build and run a docker image
     - Internal workings of the App

9. **Build the Frontend**:

   - In a different shell, navigate to the `pkgs/ui` directory and execute:
     ```bash
     direnv allow
     ```
   - Wait for the frontend to build.

10. **Start the Frontend**:

- To start the frontend, execute:
  ```bash
  npm run dev
  ```
- Access the website by going to [http://localhost:3000](http://localhost:3000).

11. **Detailed Frontend Documentation**

- For detailed frontend documentation go to [pkgs/ui/README.md](pkgs/ui/README.md)

# Setting Up Your Git Workflow

2. **Git Workflow**:

   1. Add your changes to Git using `git add <file1> <file2>`.
   2. Run `nix fmt` to lint your files. This will format your files and make changes!
   3. Commit your changes and those of nix fmt with a descriptive message: `git commit -a -m "My descriptive commit message"`.
   4. Make sure your branch has the latest changes from upstream by executing:
      ```bash
      git fetch && git rebase origin/main --autostash
      ```
   5. Use `git status` to check for merge conflicts.
   6. If conflicts exist, resolve them. Here's a tutorial for resolving conflicts in [VSCode](https://code.visualstudio.com/docs/sourcecontrol/overview#_merge-conflicts).
   7. After resolving conflicts, execute `git merge --continue` and repeat step 5 until there are no conflicts.
