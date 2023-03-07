import os
import time


#requirements
os.system("pip3 install pypresence")
os.system("pip3 install psutil")
os.system("pip3 install colorama")

from pypresence import Presence
import psutil
from colorama import init, Fore, Back, Style






cpu_per = round(psutil.cpu_percent(),1) 
mem = psutil.virtual_memory()
mem_per = round(psutil.virtual_memory().percent,1)









# START - Anything can be edited and modifed below this text, only edit text inside of the quotation marks, i.e status="I love IFN.gg!"




status = "Playing on IFN.gg Networks!"
small_text = "Rust"
large_text = f"{cpu_per}% CPU | {mem_per}% MEMORY"

buttons = [
    {"label": "Make A Ticket", "url": "https://discord.com/channels/538461069644136478/891505606517731369/1071590805271232554"}, # Change anything inside of the quotation marks besides "label" and "url" note: url has to be a url
    {"label": "Server Rules", "url": "https://discord.com/channels/538461069644136478/979114730599882773/979115218254827540"}, # Change anything inside of the quotation marks besides "label" and "url" note: url has to be a url
]


#End You may not change anything beyond this mark/comment






def ready():
    os.system("cls")
    print(Fore.RED + """
                                                                    
                                ,--.                                
    ,---,     ,---,.        ,--.'|                                
    ,`--.' |   ,'  .' |    ,--,:  : |                                
    |   :  : ,---.'   | ,`--.'`|  ' :                                
    :   |  ' |   |   .' |   :  :  | |          ,----._,.   ,----._,. 
    |   :  | :   :  :   :   |   \ | :         /   /  ' /  /   /  ' / 
    '   '  ; :   |  |-, |   : '  '; |        |   :     | |   :     | 
    |   |  | |   :  ;/| '   ' ;.    ;        |   | .\  . |   | .\  . 
    '   :  ; |   |   .' |   | | \   |        .   ; ';  | .   ; ';  | 
    |   |  ' '   :  '   '   : |  ; .'        '   .   . | '   .   . | 
    '   :  | |   |  |   |   | '`--'    ___    `---`-'| |  `---`-'| | 
    ;   |.'  |   :  \   '   : |       /  .\   .'__/\_: |  .'__/\_: | 
    '---'    |   | ,'   ;   |.'       \  ; |  |   :    :  |   :    : 
            `----'     '---'          `--"    \   \  /    \   \  /  
                                                `--`-'      `--`-'   
    """)
    print("Successfully Connected" + Style.RESET_ALL)



client_id = 995928013319446528  
RPC = Presence(client_id,pipe=0)  
RPC.connect() 



start_time = time.time()
details = "Elapsed Time: "
state = status
large_image = "largeimage"
small_image = "smallimg"


RPC.update(details=details + "0s", state=state, large_image=large_image, small_image=small_image, buttons=buttons)

ready()

while True:
    elapsed_time = round(time.time() - start_time)


    if elapsed_time < 60:
        time_string = str(elapsed_time) + "s"
    elif elapsed_time < 3600:
        time_string = str(elapsed_time // 60) + "m"
    elif elapsed_time < 86400:
        time_string = str(elapsed_time // 3600) + "h"
    else:
        time_string = str(elapsed_time // 86400) + "d"

    RPC.update(details=details + str(time_string), state=state, large_image=large_image, small_image=small_image, large_text=large_text, small_text=small_text, buttons=buttons)
    time.sleep(1)


