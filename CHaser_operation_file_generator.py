import shutil
import os

class CHaserOperationFileGenerator:
    """CHaser競技部門の運営用のファイルを生成するクラス"""

    def __init__(self, user_names_file: str, server_ip: str, is_name_number: bool = False):
        """CHaser競技部門の運営用のファイルを生成するクラス

        これによって生成された競技部門参加者のディレクトリに、各々が作成してきたプログラムを入れることで実行できる

        Parameters
        ----------
        user_names_file : str
            競技部門参加者名の一覧が書かれたファイルのパス
            各参加者毎に改行で区切られているファイルを利用すること

        server_ip : str
            サーバのIPアドレス

        is_name_number : bool
            False: 参加者名をそのままディレクトリ名にする(デフォルト)、
            True: 参加者名の前に番号(3桁)をつけてディレクトリ名にする
                (001_佐藤，002_鈴木，...)
        """
        program_count = 0

        # 参加者名一覧ファイルを読み込み
        with open(user_names_file, mode='r', encoding="utf-8") as f:
            user_names = f.readlines()

        for user_name in user_names:
            user_name = user_name.rstrip('\n')

            # 参加者名がある場合 (改行だけの場合は何もしない)
            if user_name != "":
                program_count += 1

                # 必要なら参加者名の前に番号(3桁)をつける (001_佐藤，002_鈴木，...)
                if is_name_number:
                    folder_name = f'{str(program_count).zfill(3)}_{user_name}'
                else:
                    folder_name = user_name

                # 参加者の名前でディレクトリを作成(すでにある場合は何もしない)
                os.makedirs(f'{folder_name}', exist_ok=True)

                # クライアント実行用のプログラムをディレクトリごとコピー(すでにある場合は上書き)
                shutil.copytree('client', f'{folder_name}/client', dirs_exist_ok=True)
                shutil.copytree('utils', f'{folder_name}/utils', dirs_exist_ok=True)

                # クライアント実行用のプログラムを作成
                cool_client_program = self.__create_client_program(user_name, server_ip, True)
                hot_client_program = self.__create_client_program(user_name, server_ip, False)

                # クライアント実行用のプログラムをファイルに上書き
                with open(f'{folder_name}/client/ChaserFanc_cool.py', mode='w', encoding="utf-8") as f:
                    f.write(cool_client_program)
                with open(f'{folder_name}/client/ChaserFanc_hot.py', mode='w', encoding="utf-8") as f:
                    f.write(hot_client_program)

    @staticmethod
    def __create_client_program(user_name: str, server_ip: str, is_cool: bool):
        """クライアント実行用のプログラムを作成する

        Parameters
        ----------
        user_name : str
            参加者名
        server_ip : str
            サーバのIPアドレス
        isCool : bool
            CoolならTrue, HotならFalse
        """

        if is_cool:
            client_port = 2009
        else:
            client_port = 2010

        client_program = f"""import sys
from client.ChaserClient import ChaserClient
from client.ChaserSimpleClient import ChaserSimpleClient
client = ChaserSimpleClient("{server_ip}", {client_port}, "{user_name}")

TURN_END = '0'

def get_ready():
    return client.get_ready()

def walk_right():
    return client.walk_right()
def walk_down():
    return client.walk_down()
def walk_left():
    return client.walk_left()
def walk_up():
    return client.walk_up()

def put_right():
    return client.put_right()
def put_down():
    return client.put_down()
def put_left():
    return client.put_left()
def put_up():
    return client.put_up()

def look_right():
    return client.look_right()
def look_down():
    return client.look_down()
def look_left():
    return client.look_left()
def look_up():
    return client.look_up()

def search_right():
    return client.search_right()
def search_down():
    return client.search_down()
def search_left():
    return client.search_left()
def search_up():
    return client.search_up()
"""

        return client_program

if __name__ == '__main__':
    user_names_file = "ユーザー名一覧.txt"
    server_ip = '127.0.0.1'

    g = CHaserOperationFileGenerator(user_names_file, server_ip)
