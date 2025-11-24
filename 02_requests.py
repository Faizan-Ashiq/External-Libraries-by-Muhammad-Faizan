import requests

r = requests.get('https://api.github.com/users/Faizan-Ashiq')

with open("Faizan-Ashiq.txt", "w") as f:
    f.write(r.text)