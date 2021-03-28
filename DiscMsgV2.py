import requests
import time

print("DiscMsg Made By Storm.")
time.sleep(2)
print("Edit The Python file, to Customize your Msg And Token. THIS PROGRAM NEEDS YOUR DISCORD TOKEN TO SEND A REQUEST FOR A MSG. EDIT THE FILE WITH THE IDLE AND PUT YOUR TOKEN IN IT!")
time.sleep(4)
print("Your Message Got Succfully send.")

payload = {
    'content': "fjajifhajifjajifjIJfjakjfa @everyone @everyone HAHAH U CAN'T BAN ME LMAOOOOO! (the message u wanna send)"
}

header = {
    'authorization': 'YOUR TOKEN HERE!'
}

#  Save ur link here if u forget it
r = requests.post("YOUR DISCORD API LINK!",
data=payload, headers=header )
time.sleep(4)
