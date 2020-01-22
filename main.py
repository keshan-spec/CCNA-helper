'''
Script to print all the functions and commands with a short desc and a learn more link 

Command :  test
Desc : Lorem djdasjdasdada... 
[Link] something.com

'''
import os
import json

# Gives username by splitting path based on OS
USRNAME = os.path.split(os.path.expanduser('~'))[-1]
OPTIONS = '''
1. View topics
2. Add commands
'''

# Helper functions to print colors
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))

# prints the links
def printlink(links):
    for link in links:
        prGreen(f"[Link] {link}")

# main function
def view_commands():
    with open("data.json", "r") as f:
        data = json.load(f)

    # get all the topics in the json
    print("\nAvailable topics")
    topics = {}
    c = 1
    for intents in data['data']:
        if intents['topic'] not in topics.values():
            topics[c] = intents['topic']
            c += 1
    EXIT = False
    # Prints all the topics in the json
    while not EXIT:
        [print(f"{x}) {str(j).title()}") for x, j in topics.items()]
        while True:
            opt = int(input("Which topic > "))
            if opt in list(topics.keys()):
                prCyan(f"\nChosen topic {topics[opt]}")
                break

        for intents in data['data']:
            if intents['topic'] == topics[opt]:
                print("\nCommand : ", intents['command'])
                print(f"Desc : {intents['short_desc']}...")
                printlink(intents['links'])
        
        if input("Do you want to continue? (y/n)").strip().lower() == 'n':
            EXIT = True


prCyan(f"Welcome {USRNAME}")
print(OPTIONS)

while True:
    opt = int(input("\033[96mChoose an option >\033[00m "))
    if opt in [1, 2]:
        break
    prRed("[ERROR] Invalid option")

if opt == 1:
    view_commands()
if opt == 2:
    pass
