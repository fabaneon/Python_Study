#!/usr/local/bin/python3
print("Content-Type:text/html")
print()

print('작은따옴표') 
print("<br/>")
print("큰따옴표")
print("<br/>")
print('''
pre 모드와 비슷하게도 출력 가능

''')
print("<br/>")
print("hellow" * 2)
print("<br/>")
print('len("hellow"*10)',len("hellow"*10)) # 길이 세기 함수 
print("<br/>")
print("'hellow.replace('low','OOO')'","hellow".replace('low','OOO'))
print("<br/>")
# 문자열 치환 함수

a = 1