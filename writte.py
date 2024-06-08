import os
from pw_generate import randomm_pass
from  forempty import  loweres
from newonee import  newone
def update(info):
    if info == []:
        loweres()

    else:
        print(info)
        media = input("enter the meddia ")
        media_found = False
        li_ne = ""
        updated_info = []
        for i, j in enumerate(info):
            print(f"{j} is in index {i} ")

            if media.split() == j['Social_media'].split():
                media_found = True

                a = input("Enter q to exit and r to change the password")
                if a.lower() == "r":
                    b = input("you want a random password click r and by urself enter u")
                    if b.lower() == "u":
                        j['Password'] = input("enter the password by urself")
                    elif b.lower() == "r":
                        j['Password'] = randomm_pass()

            updated_info.append(j)

        if media_found:
            file = open("passwords.txt", "w")
            for m in updated_info:
                line = f"{m['Social_media']} , {m['Username']}, {m['Password']}\n"
                li_ne = li_ne + line
            file.write(li_ne)
        if not media_found:
                print(media)
                newone(media)




