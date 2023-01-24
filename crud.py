#! /usr/local/bin/python3


def create():
        pageId = "create"
        option = "<li><a href='hello.py'>back</a></li>"
        article = '''
            <form action="process_edit.py" method="post">
                <input type="hidden" name="mode" value="create"/>
                <p>
                   <input required name="title" type="text" 
                     style="
                        width:120px; 
                        height:20px; 
                        border:1px solid rgba(255,0,0,0.2);
                        resize:none;
                    
                    " 

                   
                   
                   placeholder="new Document Title"/>
                </p>
                <p>   
                    <textarea required name="article" 
                    style="
                        width:300px; 
                        height:20.25em; 
                        border:1px solid rgba(255,0,0,0.2);
                        resize:none;
                    
                    " 
                    
                    placeholder="new Document Article"></textarea>
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
               <input required name="title" type="text"
                     style="
                        width:120px; 
                        height:20px; 
                        border:1px solid rgba(255,0,0,0.2);
                        resize:none;
                    
                    " 
               value="{form_defualt_title}">
            </p>
            <p>   
                <textarea required name="article" 
                    style="
                        width:300px; 
                        height:20.25em; 
                        border:1px solid rgba(255,0,0,0.2);
                        resize:none;
                    
                    " 
                ">
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

def TagExchanger(article):
        article = article.replace('<','&lt;')
        article = article.replace('>','&gt;')
        article = article.replace('\n','<br>')
        return(article)
