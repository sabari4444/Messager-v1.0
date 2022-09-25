import socket
import threading
import pickle
import time


class StartServer:

    def __init__(self):
        # Constants
        self.old_msg = None
        self.msg = None
        self.server = None
        self.addr = None
        self.client = None
        self.IP = "70.70.70.6"
        self.PORT = 8080
        self.FORMAT = "utf-8"
        self.clients_list = []
        self.lis = {}
        self.all_messages = []
        self.assign_protocol()

    # Assigning The Protocol For The Server
    def assign_protocol(self):

        try:
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        except Exception as e:
            print(e)
            quit()

        finally:
            print("Assigned The Protocol For The Server...")
            self.bind()

    # Binding the Protocol To a Server IP
    def bind(self):

        try:
            self.server.bind((self.IP, self.PORT))
            self.server.listen(50)

        except Exception as e:
            print(e)
            quit()

        finally:
            print(f'The Server is Running On {self.IP}:{self.PORT}')
            self.accepting_client()

    # Waiting For Client TO Connect
    def accepting_client(self):

        while True:
            self.client, self.addr = self.server.accept()
            print(f'[{self.addr} has Connected]')
            self.clients_list.append(self.client)
            self.t0 = threading.Thread(target=self.handling_client, args=(self.client, self.addr,))
            self.t0.start()

    # Receive Messages From Client
    def handling_client(self, client, addr):

        self.lis[addr] = 0
        t2 = threading.Thread(target=self.check_status, args=(addr, client))    
        t2.start()
        while True:
            try:
                self.msg = client.recv(2048)
            except Exception as e:
                print(e)
                break
            msg = pickle.loads(self.msg)
            if msg[3] == 'class:ping':
                no_msg = self.lis[addr]
                no_msg += 1
                self.lis[addr] = no_msg

            else:
                self.all_messages.append(msg)
                print(msg)

    # Receiving Ping From Client
    def check_status(self, client_name, client_data):

        length = 0
        n = 0
        while True:
            if length != self.lis[client_name]:
                length = self.lis[client_name]
                self.reply_ping(client_data)

            else:
                if n == 2:
                    print(f'[Disconnected] {client_name}')
                    self.lis.pop(client_name)
                    self.clients_list.remove(client_data)
                    print(f'[Active Connections] {len(self.lis)}')
                    break

                else:
                    n += 1
            time.sleep(3)

    def reply_ping(self, client):
        if self.old_msg != len(self.all_messages):
            msg = self.all_messages[self.old_msg:]
            for i in msg:
                i[3] = 'class:ping_msg'

            data = pickle.dumps(msg)
            try:
                for i in self.clients_list:
                    i.send(data)
            except Exception as e:
                print(e)
                quit()
            self.old_msg = len(self.all_messages)
        else:
            pass


server = threading.Thread(target=StartServer)
server.start()
