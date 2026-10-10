# Editing Tools

A code editor helps you write and revise source files. An integrated development environment (IDE) combines editing with tools for building, debugging, and managing a project. Many editors gain these features through extensions. Your book specifies the language tools to install; this guide explains the shared editing workflow.

```{contents}
:local:
:depth: 2
```

```{index} VS Code; editor; IDE; extensions
```

## Set Up an Editor

Install [Visual Studio Code](https://code.visualstudio.com/download), or the editor specified by your course. An **extension** adds capabilities such as language-aware completion, diagnostic messages, and debugging. Install the language extension named in your book; an editor alone does not replace its compiler, SDK, or interpreter.

VS Code's Extensions view lets you search for extensions and check their publisher. Its Command Palette provides searchable actions. Open it with Ctrl+Shift+P on Windows/Linux or Shift+Command+P on macOS. See the [VS Code interface guide](https://code.visualstudio.com/docs/getstarted/userinterface) for details.

```{index} project folder; workspace; Explorer; save file
```

## Open the Folder and Save a File

Use **File > Open Folder** to open the folder containing your work. A **workspace** is the set of folders open in the editor; a single project folder is enough to begin. Opening just a source file may leave language tools unable to locate its project configuration.

Use **Explorer** to identify the files in the open folder. Open or create `notes.txt`, type a short description, and save it. Confirm the file appears in Explorer. An unsaved editor buffer is not yet a saved file that another program can read.

Your language guide identifies source extensions and project configuration files. Keep those files together as directed. If the editor reports that a document is outside the workspace, open the appropriate folder and reopen the file from Explorer. For a moved file, close the old tab and open its current location.

```{index} integrated terminal; source editor; diagnostics
```

## Edit, Save, and Run

Use **Terminal > New Terminal** to open VS Code's integrated terminal. It hosts a shell, just as a separate terminal application does. Check the working directory before running a command; an existing terminal can still be in a folder you previously visited. See {doc}`Command Line Basics <command_line_basics>`.

Write source code in the editor and shell commands in the terminal. Save the source before running it, inspect the output, and use diagnostic messages to locate problems. Syntax highlighting makes code easier to read; it does not prove the program is correct. Run the checks prescribed by your language guide.

Practice: edit `notes.txt`, save it, and locate the same file in Explorer and in a terminal listing. Explain how the editor and terminal are operating on the same saved file.

```{rubric} Footnotes
```
