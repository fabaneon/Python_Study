#!/usr/local/bin/python3
print("Content-Type:text/html")
print()
print("<br/>")
id = ['fabaneon','aeck13','buildmaster']
password = [1234,1324,5768]
print('id : ', id)
print("<br/>")
print('password : ', password)
print("<br/>")
print('id[1] :',id[1])
print("<br/>")
print('password[1] :',password[1])
print("<br/>")
print('len(id) :',len(id))
print('len(password) :',len(password))
print("<br/>")
print('min(id):', min(id))
print("<br/>")
print('min(password):', min(password))
print("<br/>")
print('max(id):', max(id))

print('max(password):', max(password))
print("<br/>")
#print('sum(id):', sum(id)) # 문자열이기에 연산 연산자인 더하기 함수는 사용이 불가하다
print('sum(password):', sum(password)) # 리스트의 모든 number를 합수
print("<br/>")

import statistics # 통계 모듈

print('statistics.mean(password)',statistics.mean(password)) # 평균

import random

print('random.choice',random.choice(id)) # 랜덤하게 pick
