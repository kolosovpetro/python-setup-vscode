# Configure Visual Studio Code for Python Development and Debugging

This guide describes a clean Python development and debugging setup in
Visual Studio Code, with a focus on Ubuntu/WSL and project-local virtual
environments.

## 1. Install Python in Ubuntu/WSL

``` bash
sudo apt update

sudo apt install -y \
  python3 \
  python3-pip \
  python3-venv
```

Verify the installation:

``` bash
python3 --version
pip3 --version
```

## 2. Install the VS Code Extensions

Install the Python extension:

``` bash
code --install-extension ms-python.python
```

Install the Python debugger:

``` bash
code --install-extension ms-python.debugpy
```

Install Pylance for code completion, navigation, and type checking:

``` bash
code --install-extension ms-python.vscode-pylance
```

Verify the extensions:

``` bash
code --list-extensions | grep -E 'python|pylance|debugpy'
```

You should see approximately:

``` text
ms-python.python
ms-python.debugpy
ms-python.vscode-pylance
```

## 3. Create a Python Project

Create and enter a project directory:

``` bash
mkdir python-test
cd python-test
```

Create a project-local virtual environment:

``` bash
python3 -m venv .venv
```

Activate it:

``` bash
source .venv/bin/activate
```

Your shell prompt should now contain `.venv`, for example:

``` text
(.venv) user@host:~/projects/python-test$
```

Upgrade `pip`:

``` bash
python -m pip install --upgrade pip
```

Open the project in VS Code:

``` bash
code .
```

## 4. Select the Python Interpreter in VS Code

Open the VS Code Command Palette:

``` text
Ctrl+Shift+P
```

Search for:

``` text
Python: Select Interpreter
```

Select the interpreter from the project virtual environment:

``` text
./.venv/bin/python
```

VS Code will normally remember the selected interpreter for the
workspace.

You can verify the interpreter from the integrated terminal:

``` bash
which python
```

It should return a path similar to:

``` text
/home/user/projects/python-test/.venv/bin/python
```

## 5. Create a Test Python Program

Create `main.py`:

``` python
def calculate(a: int, b: int) -> int:
    result = a * b
    return result


def main() -> None:
    x = 10
    y = 20

    result = calculate(x, y)

    print(f"Result: {result}")


if __name__ == "__main__":
    main()
```

Run it:

``` bash
python main.py
```

Expected output:

``` text
Result: 200
```

## 6. Debug Python in VS Code

Set a breakpoint by clicking to the left of a line number.

For example, place a breakpoint on:

``` python
result = a * b
```

Press:

``` text
F5
```

If VS Code asks which debugger to use, select:

``` text
Python Debugger → Python File
```

Execution will stop at the breakpoint. You can then:

-   Inspect local variables.
-   Hover over variables to see their values.
-   Inspect the call stack.
-   Add expressions to the Watch panel.
-   Step into and out of functions.

### Debugging Shortcuts

  Key           Action
  ------------- -------------------
  `F5`          Start / Continue
  `F9`          Toggle breakpoint
  `F10`         Step over
  `F11`         Step into
  `Shift+F11`   Step out
  `Shift+F5`    Stop

## 7. Configure `.vscode/launch.json`

A `launch.json` file is not required for simple scripts, but it is
useful for a real project.

Create:

``` text
.vscode/launch.json
```

Add:

``` json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "debugpy",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal"
        }
    ]
}
```

Now pressing `F5` will launch the currently selected Python file using
the Python debugger.

## 8. Recommended Project Structure

A simple project structure can look like this:

``` text
my-python-project/
├── .venv/
├── .vscode/
│   ├── launch.json
│   └── settings.json
├── src/
│   └── main.py
├── tests/
├── requirements.txt
├── .gitignore
└── README.md
```

## 9. Configure `.gitignore`

Do not commit the project's `.venv` directory.

Create `.gitignore`:

``` gitignore
.venv/
__pycache__/
*.py[cod]
.pytest_cache/
```

Commit dependency definitions such as `requirements.txt` instead of
committing the virtual environment.

## 10. Configure VS Code Workspace Settings

Create:

``` text
.vscode/settings.json
```

Add:

``` json
{
    "python.defaultInterpreterPath": "${workspaceFolder}/.venv/bin/python",
    "python.terminal.activateEnvironment": true
}
```

This tells VS Code to prefer the project's `.venv` interpreter and
automatically activate the environment in new Python terminals.

## 11. Typical Development Workflow

Enter the project:

``` bash
cd ~/projects/my-python-project
```

Activate the virtual environment:

``` bash
source .venv/bin/activate
```

Open VS Code:

``` bash
code .
```

The resulting setup provides:

-   Python execution inside WSL/Linux.
-   Per-project dependency isolation with `.venv`.
-   Pylance autocomplete and type checking.
-   Python debugging with `debugpy`.
-   Breakpoints, variable inspection, call stack inspection, and
    stepping.
-   Consistent project-local Python interpreter selection.

For a WSL-based development environment, keeping Python, the project,
and the virtual environment inside WSL avoids mixing Windows Python
installations with Linux Python environments.
