import re

"""
regular expression rules
. (dot) represents any char, except a new line
\w word char (letters+nums)
\d digit char
\s whitespace \S non-whitespace char
+ 1 or more
* 0 or more
[\w.]+ a set of chars allowed; word char and a ***dot is allowed here
() to mark important "group" of patterns //use match.group(1) //starts from 1
"""
