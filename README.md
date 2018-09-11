# swd

[aka. *Shortest Word Distance*]

Library (and CLI) that calculates shortest distance between two words in a piece of text.

## Installation

*Requirements*: Python3

*Probably do this from within virtualenv.*

```bash
$ python setup.py install
```

## Usage

### Library

Using file-like:

```python
In [1]: import swd

In [2]: swd.calculate('first', 'second', open('textfile.txt'))
Out[2]: 4
```

Using string:

```python
In [1]: import swd

In [2]: swd.calculate('first', 'second', 'My first example for swd. With second sentence, to make sense.')
Out[2]: 4
```

### CLI

Using file (default):

```bash
swd [-f] first second textfile.txt
```

Using argument:

```bash
swd -a first second My first example for swd. With second sentence, to make sense.
```
