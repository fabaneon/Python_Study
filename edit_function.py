#!/usr/local/bin/python3
import cgi, os

form = cgi.FieldStorage()
mode = form["mode"].value
title = form["title"].value
article = form["article"].value

if mode == 'update':
    orginal_title = form['orginal_title'].value
    open_files = open("hello_data/"+orginal_title, 'w')
    open_files.write(article)
    open_files.close()

    os.rename('hello_data/'+orginal_title, 'hello_data/'+title)    


elif mode == 'create':    
    open_files = open("hello_data/"+title, 'w')
    open_files.write(article)
    open_files.close()


print("Location: hello.py?id="+title+"&mode=read")
print()