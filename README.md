# OpenKeyFinder
OpenKeyFinder is a Proof of Concept tool designed to retrieve OpenAI API Keys exposed on GitHub. Instead of using a GitHub API Key, which does not allow regex queries, it needs your GitHub's session cookie.

## Requirements
```
pip3 install requests openai
```

## Usage
You will need to log in to GitHub using your browser and look for a cookie named _user_session_. Once you have it, insert it at the beginning of the script:
```
GITHUB_COOKIE_SESSION = "" #<--- HERE
```
Now you are ready to execute the script:
```
python3 openkeyfinder.py
```
It will retrieve all the OpenAI API Keys and check whether they are valid.
<img src="/basic_example.png" alt="Basic output example" width="50%">

## Disclaimer 
This tool is intended for educational and research purposes only. The creators of this tool are not responsible for any misuse or unauthorized to OpenAI API.
