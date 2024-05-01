# A Semi-complete Guide to PyQt6
What I wish I had when I started out working on PyQt6.

## Goal:
Create a repository/codex of all PyQt6 layouts and widgets to help others (especially my students) make amazing graphical apps with PyQt6.

## Getting Started/Notes
I used poetry to manage my dependencies (see `pyproject.toml`). If you use pipenv instead or simply install all necessary libraries, you'll want to either review the `[tool.poetry.dependencies]` or the import statements in each file to know what to install.

### Using Poetry
Do the following:

1. Spawn a poetry shell: `poetry shell`
2. Run `poetry update`
3. [In VS Code] Choose 
    * Command Palette > Python: Select Interpreter then 
    * select the poetry shell.

## Instructions for learning
If you simply want the solutions to inspect, check out the solutions branch (`git checkout solutions`).

If you would like to follow along with the video tutorials [*coming soon to a YouTube channel near you!*]...
* Fork this repo (I will be actively developing this repository while publishing the videos)
* Use the main branch if you like or create a new "learning" branch (Ex: `git checkout -b learning`)
* Follow along with the tutorial and commit as you go.
* Compare your solution to mine by checking out the solutions branch (`git checkout solutions`)
    - NOTE: Be sure to commit or stash your work before checking out a new branch

## Change log:
### Version 0.1
Not yet released

* Added initial starter code
* Added starter code for vbox_layout.py
