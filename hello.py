#!/usr/local/bin/python3
print("Content-Type:text/html")
print()

import cgi, os


navlist = os.listdir('hello_data')
navbutton = ''
for links in navlist:
    navbutton = navbutton + '<li><a href="hello.py?id={name}">{name}</a></li>'.format(name=links)

form = cgi.FieldStorage()

if 'id' in form:
    pageId = form["id"].value
    if pageId == 'create':
        article = '''
        <form action="create_function.py" method="post">
            <p>
               <input required name="title" type="text" placeholder="new Document Title"/>
            </p>
            <p>   
                <textarea required name="article" row="4" placeholder="new Document Article"></textarea>
            </p>
            <p>   
                <input type="submit"/>
            </p>
        </form>
        
        '''
    else:
        
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
            {nav}
        </ol>
        <p>
            <a href='hello.py?id=create'>create</a>
            <h2>
                {title}
            </h2>
        </p>
        
        {article}
        
    </body>
</html>
'''.format(
            title=pageId,
           article=article,
           nav=navbutton
          
          ))

