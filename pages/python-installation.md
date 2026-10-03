# Python Installation

This page shows you how to check which Python versions your computer already has, install the version this book uses (Python {{python_version}}), and choose which version runs when you type `python`.

Windows does not ship with Python, while macOS and most Linux distributions include a system Python. Many computers also have several Python versions installed already, because tools such as Visual Studio or Anaconda bundle Python as a dependency. Several versions can live side by side without problems, as long as you know which one you are running.

:::{admonition} Terminal, shell, and REPL
This page uses the command line interface (CLI).

- **Terminal**: the program you open to reach the shell, such as PowerShell on Windows or Terminal on macOS and Linux.
- **Shell**: the program that interprets your commands, such as PowerShell (Windows), zsh (macOS default), or bash (Linux).
- **REPL**: a Read-Eval-Print Loop for one programming language. When you type `python` with no arguments, you enter the Python REPL and see the `>>>` prompt. Type `exit()` to leave it.
:::

(commons-python-check)=
## Check Existing Python

Open your terminal: PowerShell on Windows (search for "PowerShell" in the Start menu), Terminal on macOS (search for "Terminal" in Spotlight), or your distribution's terminal on Linux.

:::{warning}
On Windows, if Python is not installed, typing `python` may open a Microsoft Store page that offers to install it. **Do not install Python from the Microsoft Store.** The Store version often causes problems with file permissions and `pip`, and it lacks the `py` launcher. Use the python.org installer described in {ref}`commons-python-install` instead.
:::

### Check the Default Python

::::{tab-set}
:::{tab-item} Windows
```powershell
python --version
```

If Python is installed, you see a version such as `Python 3.13.7`. If it is not, you see a message like this one:

```text
Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.
```
:::

:::{tab-item} macOS
On macOS, use `python3` rather than `python`:

```bash
python3 --version
```
:::

:::{tab-item} Linux
Most distributions provide `python3`:

```bash
python3 --version
```
:::
::::

### List All Installations

::::{tab-set}
:::{tab-item} Windows
`where.exe` lists every `python.exe` on your PATH, in the order Windows searches them:

```powershell
where.exe python
```

```text
C:\Users\[user]\AppData\Local\Programs\Python\Python313\python.exe
C:\Users\[user]\AppData\Local\Programs\Python\Python312\python.exe
C:\Users\[user]\AppData\Local\Microsoft\WindowsApps\python.exe
```

The Python Launcher for Windows (`py`) lists the versions it knows about. The entry marked `*` is the launcher default:

```powershell
py --list
```

```text
 -V:3.13 *        Python 3.13 (64-bit)
 -V:3.12          Python 3.12 (64-bit)
```
:::

:::{tab-item} macOS
`which -a` lists every matching command on your PATH:

```bash
which -a python3
```

To see the version of each one, run this loop:

```bash
for p in $(which -a python3); do
    echo "$p -> $($p --version 2>&1)"
done
```

```text
/opt/homebrew/bin/python3 -> Python 3.13.7
/usr/local/bin/python3 -> Python 3.12.10
/usr/bin/python3 -> Python 3.9.6
```

If you use Homebrew, `brew list | grep python@` shows the Homebrew Python versions.
:::

:::{tab-item} Linux
```bash
which -a python3
ls /usr/bin/python3*
```
:::
::::

(commons-python-install)=
## Install Python

Install Python {{python_version}} if you have no Python, if your Python is older, or if you installed Python from the Microsoft Store.

::::{tab-set}
:::{tab-item} Windows
1. Go to [python.org/downloads/windows](https://www.python.org/downloads/windows/) and find the latest Python {{python_version}} release.
2. Download the **Windows installer (64-bit)**, a `.exe` file. Avoid the Microsoft Store and `.msix` packages.
3. Run the installer. On the first screen, check both boxes:
   - **Use admin privileges when installing py.exe**
   - **Add python.exe to PATH**
4. Click **Install Now**. The installer shows the install location, usually `C:\Users\[user]\AppData\Local\Programs\Python\Python3xx`.
5. Answer **Yes** to the permission prompt, wait for setup to finish, and click **Close**.

Open a new PowerShell window and confirm the installation with `python --version` and `py --list`.
:::

:::{tab-item} macOS
1. Go to [python.org/downloads/macos](https://www.python.org/downloads/macos/) and find the latest Python {{python_version}} release.
2. Download the **macOS 64-bit universal2 installer**, a `.pkg` file.
3. Open the installer and click **Continue** through the Read Me and License screens, **Agree** to the license, and click **Install**.
4. When the installer finishes, a Finder window opens at `/Applications/Python {{python_version}}/`. Double-click **Install Certificates.command** there so Python can make secure web requests.

```{figure} figures/python-install-macos.png
:name: commons-python-install-macos
:alt: The first screen of the python.org macOS installer, titled Welcome to the Python Installer.
:width: 400px

The python.org installer on macOS (the version shown is an example)
```

Homebrew users can run `brew install python@{{python_version}}` instead.

Open a new Terminal window and confirm with `python{{python_version}} --version`.
:::

:::{tab-item} Linux
Use your distribution's package manager. On Debian or Ubuntu:

```bash
sudo apt update
sudo apt install python3 python3-venv python3-pip
```

If your distribution does not offer Python {{python_version}}, ask your instructor which version to use, or install it with a version manager such as `pyenv` or `uv`.

Confirm with `python3 --version`.
:::
::::

(commons-python-select)=
## Choose a Python Version

### For One Command

When you have several versions, add the version number to the command to pick one. This is how you create a virtual environment with a specific Python (see {doc}`virtual-environments`).

::::{tab-set}
:::{tab-item} Windows
The `py` launcher takes the version as an option:

```powershell
py -{{python_version}} --version
py -{{python_version}}
```

The plain `python` command runs the first `python.exe` on your PATH, which is usually the version you installed most recently.
:::

:::{tab-item} macOS and Linux
Each installed version provides a command with its version number:

```bash
python{{python_version}} --version
python{{python_version}}
```

The plain `python3` command runs the first match on your PATH.
:::
::::

### Set the Default Version

The default `python` (or `python3`) is the first match found on your PATH environment variable. To change the default, change the order of PATH entries.

::::{tab-set}
:::{tab-item} Windows
1. In Windows Search, type "environment variables" and open **Edit the system environment variables**. The System Properties window appears.

   ```{figure} figures/path-windows-system-properties.png
   :name: commons-path-windows-system-properties
   :alt: The Windows System Properties window on the Advanced tab, with the Environment Variables button at the bottom.
   :width: 400px

   The System Properties window
   ```

2. Click **Environment Variables**.
3. Under **User variables for [user]**, select **Path** and click **Edit**.
4. Find the two entries for the version you want, for example:

   ```text
   C:\Users\[user]\AppData\Local\Programs\Python\Python313\Scripts\
   C:\Users\[user]\AppData\Local\Programs\Python\Python313\
   ```

5. Use **Move Up** to put both entries at the top of the list. Use **New** to add entries for a version that is missing.
6. Click **OK** in each window, then close and reopen PowerShell. You may need to sign out or restart.

Run `python --version` to confirm the change.
:::

:::{tab-item} macOS and Linux
1. Open your shell configuration file in an editor such as `nano`:

   ```bash
   nano ~/.zshrc      # zsh, the macOS default
   nano ~/.bashrc     # bash, the usual Linux default
   ```

2. Add the folder of your preferred Python to the front of PATH. For a python.org install on macOS:

   ```bash
   export PATH="/Library/Frameworks/Python.framework/Versions/{{python_version}}/bin:$PATH"
   ```

   For a Homebrew install:

   ```bash
   export PATH="$(brew --prefix python@{{python_version}})/libexec/bin:$PATH"
   ```

   Alternatively, add an alias:

   ```bash
   alias python='python{{python_version}}'
   ```

3. Save the file, then reload it:

   ```bash
   source ~/.zshrc    # or: source ~/.bashrc
   ```

4. Confirm with `python3 --version` and `which python3`.
:::
::::
