# Interactive Language Environments (REPLs)

A read-evaluate-print loop (**REPL**) accepts language input, evaluates it, displays the result, and waits for another entry. It is useful for checking an expression or exploring a small idea without creating a complete project. Python's interactive interpreter, CSharpRepl, and Java's JShell are examples. Your book provides the installation and launch instructions for its language.

```{contents}
:local:
:depth: 2
```

```{index} REPL; language shell; operating-system shell
```

## Recognize the Environment

An operating-system shell runs commands for files and processes. A language REPL evaluates code in its own language. Both can appear in the same terminal window, but they accept different input.

| Environment | Example prompt | Input it expects |
| --- | --- | --- |
| PowerShell, Bash, or Zsh | `PS ...>`, `$`, or `%` | Operating-system commands. |
| Python interactive interpreter | `>>>` | Python expressions and statements. |
| CSharpRepl | `>` | C# expressions and statements. |
| JShell | `jshell>` | Java snippets. |

Prompts can be customized, so also pay attention to the tool you started. To run an operating-system command, first return to the operating-system shell. To evaluate a language expression, enter its REPL first. Do not copy prompt characters into your input.

```{index} REPL state; expression results; saved program
```

## Experiment and Return to Saved Programs

REPLs commonly retain variables and definitions during a session. That makes experiments convenient, but a snippet can depend on something entered earlier. Start a fresh session when checking whether an example works independently.

An expression's displayed result is feedback from the REPL. A saved program generally needs an explicit output operation to display that result. Copy useful code into a source file and follow your language guide's build/run workflow when the task asks for a saved application or submission. A REPL session is not automatically a project or a submitted file.

Before proceeding, identify your current prompt, explain which language it accepts, and demonstrate returning to the operating-system shell using the exit command from your language guide. Then identify the saved files required for your next task.

```{rubric} Footnotes
```
