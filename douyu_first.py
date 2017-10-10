#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from douyu.chat.room import ChatRoom

import pymysql

mysql_config = {
    'host': '192.168.1.11',
    'port': 3306,
    'user': 'zhang',
    'password': '123456',
    'db': 'Douyu',
    'charset': 'utf8',
}


def on_chat_message(msg):
    name = msg.attr('nn')
    text = msg.attr('txt')
    # print type(name),type(text)
    time = msg.attr('level')
    print name,time
    # mysql_conn = pymysql.connect(**mysql_config)
    # mysql_cursor = mysql_conn.cursor()
    # insert_sql = "insert into danmu_barrage(User_name,User_Barrage)  values (%s,%s)"
    # mysql_cursor.execute(insert_sql,(name,text))
    # mysql_conn.commit()
    # mysql_cursor.close()
    # mysql_conn.close()
def on_dgb(mag):
    """
    赠送礼物
    :param mag:
    :return:
    """
    name = mag.attr('rid')
    print name
def spbc(mag):
    """
    榜单
    :param mag:
    :return:
    """
    user = mag.attr('sn')
    name = mag.attr('gn')
    many = mag.attr('gc')
    room = mag.attr('drid')
    print user,name,many,room
# def run():
#     room = ChatRoom('67373')
#     room.on('chatmsg', on_chat_message)
#     room.knock()
def run():
    room = ChatRoom('67373')
    room.on('spbc', spbc)
    room.knock()

if __name__ == '__main__':
    run()
