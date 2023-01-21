#!/usr/local/bin/python3
print("Content-Type:text/html")
print()

import cgi

form = cgi.FieldStorage()



if 'id' in form:
    pageId = form["id"].value
    if pageId == "welcome":

        article = '''
          
            <p>
                Welcome to my WebPage, Programed with Python!
            </p>
            <p>
                Check out the other article to use navigator link at above.
            </p>
        
        '''
    elif pageId == "about":
        article = '''
           
            <p>
                The fuck is this?
            </p>
            <p>
                From now on, I'm studying the basic level of Python<br/>
                well fine AI that handling Bigdata made with Python, that's My goal.
            </p>
        
        '''
    elif pageId == "contact":
        article = '''
           
            <p>
                Not Yet
            </p>
            <p>
                Sry but, not yet.
            </p>
        
        '''
    
else:
    pageId = "welcome"
    article = "welcome to our page"
    


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