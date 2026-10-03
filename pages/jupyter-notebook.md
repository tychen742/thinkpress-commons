# Jupyter Notebook

Jupyter Notebook is a browser-based tool for interactive coding. A notebook (`.ipynb` file) mixes runnable code, its output, and formatted notes in one document, which makes it a common tool for labs, data analysis, and prototyping.

This page assumes you have a project folder with a virtual environment (see {doc}`virtual-environments`).

(commons-jupyter-install)=
## Install Jupyter Notebook

Python installs packages with `pip`, which downloads them from the Python Package Index (PyPI). Before you install anything:

1. Change directory into your project folder.
2. Activate the project virtual environment, so the prompt starts with `(.venv)`.

Then install the `notebook` package:

```bash
pip install notebook
```

`pip` prints many `Collecting` and `Downloading` lines while it installs Jupyter and its dependencies, and ends with a `Successfully installed` line.

(commons-jupyter-launch)=
## Launch Jupyter

From the project folder, with the environment active, run:

```bash
jupyter notebook
```

The terminal now runs the **Jupyter server** and prints its log. Leave this terminal open while you work. The server also opens the Jupyter Home page in your default browser at `http://localhost:8888/tree`, showing the files in your project folder.

```{figure} figures/jupyter-new-empty.png
:name: commons-jupyter-home
:alt: The Jupyter Home page at localhost:8888/tree with Files and Running tabs and New and Upload buttons.
:width: 475px

The Jupyter Home page
```

If the browser does not open, copy the `http://localhost:8888/tree?token=...` address from the terminal log into your browser.

(commons-jupyter-new)=
## Create a Notebook

On the Home page, click **New** and choose **Notebook**, then select the **Python 3 (ipykernel)** kernel if asked. A new tab opens with a notebook named `Untitled.ipynb`.

To rename it, click the title `Untitled` at the top of the page, type a new name such as `test`, and keep the `.ipynb` extension.

```{figure} figures/jupyter-rename-notebook.png
:name: commons-jupyter-rename
:alt: The Rename File dialog with the new name test.ipynb.
:width: 250px

Renaming a notebook
```

(commons-jupyter-cells)=
## Cells

A notebook is a list of cells. There are two main kinds.

### Code Cells

A new cell is a code cell. Type Python code and press `Shift+Enter` to run it. The output appears below the cell, and the number in brackets shows the order in which cells ran.

```python
print("hello world")
```

```{figure} figures/jupyter-hello-world.png
:name: commons-jupyter-hello-world
:alt: A code cell containing print("hello world") with the output hello world below it.
:width: 350px

Running a code cell
```

Cells share one Python session, so a variable defined in one cell is available in cells you run later. Because you can run cells in any order, run them top to bottom when you want reliable results.

### Markdown Cells

Markdown cells hold formatted notes. Markdown is a lightweight markup language:

```text
# Heading level 1
## Heading level 2
**bold**, *italic*, `code`
- bulleted item
1. numbered item
$E = mc^2$ for a LaTeX equation
```

Running a Markdown cell renders the formatted text.

(commons-jupyter-modes)=
## Modes and Keyboard Shortcuts

A notebook has two modes:

- **Edit mode**: you are typing inside a cell. Press `Enter` or click inside a cell to enter it.
- **Command mode**: you are working with whole cells. Press `Esc` or click beside a cell to enter it. The single-key shortcuts below work only in command mode.

| Shortcut | Mode | Action |
|---|---|---|
| `Shift+Enter` | Either | Run the cell and move to the next one |
| `Ctrl+Enter` | Either | Run the cell and stay on it |
| `A` | Command | Insert a cell above |
| `B` | Command | Insert a cell below |
| `C`, `X`, `V` | Command | Copy, cut, paste cells |
| `D`, `D` | Command | Delete the selected cells |
| `Z` | Command | Undo a cell operation |
| `M` | Command | Change the cell to Markdown |
| `Y` | Command | Change the cell to code |
| `Ctrl+/` | Edit | Comment or uncomment lines |
| `Ctrl+S` | Either | Save the notebook |

On macOS, use `Cmd` in place of `Ctrl`. For the full list, choose **Help > Show Keyboard Shortcuts**.

(commons-jupyter-kernel)=
## The Kernel

The kernel is the Python process that runs your code. Use the **Kernel** menu to control it:

- **Interrupt Kernel** (`I`, `I` in command mode) stops a cell that runs too long, such as an infinite loop.
- **Restart Kernel** (`0`, `0` in command mode) clears all variables and starts a fresh Python session. Restart and rerun all cells when results look inconsistent.

The kernel uses the Python and packages of the environment you launched Jupyter from. If an import fails, check that you activated the right environment before running `jupyter notebook`.

## Save and Export

Jupyter autosaves every few minutes; press `Ctrl+S` to save now. To export, choose **File > Save and Export Notebook As** and pick a format such as HTML, PDF, or an executable Python script (`.py`).

(commons-jupyter-shutdown)=
## Shut Down

To shut down cleanly:

1. Save each open notebook, then close it with **File > Close and Shut Down Notebook**.
2. On the Home page, open the **Running** tab and shut down any kernels still listed.
3. Choose **File > Shut Down** on the Home page and close the tab.

If you already closed the browser tabs, go to the server terminal and press `Ctrl+C`, then confirm if prompted.

Finally, run `deactivate` to leave the virtual environment, and `exit` to close the terminal.

(commons-jupyter-aliases)=
## Optional: Launch Shortcuts

Shell aliases cut the launch routine to three short commands:

- `proj` changes to your project folder.
- `venv` activates the virtual environment.
- `jn` launches Jupyter Notebook.

::::{tab-set}
:::{tab-item} Windows
PowerShell reads a profile script at startup. Find its location and create it if it does not exist:

```powershell
echo $PROFILE
if (!(Test-Path $PROFILE)) { New-Item -Path $PROFILE -ItemType File -Force }
notepad $PROFILE
```

Paste these lines into the profile, save, and close Notepad:

```powershell
function Set-ProjectLocation { Set-Location ~\workspace\{{book_folder}} }
New-Alias -Name proj -Value Set-ProjectLocation

function Enable-Venv { .\.venv\Scripts\Activate.ps1 }
New-Alias -Name venv -Value Enable-Venv

function Start-JupyterNotebook { jupyter notebook }
New-Alias -Name jn -Value Start-JupyterNotebook
```

Open a new PowerShell window for the aliases to take effect. The profile is itself a script, so it needs the execution policy fix in {doc}`virtual-environments`.
:::

:::{tab-item} macOS and Linux
Add these lines to `~/.zshrc` (zsh) or `~/.bashrc` (bash):

```bash
alias proj='cd ~/workspace/{{book_folder}}'
alias venv='source .venv/bin/activate'
alias jn='jupyter notebook'
```

Reload the file with `source ~/.zshrc` (or `source ~/.bashrc`), or open a new terminal.
:::
::::

Now a work session starts with:

```bash
proj
venv
jn
```
