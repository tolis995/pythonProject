import requests

url = "https://imdb8.p.rapidapi.com/auto-complete"

querystring = {"q":"game of thr"}

headers = {
	"X-RapidAPI-Key": "6fe1701727mshd5868d60c5d69d7p1e9f2bjsnddd3997b6fc9",
	"X-RapidAPI-Host": "imdb8.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)