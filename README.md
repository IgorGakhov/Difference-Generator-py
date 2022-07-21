# Difference Generator
___

The training project "Difference Generator" on the Python Development course on [Hexlet.io](https://ru.hexlet.io/programs/python).

[![Actions Status](https://github.com/IgorGakhov/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/IgorGakhov/python-project-lvl2/actions) [![linter-and-tests-check](https://github.com/IgorGakhov/python-project-lvl2/actions/workflows/linter-and-tests-check.yml/badge.svg?branch=main)](https://github.com/IgorGakhov/python-project-lvl2/actions/workflows/linter-and-tests-check.yml) [![Maintainability](https://api.codeclimate.com/v1/badges/07dccb64d3cfc2473711/maintainability)](https://codeclimate.com/github/IgorGakhov/python-project-lvl2/maintainability) [![Test Coverage](https://api.codeclimate.com/v1/badges/07dccb64d3cfc2473711/test_coverage)](https://codeclimate.com/github/IgorGakhov/python-project-lvl2/test_coverage) 

### Built With
Languages, frameworks and libraries used in the implementation of the project:

[![](https://img.shields.io/badge/language-python-blue)](https://github.com/topics/python) [![](https://img.shields.io/badge/library-json-yellow)](https://github.com/topics/json) [![](https://img.shields.io/badge/library-pyyaml-red)](https://github.com/topics/pyyaml) [![](https://img.shields.io/badge/library-argparse-lightgrey)](https://github.com/topics/argparse)

### Dependencies:
List of dependencies, without which the project code will not work correctly:
- python = "^3.8"
- PyYAML = "^6.0"

## Description
Difference Generator is a program that determines the difference between two data structures. This is a popular task for which there are many online services, for example: http://www.jsondiff.com/. A similar mechanism is used when outputting tests or when automatically tracking changes in configuration files.

The main question in the project: how to describe the internal representation of the diff between the files, so that it is as convenient as possible. Although there are many different ways to do this, only a few of them lead to simple code.

Working with trees and tree recursion is very good at pumping algorithmic thinking. This is important because real-world processing involves constant data processing, various transformations, and collection output.

To build a diff between two structures, many operations have to be done: reading files, parsing incoming data, building a tree of differences, and generating the necessary output.

**Utility features:**
- [X] Suppported file formats: YAML, JSON.
- [X] Report generation as plain text, structured text or JSON.
- [X] Can be used as CLI tool or external library.

### Summary
* [Description](#description)
* [Installation](#installation)
  * [Python](#python)
  * [Poetry](#poetry)
  * [Project package](#project-package)
* [Usage](#usage)
  * [As external library](#as-external-library)
  * [As CLI tool](#as-cli-tool)
  * [Help](#help)
  * [Demo](#demo)
  * [Stylish format](#pushpin-stylish-format)
  * [Plain format](#pushpin-plain-format)
  * [JSON format](#pushpin-json-format)
* [Development](#development)
  * [Project Organization](#project-organization)
  * [Useful commands](#useful-commands)
___

## Installation

### Python
Before installing the package, you need to make sure that you have Python version 3.8 or higher installed:
```bash
# Windows, Ubuntu, Mac OS:
>> python --version # or python -V
Python 3.8.0+
```
:warning: If a command without a version does not work, specify the Python version explicitly: $ python3 --version.

If you have an older version installed, update with the following commands:
```bash
# Windows:
>> pip install python --upgrade

# Ubuntu:
>> sudo apt-get install python3.8

# Mac OS:
>> brew update && brew upgrade python
```

If you don't have Python installed, you can download and install it from [the official Python website](https://www.python.org/downloads/), but it's better to do this procedure through package managers. Open a terminal and run the command for your operating system:
```bash
# Windows, Linux:
>> sudo apt update
>> sudo apt install python3.X

# Mac OS:
# https://brew.sh/index_ru.html
>> brew install python3.X

# X - version number to be installed
```

### Poetry

The project uses the Poetry manager. Poetry is a tool for dependency management and packaging in Python. It allows you to declare the libraries your project depends on and it will manage (install/update) them for you. You can read more about this tool on [the official Poetry website](https://python-poetry.org/).

Poetry provides a custom installer that will install poetry isolated from the rest of your system by vendorizing its dependencies. This is the recommended way of installing poetry.

```bash
# Windows (WSL), Linux, Mac OS:
>> curl -sSL https://install.python-poetry.org | python3 -

# Windows (Powershell):
>> (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

:warning: By default, Poetry is installed into a platform and user-specific directory:

* ```~/Library/Application Support/pypoetry``` on *MacOS*.
* ```~/.local/share/pypoetry``` on *Linux/Unix*.
* ```%APPDATA%\pypoetry``` on *Windows*.

If you wish to change this, you may define the $POETRY_HOME environment variable:

```bash
>> curl -sSL https://install.python-poetry.org | POETRY_HOME=/etc/poetry python3 -
```

Add Poetry to your PATH.

Once Poetry is installed and in your $PATH, you can execute the following:

```bash
>> poetry --version
```

### Project package

To work with the package, you need to clone the repository to your computer. This is done using the git clone command. Copy the contents and type on the command line:

```bash
>> pip install --user git+https://github.com/IgorGakhov/python-project-lvl2.git

# If this operation passes for the first time
# You will probably see a message like this
The authenticity of host github.com cannot be established. RSA key fingerprint is SHA256: xxxxxxxxxxx Are you sure you want to continue connecting (yes/no/[fingerprint])? yes Warning: Permanently added github.com (RSA) to the list of known hosts.
# Type yes and press Enter
```

It remains to move to the directory and install the package:

```bash
>> cd python-project-lvl2
>> make build
>> make package-install
```

Finally, we can move on to using the project functionality!

___

## Usage

### As external library

```python
from gendiff import generate_diff
diff = generate_diff(file_path1, file_path2)
```

### As CLI tool

#### Help

The utility provides the ability to call the help command if you find it difficult to use:

```bash
>> gendiff --help
```
```bash
usage: gendiff [-h] [-f {stylish,json,plain}] first_file second_file

Compares two configuration files and shows a difference.

positional arguments:
  first_file
  second_file

options:
  -h, --help            show this help message and exit
  -f {stylish,json,plain}, --format {stylish,json,plain}
                        set format of output (default: stylish)
```
[![asciicast](https://asciinema.org/a/Cjlf4jWFE39jclLIljA7Pw2Zk.svg)](https://asciinema.org/a/Cjlf4jWFE39jclLIljA7Pw2Zk)

#### Demo

:zap: Both absolute and relative paths to files are supported.

##### :pushpin: _Stylish format_

If format option is omitted, output will be in _**stylish format**_ string by default.

The diff is built based on how the files have changed relative to each other, the keys are displayed in alphabetical order.

The absence of a plus or minus indicates that the key is in both files, and its values are the same. In all other situations, the key value is either different, or the key is in only one file.

**Example**:
```bash
>> gendiff filepath1.json filepath2.json
```
```bash
{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}
```

##### Compare two flat JSON and/or YAML files: stylish format
[![asciicast](https://asciinema.org/a/x47G5yv6JiCKmHHAYbR9crjOJ.svg)](https://asciinema.org/a/x47G5yv6JiCKmHHAYbR9crjOJ)

##### Compare two nested JSON and/or YAML files: stylish format
[![asciicast](https://asciinema.org/a/YD2YYYfeX1YntooVNRUWBEmug.svg)](https://asciinema.org/a/YD2YYYfeX1YntooVNRUWBEmug)

##### :pushpin: _Plain format_

The text reflects the situation, as if we have combined the second object with the first.

* If the new property value is complex, then [complex value] is written.
* If the property is nested, then the entire path to the root is displayed, and not just taking into account the parent.

**Example**:
```bash
>> gendiff --format plain filepath1.json filepath2.json
```
```bash
Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]
```

##### Compare two flat JSON and/or YAML files: plain format

[![asciicast](https://asciinema.org/a/RaF5tHGDumpZY73IrlH1uoGyh.svg)](https://asciinema.org/a/RaF5tHGDumpZY73IrlH1uoGyh)

##### Compare two nested JSON and/or YAML files: plain format

[![asciicast](https://asciinema.org/a/l95EFhzR3nDpCjzYKeC1At13i.svg)](https://asciinema.org/a/l95EFhzR3nDpCjzYKeC1At13i)

##### :pushpin: _JSON format_

JSON (JavaScript Object Notation) is a standard text format for representing structured data based on JavaScript object syntax. It is usually used to transfer data in web applications (e.g. sending some data from the server to the client so that it can be displayed on a web page or vice versa).

**Example**:
```bash
>> gendiff --format json filepath1.json filepath2.json
```
```bash
{
    "follow": {
        "value": false,
        "node type": "REMOVED"
    },
    "host": {
        "value": "hexlet.io",
        "node type": "UNCHANGED"
    },
    "proxy": {
        "value": "123.234.53.22",
        "node type": "REMOVED"
    },
    "timeout": {
        "value": {
            "old": 50,
            "new": 20
        },
        "node type": "UPDATED"
    },
    "verbose": {
        "value": true,
        "node type": "ADDED"
    }
}
```

**Node types**:

* **_<span style="color:LawnGreen">"added"</span>_**: key was not present in the first file, but was present in the second file.
* **_<span style="color:Red">"removed"</span>_**: key was present in the first file, but not present in the second file.
* **_<span style="color:Gold">"unchanged"</span>_**: key exists in both files and its values match.
* **_<span style="color:Blue">"updated"</span>_**: key exists in both files, but its values do not match.
* **_<span style="color:Purple">"nested"</span>_**: similar to 'updated', but here the values are dictionaries.

##### Compare two flat JSON and/or YAML files: JSON format

[![asciicast](https://asciinema.org/a/iq0XIb4uPPmtSJtyuthuTeWwh.svg)](https://asciinema.org/a/iq0XIb4uPPmtSJtyuthuTeWwh)

##### Compare two nested JSON and/or YAML files: JSON format

[![asciicast](https://asciinema.org/a/ovmSSaB7EtwJNYwl3ccyzuoVh.svg)](https://asciinema.org/a/ovmSSaB7EtwJNYwl3ccyzuoVh)

___

## Development

### Project Organization

```bash

.
├── gendiff
│   ├── __init__.py
│   ├── cli.py
│   ├── file_processor
│   │   ├── __init__.py
│   │   ├── gendiff.py
│   │   ├── data_parser.py
│   │   └── diff_assembler.py
│   ├── formatters
│   │   ├── __init__.py
│   │   ├── tree_render.py
│   │   ├── stylish.py
│   │   ├── plain.py
│   │   └── json.py
│   └── scripts
│       ├── __init__.py
│       └── run.py
├── Makefile
├── poetry.lock
├── pyproject.toml
├── README.md
├── setup.cfg
└── tests
    ├── fixtures
    │   ├── diff_requests
    │   └── diff_responses
    ├── test_cli.py
    └── test_gendiff.py
```

### Useful commands

The commands most used in development are listed in the Makefile:

<dl>
    <dt><code>make package-install</code></dt>
    <dd>Installing a package in the user environment.</dd>
    <dt><code>make build</code></dt>
    <dd>Building the distribution of he Poetry package.</dd>
    <dt><code>make package-force-reinstall</code></dt>
    <dd>Reinstalling the package in the user environment.</dd>
    <dt><code>make lint</code></dt>
    <dd>Checking code with linter.</dd>
    <dt><code>make test</code></dt>
    <dd>Tests the code.</dd>
    <dt><code>make fast-check</code></dt>
    <dd>Builds the distribution, reinstalls it in the user's environment, checks the code with tests and linter.</dd>
</dl>

___

**Thank you for attention!**
:man_technologist: Author: [@IgorGakhov](https://github.com/IgorGakhov)
