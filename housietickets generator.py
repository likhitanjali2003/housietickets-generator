import random
t=set()
def convert(ticket):
    tic=""
    for i in ticket:
        r=""
        for j in i:
            r+=str(j)
    tic+=r
    return tic
def check(val,ticket):
    for i in ticket:
        for j in i:
            if str(j)==str(val):
                return False
    return True
def generate_ticket():
    ticket=[]
    for i in range(3):
            ticket.append([" "]*9)
    for i in range(3):
        for j in range(5):
            c=random.randrange(0,9)
            if ticket[i][c]!=" ":
                while ticket[i][c]!=" ":
                    c=random.randrange(0,9)
            val=random.randrange(c*10+1,(c+1)*10)
            while not check(val,ticket):
                    val=random.randrange(c*10+1,(c+1)*10)
            ticket[i][c]=val
    return ticket
def print_tic(ticket):
    for i in ticket:
        print("------*-----*-----*-----*-----*-----*-----*-----*------")
        for j in i:
            print("| "+str(j)+" "*(3-len(str(j))),end=" ")
        print("|")
        print("|     "*10)
    print("------*-----*-----*-----*-----*-----*-----*-----*------")
n=int(input("enter number of tickets to be generted:"))
for i in range(n):
    if i==0:
        ticket=generate_ticket()
        r=convert(ticket)
        t.add(r)
    else:
        while 1:
            ticket=generate_ticket()
            r=convert(ticket)
            if r not in t:
                t.add(r)
                break 
    print("ticket : ",i+1)
    print_tic(ticket)