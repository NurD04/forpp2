import datetime as d
today = d.datetime.now()
yesterday = today - d.timedelta(days=1)
tomorrow = today + d.timedelta(days=1)
print("Yesterday", yesterday.strftime("%d/%m/%Y"))
print("Today", today.strftime("%d/%m/%Y"))
print("Tomorrow", tomorrow.strftime("%d/%m/%Y"))