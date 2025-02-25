import os
import sys
from pystyle import *
from colorama import *
import time
import subprocess
import ctypes
import requests



logo_shitttttt1 = """

                         0                          
                         0                         
                        000                        
                        000                        
                       00000                       
                       00000                       
                       00000                       
                      0000000                      
                      0000000                      
                     000000000                     
                     000000000                     
                0000000000000000000                
       0000000000000000000000000000000000000       
 0000000000000000000000000000000000000000000000000      OMICRON MULTI TOOL
       00000000000000000000000000000000000000      
                00000000000000000000               
                     000000000                     
                     000000000                     
                      0000000                      
                      0000000                      
                       00000                       
                       00000                       
                       00000                       
                        000                        
                        000                        
                         0                         
                         0   

"""


second_shit2 = """

                               
 _____       _                 
|     |_____|_|___ ___ ___ ___ 
|  |  |     | |  _|  _| . |   |     [omicron.aero]
|_____|_|_|_|_|___|_| |___|_|_|     [Omicron Multi Tool]
                               

"""

window = """

                                   ┌───────┐                                
       ┌───────────────────────────┼Omicron├───────────────────────────┐    
       │                           └───┬───┘                           │    
┌────────────┐                         │                          ┌────────┐
│   Webhook  │                         │                          │  Other │
│ Manipulator│                         │                          │  Tools │
└────┌──┐────┘                  ┌────────────┐                    └──┌──┐──┘
     │01│                       │    Token   │                       │03│   
     └──┘                       │ Disruptors │                       └──┘   
                                └────┌──┐────┘                              
                                     │02│                                   
                                     └──┘                                   

"""

webhookthing = """

[1] Spam Webhook    [2] Delete Webhook      [3] Change Webhook username    [X] Back

"""

def titulo(title: str):
   ctypes.windll.kernel32.SetConsoleTitleW(title)

def clear():
    os.system("cls" if os.name=="nt" else "clear")