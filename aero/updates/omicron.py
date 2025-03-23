import os
import sys
from pystyle import *
from colorama import *
import time
import subprocess
import ctypes
import time as t
import requests



logo_shitttttt1 = """

 _____       _                 
|     |_____|_|___ ___ ___ ___ 
|  |  |     | |  _|  _| . |   |
|_____|_|_|_|_|___|_| |___|_|_|
"""


second_shit2 = """

                               
 _____       _                 
|     |_____|_|___ ___ ___ ___ 
|  |  |     | |  _|  _| . |   |     [aeromicron]
|_____|_|_|_|_|___|_| |___|_|_|     [Omicron Multi Tool]
                               

"""

window = """

                                        ┌────────────┐                                      
           ┌────────────────────────────┤ Aeromicron ├───────────────────────────────┐       
           │                            └─────┬──────┘                               │       
┌──────────┴──────────┐                       │                                ┌─────┴───────┐
│ Webhook Manipulator │              ┌────────┴─────────┐                      │ Other Tools │
└─────────────────────┘              │ Token Disruptors │                      └─────────────┘
          01                         └──────────────────┘                             03      
                                              02                                            
"""

webhookthing = """

[1] Spam Webhook    [2] Delete Webhook      [3] Change Webhook username    [#] Back

"""

tokenting = """

[1] Block Friend    [2] Delete Friends      [3] Mass DM      [#] Back

"""

def titulo(title: str):
   ctypes.windll.kernel32.SetConsoleTitleW(title)

def clear():
    os.system("cls" if os.name=="nt" else "clear")
