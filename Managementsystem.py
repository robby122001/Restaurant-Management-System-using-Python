
from tkinter import *
import random
import time;
from tkinter import messagebox


rob = Tk()
rob.geometry("1600x800")
rob.title("Restaurant Management System")



Tops = Frame(rob, width =1600,height = 50,bg='linen')
Tops.pack(side = TOP)

f1= Frame(rob,width =1600,height = 700)
f1.pack(side = LEFT)


def Tat(): 
    messagebox.showinfo("Processing",'Printing the Receipt of Order') 

def Ref():
    x=random.randint(111234,525678)
    randomRef =str(x)
    rand.set(randomRef)

   
    COD=float(Drinks.get())
    COP=float(Paasta.get())
    COC=float(Chicken.get())
    COVB=float(Vegburg.get())
    COCM=float(cheesemeal.get())
    COL=float(lemonade.get())
    CODesserts=float(desserts.get())


    CostofDrinks = COD * 120
    CostofPaasta = COP * 210
    CostofChicken = COC * 300
    CostofvegBurger = COVB * 90
    CostofCheese = COCM * 130
    CostofLemonade = COL * 180
    CostofDesserts = CODesserts * 200

    CostofMeal = int(CostofDrinks + CostofPaasta + CostofChicken + CostofvegBurger + CostofCheese + CostofLemonade + CostofDesserts)

    PaidTax = float(CostofMeal * 0.05)


    TotalCost = float((CostofDrinks + CostofPaasta + CostofChicken + CostofvegBurger + CostofCheese + CostofLemonade + CostofDesserts) + PaidTax)



    Cost.set(CostofMeal)
    taxes.set(PaidTax)
    totalcost.set(TotalCost) 

    

def Exit():
    rob.destroy()



def Reset():
    rand.set("")
    Paasta.set("")
    Chicken.set("")
    Vegburg.set("")
    cheesemeal.set("")
    lemonade.set("")
    Drinks.set("")
    dessert.set("")
    Cost.set("")
    taxes.set("")
    totalcost.set("")

def doone():
    messagebox.showinfo("ORDER READY",'ENJOY YOUR MEAL SIR!')
    


localtime = time.asctime( time.localtime(time.time()) )

maintitle = Label(Tops,font=('arial',90,'bold'),text='Restaurant Management System',bd=10,bg='linen',fg='darkcyan')
maintitle.grid(row=0,column=0)
maintitle = Label(Tops, font=('arial',45,'bold'),text = localtime,bd=10,bg='linen',fg='darkcyan')
maintitle.grid(row=1,column=0)

rand = StringVar()
Paasta=StringVar()
Chicken =StringVar()
Vegburg =StringVar()
cheesemeal =StringVar()
lemonade =StringVar()
Drinks = StringVar()
dessert = StringVar()
Cost = StringVar()
taxes = StringVar()
totalcost = StringVar()


order = Label(f1,font=('arial',18,'bold'),text="Order Number", bd=16,anchor='w',fg='teal')
order.grid(row=0,column=1)
order= Entry(f1,font=('arial',15,'bold'),textvariable=rand ,bd=10,insertwidth=4,bg='khaki',justify='right')
order.grid(row=0,column=2)

cattitle = Label(f1,font=('arial',45,'bold'),text='Veg Meal',bd=10,bg='white',fg='green')
cattitle.grid(row=1,column=0)


paasta = Label(f1,font=('arial',18,'bold'),text="Macaroni Paasta    Rs.210", bd=16,anchor='w',fg='slategrey')
paasta.grid(row=2,column=0)
paasta= Entry(f1,font=('arial',15,'bold'),textvariable=Paasta , bd=10,insertwidth=4,bg='khaki',justify='right')
paasta.grid(row=2,column=1)

vegburger = Label(f1,font=('arial',18,'bold'),text="Veg Meal with Cold Drink    Rs.120", bd=16,anchor='w',fg='slategrey')
vegburger.grid(row=3,column=0)
vegburger= Entry(f1,font=('arial',15,'bold'),textvariable = Vegburg , bd=10,insertwidth=4,bg='khaki',justify='right')
vegburger.grid(row=3,column=1)


chicken = Label(f1,font=('arial',18,'bold'),text="French Fries    Rs.69", bd=16,anchor='w',fg='slategrey')
chicken.grid(row=4,column=0)
chicken= Entry(f1,font=('arial',15,'bold'),textvariable = Chicken , bd=10,insertwidth=4,bg='khaki',justify='right')
chicken.grid(row=4,column=1)



cheese = Label(f1,font=('arial',18,'bold'),text="Cheese Meal with Coke    Rs.130", bd=16,anchor='w',fg='slategrey')
cheese.grid(row=5,column=0)
cheese= Entry(f1,font=('arial',15,'bold'),textvariable = cheesemeal , bd=10,insertwidth=4,bg='khaki',justify='right')
cheese.grid(row=5,column=1)


shakes = Label(f1,font=('arial',18,'bold'),text="Mint Mojito    Rs.180", bd=16,anchor='w',fg='slategrey')
shakes.grid(row=6,column=0)
shakes= Entry(f1,font=('arial',15,'bold'),textvariable=lemonade , bd=10,insertwidth=4,bg='khaki',justify='right')
shakes.grid(row=6,column=1)


#---------------------------------------------------------------------------------------------------------------------


cattitle1 = Label(f1,font=('arial',45,'bold'),text='Non Veg Meal',bd=10,bg='white',fg='red')
cattitle1.grid(row=1,column=2)


drinks = Label(f1,font=('arial',18,'bold'),text="Chicken Combo    Rs.300", bd=16,anchor='w',fg='tomato')
drinks.grid(row=2,column=2)
drinks= Entry(f1,font=('arial',15,'bold'),textvariable = Drinks , bd=10,insertwidth=4,bg='khaki',justify='right')
drinks.grid(row=2,column=3)


desserts = Label(f1,font=('arial',18,'bold'),text="Tangri Chicken    Rs.200", bd=16,anchor='w',fg='tomato')
desserts.grid(row=3,column=2)
desserts= Entry(f1,font=('arial',15,'bold'),textvariable = dessert , bd=10,insertwidth=4,bg='khaki',justify='right')
desserts.grid(row=3,column=3)



Total = Label(f1,font=('arial',18,'bold'),text="Cost of Meal", bd=16,anchor='w',fg='slategrey')
Total.grid(row=4,column=2)
Total= Entry(f1,font=('arial',15,'bold'),textvariable = Cost , bd=10,insertwidth=4,bg='khaki',justify='right')
Total.grid(row=4,column=3)


Taxes = Label(f1,font=('arial',18,'bold'),text="GST%", bd=16,anchor='w',fg='slategrey')
Taxes.grid(row=5,column=2)
Taxes= Entry(f1,font=('arial',15,'bold'),textvariable = taxes , bd=10,insertwidth=4,bg='khaki',justify='right')
Taxes.grid(row=5,column=3)


Totalcost = Label(f1,font=('arial',18,'bold'),text="Total Cost", bd=16,anchor='w',fg='slategrey')
Totalcost.grid(row=6,column=2)
Totalcost= Entry(f1,font=('arial',15,'bold'),textvariable = totalcost , bd=10,insertwidth=4,bg='khaki',justify='right')
Totalcost.grid(row=6,column=3)

#Sidebuttons--------------------------------------------------------------------------------------------------------------------


totalwalabutton = Button(f1,padx=10,pady=19,bd=16,bg='darkturquoise',fg="midnightblue",font=('arial',18,'bold'),width=15,text="TOTAL",activebackground ='red',activeforeground ='green' ,command=Ref)
totalwalabutton.grid(row=2,column=9) 

Reset = Button(f1,padx=10,pady=19,bd=16,bg='darkturquoise',fg="midnightblue",font=('arial',18,'bold'),width=15,text="NEW ORDER",background ='red',activebackground ='red',activeforeground ='green' ,command = Reset)
Reset.grid(row=2,column=11)

Exit = Button(f1,padx=10,pady=19,bd=16,fg="midnightblue",bg='Blue' , font=('arial',18,'bold'),width=15,text="EXIT",activebackground ='red',activeforeground ='green' ,command = Exit)
Exit.grid(row=3,column=9)

Rec = Button(f1,padx=10,pady=19,bd=16,fg="midnightblue",bg='Blue' , font=('arial',18,'bold'),width=16,text="PRINT RECEIPT",activebackground ='red',activeforeground ='red' ,command = Tat)
Rec.grid(row=3,column=11)

Done = Button(f1,padx=10,pady=19,bd=16,fg="midnightblue",bg='Blue' , font=('arial',18,'bold'),width=16,text="ORDER READY",activebackground ='red',activeforeground ='red',command = doone)
Done.grid(row=4,column=11)


rob.mainloop()
 
