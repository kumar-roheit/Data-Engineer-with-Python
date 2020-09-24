*  Construct the relative path to a file or directory below your current location by subtracting the absolute path of your current location from the absolute path of the thing you want.

* The special path `..` (two dots with no spaces) means "the directory above the one I'm currently in.

* A single dot on its own, ., always means "the current directory",

* `~` (the tilde character), which means "your home directory"
* `ls ~` will always list the contents of your home directory
 * To see everything underneath a directory, no matter how deeply nested it is, you can give ls the flag -R
 * `ls` with the two flags, `-R` and `-F`, and the *absolute path to your home directory* ( to see everything it contains. (The order of the flags doesn't matter, but the directory name must come last.) e.g.  `ls -R -F ~`
* `cd ~` will always take you home

* creates a copy of original.txt called duplicate.txt. If there already was a file called duplicate.txt, it is overwritten. If the last parameter to cp is an existing directory, then a command like: `cp seasonal/autumn.csv seasonal/winter.csv backup`

* mv can also be used to rename files. If you run: `mv course.txt old-course.txt` then the file course.txt in the current working directory is "moved" to the file old-course.txt. This is different from the way file browsers work, but is often handy.

* If you give less the names of several files, you can type `:n` (colon and a lower-case 'n') to move to the next file, `:p` to go back to the previous one, or `:q` to quit.

* To prints the first few lines of a file (where "a few" means 10) we use a command called `head`.
 * The shell lets you change head's behavior by giving it a command-line flag (or just "flag" for short). If you run the command: `head -n 3 seasonal/summer.csv` head will only display the first three lines of the file. If you run `head -n 100`, it will display the first 100 (assuming there are that many), and so on.

#### Tasks
> Print the contents of all of the lines containing the word molar in seasonal/autumn.csv by running a single command while in your home directory. Don't use any flags.
```sh
grep molar seasonal/autumn.csv
```
> Invert the match to find all of the lines that don't contain the word molar in seasonal/spring.csv, and show their line numbers. Remember, it's considered good style to put all of the flags before other values like filenames or the search term "molar".
```sh
grep -n -v molar seasonal/spring.csv
```
> Count how many lines contain the word incisor in autumn.csv and winter.csv combined. (Again, run a single command from your home directory.)
```sh
grep -c incisor seasonal/autumn.csv seasonal/winter.csv
```

* **cut-paste** joining the lines with columns creates only one empty column at the start, not two.
* `sort` puts data in order. By default it does this in ascending alphabetical order, but the flags `-n` and `-r` can be used to sort numerically and reverse the order of its output, while `-b` tells it to ignore leading blanks and `-f` tells it to fold case (i.e., be case-insensitive). Pipelines often use grep to get rid of unwanted records and then sort to put the remaining records in order.

#### Task
> Write a single command using head to get the first three lines from both seasonal/spring.csv and seasonal/summer.csv, a total of six lines of data, but not from the autumn or winter data files. Use a wildcard instead of spelling out the files' names in full.
```sh
head -n 3 seasonal/s*
```
> Write a pipeline to:
    1. get the second column from seasonal/winter.csv,
    2. remove the word "Tooth" from the output so that only tooth names are displayed,
    3. sort the output so that all occurrences of a particular tooth name are adjacent; and
    4. display each tooth name once along with a count of how often it occurs.

```sh
$ cut -d , -f 2 seasonal/winter.csv | grep -v Tooth | sort | uniq -c
```
> list the number of lines in all of the seasonal data files. 
> Add another command to the previous one using a pipe to remove the line containing the word "total".
> Add two more stages to the pipeline that use sort -n and head -n 1 to find the file containing the fewest lines.
```sh
$ wc -l seasonal/*csv | grep -v total | sort -n | head -n 1
```
#### Environment Variables
| Variable     | Purpose                | Value         |
| :---         |     :---:              |          ---: |
| `HOME`       | User's home directory  | `/home/repl`  |
| `PWD`        | Present working directory | Same as `pwd` command |
| `SHELL`      | Which shell program is being used |`/bin/bash` |
| `USER`       | USer's ID              | `repl` |

* looping in shell
```sh
$ for filetype in docx odt pdf; do echo $filetype; done
```
* **Command Line Arguments** 
    1. $@ = stores all the arguments in a list of string
    2. $* = stores all the arguments as a single string
    3. $# = stores the number of arguments 

* **Remember** that datafile[1-100]txt is the equivalent of datafile1.txt, datafile2.txt ... datafile100.txt, whereas datafile[001-100].txt is the equivalent of datafile001.txt, datafile002.txt... datafile100.txt.
