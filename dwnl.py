#!/usr/bin/python3

from urllib.request import urlopen
html = urlopen("http://www.google.com/")
print(html.read())
