from aero.updates.omicron import *

def spam(webhook1):
    amount = int(input(Colorate.Diagonal(Colors.green_to_red, Center.XCenter("Amount > "))))
    message = input(Colorate.Diagonal(Colors.green_to_red, Center.XCenter("Message > ")))

    r = requests.get(webhook1)

    if r.status_code == 200:
        for i in range(amount):
            print(Colorate.Diagonal(Colors.yellow_to_red, Center.XCenter(f"Spamming {message}")))
            requests.post(webhook1, data={"content": message})
        else:
            print(Colorate.Diagonal(Colors.yellow_to_red, Center.XCenter("Invalid webhook.")))
    input(Colorate.Diagonal(Colors.green_to_red, Center.XCenter("Press [ENTER] > ")))
    clear()
    print(Colorate.Diagonal(Colors.green_to_red, Center.XCenter(second_shit2)))

def delete_hook():
    webhook2 = input(Colorate.Diagonal(Colors.green_to_red, Center.XCenter("Webhook > ")))
    requests.delete(webhook2)
    print(Colorate.Diagonal(Colors.yellow_to_red, Center.XCenter("Webhook Deleted")))
    input(Colorate.Diagonal(Colors.green_to_red, Center.XCenter("Press [ENTER] > ")))
    clear()
    print(Colorate.Diagonal(Colors.green_to_red, Center.XCenter(second_shit2)))

def changeusernamehookfr():
    webhook3 = input(Colorate.Diagonal(Colors.green_to_red, Center.XCenter("Webhook > ")))
    user = input(Colorate.Diagonal(Colors.green_to_red, Center.XCenter("New webhook username > ")))
    shit = {"name": user}
    requests.patch(webhook3, json=shit)
    input(Colorate.Diagonal(Colors.green_to_red, Center.XCenter("Press [ENTER] > ")))
    clear()
    print(Colorate.Diagonal(Colors.green_to_red, Center.XCenter(second_shit2)))


def main():
    while True:
       print(Colorate.Diagonal(Colors.yellow_to_red, Center.XCenter(webhookthing)))
       gta = input(Colorate.Diagonal(Colors.green_to_red, Center.XCenter("Selection > ")))

       if gta == "1" or gta == "01":
          webhook1 = input(Colorate.Diagonal(Colors.green_to_red, Center.XCenter("Webhook > ")))
          spam(webhook1=webhook1)
        
       if gta == "2" or gta == "02":
           delete_hook()
        
       if gta == "03" or gta == "3":
           changeusernamehookfr()
        
       if gta == "#" or gta == "#":
           break
