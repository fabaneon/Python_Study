#!/usr/local/bin/python3
print("Content-Type:text/html")
print()
print("<br/>")
#표준 라이브러리 = 내장 모듈 ex. math, statistics 등
#패키지 = 외부 개발자들이 만든 모듈(소프트웨어)
#pypi(python package index) = 파이썬 패키지를 모아 놓은 데이터베이스
#pip = 패키지를 pypi.org를 통해 import하는 프로그램
#python pip -m install pandas
#csv(comma separated values)

import pandas

house = pandas.read_csv("pypi.csv")
#print(house)
print("<br/>")
print("<br/>")
print(house.head(2))
print("<br/>")
print("<br/>")
print("<br/>")
print(house.describe)
print()

