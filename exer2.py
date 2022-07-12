# Smart Door Program
maxtry=0
for i in range(3):
    password=input(" Please enter your password : ")
    if password=="open@2022" :
        print(" The door is open, you can enter.")
        break
    else:
       print("Wrong password, try again.")
       maxtry+=1
       
       
if maxtry==3:
    fav_colour=input("What is your favorite colour ? : ") 
    if fav_colour=="Blue":
        print("Change your password .") 
    else:
       print("You are a robber !")