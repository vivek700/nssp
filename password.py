import string
import random

def PasswordGen(len):
    U = string.ascii_uppercase
    l = string.ascii_lowercase
    p = string.punctuation
    d = string.digits
    h = string.hexdigits
    
    lst = []
    lst.extend(U)
    lst.extend(l)
    lst.extend(p)
    lst.extend(d)
    lst.extend(h)

    random.shuffle(lst)
    password = "".join(lst[0:len])
    return password


def savePass(passwordg):
    username = input("Enter your username: ")
    password1 = passwordg
    s3 = f"\nUsername: {username}\nPassword: {password1}\n"
    with open("password.txt","a") as f:
        f.write(s3)
    print(s3)    
    return True



if __name__ == "__main__":
    while(True):
        welcmmsg = '''\n********* Welcome To V Pass *********
        Choose an option:
        1. To Generate Password
        2. Exit the V Pass
        '''
        alert = '''\n Do you want to save this password or Generate again.
        choose an option:
        1. To save Password
        2. Generate again
        '''
        print(welcmmsg)
        
        opt = input("Enter your choice: ")
        
        if opt.isnumeric() == True:
            m = int(opt)
            if m == 1:
                print("\nMinimum length of Password is: 8")
                passlen = input("Enter the length of the password: ")
                if passlen.isnumeric() == True:
                    k = int(passlen)
                    if  k > 7:
                        genpass = PasswordGen(k)
                        print(f"\nYour Password: {genpass}")
                        print(alert)
                        while(True):
                            c1 = input("Enter the option: ")
                            if c1.isnumeric() == True:
                                c2 = int(c1)
                                if c2 == 1:
                                    savePass(genpass) == True
                                    break
                                elif c2 == 2:
                                    break
                                else:
                                    print("Invalid option!")
                    else:
                        print("Please enter a valid length!") 
                else:
                    print("Invalid length! Enter the length of the password in integer. ") 
            elif m == 2:
                print("Thanks for using V Pass.")
                exit()

            else:
                print("Invalid option!")   
        else:
            print("Invalid option!")  
