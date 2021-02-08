import os
import re, uuid 


print ("Your current MAC address: ", end="") 
print (':'.join(re.findall('..', '%012x' % uuid.getnode())))
    
os.system("ping 10.57.1.255 -b -c 5")
os.system("sudo rm mac.txt")
os.system("sudo arp -a >> mac.txt")

text_file = open("mac.txt", "r")
lines = text_file.readlines()


text_file.close()
mac = list(lines[0])

# 19..35
x = " "
y = " "
z = " " 
for i in mac[19:35]:
    x += i
for i in mac[51:70]:
    y += i 


print(f"Your new mac address is going to be:\n{x} \nyour previous one was: " , end="")
print (':'.join(re.findall('..', '%012x' % uuid.getnode())))
confirm = input("(y: Yes, n: No): ")

if confirm == "y":
    print("OK changing mac address")
    os.system("sudo ifconfig wlp5s0 down")
    os.system(f"sudo ifconfig wlp5s0 hw ether {x}")
    os.system(f"sudo ifconfig wlp5s0 up")
    print("Finished Your new MAC ADDRESS is" + x +  "\n To change it again please let me know")
    input("Enter to exit out: ")
	
else:
    print(f"Would you like your mac address to be {y}")
    c2= input("(y,n): ")
    if(c2 == "y"):
        print("OK changing mac address")
        os.system("sudo ifconfig wlp5s0 down")
        os.system(f"sudo ifconfig wlp5s0 hw ether {y}")
        os.system(f"sudo ifconfig wlp5s0 up")
        print("Finished Your new MAC ADDRESS is" + y +  "\n To change it again run this file")
        input("Enter to exit out: ")


    else:
        print("Thank you see you soon")
        
