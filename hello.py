#!/usr/local/bin/python3
print("Content-Type:text/html")
print()

import cgi, os

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
        print('updatemode')
        print(pageId)
        file_article = open('hello_data/'+pageId, 'r').read()
        
        article = '''
        <form action="edit_function.py" method="post">
            <input type="hidden" name="mode" value="update"/>
            <input type="hidden" name="orginal_title" value="{form_defualt_title}">
            <p>
               <input required name="title" type="text" value="{form_defualt_title}">
            </p>
            <p>   
                <textarea required name="article" row="4" width="80px" height="60px">
                    {form_default_article}
                </textarea>
            </p>
            <p>   
                <input type="submit"/>
            </p>
        </form>

        '''.format(
                    form_defualt_title=pageId,
                  form_default_article=file_article
                  )
        
    elif mode == 'delete':
        article = '''
        <form action="edit_function.py" method="post">
            <input type="hidden" name="mode" value="delete"/>
            <input type="hidden" name="title" value="{form_defualt_title}">
            <p>
                <h2>Are you sure delete this page?</h2>
            </p>
            <p>   
                <input type="submit" value="Yes"/>
            </p>
        </form>

        '''.format(
                    form_defualt_title=pageId,
                  
                  )
        
    else:
        mode = 'read'
        article = open('hello_data/'+pageId, 'r').read()
        
    
else:
    if mode == 'create':
        pageId = "create"
        option = "<li><a href='hello.py'>back</a></li>"
        article = '''
            <form action="edit_function.py" method="post">
                <input type="hidden" name="mode" value="create"/>
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

