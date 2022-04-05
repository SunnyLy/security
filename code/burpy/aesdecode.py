# coding:utf-8
import re
import base64
import hashlib

import frida


class Burpy:
    """
    类名Burpy不变，文件名可以根据要Hook的场景来变，也可以多个Hook函数放一个js文件里面
    """

    def __init__(self):
        device = self._get_android_usb_device()
        pid = device.spawn("com.ese.http")
        self.abcd = device.attach(pid)
        device.resume(pid)
        self.rpc = self.load_rpc()

    @staticmethod
    def _get_android_usb_device():
        """
        获取连接的手机
        :return:
        """
        for x in frida.get_device_manager().enumerate_devices:
            if "Local Socket" in x.name:
                return x

    def load_rpc(self):
        """
        加载js脚本
        :return:
        """
        with open("D:\\workspace\\git\\Security\\security\\code\\burpy\\aesdecode2.js") as f:
            my_script = self.abcd.create_script(f.read())
            my_script.load()
        return my_script.exports

    def encrypt(self, header, body):
        """
        自动加密示例
        :param header: 请求头
        :param body: 请求体
        :return:
        """
        if body.startswith('{'):  # 请求体是json
            body = eval(body)
            print(body)
            password = body["password"]
            username = body["username"]
            # 然后调用js中的方法进行加密处理
            password = self.rpc.enc(password)
            username = self.rpc.enc(username)
            # 再将修改后的值放到json中
            body["password"] = password
            body["username"] = username
            body = str(body).replace("\'", "\"")
        else:
            body = self.rpc.enc(body)

        return header, body


def main(self, header, body):
    print
    "head:", header
    print
    "body:", body
    return header, body


def processor(self, payload):
    return payload + "burpyed"
