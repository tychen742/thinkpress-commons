# Virtual Environments

A virtual environment is a folder inside your project that holds its own copy of the Python interpreter link and its own installed packages. Packages you install while the environment is active go into that folder, not into your system Python. This keeps projects from breaking each other when they need different package versions, and it lets you rebuild the same setup on another computer.

This page assumes you have Python {{python_version}} installed (see {doc}`python-installation`).

(commons-venv-project)=
## Create a Project Folder

Create a `workspace` folder in your home folder, and a `{{book_folder}}` project folder inside it. You need three shell commands:

- `mkdir` makes a directory.
- `cd` changes the current directory.
- `ls` lists the contents of a directory.

::::{tab-set}
:::{tab-item} Windows
Use PowerShell:

```powershell
cd ~
mkdir workspace
cd workspace
mkdir {{book_folder}}
cd {{book_folder}}
```

Your prompt now ends with `\workspace\{{book_folder}}>`.
:::

:::{tab-item} macOS and Linux
Use Terminal:

```bash
cd ~
mkdir -p workspace/{{book_folder}}
cd workspace/{{book_folder}}
```

Your prompt now shows `~/workspace/{{book_folder}}`.
:::
::::

Windows separates folders with backslashes (`\`); macOS and Linux use forward slashes (`/`). PowerShell accepts both.

(commons-venv-create)=
## Create the Virtual Environment

The general command is:

```bash
python -m venv <environment_folder>
```

Here `-m venv` runs Python's built-in `venv` module. By convention, the environment folder is named `.venv`. Run the command inside your project folder, and name the Python version you want so the environment uses it even when your default Python is different:

::::{tab-set}
:::{tab-item} Windows
```powershell
py -{{python_version}} -m venv .venv
ls
```

`ls` shows the new `.venv` folder.
:::

:::{tab-item} macOS and Linux
```bash
python{{python_version}} -m venv .venv
ls -a
```

Names that start with a dot are hidden, so you need `ls -a` to see `.venv`.
:::
::::

Inside `.venv`, the `Scripts` (Windows) or `bin` (macOS and Linux) folder holds the Python and `pip` executables and the activation scripts. The `Lib\site-packages` (Windows) or `lib/python{{python_version}}/site-packages` (macOS and Linux) folder holds every package you install. A new environment contains only `pip`.

(commons-venv-activate)=
## Activate the Environment

Activate the environment each time you start working on the project. Run the command from the project folder.

::::{tab-set}
:::{tab-item} Windows
```powershell
.\.venv\Scripts\activate
```

```text
(.venv) PS C:\Users\[user]\workspace\{{book_folder}}>
```
:::

:::{tab-item} macOS and Linux
```bash
source .venv/bin/activate
```

```text
(.venv) [user]@[host]:~/workspace/{{book_folder}}$
```
:::
::::

The `(.venv)` prefix on the prompt tells you the environment is active. While it is active, `python` and `pip` refer to the environment's copies, whatever your system default is. Check with `python --version`.

(commons-venv-windows-policy)=
### Fix the Windows Activation Error

PowerShell may refuse to run the activation script with an error like this:

```text
.\.venv\Scripts\activate : File C:\Users\[user]\workspace\{{book_folder}}\.venv\Scripts\Activate.ps1
cannot be loaded because running scripts is disabled on this system.
    + CategoryInfo          : SecurityError: (:) [], PSSecurityException
    + FullyQualifiedErrorId : UnauthorizedAccess
```

PowerShell blocks local scripts by default. Allow scripts for your user account with this command (no administrator rights needed because of `-Scope CurrentUser`):

```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Close every PowerShell window, open a new one, return to the project folder, and activate again.

(commons-venv-requirements)=
## Install Packages and Record Them

With the environment active, install packages with `pip`, which downloads them from the Python Package Index (PyPI):

```bash
pip install <package_name>
```

Record the packages your project uses in a `requirements.txt` file in the project folder so you, a teammate, or another computer can rebuild the environment:

```bash
pip freeze > requirements.txt
```

To install everything listed in a `requirements.txt` file into a fresh environment:

```bash
pip install -r requirements.txt
```

If your book or course provides a `requirements.txt`, use it instead of installing packages one by one.

:::{tip}
Do not put `.venv` under version control. Add `.venv/` to your `.gitignore` file and commit `requirements.txt` instead (see {doc}`git-basics`).
:::

(commons-venv-deactivate)=
## Deactivate the Environment

When you finish working, deactivate the environment so later installs do not land in this project by mistake:

```bash
deactivate
```

The command works from any folder, and the `(.venv)` prefix disappears from the prompt.

## Start a Work Session

Each time you return to the project, open a terminal and run:

::::{tab-set}
:::{tab-item} Windows
```powershell
cd ~\workspace\{{book_folder}}
.\.venv\Scripts\activate
```
:::

:::{tab-item} macOS and Linux
```bash
cd ~/workspace/{{book_folder}}
source .venv/bin/activate
```
:::
::::
