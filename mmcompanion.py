#!/usr/local/bin/python3
from html_tools import *

# Output a basic page with a header & 1 of each list to start
html_start('Might & Magic Companion')
html_header('Might & Magic Companion App', 1)
html_list(['foo', 'bar', 'baz'])
html_list(['apple', 'berry', 'cherry'], True)
html_end()
