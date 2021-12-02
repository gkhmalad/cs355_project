import random

def password_gen():
    legalChars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p','q','r', 's', 't', 'u', 'v', 'w', 'x','y', 'z', '@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P','Q','R', 'S', 'T', 'U', 'V', 'W', 'X','Y','Z']

    f = open('./passwords.txt', 'w')

    for _ in range(263156):
    
        password = ''
        passLen = random.randint(12,16)
    
        for _ in range(passLen):
            password += legalChars[random.randint(0,len (legalChars)-1)]
    
        f.write(str(password) + "\n")
            
    f.close()