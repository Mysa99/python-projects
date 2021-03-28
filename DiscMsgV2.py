import requests
import time

print("DiscMsg Made By Storm.")
time.sleep(2)
print("Edit The Python file, to Customize your Msg And Token. THIS PROGRAM NEEDS YOUR DISCORD TOKEN TO SEND A REQUEST FOR A MSG. EDIT THE FILE WITH THE IDLE AND PUT YOUR TOKEN IN IT!")
time.sleep(4)
print("Your Message Got Succfully send.")

payload = {
    'content': "fjajifhajifjajifjIJfjakjfa @everyone @everyone HAHAH U CAN'T BAN ME LMAOOOOO!"
}

header = {
    'authorization': 'Nzc5MDA5NTU5MjUwODYyMDky.X7aTSw.V_jPSo2XALS5ENTGm_s5uFrH1Ys'
}

#  https://discord.com/api/v8/channels/825683473922261005/messages
r = requests.post("https://discord.com/api/v8/channels/825683473922261005/messages",
data=payload, headers=header )
time.sleep(4)