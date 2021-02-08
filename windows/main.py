import re, uuid 




broadcast = input("I need your broadcast ip for example mine is 10.57.1.255 \n: ")

os.system(f"ping {broadcast} -b -c 5")
os.system("del mac.txt")
os.system("arp -a >> mac.txt")

text_file = open("mac.txt", "r")
lines = text_file.readlines()


text_file.close()
mac = list(lines[0])

# 19..35
x = " "
y = " "
for i in mac[19:35]:
    x += i
for i in mac[51:70]:
    y += i 


print(f"Your new mac address is going to be:\n{x} \nyour previous one was: " , end="")
print (':'.join(re.findall('..', '%012x' % uuid.getnode())))
confirm = input("(y: Yes, n: No): ")

if confirm == "y":
    print("OK changing mac address")
    os.system("reg add HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Class\{4D36E972-E325-11CE-BFC1-08002BE10318}\_0001 /v NetworkAddress /0000d {} /f")   
 print("Finished Your new MAC ADDRESS is" + x +  "\n To change it again please let me know")
   
    input("Enter to exit out: ")
	
else:
    print(f"Would you like your mac address to be {y}")
    c2= input("(y,n): ")
    if(c2 == "y"):
        print("OK changing mac address")
        os.system("reg add HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Class\{4D36E972-E325-11CE-BFC1-08002BE10318}\_0001 /v NetworkAddress /d 3B167H899D45 /f")
        print("Finished Your new MAC ADDRESS is" + y +  "\n To change it again run this file")
        input("Enter to exit out: ")


    else:
        print("Thank you see you soon")

