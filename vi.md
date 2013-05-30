# vi

## Key commands

### Cursor Movement

* **h or left arrow** Move left one character.
* **j or down arrow** Move down one line.
* **k or up arrow** Move up one line.
* **l or right arrow** Move right one character.

### Insert text

* **i** Insert at the current cursor position.
* **I** Insert at the beginning of the current line.
* **a** Append after the current cursor position.
* **A** Append to the end of the current line.
* **o** Start a new line after the current line.
* **O** Start a new line before the current line.

### Text navigation

* **H** Move to the top of the screen.
* **L** Move to the bottom of the screen.
* **G** Move to the end of the file.
* **w** Move forward one word.
* **b** Move backward one word.
* **0 (zero)** Move to the beginning of the current line.
* **^** Move to the first nonwhitespace character on the current line.
* **$** Move to the end of the current line.
* **Ctrl-B** Move up (back) one screen.
* **Ctrl-F** Move down (forward) one screen.

### Search

* **fg** Search the **g** character to the right of the current cursor position.
* **Fg** Search the **g** character to the left of the current cursor position.
* **;** Repeats the last search done with **f**.
* **,** Repeats the last search done with **f** (the other way around).
* **/text** Search ***text*** downwards from the current position.
* **?text** Search ***text*** upwards from the current position.
* **/^text$** Search a line that only conatains ***text***.
* **/tex** Search any string that starts with ***tex***.
* **xt$** Search any string that ends with ***xt***.

## Key commands (table)

Key command | Description
----------- | -----------
h or left arrow | Move left one character.
j or down arrow | Move down one line.
k or up arrow | Move up one line.
l or right arrow | Move right one character.
H | Move to the top of the screen.
L | Move to the bottom of the screen.
G | Move to the end of the file.
w | Move forward one word.
b | Move backward one word.
0 (zero) | Move to the beginning of the current line.
^ | Move to the first nonwhitespace character on the current line.
$ | Move to the end of the current line.
Ctrl-B | Move up (back) one screen.
Ctrl-F | Move down (forward) one screen.
i | Insert at the current cursor position.
I | Insert at the beginning of the current line.
a | Append after the current cursor position.
A | Append to the end of the current line.
o | Start a new line after the current line.
O | Start a new line before the current line.
r | Replace the character at the current cursor position.
R | Start replacing (overwriting) at the current cursor position.
x | Delete the character at the current cursor position.
X | Delete the character immediately before (to the left) of the current cursor position.
s | Delete the character at the current cursor position and go into insert mode. (This is the equivalent of the combination xi.)
S | Delete the contents of the current line and go into insert mode.
dX | Given a movement command X, cut (delete) the appropriate number of characters, words, or lines from the current cursor position.
dd | Cut the entire current line.
D | Cut from the current cursor position to the end of the line. (This is equivalent to d$.)
cX | Given a movement command X, cut the appropriate number of characters, words, or lines from the current cursor position and go into insert mode.
cc | Cut the entire current line and go into insert mode.
C | Cut from the current cursor position to the end of the line and enter insert mode. (This is equivalent to c$.)
yX | Given a movement command X, copy (yanka) the appropriate number of characters, words, or lines from the current cursor position.
yy or Y | Copy the entire current line.
p | Paste after the current cursor position.
P | Paste before the current cursor position.
. | Repeat the last command.
u | Undo the last command.b
/regex | Search forward for regex.
?regex | Search backward for regex.
n | Find the next match.
N | Find the previous match. (In other words, repeat the last search in the opposite direction.)
:n | Next file; when multiple files are specified for editing, this command loads the next file. Force this action (if the current file has unsaved changes) with :n!.
:e file | Load file in place of the current file. Force this action with :e! file.
:r file | Insert the contents of file after the current cursor position.
:q | Quit without saving changes. Force this action with :q!.
:w file | Write the current buffer to file. To append to an existing file, use :w >>file. Force the write (when possible, such as when running as root) with :w! file.
:wq | Write the file contents and quit. Force this action with :wq!.
:x | Write the file contents (if changed) and quit (the ex equivalent of ZZ).
ZZ | Write the file contents (if changed) and quit.
:! command | Execute command in a subshell.
