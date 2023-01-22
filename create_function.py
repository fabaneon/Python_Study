#!/usr/local/bin/python3
import cgi

form = cgi.FieldStorage()

title = form["title"].value
article = form["article"].value


open_files = open("hello_data/"+title, 'w')
open_files.write(article)
open_files.close()


print("Location: hello.py")
print()