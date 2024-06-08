def displa(data):
    print(f"+{'-'*60}+")
    print("|   Social_media      |    Username       |    Password      |")
    for i in data:
              print(f"|{'-' * 60}|")
              a = i['Social_media']
              b = i['Username']
              c = i['Password']
              print(f"|   {a:<15}   |    {b:<15}|   {c:<15}|")
    print(f"+{'-' * 60}+")


