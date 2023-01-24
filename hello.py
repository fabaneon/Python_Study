#!/usr/local/bin/python3
print("Content-Type:text/html")
print()

import cgi, os, crud

# os 모듈 / 운영체제에서 제공되는 여러 기능
navlist = os.listdir('hello_data')
navbutton = ''
mode = 'read'
for links in navlist:
    navbutton = navbutton + '<li><a href="hello.py?id={name}&mode=read">{name}</a></li>'.format(name=links)

form = cgi.FieldStorage()
if 'mode' in form:
    mode = form['mode'].value



if 'id' in form:
    pageId = form["id"].value
    mode = form['mode'].value
    option = '''
            <li><a href='hello.py?id={pid}&mode=update'>update</a></li>
            <li><a href='hello.py?id={pid}&mode=delete'>delete</a></li>
            <li><a href='hello.py'>back</a></li>

    '''.format(pid=pageId)
    if mode == 'update':
        article = crud.update(pageId)
        
    elif mode == 'delete':
        article = crud.delete(pageId)        
    else:
        mode = 'read'
        article = open('hello_data/'+pageId, 'r').read()
        article = crud.TagExchanger(article)
        


else:
    if mode == 'create':
        pageId = "create"
        option = "<li><a href='hello.py'>back</a></li>"
        article = crud.create() 

    else:
        print('welcome')
        option = "<a href='hello.py?mode=create'>create</a>"
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
            {optionbutton}
            <h2>
                {title}
            </h2>
        </p>
        
        {art}
        
    </body>
</html>
'''.format(
            title=pageId,
           art=article,
           nav=navbutton,
          optionbutton=option
          ))

