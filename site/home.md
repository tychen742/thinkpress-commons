# ThinkPress Commons

**Shared setup guides for ThinkPress instructors, TAs, and authors.**

ThinkPress Commons holds the setup guides that several ThinkPress books share: installing Python, working in virtual environments, using Jupyter notebooks, keeping work in Git, and reaching AI models safely. Each book includes the guides it needs as appendices, so students find them inside their own book.

```{div} tp-visitor-only
This site is for instructors, TAs, and ThinkPress authors. Sign in from the account menu in the upper-right corner to read the guides.

Students: open your book from [learn.thinkpress.org](https://learn.thinkpress.org/), where these guides appear as appendices.
```

````{div} tp-staff-only
```{note}
Commands in the guides use `mycourse` as the example project folder. In each book, students see that book's own folder name instead, for example `ais` or `dsm`.
```

<h2>Python and Jupyter</h2>

- {doc}`Python Installation <pages/python-installation>`
- {doc}`Virtual Environments <pages/virtual-environments>`
- {doc}`Jupyter Notebook <pages/jupyter-notebook>`

<h2>Working with Code and AI</h2>

- {doc}`Git Basics <pages/git-basics>`
- {doc}`Model Access and API Keys <pages/model-access>`

<h2>For Authors</h2>

A book includes these guides by listing them in a `commons.yml` file at its root. Each time the book builds, its CI fetches the latest guides, fills in the book's name and project folder, and places them in the book's appendices under a short book-owned introduction. To change a guide, edit it in the [thinkpress-commons repository](https://github.com/tychen742/thinkpress-commons); this site and every book that uses it update on their next build.
````
