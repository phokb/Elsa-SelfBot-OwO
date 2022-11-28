from menu import UI
from json import load, dump
from time import sleep
from color import color

ui = UI()


# [0] Exit And Save"
# [1] Change All Settings"
# [2] Change Token"
# [3] Change Channel"
# [4] Change Sleep Mode"
# [5] Change Exp Mode"
# [6] Change Auto Setting"
# [7] Change Pray/Curse Mode"
# [8] Change Sell Mode"
# [9] Change Prefix Mode"
# [10] Change Gem Mode"
# [11] Change Casino Mode"
# [12] Change Sound Mode"
# [13] Change Webhook Setting"
# [14] Change Solve Captcha Setting"
# [15] Change TwoCaptcha Setting"
# [16] Change HuntBot Mode"

def main():
    with open("owosettings.json", "r") as f:
        data = load(f)
    ui.newData()
    choice = input(f"{color.okgreen}Enter Your Choice:  {color.reset}")
    if choice == "0":
        pass
    elif choice == "1":
        token(data, True)
        channel(data, True)
        sleep(data, True)
        exp(data, True)
        runner(data, True)
        praycurse(data, True)
        sell(data, True)
        prefix(data, True)
        gem(data, True)
        casino(data, True)
        sound(data, True)
        webhook(data, True)
        solve(data, True)
        twocaptcha(data, True)

    elif choice == "2":
        token(data, False)
    elif choice == "3":
        channel(data, False)
    elif choice == "4":
        sleep(data, False)
    elif choice == "5":
        exp(data, False)
    elif choice == "6":
        runner(data, False)
    elif choice == "7":
        praycurse(data, False)
    elif choice == "8":
        sell(data, False)
    elif choice == "9":
        prefix(data, False)
    elif choice == "10":
        gem(data, False)
    elif choice == "11":
        casino(data, False)
    elif choice == "12":
        sound(data, False)
    elif choice == "13":
        webhook(data, False)
    elif choice == "14":
        solve(data, False)
    elif choice == "15":
        twocaptcha(data, False)
    elif choice == "16":
        huntbot(data, False)
    else:
        print(f"{color.fail}[INFO] {color.reset}Invalid Choice")


def token(data, all):
    data['token'] = input("Please Enter Your Account Token: ")
    file = open("settings.json", "w")
    dump(data, file)
    file.close()
    print(f"{color.okcyan}[INFO] {color.reset}Successfully Saved!")
    if not all:
        main()


def channel(data, all):
    data['channel'] = input("Please Enter Your Channel ID: ")
    file = open("settings.json", "w")
    dump(data, file)
    file.close()
    print(f"{color.okcyan}[INFO] {color.reset}Successfully Saved!")
    if not all:
        main()


def sleep(data, all):
    data['sleep']['enable'] = input("Toggle Sleep Mode (YES/NO): ")
    if data['sleep']['enable'].lower() == 'yes':
        data['sleep']['time'] = input("Please enter the time the bot is active before sleeping")
        if data['sleep']['time'].isdigit():
            data['sleep']['time']=int(data['sleep']['time'])
        else:
            print('Wrong input')
            sleep(data,all)
        data['sleep']['duration'] = input("Please enter the time the bot sleeps ")
        if data['sleep']['duration'].isdigit():
            data['sleep']['duration']=int(data['sleep']['time'])
        else:
            print('Wrong input')
            sleep(data,all)
        data['sleep']['enable']=True
    else:
        data['sleep']['enable'] = False
    file = open("settings.json", "w")
    dump(data, file)
    file.close()
    print(f"{color.okcyan}[INFO] {color.reset}Successfully Saved!")
    if not all:
        main()


def exp(data, all):
    data['exp']['enable'] = input("Toggle Automatically Send Random Text To Level Up (YES/NO): ")
    if data['exp']['enable'].lower() == 'yes':
        data['exp']['channelspamid'] = input("Input channel id you want to spam exp(should be a private server): ")
        data['exp']['changechannel']= input("Toggle Automatically change channel spam to get more exp (YES/NO): ")
        if data['exp']['changechannel'].lower()=='yes':
            data['exp']['channelchannel']=True
        elif data['exp']['changechannel'].lower()=='no':
            data['exp']['channelchannel']=False
        else:
            print('Invalid Input')
            exp(data,all)

        data['exp']['enable']=True
    else:
        data['exp']['enable'] = False
    file = open("settings.json", "w")
    dump(data, file)
    file.close()
    print(f"{color.okcyan}[INFO] {color.reset}Successfully Saved!")
    if not all:
        main()


def runner(data, all):
    data['runner']['hunt'] = input("Do you want to owo hunt automatic?: (YES/NO)")
    data['runner']['battle'] = input("Do you want to owo battle automatic?: (YES/NO)")
    data['runner']['daily'] = input("Do you want to claim daily automatic?: (YES/NO)")
    data['runner']['owo'] = input("Do you want to say owo automatic?: (YES/NO)")
    data['runner']['ring'] = input("Do you want to buy ring (item1) automatic?: (YES/NO)")
    if data['runner']['hunt'].lower()=='yes':
        data['runner']['hunt'] = True
    else:
        data['runner']['hunt'] = False
    if data['runner']['battle'].lower()=='yes':
        data['runner']['battle'] = True
    else:
        data['runner']['battle'] = False
    if data['runner']['daily'].lower()=='yes':
        data['runner']['daily'] = True
    else:
        data['runner']['daily'] = False
    if data['runner']['owo'].lower()=='yes':
        data['runner']['owo'] = True
    else:
        data['runner']['owo'] = False
    if data['runner']['ring'].lower()=='yes':
        data['runner']['ring'] = True
    else:
        data['runner']['ring'] = False
    file = open("settings.json", "w")
    dump(data, file)
    file.close()
    print(f"{color.okcyan}[INFO] {color.reset}Successfully Saved!")
    if not all:
        main()


def praycurse(data, all):

    data['praycurse']['enable'] = input("Toggle Automatically Send Pray/Curse/No (YES/NO): ")
    if data['praycurse']['enable'].lower() == 'yes':
        data['praycurse']['mode'] = input("Do you want to Pray or Curse (PRAY/CURSE): ")
        data['praycurse']['prayother']['enable'] = input("Do you want to Pray or Curse to other player? (YES/NO) ")
        if data['praycurse']['prayother']['enable'].lower() == 'yes':
            data['praycurse']['prayother']['userid'] = input("Input player Id which you want to pray/curse to :")
            data['praycurse']['prayother']['enable']=True
        else:
            data['praycurse']['prayother']['enable']=False
        data['praycurse']['enable']=True
    else:
        data['praycurse']['enable']=False

    file = open("settings.json", "w")
    dump(data, file)
    file.close()
    print(f"{color.okcyan}[INFO] {color.reset}Successfully Saved!")
    if not all:
        main()


def sell(data, all):
    data['sell']['enable'] = input("Toggle Automatically Sell Animal (YES/NO): ")
    if data['sell']['enable'].lower() == "yes":
        print("Animal Type: C, U, R, E, M, L, F, ... (Type \"all\" To Sell All Animals)")
        print("C = Common, U = Uncommon, ect...")
        data['sell']['type'] = input("Enter Animal Type: ")
        data['sell']['enable']=True
    else:
        data['sell']['enable']=False
    file = open("settings.json", "w")
    dump(data, file)
    file.close()
    print(f"{color.okcyan}[INFO] {color.reset}Successfully Saved!")
    if not all:
        main()


def prefix(data, all):
    data['prefix']['enable'] = input("Toggle Selfbot Commands, You Can Control Your Selfbot Using Commands (YES/NO): ")
    if data['prefix']['enable'].lower() == "yes":
        data['prefix']['key'] = input("Enter Your Selfbot Prefix: ")
        data['allowedid'] = input("Do You Want Allow An User To Use Your Selfbot Commands? If Yes Enter The Account ID, Otherwise Enter \"None\": ")
        data['prefix']['enable']=True
        print("Great! You Can View Selfbot Commands At Option [3] Info At The Main Menu!")
        sleep(1)
    else:
        data['prefix']['enable']=False
    file = open("settings.json", "w")
    dump(data, file)
    file.close()
    print(f"{color.okcyan}[INFO] {color.reset}Successfully Saved!")
    if not all:
        main()


def gem(data, all):
    data['gem']['enable'] = input("Toggle Automatically Use Gems Mode (YES/NO): ")
    if data['gem']['enable'].lower() == "yes":
        data['gem']['wcrate'] = input("Toggle Automatically Open Weapon Crate Mode (YES/NO):")
        data['gem']['lbox'] = input("Toggle Automatically Open Loot Box Mode (YES/NO):")
        data['gem']['minmax'] = input("Do You Prefer Using Gems From MIN Or MAX  [MIN/MAX]:")

        data['gem']['maxtier'] = input("Which best Gems do you prefer to use : [F/L/M/E/R/C/U]")
        if  data['gem']['maxtier'].lower() == 'f':
            data['gem']['maxtier']=7
   
        elif  data['gem']['maxtier'].lower() == 'l':
            data['gem']['maxtier']=6
 
        elif  data['gem']['maxtier'].lower() == 'm':
            data['gem']['maxtier']=5
   
        elif  data['gem']['maxtier'].lower() == 'e':
            data['gem']['maxtier']=4
     
        elif  data['gem']['maxtier'].lower() == 'r':
            data['gem']['maxtier']=3

        elif  data['gem']['maxtier'].lower() == 'c':
            data['gem']['maxtier']=2

        elif  data['gem']['maxtier'].lower() == 'u':
            data['gem']['maxtier']=1

        else:
            print("Invalid Input")
            gem(data, all)

        if data['gem']['wcrate'].lower()=='yes':
            data['gem']['wcrate']=True
        else:
            data['gem']['wcrate']=False
        if data['gem']['lbox'].lower()=='yes':
            data['gem']['lbox']=True
        else:
            data['gem']['lbox']=False
        data['gem']['enable']=True
    else:
        data['gem']['enable']=False
    file = open("settings.json", "w")
    dump(data, file)
    file.close()
    print(f"{color.okcyan}[INFO] {color.reset}Successfully Saved!")
    if not all:
        main()

def casino(data, all):
    data['casino']['enable'] = input("Do you want to play Casino (YES/NO): ")
    if data['casino']['enable'].lower() == "yes":
        data['casino']['channelcasinoid'] = input("Do you want to play Casino in the special server? If Yes Enter Channel ID, Otherwise Enter \"None\" ")
        data['casino']['maxbet'] = input("Are you prefer all in to die or reset bet when the bet > 150k ? (AllIn/Reset): ")
        if data['casino']['maxbet'].lower() =='allin' or data['casino']['maxbet']=='reset':
            data['casino']['maxbet']=data['casino']['maxbet'].lower()
        else:
            print('Invalid Input')
            casino(data,all)
        data['casino']['cf']['enable'] = input("Do you want to play CoinFlip (YES/NO/): ")
        if data['casino']['cf']['enable'].lower() == 'yes':
            print(f"{color.okcyan}[INFO] {color.reset}Input Coinflip Information")
            data['casino']['cf']['bet'] = input("Enter Your Bet Amount for CoinFlip (Must Be Integer): ")
            if data['casino']['cf']['bet'].isdigit()==False:
                print('Wrong input')
                casino(data, all)
            else:
                data['casino']['cf']['bet']=int(data['casino']['cf']['bet'])

            data['casino']['cf']['rate'] = input("Enter Your Bet Rate Multiple for CoinFlip (Ngã ở đâu x? ở đó) (Best is x4) (x2 is not good) (Must Be Integer): ")
            if data['casino']['cf']['rate'].isdigit()==False:
                print('Wrong input')
                casino(data, all)
            else:
                data['casino']['cf']['rate']=int(data['casino']['cf']['rate'])

            data['casino']['cf']['enable']=True
        else:
            data['casino']['cf']['enable']=False

        data['casino']['os']['enable'] = input("Do you want to play Owo Slot (YES/NO/): ")
        if data['casino']['os']['enable'].lower() == 'yes':
            print(f"{color.okcyan}[INFO] {color.reset}Input Coinflip Information")
            data['casino']['os']['bet'] = input("Enter Your Bet Amount for OwoSlot (Must Be Integer): ")
            if data['casino']['os']['bet'].isdigit()==False:
                print('Wrong input')
                casino(data, all)
            else:
                data['casino']['os']['bet']=int(data['casino']['os']['bet'])
            data['casino']['os']['rate'] = input("Enter Your Bet Rate Multiple for OwoSlot (Ngã ở đâu x? ở đó) (Best is x3) (x2 is not good) (Must Be Integer): ")
            if data['casino']['os']['rate'].isdigit()==False:
                print('Wrong input')
                casino(data, all)
            else:
                data['casino']['os']['rate']=int(data['casino']['os']['rate'])
            data['casino']['os']['enable'] = True
        else:
            data['casino']['os']['enable'] = False
        data['casino']['enable']=True
    else:
        data['casino']['enable']=False
    file = open("settings.json", "w")
    dump(data, file)
    file.close()
    print(f"{color.okcyan}[INFO] {color.reset}Successfully Saved!")
    if not all:
        main()


def sound(data, all):
    data['sound'] = input("Do you want to ping by music?: (YES/NO)")

    file = open("settings.json", "w")
    dump(data, file)
    file.close()
    print(f"{color.okcyan}[INFO] {color.reset}Successfully Saved!")
    if not all:
        main()

def webhook(data, all):
    data['webhook']['enable'] = input("Toggle Discord Webhook, Enter Webhook Link If You Want It To Ping You If OwO Asked Captcha. Otherwise Enter \"None\": ")
    if data['webhook']['enable'].lowwer() == "none":
        data['webhook']['enable']==False
    else:
        data['webhook']['link']=data['webhook']['enable']
        data['webhook']['enable']==True
        data['webhook']['pingid'] = input("Do You Want To Ping A Specified User When OwO Asked Captcha? If Yes Enter User ID. Otherwise Enter \"None\": ")
    file = open("settings.json", "w")
    dump(data, file)
    file.close()
    print(f"{color.okcyan}[INFO] {color.reset}Successfully Saved!")
    if not all:
        main()


def solve(data, all):
    data['solve']['enable'] = input("Toggle Automatically Captcha Solving By Human Free(YES/NO): ")
    if data['solve']['enable'].lower() == "yes":
        print("Available Captcha Solving Server:\n1: https://autofarmsupport.tk\n2: https://afbot.dev")
        data['solve']['server'] = input("Which Server Do You Want To Use (1/2): ")
        if data['solve']['server']=="1" or data['solve']['server']=="2":
            data['solve']['server'] = int(data['solve']['server'])
        else:
            print("Invalid Input")
            solve(data, all)
        data['solve']['enable']=True
    else:
        data['solve']['enable']=False    

    file = open("settings.json", "w")
    dump(data, file, indent = 4)
    file.close()
    print(f"{color.okcyan}[INFO] {color.reset}Successfully Saved!")
    if not all:
        main()

def twocaptcha(data, all):
    data['twocaptcha']['enable'] = input("Do you have API 2Capcha, Enter API 2 Capcha If You have. Otherwise Enter \"None\". :")
    if data['twocaptcha']['enable'].lower() != 'none':
        data['twocaptcha']['api']=data['twocaptcha']['enable']
        data['twocaptcha']['enable']=True
    else:
        data['twocaptcha']['enable']=False
    file = open("settings.json", "w")
    dump(data, file)
    file.close()
    print(f"{color.okcyan}[INFO] {color.reset}Successfully Saved!")
    if not all:
        main()

def huntbot(data, all):
    data['huntbot']['enable'] = input("Toggle Automatically Send Huntbot/Autohunt (YES/NO): ")
    if data['huntbot']['enable'].lower() == "yes":
        data['huntbot']['sacrifice']['enable'] = input("Toggle Automatically Sacrifice Huntbot/Autohunt (YES/NO): ")
        if data['huntbot']['sacrifice']['enable'].lower()=='yes':
            print("Animal Type: C, U, R, E, M, L, F, ... (Type \"all\" To sacrifice All Animals)")
            print("C = Common, U = Uncommon, ect...")
            data['huntbot']['sacrifice']['type'] = input("Enter Animal Type: ")
            data['huntbot']['sacrifice']['enable']=True
        else:
            data['huntbot']['sacrifice']=False
        data['huntbot']['enable']=True
    else:
        data['huntbot']['enable']=False
    file = open("settings.json", "w")
    dump(data, file)
    file.close()
    print(f"{color.okcyan}[INFO] {color.reset}Successfully Saved!")
    if not all:
        main()



if __name__ == "__main__":
    main()
