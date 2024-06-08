import os
from read import readdata
from  display import displa
from writte import  update
from delete import  deletee
while True:
        a = readdata()
        print('''

                                  ____________________________________________                                     
                                  [S.N.|    Menu                             ]
                                  [════|═════════════════════════════════════]
                                  [ 1  |    Display                          ]
                                  [════|═════════════════════════════════════]
                                  [ 2  |    Update                           ]
                                  [════|═════════════════════════════════════]
                                  [ 3  |    Delete                           ]
                                  [════|═════════════════════════════════════]   
                                  [ 4  |    Exit                             ]
                                  [____|_____________________________________]


''')

        c = input("Enter operation to be performed: \n ")

        if c == "1":
            displa(a)
        elif c == "2":
            update(a)
        elif c == "3":
            deletee(a)
        elif c == "4":
            print("Exit.......")
            break
        else:
            print("Invalid choice, try again.")



