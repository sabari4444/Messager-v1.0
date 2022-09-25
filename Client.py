from xml.dom.expatbuilder import theDOMImplementation
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread
from PyQt5.QtGui import QFont, QFontDatabase
import socket
import pickle
import threading
import time
import sys
import css

# QCoreApplication.instance().quit
# To Close app
global All_Messages
All_Messages = []


class ConnectServer:

    def __init__(self):
        self.msg = None
        self.client_socket = None
        self.IP = "70.70.70.6"
        self.PORT = 8080
        self.username = "sabari"
        self.value = True
        self.assign_protocol()

    def assign_protocol(self):

        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        except Exception as e:
            print(e)
            quit()

        finally:
            print('initiating to connect to server...')
            self.connect()

    def connect(self):

        try:
            self.client_socket.connect((self.IP, self.PORT))

        except Exception as e:
            print(e)
            quit()

        finally:
            print('Connected To Server Successfully...')
            threading.Thread(target=self.ping).start()

    def send_msg(self, msg, username):

        msg_list = [username, msg, time.time(), 'class:msg']
        msg_data = pickle.dumps(msg_list)
        self.client_socket.send(msg_data)

    def send_quit(self, username):
        msg_list = [username, "quiting...", time.time(), 'class:quit']
        msg_data = pickle.dumps(msg_list)
        self.client_socket.send(msg_data)

    def ping(self):

        while self.value == True:
            msg_list = [self.username, 'Connection Still alive (200)..', time.time(), 'class:ping']
            msg_data = pickle.dumps(msg_list)
            try:
                self.client_socket.send(msg_data)

            except Exception as e:
                print(e)
                quit()

            threading.Thread(target=self.get_message).start()

            time.sleep(2)

    def get_message(self):

        try:
            msg = self.client_socket.recv(2048)
            msg = pickle.loads(msg)

            for i in msg:
                if i[3] == 'class:ping_msg':
                    global All_Messages
                    All_Messages.append(i)

        except Exception as e:
            print(e)
            quit()

    def disconnect(self):
        self.client_socket.close()
        self.value = False
        sys.exit('bye!')


class Window(QMainWindow):

    def __init__(self):
        super(Window, self).__init__()

        self.n = 2
        self.setGeometry(200, 200, 720, 434)
        self.setWindowTitle("Application")
        self.e0 = QLineEdit(self)
        self.e1 = QLineEdit(self)
        self.b0 = QPushButton(self)
        self.b1 = QPushButton(self)
        self.l0 = QLabel(self)
        self.l1 = QLabel(self)

        self.msg_l0 = QLabel(self)
        self.msg_l1 = QLabel(self)
        self.msg_l2 = QLabel(self)
        self.msg_l3 = QLabel(self)
        self.msg_l4 = QLabel(self)

        self.ui()

    def ui(self):
        # Entry

        self.e0.setGeometry(243, 370, 360, 30)
        self.e0.setObjectName("e0")

        self.e1.setGeometry(36, 377, 108, 24)
        self.e1.setObjectName("e1")
        self.e1.setText("sabari")
        self.e1.setEnabled(False)

        # Buttons

        self.b0.setGeometry(633, 367, 54, 37)
        self.b0.setObjectName("b0")
        self.b0.clicked.connect(self.command_b0)

        self.b1.setGeometry(142, 371, 32, 32)
        self.b1.setObjectName("b1")
        self.b1.clicked.connect(self.command_b1)

        # Label

        self.l0.setText("Group Chat")
        self.l0.setGeometry(255, 40, 160, 30)
        self.l0.setObjectName("l0")

        self.l1.setText("Group Info")
        self.l1.setGeometry(30, 40, 160, 30)
        self.l1.setObjectName("l1")

        self.msg_l0.move(230, 100)
        self.msg_l1.move(230, 150)
        self.msg_l2.move(230, 200)
        self.msg_l3.move(230, 250)
        self.msg_l4.move(230, 300)

        threading.Thread(target=self.add_label).start()

    def command_b0(self):

        msg = self.e0.text()
        username = self.e1.text()
        self.e0.setText("")
        self.send_message(msg, username)

    def command_b1(self):

        if self.n % 2 == 0:
            self.b1.setStyleSheet("background-image : url(Resoures//Confirm.png);")
            self.e1.setEnabled(True)

        else:
            self.b1.setStyleSheet("background-image : url(Resoures//Edit_pencil.png);")
            self.e1.setEnabled(False)
        self.n += 1

    @staticmethod
    def send_message(msg, username):
        threading.Thread(target=connect.send_msg, args=(msg, username, )).start()

    def add_label(self):

        global All_Messages
        old_list = len(All_Messages)
        while True:
            msg_len = len(All_Messages)

            if old_list != msg_len:
                new_msg_list = All_Messages
                new_msg_list = new_msg_list[::-1]

                if msg_len >= 6:
                    new_msg_list = new_msg_list[:6]

                for i in range(msg_len):

                    if i == 0:
                        msg = new_msg_list[i]
                        self.msg_l0.setText(f'{msg[0]}> {msg[1]}')

                        if msg[0] == self.e1.text():
                            self.msg_l0.setStyleSheet(css.msg_label_me)

                        else:
                            self.msg_l0.setStyleSheet(css.msg_label_notme)
                        self.msg_l0.adjustSize()

                    elif i == 1:
                        msg = new_msg_list[i]
                        self.msg_l1.setText(f'{msg[0]}> {msg[1]}')

                        if msg[0] == self.e1.text():
                            self.msg_l1.setStyleSheet(css.msg_label_me)

                        else:
                            self.msg_l1.setStyleSheet(css.msg_label_notme)

                        self.msg_l1.adjustSize()

                    elif i == 2:
                        msg = new_msg_list[i]
                        self.msg_l2.setText(f'{msg[0]}> {msg[1]}')

                        if msg[0] == self.e1.text():
                            self.msg_l2.setStyleSheet(css.msg_label_me)

                        else:
                            self.msg_l2.setStyleSheet(css.msg_label_notme)

                        self.msg_l2.adjustSize()

                    elif i == 3:
                        msg = new_msg_list[i]
                        self.msg_l3.setText(f'{msg[0]}> {msg[1]}')

                        if msg[0] == self.e1.text():
                            self.msg_l3.setStyleSheet(css.msg_label_me)

                        else:
                            self.msg_l3.setStyleSheet(css.msg_label_notme)

                        self.msg_l3.adjustSize()

                    elif i == 4:
                        msg = new_msg_list[i]
                        self.msg_l4.setText(f'{msg[0]}> {msg[1]}')

                        if msg[0] == self.e1.text():
                            self.msg_l4.setStyleSheet(css.msg_label_me)

                        else:
                            self.msg_l4.setStyleSheet(css.msg_label_notme)

                        self.msg_l4.adjustSize()

                old_list = msg_len
            time.sleep(0.5)


def exit_server(application, server):
    application.exec_()
    server.disconnect()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    root = Window()

    connect = ConnectServer()

    QFontDatabase.addApplicationFont(r"Resoures\Inter-V.ttf")
    QFontDatabase.addApplicationFont(r"Resoures\K2D-Light.ttf")

    root.setStyleSheet(css.__doc__)
    root.show()

    sys.exit(exit_server(app, connect))


"""

Sign up to get the mos
out of Programiz PRO
Self-paced Courses
Learn at your own time; no
deadlines or restrictions.
Build Real-life Projects
Project based learning to give
you a first hand experience on
solving real scenarios.
Earn Certification
Complete Leaming paths and
earn Certifications."""