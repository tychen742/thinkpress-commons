# Git Basics

Git is a version control system. It records snapshots of your project, called **commits**, so you can see what changed, when, and why, return to an earlier version, and work with others without overwriting each other's work. GitHub is a website that hosts Git repositories online for backup, sharing, and collaboration.

Git is **distributed**: every copy of a repository holds the full history, so you can commit and browse history offline and sync with GitHub when you are ready.

(commons-git-install)=
## Install and Configure Git

::::{tab-set}
:::{tab-item} Windows
Download the installer from [git-scm.com](https://git-scm.com/download/win) and accept the default options. Git for Windows adds `git` to PowerShell.
:::

:::{tab-item} macOS
Run `git --version`. If Git is missing, macOS offers to install the Command Line Developer Tools, which include Git. Homebrew users can run `brew install git` instead.
:::

:::{tab-item} Linux
On Debian or Ubuntu:

```bash
sudo apt install git
```
:::
::::

Confirm the installation:

```bash
git --version
```

Before your first commit, tell Git who you are. Git stores this name and email in every commit you make, so use the email address of your GitHub account:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global init.defaultBranch main
git config --global --list
```

(commons-git-start)=
## Start a Repository

You either turn an existing folder into a repository or copy one from GitHub.

To start tracking a project folder:

```bash
cd ~/workspace/{{book_folder}}
git init
```

Git creates a hidden `.git` folder that holds the history. Do not edit or delete it.

To copy an existing repository from GitHub, including its full history:

```bash
git clone https://github.com/<owner>/<repository>.git
cd <repository>
```

(commons-git-gitignore)=
### Ignore Files

Some files never belong in a repository: virtual environments, generated files, and anything that holds secrets. List them in a `.gitignore` file in the project folder:

```text
.venv/
__pycache__/
.ipynb_checkpoints/
.env
```

Git then leaves those files out of `git status` and commits. Add `.gitignore` before your first commit.

(commons-git-workflow)=
## Stage, Commit, and Review

A file moves through three places:

```text
working folder  --git add-->  staging area  --git commit-->  repository history
```

- The **working folder** holds your files as you edit them.
- The **staging area** holds the changes you have selected for the next commit.
- The **repository** holds the committed history.

### Check Status

`git status` shows which files changed, which are staged, and which Git does not track yet. Run it often.

```bash
git status
```

### Stage Changes

```bash
git add README.md       # stage one file
git add src/            # stage a folder
git add .               # stage everything that changed
```

Before `git add .`, check `git status` so you do not stage files you did not mean to include.

### Commit

```bash
git commit -m "Add project README"
```

The message after `-m` describes the commit. See {ref}`commons-git-habits` for how to write one.

### View History

```bash
git log                 # full history
git log --oneline       # one line per commit
git log -5              # the last five commits
git show <commit>       # one commit's details and changes
```

Each commit has an ID, a long hexadecimal hash such as `a1b2c3d...`. Most commands accept the first seven characters.

### View Differences

```bash
git diff                # unstaged changes
git diff --staged       # staged changes, what the next commit will contain
git diff README.md      # changes to one file
```

### Undo Common Mistakes

```bash
git restore README.md            # discard unstaged edits to a file
git restore --staged README.md   # unstage a file but keep the edits
git revert <commit>              # add a new commit that undoes an earlier one
```

`git restore` without `--staged` permanently discards your edits, so check `git diff` first.

(commons-git-branches)=
## Branches

A branch is an independent line of work. You can try a change on a branch while `main` stays stable, then merge it back when it works.

```bash
git branch                       # list branches; * marks the current one
git switch -c new-feature        # create a branch and switch to it
# edit, add, and commit as usual
git switch main                  # return to main
git merge new-feature            # bring the branch's commits into main
git branch -d new-feature        # delete the merged branch
```

### Merge Conflicts

If both branches changed the same lines, Git stops and marks the conflict in the file:

```text
<<<<<<< HEAD
print("version on main")
=======
print("version on new-feature")
>>>>>>> new-feature
```

Edit the file to keep the correct version, delete the marker lines, then finish the merge:

```bash
git add <file>
git commit
```

(commons-git-github)=
## Work with GitHub

A **remote** is a copy of the repository on another computer, usually GitHub. By convention the main remote is named `origin`.

### Push a Local Project to GitHub

1. Sign in to [github.com](https://github.com), click **New repository**, enter a name, choose public or private, and leave the initialize options unchecked.
2. Connect your local repository and push:

```bash
git remote add origin https://github.com/<your-username>/<repository>.git
git branch -M main
git push -u origin main
```

The `-u` option links your local `main` to `origin/main`, so afterward `git push` and `git pull` need no arguments.

The first push asks you to sign in. GitHub does not accept your account password on the command line; follow the browser sign-in prompt, or use a personal access token or SSH key as GitHub's documentation describes.

### Push and Pull

```bash
git push        # send your new commits to GitHub
git pull        # fetch new commits from GitHub and merge them into your branch
```

`git clone` sets up `origin` for you, so a cloned repository is ready for `git push` and `git pull`.

To propose changes to a shared repository, push a branch and open a **pull request** on GitHub so others can review it before it is merged.

(commons-git-habits)=
## Good Commit Habits

- **Commit small, logical changes.** One commit should do one thing, such as fix one bug or add one function. Small commits are easier to review and to undo.
- **Do not mix unrelated changes.** If you fixed a typo and added a feature, make two commits. Stage files selectively with `git add <file>`.
- **Write meaningful messages.** Use a short summary line (about 50 characters) in the imperative mood, as if completing "This commit will ...". Add a second `-m` with details when the reason is not obvious.
- **Review before you commit.** Run `git status` and `git diff --staged` to confirm exactly what goes in.
- **Pull before you start, push when you finish.** This keeps your copy current and reduces conflicts.
- **Never commit secrets.** API keys, passwords, and `.env` files stay out of the repository (see {doc}`model-access`). Removing a secret from history is hard; rotate the key if one slips in.

```text
Good: Add input validation to CSV loader
Good: Fix off-by-one error in pagination
Bad:  fixed stuff
Bad:  update
```

A typical work session:

```bash
git pull
# edit files
git status
git add <files>
git commit -m "Implement CSV parsing validation"
git push
```

## Quick Reference

| Task | Command |
|---|---|
| Set identity | `git config --global user.name "Name"` |
| Start a repository | `git init` |
| Copy a repository | `git clone <url>` |
| See what changed | `git status`, `git diff` |
| Stage | `git add <file>` |
| Commit | `git commit -m "message"` |
| History | `git log --oneline` |
| New branch | `git switch -c <name>` |
| Switch branch | `git switch <name>` |
| Merge | `git merge <name>` |
| Send to GitHub | `git push` |
| Get from GitHub | `git pull` |

To learn more, read the free [Pro Git](https://git-scm.com/book) book or practice branching at [learngitbranching.js.org](https://learngitbranching.js.org).
