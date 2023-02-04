#!/usr/local/bin/python3
print("Content-Type:text/html")
print()

import pandas as pd  

filelinks = 'https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/lemonade.csv'
lemonade = pd.read_csv(filelinks)
 
filelinks = 'https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/boston.csv'
boston = pd.read_csv(filelinks)
 
filelinks = 'https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/iris.csv'
iris = pd.read_csv(filelinks)

inde_lemon = lemonade[['온도']] 
uninde_lemon = lemonade[['판매량']] 

inde_boston = boston[['crim', 'zn', 'indus', 'chas', 'nox', 
            'rm', 'age', 'dis', 'rad', 'tax',
            'ptratio', 'b', 'lstat']] 
uninde_boston = boston[['medv']] 

inde_iris = iris[['꽃잎길이', '꽃잎폭', '꽃받침길이', '꽃받침폭']] 
uninde_iris = iris[['품종']] 



print('''
    <!DOCTYPE html>
    <html>
        <head>
            <title>Python machineLearning</title>
            <meta charset="utf-8">
        </head>
        <body>
            <li>lemonade(columns, row) | {lemonadeshape}</li>
            <li>boston(columns, row) | {bostonshape}</li>
            <li>iris(columns, row) | {irisshape}</li>

            <p>
                <li>column 이름 : {lemonadecolumns}</li>
                <li> column 이름 : {bostoncolumns}</li>
                <li> column 이름 : {iriscolumns}</li>
            </p>
            <p>
                <li> lemonade 독립 : {inde_lemon}</li>
                <li> lemonade 종속 : {uninde_lemon}</li>
            </p>

            <p>
                <li> boston 독립 : {inde_boston}</li>
                <li> boston 종속 : {uninde_boston}</li>
            </p>

            <p>
                <li> iris 독립 : {inde_iris}</li>
                <li> iris 종속 : {uninde_iris}</li>
            </p>
            <p>
                <li> lemonade data 확인 : {lemonadehead}</li>
                <li> boston data 확인 : {bostonhead}</li>
                <li> iris data 확인 : {irishead}</li>

            </p>

        </body>
        
    </html>
'''.format(
        lemonadeshape=lemonade.shape,
        bostonshape=boston.shape,
        irisshape=iris.shape,
        lemonadecolumns=lemonade.columns,
        bostoncolumns=boston.columns,
        iriscolumns=iris.columns,
        inde_lemon=inde_lemon.shape,
        uninde_lemon=uninde_lemon.shape,
        inde_boston=inde_boston.shape,
        uninde_boston=uninde_boston.shape,
        inde_iris=inde_iris.shape,
        uninde_iris=uninde_iris.shape,
        lemonadehead=lemonade.head(),
        bostonhead=boston.head(),
        irishead=iris.head()
))