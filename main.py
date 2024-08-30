from tkinter import *
from tkinter import messagebox
import random,os

#functions

def validate_quantity(input):
    
    if input.isdigit():
        return True
    elif input == "":
        return True
    else:
        messagebox.showerror('Error', 'Please enter a valid quantity (numeric value)')
        return False
        
def clear():
    
    MargheritaEntry.delete(0,END)
    FarmhouseEntry.delete(0,END)
    HawaiianEntry.delete(0,END)
    FourCheeseEntry.delete(0,END)
    PaneerTikkaEntry.delete(0,END)
    MexicanEntry.delete(0,END)
    VeggieDelightEntry.delete(0,END)
    
    
    plaingarlicEntry.delete(0,END)
    cheesygarlicEntry.delete(0,END)
    supremegarlicEntry.delete(0,END)
    PaneerTikkagarlicEntry.delete(0,END)
    StickygarlicEntry.delete(0,END)
    SweetCorngarlicEntry.delete(0,END)
    ItaliangarlicEntry.delete(0,END)
    
    
    
    MazaEntry.delete(0,END)
    CokeEntry.delete(0,END)
    spliteEntry.delete(0,END)
    MonstarEntry.delete(0,END)
    PepsiEntry.delete(0,END)
    DewEntry.delete(0,END)
    FantaEntry.delete(0,END)
    
    MargheritaEntry.insert(0,0)
    FarmhouseEntry.insert(0,0)
    HawaiianEntry.insert(0,0)
    FourCheeseEntry.insert(0,0)
    PaneerTikkaEntry.insert(0,0)
    MexicanEntry.insert(0,0)
    VeggieDelightEntry.insert(0,0)
    
    
    plaingarlicEntry.insert(0,0)
    cheesygarlicEntry.insert(0,0)
    supremegarlicEntry.insert(0,0)
    PaneerTikkagarlicEntry.insert(0,0)
    StickygarlicEntry.insert(0,0)
    SweetCorngarlicEntry.insert(0,0)
    ItaliangarlicEntry.insert(0,0)
    
    
    
    MazaEntry.insert(0,0)
    CokeEntry.insert(0,0)
    spliteEntry.insert(0,0)
    MonstarEntry.insert(0,0)
    PepsiEntry.insert(0,0)
    DewEntry.insert(0,0)

    FantaEntry.insert(0,0)
    
    
    
    pizzataxEntry.delete(0,END)
    BreadtaxEntry.delete(0,END)
    drinkstaxEntry.delete(0,END)

    pizzapriceEntry.delete(0,END)
    BreadpriceEntry.delete(0,END)
    drinkspriceEntry.delete(0,END)
    
    nameEntry.delete(0,END)
    phoneEntry.delete(0,END)
    billnumberEntry.delete(0,END)
    
    textarea.delete(1.0,END)

def search_bill():
    for i in os.listdir('bills/'):
        print("Found bill in directory:", i)    
        print("Comparing with:", i.split('.')[0])
        if i.split('.')[0] == billnumberEntry.get():
            print("Bill found!")
            f = open(f'bills//{i}', 'r')
            textarea.delete(1.0, END)
            for data in f:
                textarea.insert(END, data)
            f.close()
            break
    else:
        print("Bill not found!")
        messagebox.showerror('Error', 'Invalid Bill Number')



def save_bill():
    global billnumber
    r=messagebox.askyesno('Confirm','Do You Want To save The Bill')
    if r:
        bill_content=textarea.get(1.0,END)
        f=open(f'bills/{billnumber}.txt','w')
        f.write(bill_content)
        f.close()
        messagebox.showinfo('Sucess',f'{billnumber} is saved Sucessfully')
        billnumber=random.randint(1000,10000)
        
billnumber=random.randint(1000,10000)
def total():
    global p1,p2,p3,p4,p5,p6,p7,g1,g2,g3,g4,g5,g6,g7,c1,c2,c3,c4,c5,c6,c7,totalbill
    p1=int(MargheritaEntry.get())*120
    p2=int(FarmhouseEntry.get())*140
    p3=int(HawaiianEntry.get())*150
    p4=int(FourCheeseEntry.get())*170
    p5=int(PaneerTikkaEntry.get())*165
    p6=int(MexicanEntry.get())*167
    p7=int(VeggieDelightEntry.get())*140
    
    totalpizzaprice=p1+p2+p3+p4+p5+p6+p7
    pizzapriceEntry.insert(0,f'{totalpizzaprice}  Rs')
    pizzaatax=totalpizzaprice*0.18
    pizzataxEntry.delete(0,END)
    pizzataxEntry.insert(0,f'{pizzaatax} Rs')
    
    
    g1=int(plaingarlicEntry.get())*129
    g2=int(cheesygarlicEntry.get())*179
    g3=int(supremegarlicEntry.get())*159
    g4=int(PaneerTikkagarlicEntry.get())*149
    g5=int(StickygarlicEntry.get())*129
    g6=int(SweetCorngarlicEntry.get())*143
    g7=int(ItaliangarlicEntry.get())*129
    
    
    totalbreadprice=g1+g2+g3+g4+g5+g6+g7
    BreadpriceEntry.insert(0,f'{totalbreadprice}  Rs')
    btax=totalbreadprice*0.12
    BreadtaxEntry.delete(0,END)
    BreadtaxEntry.insert(0,f'{btax} Rs')
    
    
    
    c1=int(MazaEntry.get())*20
    c2=int(CokeEntry.get())*20
    c3=int(spliteEntry.get())*20
    c4=int(MonstarEntry.get())*120
    c5=int(PepsiEntry.get())*20
    c6=int(DewEntry.get())*25
    c7=int(FantaEntry.get())*20
    
    
    totaldrinksprice=c1+c2+c3+c4+c5+c6+c7
    drinkspriceEntry.insert(0,f'{totaldrinksprice}  Rs')
    dtax=totaldrinksprice*0.2
    drinkstaxEntry.delete(0,END)
    drinkstaxEntry.insert(0,f'{dtax} Rs')
    
    
    totalbill=totalbreadprice+totaldrinksprice+totalpizzaprice+dtax+btax+pizzaatax
    
def bill_area():
    if(nameEntry.get=='' or phoneEntry.get()==''):
        messagebox.showerror('Error','Customer Details Are Requied')
    elif(pizzapriceEntry.get()=='' and BreadpriceEntry.get()=='' and drinkspriceEntry.get()==''):
        messagebox.showerror('Error','No Products Are selected')
    elif(pizzapriceEntry.get()=='0 Rs' and BreadpriceEntry.get()=='0 Rs' and drinkspriceEntry.get()=='0 Rs'):  
        messagebox.showerror('Error','No Products Are selected')
        

        
    else:
        textarea.delete(1.0,END)
        textarea.insert(END,'\t\t\t**WelCome To Pizza Store**\n')
        textarea.insert(END,f'\nBill Number: {billnumber}\n')
        textarea.insert(END,f'\nCustomer Name: {nameEntry.get()}\n')
        textarea.insert(END,f'\nPhone Numbe: {phoneEntry.get()}\n')
        textarea.insert(END,'\n======================================================================\n')
        textarea.insert(END,f'Product\t\t\tQuantity\t\t\tPrice')
        textarea.insert(END,'\n======================================================================\n')
        if MargheritaEntry.get()!='0':
            textarea.insert(END,f"Margherita\t\t\t{MargheritaEntry.get()}\t\t\t{p1} Rs\n")       
        if FarmhouseEntry.get()!='0':
            textarea.insert(END,f"Farm House\t\t\t{FarmhouseEntry.get()}\t\t\t{p2} Rs\n")       
              
        
        if HawaiianEntry.get()!='0':
            textarea.insert(END,f"Hawaiian\t\t\t{HawaiianEntry.get()}\t\t\t{p3} Rs\n")
                   
        if FourCheeseEntry.get()!='0':
            textarea.insert(END,f"Four Cheese\t\t\t{FourCheeseEntry.get()}\t\t\t{p4} Rs\n")       
        if PaneerTikkaEntry.get()!='0':
            textarea.insert(END,f"Panner Tikka\t\t\t{PaneerTikkaEntry.get()}\t\t\t{p5} Rs\n")       
        if MexicanEntry.get()!='0':
            textarea.insert(END,f"Maxican\t\t\t{MexicanEntry.get()}\t\t\t{p6} Rs\n")       
        if VeggieDelightEntry.get()!='0':
            textarea.insert(END,f"Veggie Delight\t\t\t{VeggieDelightEntry.get()}\t\t\t{p7} Rs\n")       
        
        
        if plaingarlicEntry.get()!='0':
            textarea.insert(END,f"Plain Gallic Bread\t\t\t{plaingarlicEntry.get()}\t\t\t{g1} Rs\n")       
        if cheesygarlicEntry.get()!='0':
            textarea.insert(END,f"Cheesy Gallic Bread\t\t\t{cheesygarlicEntry.get()}\t\t\t{g2} Rs\n")       
        if supremegarlicEntry.get()!='0':
            textarea.insert(END,f"Supreme Gallic Bread\t\t\t{supremegarlicEntry.get()}\t\t\t{g3} Rs\n")       
        if PaneerTikkagarlicEntry.get()!='0':
            textarea.insert(END,f"Panner Tikaa Gallic Bread\t\t\t{PaneerTikkagarlicEntry.get()}\t\t\t{g4} Rs\n")       
        if StickygarlicEntry.get()!='0':
            textarea.insert(END,f"Sticky Gallic Bread\t\t\t{StickygarlicEntry.get()}\t\t\t{g5} Rs\n")       
        if SweetCorngarlicEntry.get()!='0':
            textarea.insert(END,f"Sweet Corn Gallic Bread\t\t\t{SweetCorngarlicEntry.get()}\t\t\t{g6} Rs\n")       
        if ItaliangarlicEntry.get()!='0':
            textarea.insert(END,f"Veggie Gallic Bread\t\t\t{ItaliangarlicEntry.get()}\t\t\t{g7} Rs\n")       




        if MazaEntry.get()!='0':
            textarea.insert(END,f"Maza\t\t\t{MazaEntry.get()}\t\t\t{c1} Rs\n")       
        if CokeEntry.get()!='0':
            textarea.insert(END,f"Coke\t\t\t{CokeEntry.get()}\t\t\t{c2} Rs\n")       
        if spliteEntry.get()!='0':
            textarea.insert(END,f"Sprite\t\t\t{spliteEntry.get()}\t\t\t{c3} Rs\n")       
        if MonstarEntry.get()!='0':
            textarea.insert(END,f"Monstar\t\t\t{MonstarEntry.get()}\t\t\t{c4} Rs\n")       
        if PepsiEntry.get()!='0':
            textarea.insert(END,f"Pepsi\t\t\t{PepsiEntry.get()}\t\t\t{c5} Rs\n")       
        if DewEntry.get()!='0':
            textarea.insert(END,f"Dew\t\t\t{DewEntry.get()}\t\t\t{c6} Rs\n")       
        if FantaEntry.get()!='0':
            textarea.insert(END,f"Fanta\t\t\t{FantaEntry.get()}\t\t\t{c7} Rs\n")    
            
        textarea.insert(END,'\n--------------------------------------------------------------------\n')
        
        
        if pizzataxEntry.get()!='0.0 Rs':
            textarea.insert(END,f"\nPIzza Tax\t\t\t{pizzataxEntry.get()}\n")
        if BreadtaxEntry.get()!='0.0 Rs':
            textarea.insert(END,f"\nGarlic Bread Tax\t\t\t{BreadtaxEntry.get()}\n")
        if drinkstaxEntry.get()!='0.0 Rs':
            textarea.insert(END,f"\nDrinks Tax\t\t\t{drinkstaxEntry.get()}\n")
            
        textarea.insert(END,'\n-------------------------------------------------------------------\n')
        textarea.insert(END,f'\nTotal Bill \t\t\t\t{totalbill}')
        textarea.insert(END,'\n-------------------------------------------------------------------\n')
        save_bill()
#GUI
root=Tk()

root.title("Hen's Billing System")
root.geometry('1470x685')
root.iconbitmap('icon.ico')

headingLabel=Label(root,text="Hen's Billing System",font=('times new roman',30,'bold'),bg='gray20',fg="gold",bd=12,relief=GROOVE)
headingLabel.pack(fill=X)

customer_details_frame=LabelFrame(root,text=('Customer Details'),font=('times new roman',15,'bold'),bg='gray20',fg="gold",bd=8,relief=GROOVE)
customer_details_frame.pack(fill=X,pady=10)

nameLabel=Label(customer_details_frame,text="Name",font=('times new roman',15,'bold'),bg='gray20',fg='white')
nameLabel.grid(row=0,column=0,padx=20)
nameEntry=Entry(customer_details_frame,font=("arial",15),bd=7,width=25)
nameEntry.grid(row=0,column=1,padx=8)


phoneLabel=Label(customer_details_frame,text="Phone Number",font=('times new roman',15,'bold'),bg='gray20',fg='white')
phoneLabel.grid(row=0,column=2,padx=20,pady=2)
phoneEntry=Entry(customer_details_frame,font=("arial",15),bd=7,width=25)
phoneEntry.grid(row=0,column=3,padx=8)


billnumberLabel=Label(customer_details_frame,text="Bill Number",font=('times new roman',15,'bold'),bg='gray20',fg='white')
billnumberLabel.grid(row=0,column=4,padx=20,pady=2)
billnumberEntry=Entry(customer_details_frame,font=("arial",15),bd=7,width=25)
billnumberEntry.grid(row=0,column=5,padx=8)

searchBuutton=Button(customer_details_frame,text='SEARCH',font=('arial',12,'bold'),bd=7,width=10,command=search_bill)
searchBuutton.grid(row=0,column=6,padx=20,pady=8)


productsFrame=Frame(root)
productsFrame.pack(pady=10)

pizzaFrame=LabelFrame(productsFrame,text="Pizza",font=('times new roman',15,'bold'),bg='gray20',fg="gold",bd=8,relief=GROOVE)
pizzaFrame.grid(row=0,column=0)

MargheritaLabel=Label(pizzaFrame,text='Margherita',font=('times new roman',15,'bold'),bg='gray20',fg='white')
MargheritaLabel.grid(row=0,column=0,pady=9,padx=10,sticky=W)
MargheritaEntry=Entry(pizzaFrame,font=('times new roman',15,'bold'),width=10,bd=5)
MargheritaEntry.grid(row=0,column=1,pady=9,padx=10)
MargheritaEntry.insert(0,0)
MargheritaEntry.config(validate="key", validatecommand=(root.register(validate_quantity), '%P'))


FarmhouseLabel=Label(pizzaFrame,text='Farmhouse',font=('times new roman',15,'bold'),bg='gray20',fg='white')
FarmhouseLabel.grid(row=1,column=0,pady=9,padx=10,sticky=W)
FarmhouseEntry=Entry(pizzaFrame,font=('times new roman',15,'bold'),width=10,bd=5)
FarmhouseEntry.grid(row=1,column=1,pady=9,padx=10)
FarmhouseEntry.insert(0,0)
FarmhouseEntry.config(validate="key", validatecommand=(root.register(validate_quantity), '%P'))

HawaiianLabel=Label(pizzaFrame,text='Hawaiian',font=('times new roman',15,'bold'),bg='gray20',fg='white')
HawaiianLabel.grid(row=2,column=0,pady=9,padx=10,sticky=W)
HawaiianEntry=Entry(pizzaFrame,font=('times new roman',15,'bold'),width=10,bd=5)
HawaiianEntry.grid(row=2,column=1,pady=9,padx=10)
HawaiianEntry.insert(0,0)

HawaiianEntry.config(validate="key", validatecommand=(root.register(validate_quantity), '%P'))


FourCheeseLabel=Label(pizzaFrame,text='Four Cheese',font=('times new roman',15,'bold'),bg='gray20',fg='white')
FourCheeseLabel.grid(row=3,column=0,pady=9,padx=10,sticky=W)
FourCheeseEntry=Entry(pizzaFrame,font=('times new roman',15,'bold'),width=10,bd=5)
FourCheeseEntry.grid(row=3,column=1,pady=9,padx=10)
FourCheeseEntry.insert(0,0)

FourCheeseEntry.config(validate="key", validatecommand=(root.register(validate_quantity), '%P'))



PaneerTikkaLabel=Label(pizzaFrame,text='Paneer Tikka ',font=('times new roman',15,'bold'),bg='gray20',fg='white')
PaneerTikkaLabel.grid(row=4,column=0,pady=9,padx=10,sticky=W)
PaneerTikkaEntry=Entry(pizzaFrame,font=('times new roman',15,'bold'),width=10,bd=5)
PaneerTikkaEntry.grid(row=4,column=1,pady=9,padx=10)
PaneerTikkaEntry.insert(0,0)

PaneerTikkaEntry.config(validate="key", validatecommand=(root.register(validate_quantity), '%P'))


MexicanLabel=Label(pizzaFrame,text='Mexican',font=('times new roman',15,'bold'),bg='gray20',fg='white')
MexicanLabel.grid(row=5,column=0,pady=9,padx=10,sticky=W)
MexicanEntry=Entry(pizzaFrame,font=('times new roman',15,'bold'),width=10,bd=5)
MexicanEntry.grid(row=5,column=1,pady=9,padx=10)
MexicanEntry.insert(0,0)

MexicanEntry.config(validate="key", validatecommand=(root.register(validate_quantity), '%P'))


VeggieDelightLabel=Label(pizzaFrame,text='Veggie Delight ',font=('times new roman',15,'bold'),bg='gray20',fg='white')
VeggieDelightLabel.grid(row=6,column=0,pady=9,padx=10,sticky=W)
VeggieDelightEntry=Entry(pizzaFrame,font=('times new roman',15,'bold'),width=10,bd=5)
VeggieDelightEntry.grid(row=6,column=1,pady=9,padx=10)
VeggieDelightEntry.insert(0,0)

VeggieDelightEntry.config(validate="key", validatecommand=(root.register(validate_quantity), '%P'))



breadFrame=LabelFrame(productsFrame,text="Garlic Breads",font=('times new roman',15,'bold'),bg='gray20',fg="gold",bd=8,relief=GROOVE)
breadFrame.grid(row=0,column=1)



plaingarlicLabel=Label(breadFrame,text='Plain Garlic',font=('times new roman',15,'bold'),bg='gray20',fg='white')
plaingarlicLabel.grid(row=0,column=0,pady=9,padx=10,sticky=W)
plaingarlicEntry=Entry(breadFrame,font=('times new roman',15,'bold'),width=10,bd=5)
plaingarlicEntry.grid(row=0,column=1,pady=9,padx=10)
plaingarlicEntry.insert(0,0)
plaingarlicEntry.config(validate="key", validatecommand=(root.register(validate_quantity), '%P'))



cheesygarlicLabel=Label(breadFrame,text='cheesy Garlic',font=('times new roman',15,'bold'),bg='gray20',fg='white')
cheesygarlicLabel.grid(row=1,column=0,pady=9,padx=10,sticky=W)
cheesygarlicEntry=Entry(breadFrame,font=('times new roman',15,'bold'),width=10,bd=5)
cheesygarlicEntry.grid(row=1,column=1,pady=9,padx=10)
cheesygarlicEntry.insert(0,0)
cheesygarlicEntry.config(validate="key", validatecommand=(root.register(validate_quantity), '%P'))



supremegarlicLabel=Label(breadFrame,text='Supreme Garlic',font=('times new roman',15,'bold'),bg='gray20',fg='white')
supremegarlicLabel.grid(row=2,column=0,pady=9,padx=10,sticky=W)
supremegarlicEntry=Entry(breadFrame,font=('times new roman',15,'bold'),width=10,bd=5)
supremegarlicEntry.grid(row=2,column=1,pady=9,padx=10)
supremegarlicEntry.insert(0,0)
supremegarlicEntry.config(validate="key", validatecommand=(root.register(validate_quantity), '%P'))



PaneerTikkagarlicLabel=Label(breadFrame,text='Paneer Tikka Garlic',font=('times new roman',15,'bold'),bg='gray20',fg='white')
PaneerTikkagarlicLabel.grid(row=3,column=0,pady=9,padx=10,sticky=W)
PaneerTikkagarlicEntry=Entry(breadFrame,font=('times new roman',15,'bold'),width=10,bd=5)
PaneerTikkagarlicEntry.grid(row=3,column=1,pady=9,padx=10)
PaneerTikkagarlicEntry.insert(0,0)
PaneerTikkagarlicEntry.config(validate="key", validatecommand=(root.register(validate_quantity), '%P'))


StickygarlicLabel=Label(breadFrame,text='Stiky Garlic',font=('times new roman',15,'bold'),bg='gray20',fg='white')
StickygarlicLabel.grid(row=4,column=0,pady=9,padx=10,sticky=W)
StickygarlicEntry=Entry(breadFrame,font=('times new roman',15,'bold'),width=10,bd=5)
StickygarlicEntry.grid(row=4,column=1,pady=9,padx=10)
StickygarlicEntry.insert(0,0)
StickygarlicEntry.config(validate="key", validatecommand=(root.register(validate_quantity), '%P'))


SweetCorngarlicLabel=Label(breadFrame,text='SweetCorn Garlic',font=('times new roman',15,'bold'),bg='gray20',fg='white')
SweetCorngarlicLabel.grid(row=5,column=0,pady=9,padx=10,sticky=W)
SweetCorngarlicEntry=Entry(breadFrame,font=('times new roman',15,'bold'),width=10,bd=5)
SweetCorngarlicEntry.grid(row=5,column=1,pady=9,padx=10)
SweetCorngarlicEntry.insert(0,0)
SweetCorngarlicEntry.config(validate="key", validatecommand=(root.register(validate_quantity), '%P'))


ItaliangarlicLabel=Label(breadFrame,text='Italian Garlic',font=('times new roman',15,'bold'),bg='gray20',fg='white')
ItaliangarlicLabel.grid(row=6,column=0,pady=9,padx=10,sticky=W)
ItaliangarlicEntry=Entry(breadFrame,font=('times new roman',15,'bold'),width=10,bd=5)
ItaliangarlicEntry.grid(row=6,column=1,pady=9,padx=10)
ItaliangarlicEntry.insert(0,0)
ItaliangarlicEntry.config(validate="key", validatecommand=(root.register(validate_quantity), '%P'))



drinksFrame=LabelFrame(productsFrame,text="Drinks",font=('times new roman',15,'bold'),bg='gray20',fg="gold",bd=8,relief=GROOVE)
drinksFrame.grid(row=0,column=2)

MazaLabel=Label(drinksFrame,text='Maza',font=('times new roman',15,'bold'),bg='gray20',fg='white')
MazaLabel.grid(row=0,column=0,pady=9,padx=10,sticky=W)
MazaEntry=Entry(drinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
MazaEntry.grid(row=0,column=1,pady=9,padx=10)
MazaEntry.insert(0,0)
MazaEntry.config(validate="key", validatecommand=(root.register(validate_quantity), '%P'))




CokeLabel=Label(drinksFrame,text='Coke',font=('times new roman',15,'bold'),bg='gray20',fg='white')
CokeLabel.grid(row=1,column=0,pady=9,padx=10,sticky=W)
CokeEntry=Entry(drinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
CokeEntry.grid(row=1,column=1,pady=9,padx=10)
CokeEntry.insert(0,0)
CokeEntry.config(validate="key", validatecommand=(root.register(validate_quantity), '%P'))



spliteLabel=Label(drinksFrame,text='Sprite',font=('times new roman',15,'bold'),bg='gray20',fg='white')
spliteLabel.grid(row=2,column=0,pady=9,padx=10,sticky=W)
spliteEntry=Entry(drinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
spliteEntry.grid(row=2,column=1,pady=9,padx=10)
spliteEntry.insert(0,0)
spliteEntry.config(validate="key", validatecommand=(root.register(validate_quantity), '%P'))


MonstarLabel=Label(drinksFrame,text='Monstar',font=('times new roman',15,'bold'),bg='gray20',fg='white')
MonstarLabel.grid(row=3,column=0,pady=9,padx=10,sticky=W)
MonstarEntry=Entry(drinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
MonstarEntry.grid(row=3,column=1,pady=9,padx=10)
MonstarEntry.insert(0,0)
MonstarEntry.config(validate="key", validatecommand=(root.register(validate_quantity), '%P'))



PepsiLabel=Label(drinksFrame,text='Pepsi',font=('times new roman',15,'bold'),bg='gray20',fg='white')
PepsiLabel.grid(row=4,column=0,pady=9,padx=10,sticky=W)
PepsiEntry=Entry(drinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
PepsiEntry.grid(row=4,column=1,pady=9,padx=10)
PepsiEntry.insert(0,0)
PepsiEntry.config(validate="key", validatecommand=(root.register(validate_quantity), '%P'))



DewLabel=Label(drinksFrame,text='Dew',font=('times new roman',15,'bold'),bg='gray20',fg='white')
DewLabel.grid(row=5,column=0,pady=9,padx=10,sticky=W)
DewEntry=Entry(drinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
DewEntry.grid(row=5,column=1,pady=9,padx=10)
DewEntry.insert(0,0)
DewEntry.config(validate="key", validatecommand=(root.register(validate_quantity), '%P'))



FantaLabel=Label(drinksFrame,text='Fanta',font=('times new roman',15,'bold'),bg='gray20',fg='white')
FantaLabel.grid(row=6,column=0,pady=9,padx=10,sticky=W)
FantaEntry=Entry(drinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
FantaEntry.grid(row=6,column=1,pady=9,padx=10)
FantaEntry.insert(0,0)
FantaEntry.config(validate="key", validatecommand=(root.register(validate_quantity), '%P'))



BillFrame=LabelFrame(productsFrame,text="Bill Area",font=('times new roman',15,'bold'),bg='gray20',fg="gold",bd=8,relief=GROOVE)
BillFrame.grid(row=0,column=3)

BillLabel=Label(BillFrame,text='Bill Area',font=('times new roman',15,'bold'),bg='gray20',fg='white')
BillLabel.pack()
scrollbar=Scrollbar(BillFrame,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)

textarea=Text(BillFrame,height=21,width=70,yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)




BillMenuFrame=LabelFrame(root,text="Bill Menu",font=('times new roman',15,'bold'),bg='gray20',fg="gold",bd=8,relief=GROOVE)
BillMenuFrame.pack()


pizzapriceLabel=Label(BillMenuFrame,text='Pizza Price',font=('times new roman',15,'bold'),bg='gray20',fg='white')
pizzapriceLabel.grid(row=0,column=0,pady=9,padx=30,sticky=W)
pizzapriceEntry=Entry(BillMenuFrame,font=('times new roman',15,'bold'),width=10,bd=5)
pizzapriceEntry.grid(row=0,column=1,pady=9,padx=30)

BreadpriceLabel=Label(BillMenuFrame,text='Galic Bread Price',font=('times new roman',15,'bold'),bg='gray20',fg='white')
BreadpriceLabel.grid(row=1,column=0,pady=9,padx=10,sticky=W)
BreadpriceEntry=Entry(BillMenuFrame,font=('times new roman',15,'bold'),width=10,bd=5)
BreadpriceEntry.grid(row=1,column=1,pady=9,padx=30)

drinkspriceLabel=Label(BillMenuFrame,text='Drinks Price',font=('times new roman',15,'bold'),bg='gray20',fg='white')
drinkspriceLabel.grid(row=2,column=0,pady=9,padx=10,sticky=W)
drinkspriceEntry=Entry(BillMenuFrame,font=('times new roman',15,'bold'),width=10,bd=5)
drinkspriceEntry.grid(row=2,column=1,pady=9,padx=30)


pizzataxLabel=Label(BillMenuFrame,text='Pizza TAX',font=('times new roman',15,'bold'),bg='gray20',fg='white')
pizzataxLabel.grid(row=0,column=2,pady=9,padx=30,sticky=W)
pizzataxEntry=Entry(BillMenuFrame,font=('times new roman',15,'bold'),width=10,bd=5)
pizzataxEntry.grid(row=0,column=3,pady=9,padx=30)

BreadtaxLabel=Label(BillMenuFrame,text='Galic Bread TAX',font=('times new roman',15,'bold'),bg='gray20',fg='white')
BreadtaxLabel.grid(row=1,column=2,pady=9,padx=30,sticky=W)
BreadtaxEntry=Entry(BillMenuFrame,font=('times new roman',15,'bold'),width=10,bd=5)
BreadtaxEntry.grid(row=1,column=3,pady=9,padx=30)

drinkstaxLabel=Label(BillMenuFrame,text='Drinks TAX',font=('times new roman',15,'bold'),bg='gray20',fg='white')
drinkstaxLabel.grid(row=2,column=2,pady=9,padx=30,sticky=W)
drinkstaxEntry=Entry(BillMenuFrame,font=('times new roman',15,'bold'),width=10,bd=5)
drinkstaxEntry.grid(row=2,column=3,pady=9,padx=30)


buttonFrame=LabelFrame(BillMenuFrame,bg='gray20',fg="gold",bd=8,relief=GROOVE)
buttonFrame.grid(row=0,column=4,rowspan=3)

totalbutton=Button(buttonFrame,text='Total',font=('times new roman',17,'bold'),bg='gray20',fg="white",bd=8,width=8,pady=10,command=total)
totalbutton.grid(row=0,column=0,pady=20,padx=20)

Billbutton=Button(buttonFrame,text='Bill',font=('times new roman',17,'bold'),bg='gray20',fg="white",bd=8,width=8,pady=10,command=bill_area)
Billbutton.grid(row=0,column=1,pady=20,padx=30)




Clearbutton=Button(buttonFrame,text='Clear',font=('times new roman',17,'bold'),bg='gray20',fg="white",bd=8,width=8,pady=10,command=clear)
Clearbutton.grid(row=0,column=4,pady=20,padx=20)



root.mainloop()

