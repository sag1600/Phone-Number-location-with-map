import tkinter
import tkintermapview
import phonenumbers

from click import style
from colorama import Style
from numpy import insert
from opencage.geocoder import OpenCageGeocode
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import phonemetadata
from tkinter import *   
from tkinter import messagebox 

root = tkinter.Tk()
root.geometry("2000x1000")
root.title("Phone number track ")

lb = Label(text="Phone number track")
lb.pack()

num = Text(height=1); 
num.pack(); 

key ="API_KEY"

def PhoneNUmber_Track():

    num_2 = num.get("1.0",END)
    try:
      num3 = phonenumbers.parse(num_2)
      num_5 = phonenumbers.country_code_for_region(num_2)
     
    except:
       messagebox.showerror("Eroor","Please try agene")

    loc = geocoder.description_for_number(num3,"en")
    ser = carrier.name_for_number(num3,"en")
    #API KEY
    
    ceg = OpenCageGeocode(key)
    que = str(loc)
    res_1 = ceg.geocode(que)
    #נתוני מיקום 
    lat = res_1[1]['geometry']['lat']
    lag = res_1[1]['geometry']['lat']
    lag = res_1[0]['geometry']['lng']
    lag = res_1[1]['geometry']['lng']
    
    my_labl = LabelFrame(root)
    my_labl.pack(pady = 20)
     # נתוני מפות
    map = tkintermapview.TkinterMapView(my_labl,width=1000,height=1000 )
    map.set_position(lat,lag)
    map.set_marker(lat,lag , text= "phone location ")
    map.place(relx=0.5,rely = 0.5,anchor=tkinter.CENTER)
    map.pack(fill="both",expand=True)
    adr = tkintermapview.convert_coordinates_to_address(lat,lag)
  
   #נתוני טעינה של המערכת 
    num1.insert(END,"The cuntry of number is : "+loc)
    num1.insert(END,"\nThe Sim card  of number is : "+ser)
    num1.insert(END,"\nlatitude : "+str(lat))
    num1.insert(END,"\nLongitude : "+str(lag))
    num1.insert(END,"\nStreet Address is: "+str(adr.street))
    num1.insert(END,"\ncity Address is: "+str(adr.city))
    num1.insert(END,"\npostal Address is: "+ str(adr.postal))
  
btn= tkinter.Button(text="shech",command=PhoneNUmber_Track)
btn.pack(pady=10,padx=100,)

num1 = Text(height=7)
num1.pack()
root.mainloop()