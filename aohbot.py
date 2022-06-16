from pynput.mouse import Listener
import pyautogui
import time
import requests #dependency

url = "https://discord.com/api/webhooks/986687262056124426/zPmh4tob7a2g_bdJCh1V7nmdBzpRBojP5Fliy-A7O-6cl7054AKdrlUYhyFFZ9SJcdaI" #webhook url, from here: https://i.imgur.com/f9XnAew.png







def send_webhook(mesaj):



    

    #for all params, see https://discordapp.com/developers/docs/resources/webhook#execute-webhook
    data = {
        "content" : mesaj,
        "username" : "aof2 bot"
    }



    result = requests.post(url, json = data)

    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    else:
        print("Payload delivered successfully, code {}.".format(result.status_code))

    #result: https://i.imgur.com/DRqXQzA.png



def say():
    global sayici
    
    if  sayici + 1 == kisi_sayisi:
        sayici = 0
    else:
        sayici += 1


sayici = 0

dc_list = []
anydesk_list = []

print('dc için id gerekiyor arayın bulun id nasıl alınır')

dc_list = (input('dc idleri giriniz: (aralarına virgül koy va sırayla olmalı)').split(','))


kisi_sayisi = len(dc_list)



pass
send_webhook('<@' + dc_list[sayici]+'>')
say()

pyautogui.click(x=1843, y=992)
pyautogui.click(x=1832, y=888)
time.sleep(0.2)
pyautogui.click(1121,594)
time.sleep(0.2)
pyautogui.click(x=1888, y=112)






def on_move(x, y):
    pass

def on_click(x, y, button, pressed):
    
    
    if x>1729 and y>1019:
        print('clicked')
        send_webhook('<@' + dc_list[sayici]+'>')
        say()

        pyautogui.click(x=1843, y=992)
        pyautogui.click(x=1832, y=888)
        time.sleep(0.2)
        pyautogui.click(1121,594)
        time.sleep(0.2)
        pyautogui.click(x=1888, y=112)


        '''
        time.sleep(0.5)
        pyautogui.click(x=1891, y=108)
        time.sleep(0.1)
        pyautogui.click(x=1187, y=687)
        time.sleep(0.2)
        pyautogui.click(x=901, y=519)
        pyautogui.click(x=1056, y=540)
        pyautogui.click(x=1086, y=511)
        time.sleep(0.2)
        pyautogui.click(x=792, y=481)
        pyautogui.click(x=1096, y=759)
        time.sleep(0.3)
        pyautogui.click(x=991, y=496)
        pyautogui.typewrite(anydesk_list[sayici])
        pyautogui.click(x=980, y=785)
        '''



    
    if not pressed:
        # Stop listener
        #return False
        pass

def on_scroll(x, y, dx, dy):
    pass

# Collect events until released
with Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll) as listener:
    listener.join()

