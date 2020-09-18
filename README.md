# AdventOfCode

Solutions to [Advent of Code](https://adventofcode.com/)

## Installation

Some scripts use the package [matplotlib](https://matplotlib.org/) for visualization. Use this command to install.

```sh
pip install matplotlib
```

## Usage

I recommend to use [Visual Studio Code](https://code.visualstudio.com/) and to create a virtual environment. Download VSCode and inside the directory 2019/python in the integrated terminal do

```python
# Linux
python3 -m venv .venv
source .venv/bin/activate

# Windows
python -m venv .venv
.venv\scripts\activate
```

to create a virtual environemnt and activate it. For a more detailed descrition see the [VSCode tutorial](https://code.visualstudio.com/docs/python/python-tutorial)

To enable globally installed packages, in the .venv directoy in pyvenv.cfg, set

```python
include-system-site-packages = true
```