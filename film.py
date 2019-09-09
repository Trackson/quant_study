#!usr/bin/env python3
import tushare as ts

df_dayly = ts.realtime_boxoffice()
# df_mon = ts.month_boxoffice()

df_dayly.to_csv("D:/file.csv", encoding="utf_8_sig")
