# coding: utf-8
import commands
import socket


def get_localip():
    ip = socket.gethostbyname(socket.gethostname())
    return ip


def windows():
    print 'windows'


def Linux():
    key_map = {
        'Size': 'ram',
    }

    shell_command = 'dmidecode -q -t 17 2> /dev/null'
    status, result = commands.getstatusoutput(shell_command)
    if status != 0:
        raise Exception('command is exception')
    else:
        segment = {}
        devices = result.split('Memory Device')[1]
        devices = devices.strip('\n')
        devices = devices.strip('\t')
        lines = devices.split('\n\t')
        for line in lines:
            if len(line.split(':')) > 1:
                key, value = line.split(':')
            else:
                key = line.split(':')[0]
                value = ''
            if key_map.has_key(key):
                if key == 'Size':
                    segment[key_map['Size']] = value

        else:
            segment['ip'] = get_localip()

    return segment


if __name__ == '__main__':
    print Linux()


"""

1. 客户端包含本地ip像服务器发起请求
2. 获取uuid存入本地
3. 并把更新数据更新到server

status, result = commands.getstatusoutput('http  http://127.0.0.1:8000/api/client/username=6/')

dic = json.loads(ss)[0]


"""