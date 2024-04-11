print(r''''⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣤⣤⣤⣤⣤⣤⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⡿⠿⠿⠟⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠹⠟⠛⢉⣉⣤⣤⣶⣾⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⡄⢠⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣧⠈⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣀⠐⣿⠀⢿⣿⣿⣿⣿⣿⣿⣿⡆⢹⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣴⣶⣿⣿⣿⡄⢻⣇⠸⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⣠⡄⠀⠀⠀⠀⠀⠀⠀
⠀⣿⡿⠿⠛⠛⠁⠈⠛⠀⢻⣿⣿⣿⣿⣿⣿⣿⡇⢰⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣀⣀⣀⡀⠘⣿⣿⣿⣿⠿⠿⠛⢃⣀⣀⠘⣿⣿⣿⣿⠿⠋⠁⠀
⠀⠀⠀⠀⠀⠀⠈⢻⡟⠛⠀⣉⣩⣥⣤⣶⣶⣿⣿⣿⣿⡄⢹⡿⠋⠁⠀⠀⠀⠀
⠀⠀⠀⢀⣠⣴⣾⣿⣿⡀⢿⣿⣿⣿⣿⣿⡿⠿⠛⠛⣉⣁⣬⣿⣷⣄⠀⠀⠀⠀
⠀⠀⠈⠉⠉⠙⠛⠛⣿⣇⠘⠟⠛⢉⣁⣤⣤⣶⣾⣿⣿⡟⠛⠛⠛⠛⠛⠂⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⡶⠶⣿⣿⣿⣿⠟⠙⠻⢿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠠⠟⠋⠁⠀⠀⢻⣿⠟⠁⠀⠀⠀⠀⠀⠉⠃⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀''')

import os
def clear():
    if os.name=="nt":
        os.system("cls")
    else:
        os.system("clear")

def bid_collector():
    bidder_dict={}
    highest_bidder=['',0]
    loop=True
    while loop:
        name=input("Enter the name : ")
        bid=int(input("Enter the bid : "))
        bidder_dict[name]=bid
        if input("Are there more poeples for bid 'y' or 'n' : ")=='n':
            loop=False
        else:
            clear()
    for keys , values in bidder_dict.items():
         if max(bidder_dict.values())==values:
             highest_bidder=[keys,values]
        #alternate method
        # if values>highest_bidder[1]:
        #     highest_bidder = [keys, values]
    print(f"\n\nThe highest bid is {highest_bidder[1]} by {highest_bidder[0]} !")
bid_collector()
