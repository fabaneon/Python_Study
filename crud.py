#! /usr/local/bin/python3


def create():
        pageId = "create"
        option = "<li><a href='hello.py'>back</a></li>"
        article = '''
            <form action="process_edit.py" method="post">
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
        return(article)
    
    
    
    
def update(pageId):
        print('updatemode')
        print(pageId)
        file_article = open('hello_data/'+pageId, 'r').read()
        
        article = '''
        <form action="process_edit.py" method="post">
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
        return(article)
    
    
    
    
def delete(pageId):
        article = '''
            <form action="process_edit.py" method="post">
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
        return(article)

    