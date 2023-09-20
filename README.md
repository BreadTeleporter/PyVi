# 📝 PyVi, a Vi-like text editor written in Python!

PyVi is designed to be very easy to use for Vi/Vim/NeoVim users, as the commands are very similar.
Speaking of, the commands PyVi currently supports are:

 - :i, Insert text
 - :a, Append text
 - :c, Clear line
 - :w, Write file
 - :o, Open file
 - :q, Quit

## Getting started
After downloading PyVi, and creating a new file, use `:i 0 Some Text` to insert text at line 0
Most commands (other than, w, o and q) use line numbers before the action.

## Command syntax
 - `:i [line] [text]`
 - `:a [line] [text]`
 - `:c [line]`
 - `:w [file]`
 - `:o [file]`
 - `:q`
