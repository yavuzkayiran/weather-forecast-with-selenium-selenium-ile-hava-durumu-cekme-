import pyautogui as p
import time
import datetime as dt
import selenium
from selenium import webdriver
from tkinter import *
from tkcalendar import Calendar
from PIL import ImageTk, Image 
import os
import urllib

today = dt.datetime.today()
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(options=options)
sayfa=Tk()
sayfa.title("Hava Durumu")
sayfa.geometry("925x600")
sayfa.maxsize(925,600)
sayfa.minsize(925,600)
def getWeather(tarih,city):

    tarih=tarih.split("/")
    tarih=tarih[::-1]
    print(tarih)
    tarih='-'.join(tarih)
   

    tokyoLink="https://www.wunderground.com/history/daily/jp/tokyo/RJTT/date/20"
    parisLink="https://www.wunderground.com/history/daily/fr/paray-vieille-poste/LFPO/date/20"
    ankaraLink="https://www.wunderground.com/history/daily/tr/çubuk/LTAC/date/20"
    romaLink="https://www.wunderground.com/history/daily/it/ciampino/LIRA/date/20"
    if city=="Tokyo":
        url=tokyoLink+tarih
        img = ImageTk.PhotoImage(Image.open("tokyo.jpeg"))
        panel =Label(sayfa, image = img)
        panel.place(x=325,y=0)
    if city=="Paris":
        url=parisLink+tarih
        img = ImageTk.PhotoImage(Image.open("paris.jpeg"))
        panel =Label(sayfa, image = img)
        panel.place(x=325,y=0)
    if city=="Ankara":    
        url=ankaraLink+tarih
        img = ImageTk.PhotoImage(Image.open("ankara.jpeg"))
        panel =Label(sayfa, image = img)
        panel.place(x=325,y=0)
    if city=="Roma":
        url=romaLink+tarih
        img = ImageTk.PhotoImage(Image.open("roma.jpeg"))
        panel =Label(sayfa, image = img)
        panel.place(x=325,y=0)
    driver.get(url)
    time.sleep(2)
    max_Temperature = driver.find_element("xpath","/html/body/app-root/app-history/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[2]/div[1]/div[3]/div[1]/div/lib-city-history-summary/div/div[2]/table/tbody[1]/tr[1]/td[1]")
    min_Temperature = driver.find_element("xpath","/html/body/app-root/app-history/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[2]/div[1]/div[3]/div[1]/div/lib-city-history-summary/div/div[2]/table/tbody[1]/tr[2]/td[1]")
    avr_Temperature = driver.find_element("xpath","/html/body/app-root/app-history/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[2]/div[1]/div[3]/div[1]/div/lib-city-history-summary/div/div[2]/table/tbody[1]/tr[3]/td[1]")
    max=max_Temperature.text
    min=min_Temperature.text
    davr=avr_Temperature.text
    max=round(((float(max)-32)/1.8),2)
    min=round(((float(min)-32)/1.8),2)
    davr=round(((float(davr)-32)/1.8),2)
    
    print(url)
    tarih=tarih.replace("-", "/")
    label=Label(sayfa,text="20{} Tarihinde {} şehrinde".format(tarih,city),anchor = "w",font=("Arial",11))
    label.place(x=15,y=480)
    label1=Label(sayfa,text="En yüksek sıcaklik: {}°  ".format(max),anchor = "w",font=("Arial",11))
    label1.place(x=15,y=510)
    label2=Label(sayfa,text="En düşük sıcaklik: {}°   ".format(min),anchor = "w",font=("Arial",11))
    label2.place(x=15,y=540)
    label3=Label(sayfa,text="Ortalama sıcaklik: {}°    ".format(davr),anchor = "w",font=("Arial",11))
    label3.place(x=15,y=570)
    sayfa.mainloop()

#try catch yapcaz


#listbox oluşturuldu
Lb1 = Listbox(sayfa)
Lb1.insert(1, "Tokyo")
Lb1.insert(2, "Paris")
Lb1.insert(3, "Ankara")
Lb1.insert(4, "Roma")
Lb1.place(x=25,y=0)
#listbox seçilen değeri alma

    
#resim yerleştirme
img = ImageTk.PhotoImage(Image.open("stock.jpeg"))
panel =Label(sayfa, image = img)
panel.place(x=325,y=0)
#tarih getirme
def getData():
    tarih=cal.get_date()
    for i in Lb1.curselection():
        city=Lb1.get(i)
        
    getWeather(tarih,city)    
      
        
#tarih tasarım
mindate=dt.datetime(2000,1,1)
cal = Calendar(sayfa, selectmode = 'day',maxdate=today,mindate=mindate)
cal.place(x=15,y=225)
#buton tasarım
print(today)
btn = Button(sayfa, text='Hava durumunu getir',font=("Arial",12), command=getData)
btn.place(x=15,y=440)
sayfa.mainloop()
driver.close()