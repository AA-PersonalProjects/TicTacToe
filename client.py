from PyQt5 import QtCore, QtGui, QtWidgets
import socket
from time import sleep
import threading
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, button_list):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(675, 799)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button_grid = QtWidgets.QFrame(self.centralwidget)
        self.button_grid.setGeometry(QtCore.QRect(10, 120, 671, 681))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.button_grid.setFont(font)
        self.button_grid.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.button_grid.setFrameShadow(QtWidgets.QFrame.Raised)
        self.button_grid.setObjectName("button_grid")
        self.button_1 = QtWidgets.QPushButton(self.button_grid)
        self.button_1.setGeometry(QtCore.QRect(10, 20, 200, 200))
        self.button_1.setText("")
        self.button_1.setCheckable(False)
        self.button_1.setChecked(False)
        self.button_1.setAutoDefault(False)
        self.button_1.setDefault(False)
        self.button_1.setFlat(False)
        self.button_1.setObjectName("button_1")
        self.button_2 = QtWidgets.QPushButton(self.button_grid)
        self.button_2.setGeometry(QtCore.QRect(230, 20, 200, 200))
        self.button_2.setText("")
        self.button_2.setCheckable(False)
        self.button_2.setAutoDefault(False)
        self.button_2.setDefault(False)
        self.button_2.setFlat(False)
        self.button_2.setObjectName("button_2")
        self.button_3 = QtWidgets.QPushButton(self.button_grid)
        self.button_3.setGeometry(QtCore.QRect(450, 20, 200, 200))
        self.button_3.setText("")
        self.button_3.setCheckable(False)
        self.button_3.setAutoDefault(False)
        self.button_3.setDefault(False)
        self.button_3.setFlat(False)
        self.button_3.setObjectName("button_3")
        self.button_6 = QtWidgets.QPushButton(self.button_grid)
        self.button_6.setGeometry(QtCore.QRect(450, 240, 200, 200))
        self.button_6.setText("")
        self.button_6.setCheckable(False)
        self.button_6.setAutoDefault(False)
        self.button_6.setDefault(False)
        self.button_6.setFlat(False)
        self.button_6.setObjectName("button_6")
        self.button_4 = QtWidgets.QPushButton(self.button_grid)
        self.button_4.setGeometry(QtCore.QRect(10, 240, 200, 200))
        self.button_4.setText("")
        self.button_4.setCheckable(False)
        self.button_4.setAutoDefault(False)
        self.button_4.setDefault(False)
        self.button_4.setFlat(False)
        self.button_4.setObjectName("button_4")
        self.button_5 = QtWidgets.QPushButton(self.button_grid)
        self.button_5.setGeometry(QtCore.QRect(230, 240, 200, 200))
        self.button_5.setText("")
        self.button_5.setCheckable(False)
        self.button_5.setAutoDefault(False)
        self.button_5.setDefault(False)
        self.button_5.setFlat(False)
        self.button_5.setObjectName("button_5")
        self.button_9 = QtWidgets.QPushButton(self.button_grid)
        self.button_9.setGeometry(QtCore.QRect(450, 460, 200, 200))
        self.button_9.setText("")
        self.button_9.setCheckable(False)
        self.button_9.setAutoDefault(False)
        self.button_9.setDefault(False)
        self.button_9.setFlat(False)
        self.button_9.setObjectName("button_9")
        self.button_7 = QtWidgets.QPushButton(self.button_grid)
        self.button_7.setGeometry(QtCore.QRect(10, 460, 200, 200))
        self.button_7.setText("")
        self.button_7.setCheckable(False)
        self.button_7.setAutoDefault(False)
        self.button_7.setDefault(False)
        self.button_7.setFlat(False)
        self.button_7.setObjectName("button_7")
        self.button_8 = QtWidgets.QPushButton(self.button_grid)
        self.button_8.setGeometry(QtCore.QRect(230, 460, 200, 200))
        self.button_8.setText("")
        self.button_8.setCheckable(False)
        self.button_8.setAutoDefault(False)
        self.button_8.setDefault(False)
        self.button_8.setFlat(False)
        self.button_8.setObjectName("button_8")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(0, 0, 671, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setAutoFillBackground(False)
        self.title.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.my_wins_label = QtWidgets.QLabel(self.centralwidget)
        self.my_wins_label.setGeometry(QtCore.QRect(20, 60, 251, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.my_wins_label.setFont(font)
        self.my_wins_label.setObjectName("my_wins_label")
        self.opp_wins_label = QtWidgets.QLabel(self.centralwidget)
        self.opp_wins_label.setGeometry(QtCore.QRect(410, 60, 241, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.opp_wins_label.setFont(font)
        self.opp_wins_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.opp_wins_label.setObjectName("opp_wins_label")
        self.name_frame = QtWidgets.QFrame(self.centralwidget)
        self.name_frame.setGeometry(QtCore.QRect(200, 70, 271, 51))
        self.name_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.name_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.name_frame.setObjectName("name_frame")
        self.name_label = QtWidgets.QLabel(self.name_frame)
        self.name_label.setGeometry(QtCore.QRect(0, 10, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.name_label.setFont(font)
        self.name_label.setObjectName("name_label")
        self.name_entry = QtWidgets.QLineEdit(self.name_frame)
        self.name_entry.setGeometry(QtCore.QRect(80, 10, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.name_entry.setFont(font)
        self.name_entry.setObjectName("name_entry")
        self.name_submit = QtWidgets.QPushButton(self.name_frame)
        self.name_submit.setGeometry(QtCore.QRect(190, 10, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.name_submit.setFont(font)
        self.name_submit.setObjectName("name_submit")
        MainWindow.setCentralWidget(self.centralwidget)

        button_list.append(self.button_1)
        button_list.append(self.button_2)
        button_list.append(self.button_3)
        button_list.append(self.button_4)
        button_list.append(self.button_5)
        button_list.append(self.button_6)
        button_list.append(self.button_7)
        button_list.append(self.button_8)
        button_list.append(self.button_9)
        # for i, button in enumerate(button_list):
        #     button.clicked.connect(lambda: clicked(button, i))
        # print("hi")

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

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "Tic Tac Toe"))
        self.my_wins_label.setText(_translate("MainWindow", "My Wins: 0"))
        self.opp_wins_label.setText(_translate("MainWindow", "Opp Wins: 0"))
        self.name_label.setText(_translate("MainWindow", "Name:"))
        self.name_submit.setText(_translate("MainWindow", "Submit"))


def connect():
    global your_details
    if len(ui.name_entry.text()) < 1:
        # TODO - add msgbox
        # tk.messagebox.showerror(title="ERROR!!!", message="You MUST enter your first name <e.g. John>")
        print("ape you need a name")
    else:
        your_details["name"] = ui.name_entry.text()
        connect_to_server(ui.name_entry.text())

def connect_to_server(name):
    global client, HOST_PORT, HOST_ADDR
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((HOST_ADDR, HOST_PORT))
        client.send(name.encode('utf-8'))  # Send name to server after connecting
        # start a thread to keep receiving message from server
        # do not block the main thread
        thread = threading.Thread(target=receive_message_from_server, args=(client, "m"))
        thread.start()

        MainWindow.setWindowTitle("TicTacToe Client - " + name)
    except Exception as e:
        # TODO - add msgbox
        # tk.messagebox.showerror(title="ERROR!!!", message="Error: Cannot connect to host: " + HOST_ADDR + " on port: " + str(
        #     HOST_PORT) + " Server may be Unavailable. Try again later")
        print("ah rip connection issue")

def receive_message_from_server(sck, m):
    global your_details, opponent_details, your_turn, you_started
    while True:
        from_server = sck.recv(4096).decode('utf-8')

        if not from_server:
            break

        if from_server.startswith("welcome"):
            if from_server == "welcome1":
                your_details["color"] = "purple"
                opponent_details["color"] = "orange"
                # lbl_status["text"] = "Server: Welcome " + your_details["name"] + "! Waiting for player 2"
                print("welcome p1!")
            elif from_server == "welcome2":
                # lbl_status["text"] = "Server: Welcome " + your_details["name"] + "! Game will start soon"
                print("welcome p2!")
                your_details["color"] = "orange"
                opponent_details["color"] = "purple"

        elif from_server.startswith("opp_name:"):
            temp = from_server.replace("opp_name:", "")
            temp = temp.replace("symbol:", "")
            opponent_details["name"] = temp[0:-1]
            your_details["symbol"] = temp[-1]

            # set opponent symbol
            if your_details["symbol"] == "O":
                opponent_details["symbol"] = "X"
            else:
                opponent_details["symbol"] = "O"

            print("STARTINGGGGG")
            # lbl_status["text"] = "STATUS: " + opponent_details["name"] + " is connected!"
            sleep(3)
            # is it your turn to play? hey! 'O' comes before 'X'
            if your_details["symbol"] == "O":
                # lbl_status["text"] = "STATUS: Your turn!"
                your_turn = True
                you_started = True
            else:
                # lbl_status["text"] = "STATUS: " + opponent_details["name"] + "'s turn!"
                you_started = False
                your_turn = False
        elif from_server.startswith("index:"):
            label_index = int(from_server.replace("index:", ""))

            # update board
            button_list[label_index].setText(opponent_details["symbol"])
            button_list[label_index].setEnabled(False)
            """
            if label_index == 0:
                ui.button_1.setText(opponent_details["symbol"])
                ui.button_1.setEnabled(False)
            if label_index == 1:
                ui.button_2.setText(opponent_details["symbol"])
                ui.button_2.setEnabled(False)
            if label_index == 2:
                ui.button_3.setText(opponent_details["symbol"])
                ui.button_3.setEnabled(False)
            if label_index == 3:
                ui.button_4.setText(opponent_details["symbol"])
                ui.button_4.setEnabled(False)
            if label_index == 4:
                ui.button_5.setText(opponent_details["symbol"])
                ui.button_5.setEnabled(False)
            if label_index == 5:
                ui.button_6.setText(opponent_details["symbol"])
                ui.button_6.setEnabled(False)
            if label_index == 6:
                ui.button_7.setText(opponent_details["symbol"])
                ui.button_7.setEnabled(False)
            if label_index == 7:
                ui.button_8.setText(opponent_details["symbol"])
                ui.button_8.setEnabled(False)
            if label_index == 8:
                ui.button_9.setText(opponent_details["symbol"])
                ui.button_9.setEnabled(False)
            """
            # label = list_labels[label_index]
            # label["symbol"] = opponent_details["symbol"]
            # label["label"]["text"] = opponent_details["symbol"]
            # TODO - color?
            #label["label"].config(foreground=opponent_details["color"])

            # label["ticked"] = True
            # TODO - prooobably a way to combine this with the self check game, but its ok
            # Does this coordinate lead to a win or a draw

            if check_win(opponent_details["symbol"]):
                # TODO - game over msg
                print("YOU LOSE")
                opponent_details["score"] += 1
                thread = threading.Thread(target=init, args=("", ""))
                thread.start()
            elif check_tie():
                print("TIE")
                thread = threading.Thread(target=init, args=("", ""))
                thread.start()
            else:
                your_turn = True
                # TODO - send msg
            """
            result = check_win()
            if result[0] is False:
                result = check_tie()
            if result[0] is True and result[1] != "":  # opponent win
                opponent_details["score"] = opponent_details["score"] + 1
                if result[1] == opponent_details["symbol"]:
                    # lbl_status["text"] = "Game over, You Lost! You(" + str(your_details["score"]) + ") - " \
                    #     "" + opponent_details["name"] + "(" + str(opponent_details["score"]) + ")"
                    # lbl_status.config(foreground="red")
                    print("YOU LOSE")
                    thread = threading.Thread(target=init, args=("", ""))
                    thread.start()
            elif result[0] is True and result[1] == "T":  # a draw
                # lbl_status["text"] = "Game over, Draw! You(" + str(your_details["score"]) + ") - " \
                #     "" + opponent_details["name"] + "(" + str(opponent_details["score"]) + ")"
                # lbl_status.config(foreground="blue")
                print("TIE")
                thread = threading.Thread(target=init, args=("", ""))
                thread.start()
            else:
                your_turn = True
                # lbl_status["text"] = "STATUS: Your turn!"
                # lbl_status.config(foreground="black")
            """

    sck.close()

def init(arg0, arg1):
    global list_labels, your_turn, your_details, opponent_details, you_started

    sleep(3)

    for b in button_list:
        b.setText("")
        b.setEnabled(True)

    # lbl_status.config(foreground="black")
    # lbl_status["text"] = "STATUS: Game's starting."
    # sleep(1)
    # lbl_status["text"] = "STATUS: Game's starting.."
    # sleep(1)
    # lbl_status["text"] = "STATUS: Game's starting..."
    sleep(1)

    if you_started:
        you_started = False
        your_turn = False
        # lbl_status["text"] = "STATUS: " + opponent_details["name"] + "'s turn!"
    else:
        you_started = True
        your_turn = True
        # lbl_status["text"] = "STATUS: Your turn!"

def clicked(button, label_index):
    # TODO - send number through
    global client, your_turn
    # label = list_labels[label_index]

    if your_turn:

        button.setText(your_details["symbol"])
        button.setEnabled(False)
        client.send(("index:" + str(label_index)).encode('utf-8'))
        your_turn = False

        # Check for game end
        if check_win(your_details["symbol"]):
            # TODO - game over msg
            print("YOU WIN")
            your_details["score"] += 1
            thread = threading.Thread(target=init, args=("", ""))
            thread.start()
        elif check_tie():
            print("TIE")
            thread = threading.Thread(target=init, args=("", ""))
            thread.start()
        # else:
            # TODO - send msg
            # print("opponent's turn")
        """
        result = check_win()
        if result[0] is False:
            result = check_tie()

        if result[0] is True and result[1] != "":  # WIN
            # TODO - game over message?
            print("YOU WIN - " + result[1])
            your_details["score"] += 1
            thread = threading.Thread(target=init, args=("", ""))
            thread.start()
        elif result[0] is True and result[1] == "T":  # DRAW
            # TODO - game over message?
            print("TIE")
            thread = threading.Thread(target=init, args=("", ""))
            thread.start()
        else:
            print("opponent's turn!")
            # TODO - send message?
        """
    else:
        # lbl_status["text"] = "STATUS: Wait for your turn!"
        # lbl_status.config(foreground="red")
        print("wait your turn!")
        # send xy coordinate to server to server
"""
# check the rows
def check_row():
    list_symbols = []
    list_labels_temp = []
    winner = False
    win_symbol = ""
    for i in range(len(list_labels)):
        list_symbols.append(list_labels[i]["symbol"])
        list_labels_temp.append(list_labels[i])
        if (i + 1) % 3 == 0:
            if (list_symbols[0] == list_symbols[1] == list_symbols[2]):
                if list_symbols[0] != "":
                    winner = True
                    win_symbol = list_symbols[0]

                    list_labels_temp[0]["label"].config(foreground="green", highlightbackground="green",
                                                        highlightcolor="green", highlightthickness=2)
                    list_labels_temp[1]["label"].config(foreground="green", highlightbackground="green",
                                                        highlightcolor="green", highlightthickness=2)
                    list_labels_temp[2]["label"].config(foreground="green", highlightbackground="green",
                                                        highlightcolor="green", highlightthickness=2)

            list_symbols = []
            list_labels_temp = []

    return [winner, win_symbol]

# check the columns
def check_col():
    winner = False
    win_symbol = ""
    for i in range(num_cols):
        if list_labels[i]["symbol"] == list_labels[i + num_cols]["symbol"] == list_labels[i + num_cols + num_cols][
            "symbol"]:
            if list_labels[i]["symbol"] != "":
                winner = True
                win_symbol = list_labels[i]["symbol"]

                list_labels[i]["label"].config(foreground="green", highlightbackground="green",
                                               highlightcolor="green", highlightthickness=2)
                list_labels[i + num_cols]["label"].config(foreground="green", highlightbackground="green",
                                                          highlightcolor="green", highlightthickness=2)
                list_labels[i + num_cols + num_cols]["label"].config(foreground="green", highlightbackground="green",
                                                                     highlightcolor="green", highlightthickness=2)

    return [winner, win_symbol]
"""
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
    "color" : "",
    "score" : 0
}

opponent_details = {
    "name": " ",
    "symbol": "O",
    "color": "",
    "score": 0
}

sys.exit(app.exec_())

"""

# Code from Charles Effiong
# (https://levelup.gitconnected.com/program-a-networked-tic-tac-toe-game-in-python-30f8826e591d)

import tkinter as tk
# from tkinter import PhotoImage
from tkinter import messagebox
import socket
from time import sleep
import threading

# MAIN GAME WINDOW
window_main = tk.Tk()
window_main.title("Tic-Tac-Toe Client")
top_welcome_frame= tk.Frame(window_main)
lbl_name = tk.Label(top_welcome_frame, text = "Name:")
lbl_name.pack(side=tk.LEFT)
ent_name = tk.Entry(top_welcome_frame)
ent_name.pack(side=tk.LEFT)
btn_connect = tk.Button(top_welcome_frame, text="Connect", command=lambda : connect())
btn_connect.pack(side=tk.LEFT)
top_welcome_frame.pack(side=tk.TOP)

top_frame = tk.Frame(window_main)


# network client
client = None
HOST_ADDR = "10.0.0.81"
HOST_PORT = 5050

list_labels = []
num_cols = 3
your_turn = False
you_started = False

your_details = {
    "name": "Charles",
    "symbol": "X",
    "color" : "",
    "score" : 0
}

opponent_details = {
    "name": " ",
    "symbol": "O",
    "color": "",
    "score": 0
}

for x in range(3):
    for y in range(3):
        lbl = tk.Label(top_frame, text=" ", font="Helvetica 45 bold", height=2, width=5, highlightbackground="grey",
                       highlightcolor="grey", highlightthickness=1)
        lbl.bind("<Button-1>", lambda e, xy=(x, y): get_coordinate(xy))
        lbl.grid(row=x, column=y)

        dict_labels = {"xy": [x, y], "symbol": "", "label": lbl, "ticked": False}
        list_labels.append(dict_labels)

lbl_status = tk.Label(top_frame, text="Status: Not connected to server", font="Helvetica 14 bold")
lbl_status.grid(row=3, columnspan=3)

top_frame.pack_forget()


def init(arg0, arg1):
    global list_labels, your_turn, your_details, opponent_details, you_started

    sleep(3)

    for i in range(len(list_labels)):
        list_labels[i]["symbol"] = ""
        list_labels[i]["ticked"] = False
        list_labels[i]["label"]["text"] = ""
        list_labels[i]["label"].config(foreground="black", highlightbackground="grey",
                                       highlightcolor="grey", highlightthickness=1)

    lbl_status.config(foreground="black")
    lbl_status["text"] = "STATUS: Game's starting."
    sleep(1)
    lbl_status["text"] = "STATUS: Game's starting.."
    sleep(1)
    lbl_status["text"] = "STATUS: Game's starting..."
    sleep(1)

    if you_started:
        you_started = False
        your_turn = False
        lbl_status["text"] = "STATUS: " + opponent_details["name"] + "'s turn!"
    else:
        you_started = True
        your_turn = True
        lbl_status["text"] = "STATUS: Your turn!"


def get_coordinate(xy):
    global client, your_turn
    # convert 2D to 1D coordinate i.e. index = x * num_cols + y
    label_index = xy[0] * num_cols + xy[1]
    label = list_labels[label_index]

    if your_turn:
        if label["ticked"] is False:
            label["label"].config(foreground=your_details["color"])
            label["label"]["text"] = your_details["symbol"]
            label["ticked"] = True
            label["symbol"] = your_details["symbol"]
            # send xy coordinate to server
            client.send(("$xy$" + str(xy[0]) + "$" + str(xy[1])).encode('utf-8'))
            your_turn = False

            # Does this play leads to a win or a draw
            result = game_logic()
            if result[0] is True and result[1] != "":  # a win
                your_details["score"] = your_details["score"] + 1
                lbl_status["text"] = "Game over, You won! You(" + str(your_details["score"]) + ") - " \
                    "" + opponent_details["name"] + "(" + str(opponent_details["score"])+")"
                lbl_status.config(foreground="green")
                thread = threading.Thread(target=init, args=("", ""))
                thread.start()

            elif result[0] is True and result[1] == "":  # a draw
                lbl_status["text"] = "Game over, Draw! You(" + str(your_details["score"]) + ") - " \
                    "" + opponent_details["name"] + "(" + str(opponent_details["score"]) + ")"
                lbl_status.config(foreground="blue")
                thread = threading.Thread(target=init, args=("", ""))
                thread.start()

            else:
                lbl_status["text"] = "STATUS: " + opponent_details["name"] + "'s turn!"
    else:
        lbl_status["text"] = "STATUS: Wait for your turn!"
        lbl_status.config(foreground="red")

        # send xy coordinate to server to server


# [(0,0) -> (0,1) -> (0,2)], [(1,0) -> (1,1) -> (1,2)], [(2,0), (2,1), (2,2)]
def check_row():
    list_symbols = []
    list_labels_temp = []
    winner = False
    win_symbol = ""
    for i in range(len(list_labels)):
        list_symbols.append(list_labels[i]["symbol"])
        list_labels_temp.append(list_labels[i])
        if (i + 1) % 3 == 0:
            if (list_symbols[0] == list_symbols[1] == list_symbols[2]):
                if list_symbols[0] != "":
                    winner = True
                    win_symbol = list_symbols[0]

                    list_labels_temp[0]["label"].config(foreground="green", highlightbackground="green",
                                                        highlightcolor="green", highlightthickness=2)
                    list_labels_temp[1]["label"].config(foreground="green", highlightbackground="green",
                                                        highlightcolor="green", highlightthickness=2)
                    list_labels_temp[2]["label"].config(foreground="green", highlightbackground="green",
                                                        highlightcolor="green", highlightthickness=2)

            list_symbols = []
            list_labels_temp = []

    return [winner, win_symbol]


# [(0,0) -> (1,0) -> (2,0)], [(0,1) -> (1,1) -> (2,1)], [(0,2), (1,2), (2,2)]
def check_col():
    winner = False
    win_symbol = ""
    for i in range(num_cols):
        if list_labels[i]["symbol"] == list_labels[i + num_cols]["symbol"] == list_labels[i + num_cols + num_cols][
            "symbol"]:
            if list_labels[i]["symbol"] != "":
                winner = True
                win_symbol = list_labels[i]["symbol"]

                list_labels[i]["label"].config(foreground="green", highlightbackground="green",
                                               highlightcolor="green", highlightthickness=2)
                list_labels[i + num_cols]["label"].config(foreground="green", highlightbackground="green",
                                                          highlightcolor="green", highlightthickness=2)
                list_labels[i + num_cols + num_cols]["label"].config(foreground="green", highlightbackground="green",
                                                                     highlightcolor="green", highlightthickness=2)

    return [winner, win_symbol]


def check_diagonal():
    winner = False
    win_symbol = ""
    i = 0
    j = 2

    # top-left to bottom-right diagonal (0, 0) -> (1,1) -> (2, 2)
    a = list_labels[i]["symbol"]
    b = list_labels[i + (num_cols + 1)]["symbol"]
    c = list_labels[(num_cols + num_cols) + (i + 1)]["symbol"]
    if list_labels[i]["symbol"] == list_labels[i + (num_cols + 1)]["symbol"] == \
            list_labels[(num_cols + num_cols) + (i + 2)]["symbol"]:
        if list_labels[i]["symbol"] != "":
            winner = True
            win_symbol = list_labels[i]["symbol"]

            list_labels[i]["label"].config(foreground="green", highlightbackground="green",
                                           highlightcolor="green", highlightthickness=2)

            list_labels[i + (num_cols + 1)]["label"].config(foreground="green", highlightbackground="green",
                                                            highlightcolor="green", highlightthickness=2)
            list_labels[(num_cols + num_cols) + (i + 2)]["label"].config(foreground="green",
                                                                         highlightbackground="green",
                                                                         highlightcolor="green", highlightthickness=2)

    # top-right to bottom-left diagonal (0, 0) -> (1,1) -> (2, 2)
    elif list_labels[j]["symbol"] == list_labels[j + (num_cols - 1)]["symbol"] == list_labels[j + (num_cols + 1)]["symbol"]:
        if list_labels[j]["symbol"] != "":
            winner = True
            win_symbol = list_labels[j]["symbol"]

            list_labels[j]["label"].config(foreground="green", highlightbackground="green",
                                           highlightcolor="green", highlightthickness=2)
            list_labels[j + (num_cols - 1)]["label"].config(foreground="green", highlightbackground="green",
                                                            highlightcolor="green", highlightthickness=2)
            list_labels[j + (num_cols + 1)]["label"].config(foreground="green", highlightbackground="green",
                                                            highlightcolor="green", highlightthickness=2)
    else:
        winner = False

    return [winner, win_symbol]


# it's a draw if grid is filled
def check_draw():
    for i in range(len(list_labels)):
        if list_labels[i]["ticked"] is False:
            return [False, ""]
    return [True, ""]


def game_logic():
    result = check_row()
    if result[0]:
        return result

    result = check_col()
    if result[0]:
        return result

    result = check_diagonal()
    if result[0]:
        return result

    result = check_draw()
    return result


def connect():
    global your_details
    if len(ent_name.get()) < 1:
        tk.messagebox.showerror(title="ERROR!!!", message="You MUST enter your first name <e.g. John>")
    else:
        your_details["name"] = ent_name.get()
        connect_to_server(ent_name.get())


def connect_to_server(name):
    global client, HOST_PORT, HOST_ADDR
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((HOST_ADDR, HOST_PORT))
        client.send(name.encode('utf-8'))  # Send name to server after connecting
        # start a thread to keep receiving message from server
        # do not block the main thread :)
        thread = threading.Thread(target=receive_message_from_server, args=(client, "m"))
        thread.start()
        top_welcome_frame.pack_forget()
        top_frame.pack(side=tk.TOP)
        window_main.title("Tic-Tac-Toe Client - " + name)
    except Exception as e:
        tk.messagebox.showerror(title="ERROR!!!", message="Error: Cannot connect to host: " + HOST_ADDR + " on port: " + str(
            HOST_PORT) + " Server may be Unavailable. Try again later")


def receive_message_from_server(sck, m):
    global your_details, opponent_details, your_turn, you_started
    while True:
        from_server = sck.recv(4096).decode('utf-8')

        if not from_server:
            break

        if from_server.startswith("welcome"):
            if from_server == "welcome1":
                your_details["color"] = "purple"
                opponent_details["color"] = "orange"
                lbl_status["text"] = "Server: Welcome " + your_details["name"] + "! Waiting for player 2"
            elif from_server == "welcome2":
                lbl_status["text"] = "Server: Welcome " + your_details["name"] + "! Game will start soon"
                your_details["color"] = "orange"
                opponent_details["color"] = "purple"

        elif from_server.startswith("opponent_name$"):
            temp = from_server.replace("opponent_name$", "")
            temp = temp.replace("symbol", "")
            name_index = temp.find("$")
            symbol_index = temp.rfind("$")
            opponent_details["name"] = temp[0:name_index]
            your_details["symbol"] = temp[symbol_index:len(temp)]

            # set opponent symbol
            if your_details["symbol"] == "O":
                opponent_details["symbol"] = "X"
            else:
                opponent_details["symbol"] = "O"

            lbl_status["text"] = "STATUS: " + opponent_details["name"] + " is connected!"
            sleep(3)
            # is it your turn to play? hey! 'O' comes before 'X'
            if your_details["symbol"] == "O":
                lbl_status["text"] = "STATUS: Your turn!"
                your_turn = True
                you_started = True
            else:
                lbl_status["text"] = "STATUS: " + opponent_details["name"] + "'s turn!"
                you_started = False
                your_turn = False
        elif from_server.startswith("$xy$"):
            temp = from_server.replace("$xy$", "")
            _x = temp[0:temp.find("$")]
            _y = temp[temp.find("$") + 1:len(temp)]

            # update board
            label_index = int(_x) * num_cols + int(_y)
            label = list_labels[label_index]
            label["symbol"] = opponent_details["symbol"]
            label["label"]["text"] = opponent_details["symbol"]
            label["label"].config(foreground=opponent_details["color"])
            label["ticked"] = True

            # Does this cordinate leads to a win or a draw
            result = game_logic()
            if result[0] is True and result[1] != "":  # opponent win
                opponent_details["score"] = opponent_details["score"] + 1
                if result[1] == opponent_details["symbol"]:  #
                    lbl_status["text"] = "Game over, You Lost! You(" + str(your_details["score"]) + ") - " \
                        "" + opponent_details["name"] + "(" + str(opponent_details["score"]) + ")"
                    lbl_status.config(foreground="red")
                    thread = threading.Thread(target=init, args=("", ""))
                    thread.start()
            elif result[0] is True and result[1] == "":  # a draw
                lbl_status["text"] = "Game over, Draw! You(" + str(your_details["score"]) + ") - " \
                    "" + opponent_details["name"] + "(" + str(opponent_details["score"]) + ")"
                lbl_status.config(foreground="blue")
                thread = threading.Thread(target=init, args=("", ""))
                thread.start()
            else:
                your_turn = True
                lbl_status["text"] = "STATUS: Your turn!"
                lbl_status.config(foreground="black")

    sck.close()


window_main.mainloop()


"""
