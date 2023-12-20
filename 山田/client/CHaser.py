import socket
import ipaddress
import os
import sys

class Client:
    def __init__(self):
        # self.port = input("ポート番号を入力してください → ")
        # self.name = input("ユーザー名を入力してください → ")[:15]
        # self.host = input("サーバーのIPアドレスを入力してください → ")
        self.port = sys.argv[1]
        self.name = sys.argv[2]
        self.host = sys.argv[3]

        if not self.__ip_judge(self.host):
            os._exit(1)

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.host, int(self.port)))

        print("port:", self.port)
        print("name:", self.name)
        print("host:", self.host)

        self.__str_send(self.name + "\r\n")

    def __ip_judge(self, host):
        try:
            ipaddress.ip_address(host)
        except Exception as e:
            print("IPアドレスの形式に誤りがあります : {0}".format(e))
            return False
        else:
            return True

    def __str_send(self, send_str):
        try:
            self.client.sendall(send_str.encode("utf-8"))
        except:
            print("send error:{0}\0".format(send_str))

    def __order(self, order_str, gr_flag = False):
        try:
            if gr_flag:
                response = self.client.recv(4096)

                if(b'@' in response):
                    pass # Connection completed.
                else:
                    print("Connection failed.")

            self.__str_send(order_str + "\r\n")

            response = self.client.recv(4096)[0:11].decode("utf-8")

            if not gr_flag:
                self.__str_send("#\r\n")

            if response[0] == '1':
                return [int(x) for x in response[1:10]]
            elif response[0] == '0':
                raise OSError("Game Set!")
            else:
                print("response[0] = {0} : Response error.".format(response[0]))
                raise OSError("Response Error")

        except OSError as e:
            print(e)
            self.client.close()
            os._exit(0)

    def get_ready(self):
        return self.__order("gr", True)

    def walk_right(self):
        return self.__order("wr")

    def walk_up(self):
        return self.__order("wu")

    def walk_left(self):
        return self.__order("wl")

    def walk_down(self):
        return self.__order("wd")

    def look_right(self):
        return self.__order("lr")

    def look_up(self):
        return self.__order("lu")

    def look_left(self):
        return self.__order("ll")

    def look_down(self):
        return self.__order("ld")

    def search_right(self):
        return self.__order("sr")

    def search_up(self):
        return self.__order("su")

    def search_left(self):
        return self.__order("sl")

    def search_down(self):
        return self.__order("sd")

    def put_right(self):
        return self.__order("pr")

    def put_up(self):
        return self.__order("pu")

    def put_left(self):
        return self.__order("pl")

    def put_down(self):
        return self.__order("pd")
