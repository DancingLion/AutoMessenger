import sys
import os
import pyautogui
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QGridLayout, QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize
import main 
#from main import main, save_capturedIMG, open_kakaotalk, chat_room, send_msg, initialize, glovar_value_set, glovar_value_Clear

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
        
        #glovar = 0
    
    def clickMethod(self):
        print('Clicked Pyqt button.')
        glovar_value_set()
        main()
        #save_capturedIMG()
        #os.system('main.py')
        #subprocess.run("main.py", shell=True)

    def Endprogram(self):
        glovar_value_Clear()
        QtCore.QCoreApplication.instance().quit()
        #glovar = 0
        #sys.exit()
       

if __name__ == "__main__":                                                                                                                                                                                       
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())


