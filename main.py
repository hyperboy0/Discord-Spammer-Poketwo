from webserver import keep_alive
import requests

channelID = PUT THE CHANNEL ID 1079076700429750433
headers = {
    "authorization":"MTA3NjU3NjU4NTM0OTYxNTY1Ng.GxvogG.TYWB1YlYFDxq4t3_2ael4XD_0l0AX0eC3JHHyE"
    "YOUR TOKEN HERE"
}
keep_alive()
file = open("text.txt", "r")
lines = file.readlines()

while True:
    for line in lines:
        requests.post(
            f"https://discord.com/api/v9/channels/{channelID}/messages",
            headers=headers,
            json={"content": line})
