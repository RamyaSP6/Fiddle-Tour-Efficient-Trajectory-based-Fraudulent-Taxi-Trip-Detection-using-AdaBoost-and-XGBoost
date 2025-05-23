import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()
nltk.download('punkt')
import numpy
import tflearn
import os
import subprocess
import numpy
import random
import json
import pickle
from time import sleep
from sklearn.neighbors import KNeighborsClassifier
from tkinter import *
from tkinter import ttk  
from tkinter import Menu  
from tkinter import messagebox as mbox  
# import filedialog module
from tkinter import filedialog
flg=0;
import tkinter as tk


def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1
            
    return numpy.array(bag)

def checkTaxifraud():
    q=0
    while(q==0):
        
        with open("taxi.pickle", "rb") as f:
            words, labels, training, output = pickle.load(f)
        with open("taxi.json") as file:
            data = json.load(file)
        model1 = pickle.load(open('knnpickle_file', 'rb'))
        c1 = ""
        c2 = ""
        c3 = ""
        c1 = clicked.get()
        c2 = clicked2.get()
        c3 = clicked3.get()
        c4 = inputtxt4.get()
        c5 = clicked4.get()
        print(c1)
        print(c2)
        print(c3)
        print(c4)
        print(c5)
        inp='2'
        if((c1!="")and(c2!="")and(c3!="")):
            while(q==0):
                q=1;
                inp = "from:"+c1+" "+"to:"+c2+" "+"through:"+c3
                print(inp)
                print("")
                results = model1.predict([bag_of_words(inp, words)])[0]
                results_index = numpy.argmax(results)
                tag = labels[results_index]
                
                if results[results_index] > 0:
                    for tg in data["intents"]:
                        if tg['tag'] == tag:
                            responses = tg['responses']
                    datav = random.choice(responses)
                    lst = []
                    print(datav)
                    for i in datav:
                        lst.append(i)
                    
                    print(lst)
                    print(len(lst))
                    val1=""
                    val2=""
                    for k in range(0,len(lst)):
                        print(k)
                        if(lst[k]=='$'):
                            j=k
                            j+=1;
                            val1=""
                            while(lst[j]!='$'):
                                val1 = val1+lst[j]
                                j+=1;
                            print("val1")
                            print(val1)
                            break
                        
                       
                    for k in range(0,len(lst)):
                         if(lst[k]=='#'):
                            j=k
                            j+=1;
                            val2=""
                            print("val2")
                            while(lst[j]!='#'):
                                val2 = val2+lst[j]
                                j+=1;
                            print(val2)
                            break
                    km = 0
                    price = 0
                    km = int(val1)
                    price = int(val2)
                    total = km*price
                    acc = ((total/100)*10)
                    print("total")
                    print(total)
                    ud = total*2
                    if(c4==""):
                        if(c5=="AC"):
                            messagebox.showinfo('message',f'Hi! here is your results\n From: {c1}\n To: {c2}\n Through: {c3} \n Total Distance in kilometers: {km}\n Price per km: {price}\n Total Amount: {total} \n AC Charge is(10% of total Amount): {acc}\n Total Amount with AC: {total+acc}\n Total Amount for up and down: {ud+(acc*2)}\n')
                        else:
                            messagebox.showinfo('message',f'Hi! here is your results\n From: {c1}\n To: {c2}\n Through: {c3} \n Total Distance in kilometers: {km}\n Price per km: {price}\n Total Amount: {total}\n Total Amount for up and down: {ud}\n')

                    else:
                        amt = 0
                        amt = int(c4)
                        if(c5=="AC"):
                            if((amt<(ud+acc+50))):
                                messagebox.showinfo('message',f'Hi! here is your results\n From: {c1}\n To: {c2}\n Through: {c3} \n Total Distance in kilometers: {km}\n Price per km: {price}\n Total Amount: {total}\n AC Charge is(10% of total Amount): {acc}\n Total Amount with AC: {total+acc}\n Total Amount for up and down: {ud+(acc*2)}\n Taxi Fraud not detected\n')
                            else:
                                messagebox.showinfo('message',f'Hi! here is your results\n From: {c1}\n To: {c2}\n Through: {c3} \n Total Distance in kilometers: {km}\n Price per km: {price}\n Total Amount: {total}\n AC Charge is(10% of total Amount): {acc}\n Total Amount with AC: {total+acc}\n Total Amount for up and down: {ud+(acc*2)}\n Taxi Fraud detected\n')    
                        else:
                            if((amt<(ud+acc+50))):
                                messagebox.showinfo('message',f'Hi! here is your results\n From: {c1}\n To: {c2}\n Through: {c3} \n Total Distance in kilometers: {km}\n Price per km: {price}\n Total Amount: {total}\n Total Amount for up and down: {ud}\n Taxi Fraud not detected\n')
                            else:
                                messagebox.showinfo('message',f'Hi! here is your results\n From: {c1}\n To: {c2}\n Through: {c3} \n Total Distance in kilometers: {km}\n Price per km: {price}\n Total Amount: {total}\n Total Amount for up and down: {ud}\n Taxi Fraud detected\n')    
                else:
                    print("I didn't get that, try again")
        else:
            messagebox.showinfo('Please fill all fields')

t=0;
if(t==0):
    #if __name__ == '__main__':
    print("started")
    window = Tk()
  
    # Set window title
    window.title('Taxi Fault Detection system')
      
    # Set window size
    window.geometry("700x600")
      
    #Set window background color
    window.config(background = "white")
      
    # Create a File Explorer label
    label_file_explorer = Label(window,
                                text = "Please fill Inputs",
                                width = 100, height = 4,
                                fg = "blue")
      
    # Dropdown menu options
    options = [
        "tirunelveli new bus stand",
        "tirunelveli junction",
        "vannarapettai",
        "samadhanapuram",
        "thachanallur",
        "high ground",
        "nec college kovilpatti",
        "psn college prancheri",
        "pettai",
        "alangulam",
        "sankarnagar",
        "papanasam",
        "nagarcoil",
        "madurai",
        "tenkasi",
        "chennai",
        "coimbatore",
        "thoothukudi",
        "tiruchendur"
    ]
    options2 = [
         "tirunelveli new bus stand",
        "tirunelveli old bus stand",
        "town",
        "samadhanapuram",
        "ktc nagar",
        "high ground",
        "thachanallur",
        "nec college kovilpatti",
        "psn college prancheri",
        "pettai",
        "alangulam",
        "sankarnagar",
        "papanasam",
        "nagarcoil",
        "madurai",
        "tenkasi",
        "chennai",
        "coimbatore",
        "thoothukudi",
        "tiruchendur",
        "tirunelveli junction",
        "vannarapettai"
    ]
    
    options3 = [
        "bypass",
        "palayamkottai",
        "murugankurichi",
        "samadhanapuram",
        "vannarapettai",
        "sivasakthi road",
        "munneerpallam",
        "town",
        "pettai",
        "cheranmahadevi",
        "nanguneri",
        "virudhunagar",
        "alangulam",
        "tiruchirapalli",
        "madurai",
        "vagaikulam",
        "kurumbur"
    ]
    options4 = [
        "NON AC",
        "AC"
    ]
      
    # datatype of menu text
    clicked = StringVar()
    clicked2 = StringVar()
    clicked3 = StringVar()
    clicked4 = StringVar()
      
    # initial menu text
    clicked.set( "tirunelveli new bus stand" )
    clicked2.set( "tirunelveli old bus stand" )
    clicked3.set( "bypass" )
    clicked4.set( "NON AC" )
      
    # Create Dropdown menu
    drop = OptionMenu( window , clicked , *options )
    drop2 = OptionMenu( window , clicked2 , *options2 )
    drop3 = OptionMenu( window , clicked3 , *options3 )
    drop4 = OptionMenu( window , clicked4 , *options4 )
    
    lbl1 = tk.Label(window, text = "From")
    
    lbl2 = tk.Label(window, text = "To")
    lbl3 = tk.Label(window, text = "Through")
    lbl5 = tk.Label(window, text = "NON AC / AC ")

    lbl4 = tk.Label(window, text = "Price asked by Taxi driver")

    inputtxt4 = Entry(window)
  
    #inputtxt1.pack()
         
    button_start = Button(window,
                         text = "submit", command = checkTaxifraud)

       
    # Grid method is chosen for placing
    # the widgets at respective positions
    # in a table like structure by
    # specifying rows and columns
    label_file_explorer.grid(column = 1, row = 1, padx=5, pady=5)
    
    lbl1.grid(column = 1, row = 2, padx=5, pady=5)
    drop.grid(column = 1, row = 3, padx=5, pady=5)
    lbl2.grid(column = 1, row = 8, padx=5, pady=5)
    drop2.grid(column = 1,row = 9, padx=5, pady=5)
    lbl3.grid(column = 1, row = 11, padx=5, pady=5)
    drop3.grid(column = 1,row = 12, padx=5, pady=5)
    lbl4.grid(column = 1, row = 15, padx=5, pady=5)
    inputtxt4.grid(column = 1,row = 16, padx=5, pady=5)
    lbl5.grid(column = 1, row = 18, padx=5, pady=5)
    drop4.grid(column = 1,row = 20, padx=5, pady=5)
    button_start.grid(column = 1,row = 22, padx=5, pady=5)
      
    # Let the window wait for any events
    
    
    window.mainloop()

    #checkTaxifraud()
