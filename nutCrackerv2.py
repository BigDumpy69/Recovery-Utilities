import zipfile
import itertools
import string
import time

def crack_Passwd(zip_file , max_length ):
    chars = string.printable

    for length in range(1, max_length+1):
        for password in itertools.product(chars , repeat=length):
            password = ''.join(password)
            try :
                zip_file.extractall(pwd=password.encode())
                print(f"Password Found : {password}")
                return
            except RuntimeError :
                pass
            except zipfile.BadZipFile :
                print("Password Not found : Process will continue")
                continue
            except KeyboardInterrupt :
                print("Press One more time to interrupt.")
                break
                return 0



print("This Utility will crack the password of any ZIP file using UTF-8 , ASCII printable characters.\n")
print("Version : v2.09\n")


temp = False
while (temp != True):
    try:
        zip_file_path = input("Enter the entire path of your ZIP file : ")
        with zipfile.ZipFile(zip_file_path) as zip_file :
            print("Starting Process... Press Ctrl + C to interrupt.")
            time.sleep(5)
            crack_Passwd(zip_file , 20)

        temp = True
    except FileNotFoundError :
        print("No such File or Directory , Enter a valid PATH")
    except KeyboardInterrupt :
        print("Process Interrupted by the user.")
        break
    except IsADirectoryError :
        print("Please Enter the full PATH")

