#!/usr/local/bin/python3
print("Content-Type:text/html")
print()

import cgi

form = cgi.FieldStorage()



if 'id' in form:
    pageId = form["id"].value
    article = open('hello_data/'+pageId, 'r').read()
else:
    pageId = "welcome"
    article = "Check out the other article to use navigator link at above."
    
print('''<!DOCTYPE html>
<html>
    <head>
        <title>Web Dev with Python</title>
        <meta charset="utf-8">
        
    </head>
    <body>
        <h1>
            <a href="hello.py">Welcome To Python Web Page</a>
        </h1>
        <ol>
            <li><a href="hello.py?id=welcome">Welcome</a></li>
            <li><a href="hello.py?id=about">about</a></li>
            <li><a href="hello.py?id=contact">contact</a></li>
        </ol>
        <p>
            <h2>
                {title}
            </h2>
        </p>
        
        {article}
        
    </body>
</html>
'''.format(title=pageId,article=article))