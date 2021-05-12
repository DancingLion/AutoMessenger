import sys
import pyautogui
import time
import pyperclip
import os
import random
from PIL import Image
import schedule
from datetime import datetime
import datetime
import threading
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QGridLayout, QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize

# Saving captured image 
def save_capturedIMG():

    # Open the capture program browser
    try:
        click_img(img_path + 'frmWebBrowser.PNG')
    except Exception as e:
        print('e', e)
    time.sleep(1)

    # Refresh and capture current screen 
    try: 
        click_img(img_path + 'Refresh.PNG')
        try:
            click_img(img_path + 'Refresh2.PNG')
        except Exception as e:
            print('e', e)
    except Exception as e:
        print('e', e)
    time.sleep(1)

    try:
        click_img(img_path + 'save.PNG')         
        time.sleep(1)
    except Exception as e:
        print('e', e)

    # Save current image file 
    pyautogui.typewrite('captured1.jpg')
    pyautogui.press('enter')
    pyautogui.press('left')
    pyautogui.press('enter')

    # Minimize the current browser
    pyautogui.hotkey('Alt', 'space', 'n')
    time.sleep(1)
 
# Open kakao talk app
def open_kakaotalk(repeat_number):
    
    for i in range(int(repeat_number)):
        pyautogui.press('win')
        pyautogui.typewrite('kakao')
        time.sleep(1)
        pyautogui.press('enter') 
        

'''
# Click icon images filter friend, keywrod, init_number    
def filter_friend(filter_keyword, init_number):
    
    # Click person icon
    try:
        click_img(img_path + 'person_icon.png')                                                                               
        try:
            click_img(img_path + 'person_icon2.png')
        except Exception as e :
            print('e ', e)
    except Exception as e :
        print('e ', e)

    # click x button 
    try:
        click_img(img_path + 'x.png')
    except:
        pass
    time.sleep(1)

    # Click Search icon
    click_img_plus_x(img_path+'search_icon.png', 30)
    if filter_keyword == '':
        pyautogui.keyDown('esc')
    else:
        pyperclip.copy(filter_keyword)
    pyautogui.hotkey('ctrl', 'v')

    for i in range(int(init_number)-1):
        pyautogui.keyDown('down')
    time.sleep(2)
'''

# Sending message to chat room
def chat_room(filter_keyword, init_number):
    #Click chat room icon
    try:
        click_img(img_path + 'chat_room.png')
        try:
            click_img(img_path + 'chat_room2.png')
        except Exception as e:
            print('e', e)
    except Exception as e:
        print('e', e)
    time.sleep(1)
    # click x button 
    try:
        click_img(img_path + 'x.png')
    except:
        pass
    time.sleep(1)

    # Click Search icon
    click_img_plus_x(img_path+'search_icon.png', 30)
    if filter_keyword == '':
        pyautogui.keyDown('esc')
    else:
        pyperclip.copy(filter_keyword)
    pyautogui.hotkey('ctrl', 'v')

    for i in range(int(init_number)-1):
        pyautogui.keyDown('down')
    time.sleep(2)



# Process of sending message 
def send_msg(my_msg, repeat_number):
    for i in range(int(repeat_number)):
        time_wait = random.uniform(2, 3)
        print('Repeat Number : ', i + 1, end='')
        print(' // Time wait : ', time_wait)
        time.sleep(time_wait)
        pyautogui.keyDown('enter')

        #Sending text
        pyperclip.copy(my_msg)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.keyDown('enter')
        time.sleep(1)
        
        #Sending image file
        pyautogui.hotkey('ctrl', 't')
        pyautogui.typewrite('captured1.jpg')
        time.sleep(1)
        pyautogui.press('enter')
        pyautogui.press('esc')

        #Exit
        pyautogui.press('esc')
        pyautogui.press('esc')

        #pyautogui.keyDown('down') # Choose next friend
    

# click center of image 
def click_img(imagePath):
    location = pyautogui.locateCenterOnScreen(imagePath, confidence = conf)
    x, y = location
    pyautogui.click(x, y)

# click image away from x distance
def click_img_plus_x(imagePath, pixel):
    location = pyautogui.locateCenterOnScreen(imagePath, confidence = conf)
    x, y = location
    pyautogui.click(x + pixel, y)

# doubleclick image 
def doubleClickImg(imagePath):
    location = pyautogui.locateCenterOnScreen(imagePath, confidence = conf)
    x, y = location
    pyautogui.click(x, y, clicks=2)

# End Program
def bye_msg():
    input('End program.')

# Sending text msg in txt file
def set_import_msg():
    with open("send_for_text.txt", "r", encoding='UTF-8') as f:
        text = f.read()
        #print('======== Text to be sent below. ========\n', text)
        return text


# Initialize input values here
def initialize():
    print('Monitor size : ', end='')
    print(pyautogui.size())
    print(pyautogui.position())
    #filter_keyword = input("Enter the name to be filtered. *If no, press enter.*: ")
    #init_number = input("Enter the initial point: ")
    #repeat_number = input("Enter the iteration: ")
    #my_msg = input("Enter the message. *If press Enter, send_for_text.txt sending* : ")
    filter_keyword = 'Daniel'
    init_number = '0'
    repeat_number = '1'
    my_msg = set_import_msg()
    return (filter_keyword, init_number, repeat_number, my_msg)
    
# config
img_path = os.path.dirname(os.path.realpath(__file__)) + '/img/'
conf = 0.7 # Confidence value (0 to 1)
pyautogui.PAUSE = 0.5

'''
glovar = 0
 
def glovar_value_set():
    global glovar
    glovar = 1
    print ("point_value_effect = ", glovar)

def glovar_value_Clear():
    global glovar 
    glovar = 0
'''
# Main function to initialize
#if __name__ == "__main__":
'''
def Timer():

    (filter_keyword, init_number, repeat_number, my_msg) = initialize()    
    # Get Current time 
    currentDT = datetime.datetime.now().strftime("%H:%M")
    print ("Now time = ", currentDT)

    # Set Expected time to match with current time
    ExpectedDT_str1 = '18:00'    
    ExpectedDT_obj1 = datetime.datetime.strptime(ExpectedDT_str1, "%H:%M")
    ExpectedDT_str2 = '16:37'    
    ExpectedDT_obj2 = datetime.datetime.strptime(ExpectedDT_str2, "%H:%M")
    ExpectedDT_str3 = '18:54'    
    ExpectedDT_obj3 = datetime.datetime.strptime(ExpectedDT_str3, "%H:%M")
    ExpectedDT_str4 = '14:44'    
    ExpectedDT_obj4 = datetime.datetime.strptime(ExpectedDT_str4, "%H:%M")
    ExpectedDT_str5 = '14:46'    
    ExpectedDT_obj5 = datetime.datetime.strptime(ExpectedDT_str5, "%H:%M")
    ExpectedDT_str6 = '14:48'    
    ExpectedDT_obj6 = datetime.datetime.strptime(ExpectedDT_str6, "%H:%M")

    glovar == 1
    # Execute infinitely 
    while (1):
        currentDT = datetime.datetime.now().strftime("%H:%M")
        time.sleep(1)
        if(currentDT == ExpectedDT_str1 or currentDT == ExpectedDT_str2 or 
            currentDT == ExpectedDT_str3 or currentDT == ExpectedDT_str4
            or currentDT == ExpectedDT_str5 or currentDT == ExpectedDT_str6):

            # print message if current time and expected time matched
            if(currentDT == ExpectedDT_str1):
                print("Time matched!!", "Current Time: ", currentDT, "Expected Time: ", ExpectedDT_obj1.time())
            elif(currentDT == ExpectedDT_str2):
                print("Time matched!!", "Current Time: ", currentDT, "Expected Time: ", ExpectedDT_obj2.time())
            elif(currentDT == ExpectedDT_str3):    
                print("Time matched!!", "Current Time: ", currentDT, "Expected Time: ", ExpectedDT_obj3.time())
            elif(currentDT == ExpectedDT_str4):
                print("Time matched!!", "Current Time: ", currentDT, "Expected Time: ", ExpectedDT_obj4.time())
            elif(currentDT == ExpectedDT_str5):
                print("Time matched!!", "Current Time: ", currentDT, "Expected Time: ", ExpectedDT_obj5.time())
            elif(currentDT == ExpectedDT_str6):
                print("Time matched!!", "Current Time: ", currentDT, "Expected Time: ", ExpectedDT_obj6.time())
            
            save_capturedIMG()
            open_kakaotalk(repeat_number)
            chat_room(filter_keyword, init_number)
            # filter_friend(filter_keyword, init_number)
            send_msg(my_msg, repeat_number)
            time.sleep(60)
        else:
            # print missed message if current time and expected time unmatched
            print("Time missed!! ", "Current Time: ", currentDT, time.sleep(2))
           
'''
def Timer1(id):

    (filter_keyword, init_number, repeat_number, my_msg) = initialize()    
    # Get Current time 
    currentDT = datetime.datetime.now().strftime("%H:%M")

    # Set Expected time to match with current time
    ExpectedDT_str1 = '06:40'    
    ExpectedDT_obj1 = datetime.datetime.strptime(ExpectedDT_str1, "%H:%M")
    ExpectedDT_str2 = '06:55'    
    ExpectedDT_obj2 = datetime.datetime.strptime(ExpectedDT_str2, "%H:%M")
    ExpectedDT_str3 = '07:40'    
    ExpectedDT_obj3 = datetime.datetime.strptime(ExpectedDT_str3, "%H:%M")
    ExpectedDT_str4 = '18:40'    
    ExpectedDT_obj4 = datetime.datetime.strptime(ExpectedDT_str4, "%H:%M")
    ExpectedDT_str5 = '18:55'    
    ExpectedDT_obj5 = datetime.datetime.strptime(ExpectedDT_str5, "%H:%M")
    ExpectedDT_str6 = '19:40'    
    ExpectedDT_obj6 = datetime.datetime.strptime(ExpectedDT_str6, "%H:%M")

    if(currentDT == ExpectedDT_str1 or currentDT == ExpectedDT_str2 or 
        currentDT == ExpectedDT_str3 or currentDT == ExpectedDT_str4
        or currentDT == ExpectedDT_str5 or currentDT == ExpectedDT_str6):

        # print message if current time and expected time matched
        if(currentDT == ExpectedDT_str1):
            print("Time matched!!", "Current Time: ", currentDT, "Expected Time: ", ExpectedDT_obj1.time())
        elif(currentDT == ExpectedDT_str2):
            print("Time matched!!", "Current Time: ", currentDT, "Expected Time: ", ExpectedDT_obj2.time())
        elif(currentDT == ExpectedDT_str3):    
            print("Time matched!!", "Current Time: ", currentDT, "Expected Time: ", ExpectedDT_obj3.time())
        elif(currentDT == ExpectedDT_str4):
            print("Time matched!!", "Current Time: ", currentDT, "Expected Time: ", ExpectedDT_obj4.time())
        elif(currentDT == ExpectedDT_str5):
            print("Time matched!!", "Current Time: ", currentDT, "Expected Time: ", ExpectedDT_obj5.time())
        elif(currentDT == ExpectedDT_str6):
            print("Time matched!!", "Current Time: ", currentDT, "Expected Time: ", ExpectedDT_obj6.time())
        
        save_capturedIMG()
        open_kakaotalk(repeat_number)
        chat_room(filter_keyword, init_number)
        send_msg(my_msg, repeat_number)
        time.sleep(60)
    else:
        # print missed message if current time and expected time unmatched
        print("Time missed!! ", "Current Time: ", currentDT)

# Thread timer
def thproc(id,sec):
    while True:
        Timer1(id)
        time.sleep(sec)
t = threading.Thread(target=thproc,args=("TST",30))

class MainWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(400, 300))    
        self.setWindowTitle("Kakao auto message sender") 
        
        pybutton = QPushButton('Click me', self)
        pybutton.clicked.connect(self.clickMethod)
        pybutton.resize(130,45)
        pybutton.move(50, 50)        
        

        pybutton1 = QPushButton('End program', self)
        pybutton1.clicked.connect(self.Endprogram)
        pybutton1.resize(130,45)
        pybutton1.move(220,50)
        
    def clickMethod(self):
        print('=================')
        print('Starting send message!')
        print('=================')
    
        t.start()

    def Endprogram(self):
        t._stop()
      
if __name__ == "__main__":                                                                                                                                                                                       
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())


