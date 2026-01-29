import os
import json
import time
import requests
logo=(

    "\033[92m" + r"""
    ███████▒▄▄▄█████▓ ██▓███     
    ▓██   ▒ ▓  ██▒ ▓▒▓██░  ██▒  
    ▒████ ░ ▒ ▓██░ ▒░▓██░ ██▓▒  
    ░▓█▒  ░ ░ ▓██▓ ░ ▒██▄█▓▒ ▒  
    ░▒█░      ▒██▒ ░ ▒██▒ ░  ░   
    ▒ ░      ▒ ░░   ▒▓▒░ ░  ░   
    ░          ░    ░▒ ░        
    ░ ░      ░      ░░             
    """ + "\033[0m"  )


while True:
  os.system('cls')
  print(logo)
  os.system('title Orbit IP - by peers')
  x = input('Press Enter to Start!')

  if x == "":
    os.system('cls')
    IP = input('ENTER TARTGET IP: ')
    r = requests.get(f'http://ip-api.com/json/{IP}')
    data = r.json()
    print('RESULTS\n')
    print("")
    print(f"Country: {data['country']}")
    print(f"Region: {data['regionName']}")
    print(f"City: {data['city']}")
    print(f"Zip: {data['zip']}")
    print(f"ISP: {data['isp']}")
    print(f"IP: {data['query']}")
    pause = input('Press Enter To Proceed .. ')
          
