
!/usr/bin/env python

# write-good-py

## Inspired by Brian Ford



This is designed as a naive linter for the English Language, using specific modules.

This program is also developed in literal form, where the program is it's own documentation.

(Inspired by CoffeeScript Literal programs.)

# Development Notes:



* No Tabs used, 4 Spaces Instead

* Dependencies should be as few as possible.

* Unlike the original write-good, developing this project as a single script file, ala Bottle.py, is preferable.

* It allows it to be a drop-in file, to get up and running inside any other project out there.

* When commenting code, the comment goes above the line that is being commented about.

* Try and use a Markdown flavour of code, though beginning each line with a '#' symbol.

* Flags should only be utilised for functions that are optional to the core function. (If in doubt, go to [Issues](https://github.com/shakna-israel/write-good-py)

# Versioning Notes:



This project was developed under Python 2.7 originally, though support for Python 3.x is incoming.

But as of this commit, it remains untested.

Dependencies



```import sys```

```import os```

Debugging tools

```global verbose```

```verbose = False```

Print a helpful statement about arguments.

```def help():```

Fetch the global verbose setting, to allow for complex debugging

```global verbose```

Print a simple help statement of what to do.

```print "./write-good.py FILENAME"```

Grab a file from the commandline argument, and store it into memory:

```def get_file():```

Fetch the global verbose setting, to allow for complex debugging

```global verbose```

Check if any commandline arguments are issued to the linter.

```try:```

Expect the user to supply the filename as the first argument.

This lets the developer integrate write-good-py into all sorts of scripting environments, and doesn't put the weight of interfacing at this end.

Also means that we don't need a dozen flags. Flags are for optional things.

```if sys.argv[1]:```

```FILENAME = sys.argv[1]```

```else:```

```if verbose:```

```print sys.argv[1]```

Check if the argument the user has given is actually a file.

```if os.path.isfile(FILENAME):```

Attempt to open the file, if it fails, throw an exception.

```try:```

```file = open(FILENAME,"r")```

For each line in the file, let's run the annotate function.

```for line in file.read().split('\n'):```

```annotate(file)```

Close the file to remove any locks.

```file.close()```

```except:```

```raise Exception, "File could not be opened. Do you have permissions?"```

```except Exception as exception:```

```print "Exception: %s" % exception```

```else:```

If the user has given an argument that is not a file, raise an exception for that.

```try:```

```raise Exception, "File either does not exist, is not a file, or you do not have permissions to the file."```

```except Exception as exception:```

```print "Exception: %s" % exception```

```help()```

If no arguments are found, then run a function for that.

```except IndexError as exception:```

```if verbose:```

```print "Exception: %s" % exception```

```help()```

If any other exceptions come up, send them to the verbose system, rather than crashing on them.

```except:```

```if verbose:```

```print "Except: %s" % exception```

```help()```

This is not the final function. This program will have a main function, and that will be the final function to handle everything and which way to take things. It's just for testing.

```get_file()```
