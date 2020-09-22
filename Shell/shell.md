*  Construct the relative path to a file or directory below your current location by subtracting the absolute path of your current location from the absolute path of the thing you want.

* The special path `..` (two dots with no spaces) means "the directory above the one I'm currently in.
* A single dot on its own, ., always means "the current directory",
* `~` (the tilde character), which means "your home directory"
  * `ls ~` will always list the contents of your home directory
  * `cd ~` will always take you home
* creates a copy of original.txt called duplicate.txt. If there already was a file called duplicate.txt, it is overwritten. If the last parameter to cp is an existing directory, then a command like:

    `cp seasonal/autumn.csv seasonal/winter.csv backup`

* mv can also be used to rename files. If you run:
`mv course.txt old-course.txt`
then the file course.txt in the current working directory is "moved" to the file old-course.txt. This is different from the way file browsers work, but is often handy.
