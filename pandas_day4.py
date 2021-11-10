from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

# 파일경로를 찾고, 변수 file_path에 저장
file_path = './read_csv_sample.csv'

# read_csv() 함수로 데이터프레임 변환. 변수 df1에 저장
df1 = pd.read_csv(file_path)
print(df1)
print('\n')

# read_csv() 함수로 데이터프레임 변환. 변수 df2에 저장. header=None 옵션
df2 = pd.read_csv(file_path, header=None)
print(df2)
print('\n')

# read_csv() 함수로 데이터프레임 변환. 변수 df3에 저장. index_col=None 옵션
df3 = pd.read_csv(file_path, index_col=None)
print(df3)
print('\n')

# read_csv() 함수로 데이터프레임 변환. 변수 df4에 저장. index_col='c0' 옵션
df4 = pd.read_csv(file_path, index_col='c0')
print(df4)
print('\n')


#엑셀파일 불러오기
df5 = pd.read_excel('./남북한발전전력량.xlsx', engine='openpyxl')            # header=0 (default 옵션)
df6 = pd.read_excel('./남북한발전전력량.xlsx', engine='openpyxl', 
                    header=None)  # header=None 옵션

# 데이터프레임 출력
print(df5)
print('\n')
print(df6)
print('\n')

#json파일 불러오기
df7 = pd.read_json('./read_json_sample.json')  
print(df7)
print('\n')
print(df7.index)
print('\n')


# HTML 파일 경로 or 웹 페이지 주소를 url 변수에 저장
url ='./sample.html'

# HTML 웹페이지의 표(table)를 가져와서 데이터프레임으로 변환 
tables = pd.read_html(url)

# 표(table)의 개수 확인
print(len(tables))
print('\n')

# tables 리스트의 원소를 iteration하면서 각각 화면 출력
for i in range(len(tables)):
    print("tables[%s]" % i)
    print(tables[i])
    print('\n')

# 파이썬 패키지 정보가 들어 있는 두 번째 데이터프레임을 선택하여 df 변수에 저장
df8 = tables[1] 

# 'name' 열을 인덱스로 지정
df8.set_index(['name'], inplace=True)
print(df8)
print('\n')

#웹 스크래핑-beautifulsoup사용
url = "https://en.wikipedia.org/wiki/List_of_American_exchange-traded_funds"
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'lxml')   
rows = soup.select('div > ul > li')
    
etfs = {}
for row in rows:
    
    try:
        etf_name = re.findall('^(.*) \(NYSE', row.text)
        etf_market = re.findall('\((.*)\|', row.text)
        etf_ticker = re.findall('NYSE Arca\|(.*)\)', row.text)
        
        if (len(etf_ticker) > 0) & (len(etf_market) > 0) & (len(etf_name) > 0):
            etfs[etf_ticker[0]] = [etf_market[0], etf_name[0]]

    except AttributeError as err:
        pass    

# etfs 딕셔너리 출력
print(etfs)
print('\n')

# etfs 딕셔너리를 데이터프레임으로 변환
df9 = pd.DataFrame(etfs)
print(df9)






