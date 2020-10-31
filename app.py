## pip install requests
## pip install bs4
## pip install python-telegram-bot

import requests
import bs4
import datetime

현재 = str(datetime.datetime.now())
# print(현재)

날짜 = 현재[:4] + 현재[5:7] + 현재[8:10]
# print(날짜)

html = requests.get("http://school.cbe.go.kr/nampyeong-e/M01040601/list?ymd="+ 날짜)
# print(html.text)

수프 = bs4.BeautifulSoup(html.text, "html.parser")
# print(수프)

a = 수프.find("a", href="/nampyeong-e/M01040601/list?ymd="+날짜)
# print(a)
리스트 = a.find_all('li')

식단 = ""
for i in 리스트:
    식단 = 식단 + i.text + "\n"
print(식단)

if 식단 =="":
    식단 = "오늘은 급식이 없어요."

import telegram
토큰 = "1424935162:AAEJgRFQ3x6wktn5UHFohnhzxYoqgMcI--I"
봇 = telegram.Bot(token = 토큰)

for i in 봇.getUpdates():
    print(i.message)
봇.sendMessage("1272076488", "오늘의 식단은\n"+식단)
