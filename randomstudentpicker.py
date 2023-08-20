font = ("Arial", 20)
import os.path
if os.path.isfile('stlist.txt'):
    print("file exists")
    filerr=0
else:
    print("stlist.txt file DOES NOT EXIST")
    filerr=1



if not filerr:
    # Open the file in read mode
    with open('stlist.txt', 'r') as file:
        # Read all the lines of the file into a list
        lines = file.read().splitlines()
else:
    lines=[]
    lines.append("stlist.txt DOES NOT EXIST")
    lines.append("stlist.txt DOES NOT EXIST")
    lines.append("stlist.txt DOES NOT EXIST")
    


import random
random.seed(999)
def pickavictim(lines):
    randomnum = random.randint(0, len(lines)-1)
    print(randomnum)
    return lines[randomnum]


default_victim='Jerry Seinfeld'

import PySimpleGUI as sg
layout = [[sg.T("",font=font)],[sg.T("        "), sg.Button('Pick a victim',size=(20,4),font=font)], [sg.T("")],
          [sg.T("         "), sg.T(default_victim, key='-TEXT-',size=(20,4),font=font)]]

###Setting Window
window = sg.Window('PICK THE VICTIM', layout, size=(600,400))

###Showing the Application, also GUI functions can be placed here.

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event=="Exit":
        break
    else:
        myvict=pickavictim(lines)
        window['-TEXT-'].update(myvict) 
    
    
window.close()


