# Diffie Hellman Key Exchange Algorithm
#By Ayush J.
#AP18110010616 (CSE J)

def uniqList(l):
    if(len(set(l)) == len(l)):
       return True
    else:
       return False

def PrimRoots(q):
    primitRoots=[]
    for i in range(1, q):
        pr=[]
        for j in range(1, q):
            pr.append((i**j)%q)
        if(uniqList(pr)):
            primitRoots.append(i)
    return primitRoots        


print("-------Diffie-Hellman Key Exchange Algorithm-----")
print("-------------------------------------------------")
print("                          -Implemented By Ayush J")
q = int(input("Enter any prime number q: "))
print("Primitive Roots:- ",PrimRoots(q))

alpha = int(input("Choose one of the given primitive roots: "))
while(alpha not in PrimRoots(q)):
    alpha = int(input("Wrong Input!! Choose one of the given primitive roots: "))
     
pa = int(input("Enter Private Key of Sender such that it is less than q:"))
while(pa>=q):
    pa = int(input("Wrong Input!! Enter Private Key of Sender such that it is less than q: "))

pb = int(input("Enter Private Key of Receiver such that it is less than q:"))
while(pb>=q):
    pb = int(input("Wrong Input!! Enter Private Key of Receiver such that it is less than q: "))    

publicA = (alpha**pa)%q;
publicB = (alpha**pb)%q;

print("Secret Key for the Sender side:",(publicB**pa)%q)
print("Secret Key for the Receiver side:",(publicA**pb)%q)