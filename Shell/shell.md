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
