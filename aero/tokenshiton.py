from aero.updates.omicron import *

def blockfriends(token):
    headers = {"authorization": token, "user-agent": "bruh6/9"}
    json = {"type": 2}
    block_friends_request = requests.get("https://discord.com/api/v8/users/@me/relationships", headers=headers).json()
    for i in block_friends_request:
        requests.put(
            f"https://discord.com/api/v8/users/@me/relationships/{i['id']}",
            headers=headers,
            json=json,
        )
        print(Colorate.Diagonal(Colors.green_to_red, Center.XCenter("Deleted All Friends")))
    input(Colorate.Diagonal(Colors.green_to_red, Center.XCenter("Press [ENTER] > ")))

def deleteFriends(token2):

    getheaders = {"Authorization": token2, "Content-Type": "application/json"}

    friendIds = requests.get("https://discord.com/api/v9/users/@me/relationships", headers=getheaders).json()

    for friend in friendIds:
        try:
            response = requests.delete(
                f'https://discord.com/api/v9/users/@me/relationships/{friend["id"]}', headers=getheaders
            )
            if response.status_code == 204:
                print(Colorate.Diagonal(Colors.green_to_red, Center.XCenter(f"Removed Friend | {friend['user']['username']}#{friend['user']['discriminator']}")))
            else:
                print(Colorate.Diagonal(Colors.green_to_red, Center.XCenter(f"Failed to remove friend | {friend['user']['username']}#{friend['user']['discriminator']}")))
        except Exception as e:
            print(Colorate.Diagonal(Colors.green_to_red, Center.XCenter("Error.")))
    input(Colorate.Diagonal(Colors.green_to_red, Center.XCenter("Press [ENTER] > ")))

def massdm(token3, msg):

    rs = requests.Session()
    headers = {"Authorization": token3, "User -Agent": "Mozilla/5.0"}

    response = rs.get("https://discord.com/api/v9/users/@me/channels", headers=headers)
    
    if response.status_code != 200:
        print(f"Failed to retrieve channels. Status code: {response.status_code}")
        print("Response:", response.text)
        return

    channels = response.json()
    print(Colorate.Diagonal(Colors.green_to_red, Center.XCenter(f"{len(channels)} Available.")))

    for channel in channels:
        if channel['type'] == 1:
            json_data = {"content": msg}
            t.sleep(1)
            response = rs.post(f"https://discord.com/api/v9/channels/{channel['id']}/messages", headers=headers, json=json_data)
            
            if response.status_code == 200:
                print(Colorate.Diagonal(Colors.green_to_red, Center.XCenter(f"Message sent to channel ID | {channel['id']}")))
            else:
                print(Colorate.Diagonal(Colors.green_to_red, Center.XCenter(f"Failed to send message to channel ID | {channel['id']}")))
    input(Colorate.Diagonal(Colors.green_to_red, Center.XCenter("Press [ENTER] > ")))


def run():
    while True:
        print(Colorate.Diagonal(Colors.yellow_to_red, Center.XCenter(tokenting)))
        nigga = input(Colorate.Diagonal(Colors.green_to_red, Center.XCenter("Selection > ")))

        if nigga == "1" or nigga == "01":
            token = input(Colorate.Diagonal(Colors.green_to_red, Center.XCenter("Token > ")))
            blockfriends(token=token)
        
        if nigga == "2" or nigga == "02":
            token2 = input(Colorate.Diagonal(Colors.green_to_red, Center.XCenter("Token > ")))
            deleteFriends(token=token)
        
        if nigga == "3" or nigga == "03":
            token3 = input(Colorate.Diagonal(Colors.green_to_red, Center.XCenter("Token > ")))
            msg = input(Colorate.Diagonal(Colors.green_to_red, Center.XCenter("Message > ")))
            massdm(token3=token3, msg=msg)
        
        if nigga == "#":
            break
