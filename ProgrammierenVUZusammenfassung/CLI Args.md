Leichteren Umgang mit CLI Argumenten bieten die Pakete getopt und argparse
![[Screenshot 2024-05-05 220021.png]]
The [**getopt module**](https://docs.python.org/3/library/getopt.html) is a parser for command-line options based on the convention established by the Unix `getopt()` function. It is in general used for parsing an argument sequence such as sys.argv. In other words, this module helps scripts to parse command-line arguments in sys.argv. It works similar to the C `getopt()` function for parsing command-line parameters.

## [[GETOPT]]

Python comes with a couple of tools that you can use to write command-line interfaces for your programs and apps. If you need to quickly create a minimal CLI for a small program, then you can use the [`argv`](https://docs.python.org/3/library/sys.html#sys.argv) attribute from the [`sys`](https://docs.python.org/3/library/sys.html#module-sys) module. This attribute automatically stores the arguments that you pass to a given program at the command line.

### Using `sys.argv` to Build a Minimal CLI[](https://realpython.com/command-line-interfaces-python-argparse/#using-sysargv-to-build-a-minimal-cli "Permanent link")

As an example of using `argv` to create a minimal CLI, say that you need to write a small program that lists all the files in a given directory, similar to what `ls` does. In this situation, you can write something like this:
```python
# ls_argv.py

import sys
from pathlib import Path

if (args_count := len(sys.argv)) > 2:
    print(f"One argument expected, got {args_count - 1}")
    raise SystemExit(2)
elif args_count < 2:
    print("You must specify the target directory")
    raise SystemExit(2)

target_dir = Path(sys.argv[1])

if not target_dir.is_dir():
    print("The target directory doesn't exist")
    raise SystemExit(1)

for entry in target_dir.iterdir():
    print(entry.name)
```

### Creating a CLI With `argparse`[](https://realpython.com/command-line-interfaces-python-argparse/#creating-a-cli-with-argparse "Permanent link")

A much more convenient way to create CLI apps in Python is using the [`argparse`](https://docs.python.org/3/library/argparse.html?highlight=argparse#module-argparse) module, which comes in the [standard library](https://docs.python.org/3/library/index.html). This module was first released in [Python 3.2](https://docs.python.org/3/whatsnew/3.2.html#pep-389-argparse-command-line-parsing-module) with PEP [389](https://www.python.org/dev/peps/pep-0389/) and is a quick way to create CLI apps in Python without installing a third-party library, such as [Typer](https://realpython.com/python-typer-cli/) or [Click](https://realpython.com/python-click/).

This module was released as a replacement for the older [`getopt`](https://docs.python.org/3/library/getopt.html) and [`optparse`](https://docs.python.org/3/library/optparse.html) modules because they lacked some important features.

Python’s `argparse` module allows you to:

- Parse command-line **arguments** and **options**
- Take a **variable number of parameters** in a single option
- Provide **subcommands** in your CLIs

These features turn `argparse` into a powerful CLI framework that you can confidently rely on when creating your CLI applications. To use Python’s `argparse`, you’ll need to follow four straightforward steps:

1. Import `argparse`.
2. Create an **argument parser** by instantiating [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser).
3. Add **arguments** and **options** to the parser using the [`.add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument) method.
4. Call [`.parse_args()`](https://docs.python.org/3/library/argparse.html?highlight=argparse#argparse.ArgumentParser.parse_args) on the parser to get the [`Namespace`](https://docs.python.org/3/library/argparse.html#namespace) of arguments.

As an example, you can use `argparse` to improve your `ls_argv.py` script. Go ahead and create `ls.py` with the following code:

```python
# ls.py v1

import argparse
from pathlib import Path

parser = argparse.ArgumentParser()

parser.add_argument("path")

args = parser.parse_args()

target_dir = Path(args.path)

if not target_dir.exists():
    print("The target directory doesn't exist")
    raise SystemExit(1)

for entry in target_dir.iterdir():
    print(entry.name)**
```
