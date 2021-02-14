from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import socket
import threading
from time import sleep

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(391, 319)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setGeometry(QtCore.QRect(100, 60, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.start_button.setFont(font)
        self.start_button.setObjectName("start_button")
        self.stop_button = QtWidgets.QPushButton(self.centralwidget)
        self.stop_button.setGeometry(QtCore.QRect(200, 60, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.stop_button.setFont(font)
        self.stop_button.setObjectName("stop_button")
        self.stop_button.setEnabled(False)
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(0, 0, 391, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setAutoFillBackground(False)
        self.title.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.address_label = QtWidgets.QLabel(self.centralwidget)
        self.address_label.setGeometry(QtCore.QRect(60, 100, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.address_label.setFont(font)
        self.address_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.address_label.setObjectName("address_label")
        self.port_label = QtWidgets.QLabel(self.centralwidget)
        self.port_label.setGeometry(QtCore.QRect(200, 100, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.port_label.setFont(font)
        self.port_label.setObjectName("port_label")
        self.clients_label = QtWidgets.QLabel(self.centralwidget)
        self.clients_label.setGeometry(QtCore.QRect(90, 140, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.clients_label.setFont(font)
        self.clients_label.setAlignment(QtCore.Qt.AlignCenter)
        self.clients_label.setObjectName("clients_label")
        self.clients_list = QtWidgets.QScrollArea(self.centralwidget)
        self.clients_list.setGeometry(QtCore.QRect(10, 180, 371, 131))
        self.clients_list.setWidgetResizable(True)
        self.clients_list.setObjectName("clients_list")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 369, 129))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.clients_list.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)

        self.start_button.clicked.connect(start_server)
        self.stop_button.clicked.connect(stop_server)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.start_button.setText(_translate("MainWindow", "Start"))
        self.stop_button.setText(_translate("MainWindow", "Stop"))
        self.title.setText(_translate("MainWindow", "Tic Tac Toe Server"))
        self.address_label.setText(_translate("MainWindow", "Address: X.X.X.X"))
        self.port_label.setText(_translate("MainWindow", "Port: XXXX"))
        self.clients_label.setText(_translate("MainWindow", "Clients (under construction):"))

# Start server function
def start_server():
    global server, HOST_ADDR, HOST_PORT  # code is fine without this
    ui.start_button.setEnabled(False)
    ui.stop_button.setEnabled(True)

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST_ADDR, HOST_PORT))
    server.listen()  # server is listening for client connection

    print("we chillin")

    thread = threading.Thread(target=accept_clients, args=(server, ""))
    thread.start()

    ui.address_label.setText("Address: " + HOST_ADDR)
    ui.port_label.setText("Port: " + str(HOST_PORT))

# Stop server function
def stop_server():
    global server
    # TODO - actually stop the server
    ui.start_button.setEnabled(True)
    ui.stop_button.setEnabled(False)

# Accept clients to server
def accept_clients(the_server, y):
    while True:
        if len(clients) < 2:
            client, addr = the_server.accept()
            clients.append(client)

            print("ay wtf")

            # use a thread so as not to clog the gui thread
            thread = threading.Thread(target=send_receive_client_message, args=(client, addr))
            thread.start()

# Function to receive message from current client AND
# Send that message to other clients
def send_receive_client_message(client_connection, client_ip_addr):
    global server, client_name, clients, player_data

    client_msg = " "

    # send welcome message to client
    client_name = client_connection.recv(4096).decode('utf-8')

    if len(clients) < 2:
        client_connection.send("welcome1".encode('utf-8'))
    else:
        client_connection.send("welcome2".encode('utf-8'))

    clients_names.append(client_name)
    # update_client_names_display(clients_names)  # update client names display

    if len(clients) > 1:
        sleep(1)
        symbols = ["O", "X"]

        # send opponent name and symbol
        clients[0].send(("opp_name:" + clients_names[1] + "symbol:" + symbols[0]).encode('utf-8'))
        clients[1].send(("opp_name:" + clients_names[0] + "symbol:" + symbols[1]).encode('utf-8'))

    while True:
        # get the player choice from received data
        data = client_connection.recv(4096).decode('utf-8')
        if not data:
            break

        # player x,y coordinate data. forward to the other player
        if data.startswith("index:"):
            # is the message from client1 or client2?
            if client_connection == clients[0]:
                # send the data from this player (client) to the other player (client)
                clients[1].send(data.encode('utf-8'))
            else:
                # send the data from this player (client) to the other player (client)
                clients[0].send(data.encode('utf-8'))

    # find the client index then remove from both lists(client name list and connection list)
    idx = get_client_index(clients, client_connection)
    del clients_names[idx]
    del clients[idx]
    client_connection.close()

    # update_client_names_display(clients_names)  # update client names display

# Return the index of the current client in the list of clients
def get_client_index(client_list, curr_client):
    idx = 0
    for conn in client_list:
        if conn == curr_client:
            break
        idx = idx + 1

    return idx

# TODO - set up client names display
"""
# Update client name display when a new client connects OR
# When a connected client disconnects
def update_client_names_display(name_list):
    tkDisplay.config(state=tk.NORMAL)
    tkDisplay.delete('1.0', tk.END)

    for c in name_list:
        tkDisplay.insert(tk.END, c+"\n")
    tkDisplay.config(state=tk.DISABLED)
"""

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.setWindowTitle("TicTacToe Server")
MainWindow.show()

server = None
HOST_ADDR = socket.gethostbyname(socket.gethostname())
HOST_PORT = 5050
client_name = " "
clients = []
clients_names = []
player_data = []

sys.exit(app.exec_())

"""
# Code from Charles Effiong
# (https://levelup.gitconnected.com/program-a-networked-tic-tac-toe-game-in-python-30f8826e591d)

import tkinter as tk
import socket
import threading
from time import sleep
# import random


window = tk.Tk()
window.title("Tic-Tac-Toe Server")

# Top frame consisting of two buttons widgets (i.e. btnStart, btnStop)
topFrame = tk.Frame(window)
btnStart = tk.Button(topFrame, text="Start", command=lambda : start_server())
btnStart.pack(side=tk.LEFT)
btnStop = tk.Button(topFrame, text="Stop", command=lambda : stop_server(), state=tk.DISABLED)
btnStop.pack(side=tk.LEFT)
topFrame.pack(side=tk.TOP, pady=(5, 0))

# Middle frame consisting of two labels for displaying the host and port info
middleFrame = tk.Frame(window)
lblHost = tk.Label(middleFrame, text = "Address: X.X.X.X")
lblHost.pack(side=tk.LEFT)
lblPort = tk.Label(middleFrame, text = "Port:XXXX")
lblPort.pack(side=tk.LEFT)
middleFrame.pack(side=tk.TOP, pady=(5, 0))

# The client frame shows the client area
clientFrame = tk.Frame(window)
lblLine = tk.Label(clientFrame, text="**********Client List**********").pack()
scrollBar = tk.Scrollbar(clientFrame)
scrollBar.pack(side=tk.RIGHT, fill=tk.Y)
tkDisplay = tk.Text(clientFrame, height=10, width=30)
tkDisplay.pack(side=tk.LEFT, fill=tk.Y, padx=(5, 0))
scrollBar.config(command=tkDisplay.yview)
tkDisplay.config(yscrollcommand=scrollBar.set, background="#F4F6F7", highlightbackground="grey", state="disabled")
clientFrame.pack(side=tk.BOTTOM, pady=(5, 10))


server = None
HOST_ADDR = "10.0.0.81"  # socket.gethostbyname(socket.gethostname())
HOST_PORT = 5050
client_name = " "
clients = []
clients_names = []
player_data = []


# Start server function
def start_server():
    global server, HOST_ADDR, HOST_PORT  # code is fine without this
    btnStart.config(state=tk.DISABLED)
    btnStop.config(state=tk.NORMAL)

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(socket.AF_INET)
    print(socket.SOCK_STREAM)

    server.bind((HOST_ADDR, HOST_PORT))
    server.listen()  # server is listening for client connection

    thread = threading.Thread(target=accept_clients, args=(server, " "))
    thread.start()

    lblHost["text"] = "Address: " + HOST_ADDR
    lblPort["text"] = "Port: " + str(HOST_PORT)


# Stop server function
def stop_server():
    global server
    btnStart.config(state=tk.NORMAL)
    btnStop.config(state=tk.DISABLED)


def accept_clients(the_server, y):
    while True:
        if len(clients) < 2:
            client, addr = the_server.accept()
            clients.append(client)

            # use a thread so as not to clog the gui thread
            thread = threading.Thread(target=send_receive_client_message, args=(client, addr))
            thread.start()


# Function to receive message from current client AND
# Send that message to other clients
def send_receive_client_message(client_connection, client_ip_addr):
    global server, client_name, clients, player_data

    client_msg = " "

    # send welcome message to client
    client_name = client_connection.recv(4096).decode('utf-8')

    if len(clients) < 2:
        client_connection.send("welcome1".encode('utf-8'))
    else:
        client_connection.send("welcome2".encode('utf-8'))

    clients_names.append(client_name)
    update_client_names_display(clients_names)  # update client names display

    if len(clients) > 1:
        sleep(1)
        symbols = ["O", "X"]

        # send opponent name and symbol
        clients[0].send(("opponent_name$" + clients_names[1] + "symbol" + symbols[0]).encode('utf-8'))
        clients[1].send(("opponent_name$" + clients_names[0] + "symbol" + symbols[1]).encode('utf-8'))

    while True:
        # get the player choice from received data
        data = client_connection.recv(4096).decode('utf-8')
        if not data:
            break

        # player x,y coordinate data. forward to the other player
        if data.startswith("$xy$"):
            # is the message from client1 or client2?
            if client_connection == clients[0]:
                # send the data from this player (client) to the other player (client)
                clients[1].send(data.encode('utf-8'))
            else:
                # send the data from this player (client) to the other player (client)
                clients[0].send(data.encode('utf-8'))

    # find the client index then remove from both lists(client name list and connection list)
    idx = get_client_index(clients, client_connection)
    del clients_names[idx]
    del clients[idx]
    client_connection.close()

    update_client_names_display(clients_names)  # update client names display


# Return the index of the current client in the list of clients
def get_client_index(client_list, curr_client):
    idx = 0
    for conn in client_list:
        if conn == curr_client:
            break
        idx = idx + 1

    return idx


# Update client name display when a new client connects OR
# When a connected client disconnects
def update_client_names_display(name_list):
    tkDisplay.config(state=tk.NORMAL)
    tkDisplay.delete('1.0', tk.END)

    for c in name_list:
        tkDisplay.insert(tk.END, c+"\n")
    tkDisplay.config(state=tk.DISABLED)


window.mainloop()
"""