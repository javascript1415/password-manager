from pw_generate import randomm_pass
def loweres():
 try:
    i = {}
    i['Social_media'] = input("Enter the name of the media")
    i['Username'] = input("Enter the username of the media")
    cho = input(
        "If You want to chose the random password then click 'r' and if you wanna make your own password then click 'c'")
    if cho == "c":
        while True:
            mak = input(f"enter the password length more than 8 and smaller than 32")
            if 8 < len(mak) < 32:
                i['Password'] = mak
                break
        else:
            print("try again")
    elif cho == 'r':
        mak2 = randomm_pass()
        print(mak2)
        i['Password'] = mak2
    file = file = open("passwords.txt", "w")
    line = f"{i['Social_media']} , {i['Username']}, {i['Password']}\n"
    file.write(line)
    file.close()

 except FileNotFoundError:
     print(" file not found")