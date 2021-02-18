from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import socket
from time import sleep
import threading
import sys


class Ui_MainWindow(object):

    # noinspection PyAttributeOutsideInit
    def setupUi(self, mainWindow, button_list_element):
        mainWindow.setObjectName("MainWindow")
        mainWindow.resize(676, 799)
        mainWindow.setStyleSheet("background-color: rgb(204, 255, 203);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button_grid = QtWidgets.QFrame(self.centralwidget)
        self.button_grid.setGeometry(QtCore.QRect(10, 120, 671, 681))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(36)
        font.setBold(True)
        self.button_grid.setFont(font)
        self.button_grid.setStyleSheet("background-color: rgb(204, 255, 203);")
        self.button_grid.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.button_grid.setFrameShadow(QtWidgets.QFrame.Raised)
        self.button_grid.setObjectName("button_grid")
        self.button_1 = QtWidgets.QPushButton(self.button_grid)
        self.button_1.setGeometry(QtCore.QRect(10, 20, 200, 200))
        self.button_1.setMouseTracking(False)
        self.button_1.setStyleSheet("background-color: rgb(255, 232, 203);")
        self.button_1.setText("")
        self.button_1.setCheckable(False)
        self.button_1.setChecked(False)
        self.button_1.setAutoDefault(False)
        self.button_1.setDefault(False)
        self.button_1.setFlat(False)
        self.button_1.setObjectName("button_1")
        self.button_1.setFont(font)
        self.button_2 = QtWidgets.QPushButton(self.button_grid)
        self.button_2.setGeometry(QtCore.QRect(230, 20, 200, 200))
        self.button_2.setStyleSheet("background-color: rgb(255, 232, 203);")
        self.button_2.setText("")
        self.button_2.setCheckable(False)
        self.button_2.setAutoDefault(False)
        self.button_2.setDefault(False)
        self.button_2.setFlat(False)
        self.button_2.setObjectName("button_2")
        self.button_2.setFont(font)
        self.button_3 = QtWidgets.QPushButton(self.button_grid)
        self.button_3.setGeometry(QtCore.QRect(450, 20, 200, 200))
        self.button_3.setStyleSheet("background-color: rgb(255, 232, 203);\n"
                                    "")
        self.button_3.setText("")
        self.button_3.setCheckable(False)
        self.button_3.setAutoDefault(False)
        self.button_3.setDefault(False)
        self.button_3.setFlat(False)
        self.button_3.setObjectName("button_3")
        self.button_3.setFont(font)
        self.button_6 = QtWidgets.QPushButton(self.button_grid)
        self.button_6.setGeometry(QtCore.QRect(450, 240, 200, 200))
        self.button_6.setStyleSheet("background-color: rgb(255, 232, 203);")
        self.button_6.setText("")
        self.button_6.setCheckable(False)
        self.button_6.setAutoDefault(False)
        self.button_6.setDefault(False)
        self.button_6.setFlat(False)
        self.button_6.setObjectName("button_6")
        self.button_6.setFont(font)
        self.button_4 = QtWidgets.QPushButton(self.button_grid)
        self.button_4.setGeometry(QtCore.QRect(10, 240, 200, 200))
        self.button_4.setStyleSheet("background-color: rgb(255, 232, 203);")
        self.button_4.setText("")
        self.button_4.setCheckable(False)
        self.button_4.setAutoDefault(False)
        self.button_4.setDefault(False)
        self.button_4.setFlat(False)
        self.button_4.setObjectName("button_4")
        self.button_4.setFont(font)
        self.button_5 = QtWidgets.QPushButton(self.button_grid)
        self.button_5.setGeometry(QtCore.QRect(230, 240, 200, 200))
        self.button_5.setStyleSheet("background-color: rgb(255, 232, 203);")
        self.button_5.setText("")
        self.button_5.setCheckable(False)
        self.button_5.setAutoDefault(False)
        self.button_5.setDefault(False)
        self.button_5.setFlat(False)
        self.button_5.setObjectName("button_5")
        self.button_5.setFont(font)
        self.button_9 = QtWidgets.QPushButton(self.button_grid)
        self.button_9.setGeometry(QtCore.QRect(450, 460, 200, 200))
        self.button_9.setStyleSheet("background-color: rgb(255, 232, 203);")
        self.button_9.setText("")
        self.button_9.setCheckable(False)
        self.button_9.setAutoDefault(False)
        self.button_9.setDefault(False)
        self.button_9.setFlat(False)
        self.button_9.setObjectName("button_9")
        self.button_9.setFont(font)
        self.button_7 = QtWidgets.QPushButton(self.button_grid)
        self.button_7.setGeometry(QtCore.QRect(10, 460, 200, 200))
        self.button_7.setStyleSheet("background-color: rgb(255, 232, 203);")
        self.button_7.setText("")
        self.button_7.setCheckable(False)
        self.button_7.setAutoDefault(False)
        self.button_7.setDefault(False)
        self.button_7.setFlat(False)
        self.button_7.setObjectName("button_7")
        self.button_7.setFont(font)
        self.button_8 = QtWidgets.QPushButton(self.button_grid)
        self.button_8.setGeometry(QtCore.QRect(230, 460, 200, 200))
        self.button_8.setStyleSheet("background-color: rgb(255, 232, 203);")
        self.button_8.setText("")
        self.button_8.setCheckable(False)
        self.button_8.setAutoDefault(False)
        self.button_8.setDefault(False)
        self.button_8.setFlat(False)
        self.button_8.setObjectName("button_8")
        self.button_8.setFont(font)
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(0, 0, 681, 51))
        font.setPointSize(24)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setAutoFillBackground(False)
        self.title.setStyleSheet("background-color: rgb(0, 170, 255);\n"
                                 "background-color: rgb(181, 227, 255);")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.my_wins_label = QtWidgets.QLabel(self.centralwidget)
        self.my_wins_label.setGeometry(QtCore.QRect(20, 60, 300, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(16)
        self.my_wins_label.setFont(font)
        self.my_wins_label.setStyleSheet("background-color: rgb(204, 255, 203);")
        self.my_wins_label.setObjectName("my_wins_label")
        self.opp_wins_label = QtWidgets.QLabel(self.centralwidget)
        self.opp_wins_label.setGeometry(QtCore.QRect(350, 60, 300, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(16)
        self.opp_wins_label.setFont(font)
        self.opp_wins_label.setStyleSheet("background-color: rgb(204, 255, 203);")
        self.opp_wins_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.opp_wins_label.setObjectName("opp_wins_label")
        self.name_frame = QtWidgets.QFrame(self.centralwidget)
        self.name_frame.setGeometry(QtCore.QRect(200, 70, 271, 51))
        self.name_frame.setStyleSheet("background-color: rgb(185, 252, 255);")
        self.name_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.name_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.name_frame.setObjectName("name_frame")
        self.name_label = QtWidgets.QLabel(self.name_frame)
        self.name_label.setGeometry(QtCore.QRect(0, 10, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setBold(False)
        font.setPointSize(16)
        self.name_label.setFont(font)
        self.name_label.setStyleSheet("")
        self.name_label.setObjectName("name_label")
        self.name_entry = QtWidgets.QLineEdit(self.name_frame)
        self.name_entry.setGeometry(QtCore.QRect(80, 10, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.name_entry.setFont(font)
        self.name_entry.setStyleSheet("\n"
                                      "background-color: rgb(255, 255, 255);")
        self.name_entry.setObjectName("name_entry")
        self.name_submit = QtWidgets.QPushButton(self.name_frame)
        self.name_submit.setGeometry(QtCore.QRect(190, 10, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(10)
        self.name_submit.setFont(font)
        self.name_submit.setStyleSheet("\n"
                                       "background-color: rgb(255, 238, 175);")
        self.name_submit.setObjectName("name_submit")
        mainWindow.setCentralWidget(self.centralwidget)

        button_list_element.append(self.button_1)
        button_list_element.append(self.button_2)
        button_list_element.append(self.button_3)
        button_list_element.append(self.button_4)
        button_list_element.append(self.button_5)
        button_list_element.append(self.button_6)
        button_list_element.append(self.button_7)
        button_list_element.append(self.button_8)
        button_list_element.append(self.button_9)
        self.button_1.clicked.connect(lambda: clicked(self.button_1, 0))
        self.button_2.clicked.connect(lambda: clicked(self.button_2, 1))
        self.button_3.clicked.connect(lambda: clicked(self.button_3, 2))
        self.button_4.clicked.connect(lambda: clicked(self.button_4, 3))
        self.button_5.clicked.connect(lambda: clicked(self.button_5, 4))
        self.button_6.clicked.connect(lambda: clicked(self.button_6, 5))
        self.button_7.clicked.connect(lambda: clicked(self.button_7, 6))
        self.button_8.clicked.connect(lambda: clicked(self.button_8, 7))
        self.button_9.clicked.connect(lambda: clicked(self.button_9, 8))
        self.name_submit.clicked.connect(connect)
        self.my_wins_label.setVisible(False)
        self.opp_wins_label.setVisible(False)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "Tic Tac Toe"))
        self.my_wins_label.setText(_translate("MainWindow", "My Wins: 0"))
        self.opp_wins_label.setText(_translate("MainWindow", "Opp Wins: 0"))
        self.name_label.setText(_translate("MainWindow", "Name:"))
        self.name_submit.setText(_translate("MainWindow", "Submit"))


def connect():
    global your_details
    if len(ui.name_entry.text()) < 1:
        need_name = QMessageBox()
        need_name.setIcon(QMessageBox.Critical)
        need_name.setText("You need to set a name first!")
        need_name.setWindowTitle("Need Name")
        need_name.exec_()
    else:
        your_details["name"] = ui.name_entry.text()
        connect_to_server(ui.name_entry.text())


def connect_to_server(name):
    global client, HOST_PORT, HOST_ADDR
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((HOST_ADDR, HOST_PORT))
        client.send(name.encode('utf-8'))
        # start a thread to keep receiving message from server
        thread = threading.Thread(target=receive_message_from_server, args=(client, "m"))
        thread.start()

        MainWindow.setWindowTitle("TicTacToe Client - " + name)
    except socket.error:
        error = QMessageBox()
        error.setIcon(QMessageBox.Critical)
        error.setText("Error: Could not connect to server")
        error.setWindowTitle("Connection Issue")
        error.exec_()


def receive_message_from_server(sck, m):
    global your_details, opponent_details, your_turn, you_started
    while True:
        from_server = sck.recv(4096).decode('utf-8')

        if not from_server:
            break

        if from_server.startswith("welcome"):
            if from_server == "welcome1":
                ui.title.setText("Tic Tac Toe - waiting for P2...")
            elif from_server == "welcome2":
                ui.title.setText("Tic Tac Toe - connecting...")

        elif from_server.startswith("opp_name:"):
            ui.title.setText("Tic Tac Toe")
            temp = from_server.replace("opp_name:", "")
            temp = temp.replace("symbol:", "")
            opponent_details["name"] = temp[0:-1]
            your_details["symbol"] = temp[-1]

            ui.name_frame.setVisible(False)
            ui.my_wins_label.setVisible(True)
            ui.opp_wins_label.setVisible(True)

            # set opponent symbol
            if your_details["symbol"] == "O":
                opponent_details["symbol"] = "X"
            else:
                opponent_details["symbol"] = "O"

            # update wins UI
            ui.my_wins_label.setText(your_details["name"] + " (" + your_details["symbol"] + ") Wins: " +
                                     str(your_details["score"]))
            ui.opp_wins_label.setText(opponent_details["name"] + " (" + opponent_details["symbol"] + ") Wins: " +
                                      str(opponent_details["score"]))

            sleep(2)

            # O starts the game
            if your_details["symbol"] == "O":
                ui.my_wins_label.setStyleSheet("background-color: rgb(48, 190, 255)")
                ui.opp_wins_label.setStyleSheet("")
                your_turn = True
                you_started = True
            else:
                ui.opp_wins_label.setStyleSheet("background-color: rgb(48, 190, 255)")
                ui.my_wins_label.setStyleSheet("")
                you_started = False
                your_turn = False
        elif from_server.startswith("index:"):
            label_index = int(from_server.replace("index:", ""))

            # update board
            button_list[label_index].setText(opponent_details["symbol"])
            button_list[label_index].setEnabled(False)

            # check for win or tie
            if check_win(opponent_details["symbol"]):
                opponent_details["score"] += 1
                thread = threading.Thread(target=init)
                thread.start()
            elif check_tie():
                thread = threading.Thread(target=init)
                thread.start()
            else:
                your_turn = True
                ui.my_wins_label.setStyleSheet("background-color: rgb(48, 190, 255)")
                ui.opp_wins_label.setStyleSheet("")

    sck.close()


def init():
    global your_turn, your_details, opponent_details, you_started

    ui.my_wins_label.setText(your_details["name"] + " (" + your_details["symbol"] + ") Wins: " +
                             str(your_details["score"]))
    ui.opp_wins_label.setText(opponent_details["name"] + " (" + opponent_details["symbol"] + ") Wins: " +
                              str(opponent_details["score"]))

    for b in button_list:
        b.setText("")
        b.setEnabled(True)

    sleep(2)

    if you_started:
        you_started = False
        your_turn = False
        ui.my_wins_label.setStyleSheet("")
        ui.opp_wins_label.setStyleSheet("background-color: rgb(48, 190, 255)")
    else:
        you_started = True
        your_turn = True
        ui.my_wins_label.setStyleSheet("background-color: rgb(48, 190, 255)")
        ui.opp_wins_label.setStyleSheet("")


def clicked(button, label_index):
    global client, your_turn

    if your_turn:

        button.setText(your_details["symbol"])
        button.setEnabled(False)
        client.send(("index:" + str(label_index)).encode('utf-8'))
        your_turn = False

        # Check for game end
        if check_win(your_details["symbol"]):
            your_details["score"] += 1
            thread = threading.Thread(target=init)
            thread.start()
        elif check_tie():
            thread = threading.Thread(target=init)
            thread.start()
        else:
            ui.my_wins_label.setStyleSheet("")
            ui.opp_wins_label.setStyleSheet("background-color: rgb(48, 190, 255)")

    else:
        wait_turn = QMessageBox()
        wait_turn.setIcon(QMessageBox.Critical)
        wait_turn.setText("It's not your turn!")
        wait_turn.setWindowTitle("Wait!")
        wait_turn.exec_()


# check if a player has won
def check_win(player):
    if (button_list[0].text() == button_list[1].text() == button_list[2].text() == player or
            button_list[0].text() == button_list[3].text() == button_list[6].text() == player or
            button_list[3].text() == button_list[4].text() == button_list[5].text() == player or
            button_list[1].text() == button_list[4].text() == button_list[7].text() == player or
            button_list[0].text() == button_list[4].text() == button_list[8].text() == player or
            button_list[2].text() == button_list[4].text() == button_list[6].text() == player or
            button_list[6].text() == button_list[7].text() == button_list[8].text() == player or
            button_list[2].text() == button_list[5].text() == button_list[8].text() == player):
        return True
    return False


# it's a tie if grid is filled
def check_tie():
    for i, b in enumerate(button_list):
        if b.text() == "":
            return False
    return True


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
button_list = []
ui.setupUi(MainWindow, button_list)
MainWindow.setWindowTitle("TicTacToe Client")
MainWindow.show()

# network client
client = None
HOST_ADDR = socket.gethostbyname(socket.gethostname())
HOST_PORT = 5050

num_cols = 3
your_turn = False
you_started = False

your_details = {
    "name": "Charles",
    "symbol": "X",
    "score": 0
}

opponent_details = {
    "name": " ",
    "symbol": "O",
    "score": 0
}

sys.exit(app.exec_())
