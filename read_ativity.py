import os,re

# print(result.read(1024))
# 返回的结果是一个<class 'os._wrap_close'>对象，需要读取后才能处理
def execCmd(cmd):  
    r = os.popen(cmd)  
    text = r.read(1024)  
    r.close()  
    return text  

def apktool_d(apk,name):
	apktool="java -jar Apktool_2.5.0.jar d "+apk+' -o F:/apk/'+name
	print(apktool)
	r = os.popen(apktool)
	text = r.read(1024) 
	r.close()
	return text 

def apktool_b(apk_mkdir):
	apktool="java -jar Apktool_2.5.0.jar b "+apk_mkdir+" -o F:/apk/wow.apk"
	print(apktool)
	r = os.popen(apktool)
	text = r.read(1024) 
	r.close()
	return text 	
	
def writeFile(filename, data):  
    f = open(filename, "w")  
    f.write(data)  
    f.close()  

if __name__ == '__main__':  
    cmd = "adb -s fea4b345 shell dumpsys activity top "  
    # cmd1 = "adb devices "  
    # result1 = execCmd(cmd1) 
    # cmd = "adb -s fea4b345 install F:/apk/植物大战僵尸2_2.6.3.apk "  
    # result = execCmd(cmd) 
    pat1 = "ACTIVITY (.*?)/. "  
    # pat2 = "IP Address[\. ]+: ([\.\d]+)"  
    # ACTIVITY = re.findall(pat1, result)      # 找到ACTIVITY   
    # IP = re.findall(pat2, result)[0]        # 找到IP  
    # print("MAC=%s, IP=%s" %(MAC, IP))  
    # print(result)
    # write=writeFile('1.txt',result)
    # apk='F:/apk/植物大战僵尸2_2.6.3.apk'
    name='zsxq'
    apk='F:/apk/'+name+'.apk'
    apk_mkdir='F:/apk/'+name
    result_apktool=apktool_d(apk,name)

    # result_apktool=apktool_b(apk_mkdir)
    print(result_apktool)

    # print(os.popen(cmd).read(1024))
    print('success!')

