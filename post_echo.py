import get_jwt
import requests


def post_token(username):
    
    jwt=get_jwt.jwtoken(username.decode("utf-8","ignore"))


    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
    }
    
    url = "https://postman-echo.com/post"

    response = requests.post(url, jwt, headers = headers)

    response_json = response.content

    #print("------token------")
    #print(response_json)
    #print("------token------")

    return response_json
