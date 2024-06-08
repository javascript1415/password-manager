import os
def readdata():
    data = []
    try:
            file = open("passwords.txt", "r")
            for line in file:
                indexx = line.strip().split(", ")
                if len(indexx) >= 3:  # Check if there are at least three values
                    Social_media, Username, Password = indexx[:3]  # Unpack the first three values
                    info = {
                        "Social_media": Social_media,
                        "Username": Username,
                        "Password": Password
                    }
                    data.append(info)
            file.close()
            return data

    except FileNotFoundError:
        print("File not found")



