import requests
import json
import os
import sys
sys.path.append('..')
import settings

def main():
        
    url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id="+os.getenv("QIANFAN_AK")+"&client_secret="+os.getenv("QIANFAN_SK")
    
    payload = ""
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)
    
    print(response.text)
    

if __name__ == '__main__':
    main()
