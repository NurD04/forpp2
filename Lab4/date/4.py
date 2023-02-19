import datetime as d

t = d.datetime.now()
dws = d.datetime.strptime( "23/October/2022, 23:32:00", "%d/%B/%Y, %H:%M:%S" )
diff = int((t-dws).seconds)
print(diff)
