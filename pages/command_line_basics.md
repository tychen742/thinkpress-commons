# Command Line Basics

A command-line interface (CLI) lets you operate a computer by entering text commands. You will use it to find files, create folders, and start development tools. Learn the working directory and the prompt first: they tell you where a command will operate and which program is waiting for input.

```{contents}
:local:
:depth: 2
```

```{index} terminal; operating-system shell; prompt
```

## Terminal and Shell

A **terminal** is the window displaying text input and output. A **shell** is the program inside it that interprets operating-system commands. Windows Terminal can run PowerShell; macOS Terminal commonly runs Zsh; Linux terminals commonly run Bash. The same terminal can also host an application or a language REPL.

A prompt indicates that the current program is ready for input. Examples include `PS C:\Users\Alex>` in PowerShell and a prompt ending in `$` or `%` in Bash or Zsh. These are examples, not text to copy into a command. If you have entered a language REPL, exit it before typing operating-system commands. See {doc}`Interactive Language Environments <interactive_language_environments>`.

```{index} paths; working directory; relative path; absolute path
```

## Files, Folders, and Paths

A **directory**, also called a folder, contains files and other directories. A **path** identifies their location. An absolute path begins at a filesystem root, such as `C:\Users\Alex\workspace` on Windows or `/Users/alex/workspace` on macOS. A relative path starts from the shell's **current working directory**: the folder in which commands operate.

`.` means the current directory; `..` means its parent. Changing the working directory does not move the files. Put quotes around paths containing spaces, for example `cd "course projects"`.

```{index} pwd; Get-Location; cd; mkdir; ls; Get-ChildItem
```

## Navigate and Create a Practice Folder

Choose the commands for the shell you are using. PowerShell and Bash/Zsh are different command languages, even when their basic commands look similar.

| Task | Windows PowerShell | macOS/Linux Bash or Zsh |
| --- | --- | --- |
| Show the current directory. | `Get-Location` | `pwd` |
| Go to your home directory. | `cd ~` | `cd ~` |
| List files and folders. | `Get-ChildItem` | `ls` |
| Create a folder. | `mkdir tooling_practice` | `mkdir tooling_practice` |
| Enter that folder. | `cd tooling_practice` | `cd tooling_practice` |
| Return to its parent. | `cd ..` | `cd ..` |

From your home directory, create `tooling_practice`, enter it, and show its location. If the folder already exists, enter it instead of creating another one. Open a text editor, save `notes.txt` in that folder, and list the folder again. Explain the difference between the file's name and its full path.

```{index} command arguments; command history; terminal copy and paste
```

## Run and Repeat Commands

A command can include arguments, values describing what it should do. `cd tooling_practice` names a destination; `cd ..` names its parent. Your language guide will supply commands for building or running programs. Run them from the folder it specifies.

Press the up arrow to recall earlier commands. Tab completion can help fill in filenames. Copy only the command, excluding the prompt and displayed output. In macOS terminals, paste with Command+V; in Windows Terminal, use Ctrl+Shift+V; many Linux terminals also use Ctrl+Shift+V. Terminal applications can configure these shortcuts differently. Ctrl+C usually interrupts the running program rather than copying text.

If a command is not found, check its spelling, confirm the tool is installed, and open a new terminal after installation. If a file is not found, check your working directory and the path you supplied.

```{rubric} Footnotes
```
