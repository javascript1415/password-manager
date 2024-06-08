from pw_generate import randomm_pass
def newone(media):
    i = {}
    print("loading....")
    i['Social_media'] = media
    i["Username"] = input(f"Enter the username for the {media}")
    a = input("Enteer r for random password and enteer u for password byu urself")
    if a.lower() == "r":
        i['Password'] = randomm_pass()
    elif a.lower() == "u":
           i['Password'] = input("enter the password by urself")
    print(i)
    file = open("passwords.txt", "a")
    line = f"{i['Social_media']}, {i['Username']}, {i['Password']}\n"
    file.write(line)
    file.close()