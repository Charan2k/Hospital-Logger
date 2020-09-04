# =============================================================================
# def log():
#     pass
# 
# def retrieve():
#     pass
# 
# =============================================================================


import time
time = time.asctime(time.localtime(time.time()))

d1 = {1:"Harry", 2:"Carry", 3:"Larry"}
print(d1,end="")
q1 = int(input("Enter your choice: "))
d2 = {1:"Log", 2:"Retrieve"}
print(d2)
q2 = int(input("What do you want?: "))
    

if q1 == 1:
    if q2 == 1:
        with open("harry.txt","a+") as f:
            food = input("What did you eat/drink now? ")
            f.write(f"\n{time} \t {food}")
    elif q2 == 2:
        try:
            with open("harry.txt","r+") as f:
                for line in f:
                    print(line,end="")  
        except Exception as e:
            print("No such logs registered")
    else:
        print("Wrong option")
        
        
elif q1 == 2:
    if q2 == 1:
        with open("carry.txt","a+") as f:
            food = input("What did you eat/drink now? ")
            f.write(f"\n{time} \t {food}")
    elif q2 == 2:
        try:
            with open("carry.txt","r+") as f:
                for line in f:
                    print(line,end="")  
        except:
            print("No such logs registered")
    else:
        print("Wrong option")             
        
        
elif q1 == 3:
    if q2 == 1:
        with open("larry.txt","a+") as f:
            food = input("What did you eat/drink now? ")
            f.write(f"\n{time} \t {food}")
    elif q2 == 2:
        try:
            with open("larry.txt","r+") as f:
                for line in f:
                    print(line,end="")  
        except:
            print("No such logs registered")
    else:
        print("Wrong option")
    
            
else:
    print("Wrong option")
