import sys
from client.ChaserClient import ChaserClient
from client.ChaserSimpleClient import ChaserSimpleClient
client = ChaserSimpleClient("127.0.0.1", 2010, "佐藤")

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
