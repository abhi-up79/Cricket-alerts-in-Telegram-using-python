# importing all required libraries 
import json
import requests

# URL of API comes here
# Ex- "https://hsapi.espncricinfo.com/v1/pages/match/home?lang=en&leagueId=19930&eventId=1233957&liveTest=false&qaTest=false" 
url = "API URL HERE"

# Get response object
response = requests.get(url)

# Parse JSON
data = response.json()

# Print Score
print(data['meta']['fullScore'])