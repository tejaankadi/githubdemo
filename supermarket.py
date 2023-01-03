from datetime import datetime

name = input("enter your name:")

lists='''
Rice  Rs 35\kg
Sugar Rs 20\kg
salt  Rs 15\kg
oil   Rs 95\litre
Tea   Rs 50\500gms
Ghee  Rs 88\kg
milk  Rs 25\500ml
'''

price=0
pricelist=[]
totalprice=0
ilist=[]
qlist=[]
plist=[]

items={'rice':35,'sugar':20,'salt':15,'oil':95,'tea':50,'ghee':88,'milk':25}
opton = int(input("for list of items press 1:"))
if opton==1:
    print(lists)
for i in range(len(items)):
    inp1 = int(input("if you want to buy press 1 or 2 for cancel:"))
    if inp1==2:
        break
    if inp1==1:
        item = input("enter your items:")
        quantity = int(input("enter quantity:"))
        if item in items.keys():
            price = quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst = (totalprice * 5)/100
            finalamount = gst+totalprice
        else:
            print("sorry you entered item is not avilable")
    else:
        print("you entered wrong number")
    inp = input("can i bill the items yes or no:")
    if inp=='yes':
        pass
        if finalamount!=0:
            print(25*"=","kiran supermarket",25*"=")
            print(28*" ","Banjara hills")
            print("Name:",name,30*" ","Date:",datetime.now())
            print(75*"-")
            print("sno",8*" ",'items',8*" ",'quantity',3*" ",'price')
            for i in range(len(pricelist)):
                print(i,8*" ",2*" ",ilist[i],11*" ",qlist[i],8*" ",plist[i])
            print(75*"-")
            print(50*" ",'totalamount:','Rs',totalprice)
            print('gst amount',40*" ",'Rs',gst)
            print(75 * "-")
            print(50 * " ", 'finalamount:', 'Rs', finalamount)
            print(75 * "-")
            print(20 * " ", "Thanks for watching")
            print(75 * "-")



