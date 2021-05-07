import sys
import frida

jscode = """ 
    Java.perform(function(){  
        var MainActivity = Java.use('top.q0o0p.q0o0p_six.MainActivity'); //获得MainActivity类
         MainActivity.onClick.implementation = function(){ //Hook testFrida函数，用js自己实现
            send('Statr! Hook!'); //发送信息，用于回调python中的函数
            return 'wow q0o0p wow!' //劫持返回值，修改为我们想要返回的字符串
        }
    });
"""

def on_message(message,data): #js中执行send函数后要回调的函数
    print(message)

process = frida.get_remote_device().attach('top.q0o0p.q0o0p_six') #得到设备并劫持进程com.example.testfrida（该开始用get_usb_device函数用来获取设备，但是一直报错找不到设备，改用get_remote_device函数即可解决这个问题）
script = process.create_script(jscode) #创建js脚本
script.on('message',on_message) #加载回调函数，也就是js中执行send函数规定要执行的python函数
script.load() #加载脚本
sys.stdin.read()