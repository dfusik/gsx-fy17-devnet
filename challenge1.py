import requests

link = "https://1faoejtuza.execute-api.us-east-1.amazonaws.com/prod/gsx-challenge"
r = requests.get(link)

print(r.text)


# from this url> http://stackoverflow.com/questions/15138614/how-can-i-read-the-contents-of-an-url-with-python