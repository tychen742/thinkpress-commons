# Model Access and API Keys

Many labs in {{book_title}} send requests to an AI model. This page explains the ways your code can reach a model, how to handle an API key safely, and what to watch for in cost and privacy. The book's own model-access page lists the current models, providers, and prices; check it before you start a lab, because those details change often.

(commons-model-options)=
## Ways to Reach a Model

Your instructor or book tells you which option to use. The lab code is written so that switching options changes configuration, not your program logic.

**ThinkPress model gateway.** Some courses provide a gateway: a service that forwards your requests to a model provider under a course account. You receive a course key or sign-in, and the instructor sets the available models and usage limits. You do not pay a provider directly.

**Your own API key.** You create an account with a model provider, add a payment method or use a free tier, and generate an API key. Requests are billed to your account, so you control the model choice and are responsible for the cost.

**Local models.** You run an open-weight model on your own computer with a local model server. Requests never leave your machine and cost nothing per call, but you need enough memory and disk space, and small local models are usually less capable than hosted ones.

(commons-model-api-key)=
## Create an API Key

An API key is a secret string that identifies you to a provider or gateway. Anyone who has your key can make requests billed to you.

1. Sign in to the provider's or gateway's web dashboard.
2. Find the API keys section and create a new key. Give it a descriptive name, such as the course and term.
3. Copy the key right away. Most dashboards show the full key only once.
4. If the dashboard allows it, set a monthly spending limit.

(commons-model-env-var)=
## Store the Key in an Environment Variable

Keep the key out of your code. **Never type a key into a script, a notebook cell, or a Markdown note, and never commit it to Git.** Notebooks are especially risky: a key printed in an output cell stays in the file even after you delete the code that printed it.

Instead, store the key in an environment variable, and let your code read it from there. The variable name depends on the provider or gateway; the examples below use `MODEL_API_KEY`, so use the name your book specifies.

(commons-model-dotenv)=
### Option 1: A `.env` File (Recommended)

Create a file named `.env` in your project folder:

```text
MODEL_API_KEY=paste-your-key-here
```

Add `.env` to your `.gitignore` file **before** your first commit, so Git never tracks it (see {doc}`git-basics`):

```text
.env
```

With your virtual environment active, install `python-dotenv`:

```bash
pip install python-dotenv
```

Then load the file at the top of your script or notebook:

```python
import os
from dotenv import load_dotenv

load_dotenv()  # reads .env in the current folder into the environment
api_key = os.environ["MODEL_API_KEY"]
```

If the variable is missing, `os.environ[...]` raises a `KeyError`, which tells you right away that the key was not loaded. Do not print the key to check it; print `len(api_key)` or `"MODEL_API_KEY" in os.environ` instead.

### Option 2: Set the Variable in Your Shell

You can also set the variable in your terminal before launching Python or Jupyter.

::::{tab-set}
:::{tab-item} Windows
For the current PowerShell session only:

```powershell
$env:MODEL_API_KEY = "paste-your-key-here"
```

To save it for your user account (takes effect in new windows):

```powershell
[Environment]::SetEnvironmentVariable("MODEL_API_KEY", "paste-your-key-here", "User")
```
:::

:::{tab-item} macOS and Linux
For the current terminal session only:

```bash
export MODEL_API_KEY="paste-your-key-here"
```

To save it, add the same line to `~/.zshrc` or `~/.bashrc` and open a new terminal.
:::
::::

Launch Jupyter from that same terminal so the notebook inherits the variable. Your code reads it with `os.environ["MODEL_API_KEY"]`, as above.

(commons-model-leak)=
### If a Key Leaks

If you commit a key, paste it somewhere public, or share it by accident, **revoke it immediately** in the dashboard and create a new one. Deleting the file or commit is not enough, because the key remains in Git history and in any copy someone already made.

(commons-model-cost)=
## Cost and Rate Limits

- **You pay per use.** Hosted models usually charge by the amount of text sent and received, measured in tokens. Long prompts, long documents, and long outputs cost more.
- **Loops multiply cost.** A cell that calls a model inside a loop over a thousand rows makes a thousand requests. Test on a few rows first.
- **Rate limits cap your speed.** Providers and gateways limit requests per minute and tokens per minute. If you exceed a limit, requests fail with an error (often HTTP status 429). Wait and retry, add a short pause between calls, or reduce the batch size.
- **Watch your usage.** Provider and gateway dashboards show usage and spending. Check them after your first few labs, and set a spending limit if one is available.
- **Choose the right model.** Smaller, cheaper models handle many lab tasks well. Use the model the lab specifies unless the exercise asks you to compare.

(commons-model-privacy)=
## Privacy

Text you send to a hosted model leaves your computer and is processed, and possibly stored, by the provider.

- **Do not send personal data**, such as names with contact details, student records, health information, or identification numbers, about yourself or anyone else.
- **Do not send confidential data**, such as an employer's internal documents, customer data, or source code you are not allowed to share.
- **Use the course data.** Labs provide synthetic or public data for a reason. If you want to try your own data, remove identifying details first.
- **Read the terms.** Providers differ in whether they retain requests or use them for training, and the terms for free tiers may differ from paid plans. A gateway or local model may be the right choice when privacy matters.

(commons-model-current)=
## Current Models and Prices

Model names, versions, prices, and provider details change faster than any book edition. {{book_title}} keeps them in one place, its own page on models and prices, so the lab instructions stay stable. When a lab says "the default model," look up the current name there.
