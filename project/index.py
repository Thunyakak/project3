import datetime
today = datetime.datetime.now() #ดึงเวลาปัจจุบัน
print("เกิดวัน เดือน ไหนคะ")
h=int(input("ชั่วโมง :"))
d=int(input("วัน :"))
M=int(input("เดือน :"))
y=int(input("ปี (ค.ศ.) :"))
nowdayD=today.day #ดึงวันที่ปัจจุบัน
nowdayH=today.hour #ดึงชัาวโมงปัจจุบัน
x=datetime.datetime(y,M,d,h)
c=today-x
h=(c.total_seconds())/(60*60)
print("คุณเกิดมาแล้ว %.2f ชั่วโมง" %h)
