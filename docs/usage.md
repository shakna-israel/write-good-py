# Usage

usage: write_good.py [-h] [-i INPUT] [-o OUTPUT] [-dp] [-di] [-ds] [-dt] [-dw]
                     [-da] [-dwo] [-dc]

WriteGoodPy - naive grammar linter

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        (REQUIRED) The input file. Hopefully plain text.
  -o OUTPUT, --output OUTPUT
                        (OPTIONAL) An output file to generate.
  -dp, --disable-passive
                        (OPTIONAL) Disable checking for passive voice.
  -di, --disable-illusion
                        (OPTIONAL) Disable checking for lexical illusions,
                        such as the the.
  -ds, --disable-so     (OPTIONAL) Disable checking for So at the start of a
                        sentence.
  -dt, --disable-there  (OPTIONAL) Disable checking for There Is or There Are
                        at the start of a sentence.
  -dw, --disable-weasel
                        (OPTIONAL) Disable checking for weasel words.
  -da, --disable-adverb
                        (OPTIONAL) Disable checking for words that may weaken
                        meaning.
  -dwo, --disable-wordy
                        (OPTIONAL) Disable checking for wordiness.
  -dc, --disable-cliches
                        (OPTIONAL) Disable checking for cliches.

Inspired by btford

# Examples

* Using write-good-py with all checks enabled, on a file called 'myfile.txt', and sending the output to a file called 'output.txt':

```
python write_good.py -i myfile.txt -o output.txt
```

* Using write-good-py with all checks enabled, on a file called 'myfile.txt', and sending the output to the terminal:

```
python write_good.py -i myfile.txt
```

* Using write-good-py with the Passive Voice check disabled, on a file called 'myfile.txt', and outputting to terminal:

```
python write_good.py -i myfile.txt --disable-passive
```
