def deletee(a):
    # a = input("Enter the media")
    print(a[1])
    media = input("enter the meddia ")
    media_found = False
    li_ne = ""
    for i, j in enumerate(a):
        print(f"{j} is in index {i} ")

        if media.split() == j['Social_media'].split():
            del a[i]
    for i in a:
        line = f"{i['Social_media']} , {i['Username']}, {i['Password']}\n"
        li_ne = li_ne + line
    file = open("passwords.txt","w")
    file.write(li_ne)
    file.close()
    print(a)
