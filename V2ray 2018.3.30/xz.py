import paramiko
import os
import sys

gzlj = os.getcwd()
jdlj_1 = os.path.join(gzlj,"download.py")
jdlj_2 = os.path.join(gzlj,"del.py")

serverlj_1 = "/zzz/V2BT/Xconfig.json" 
serverlj_2 = "/zzz/V2BT/Xgeosite.dat" 
serverlj_3 = "/zzz/V2BT/Xv2ctl.exe" 
serverlj_4 = "/zzz/V2BT/Xv2ray.exe" 
serverlj_5 = "/zzz/V2BT/Xwv2ray.exe" 
serverlj_6 = "/zzz/V2BT/Xgeoip.dat" 
serverlj_7 = "/zzz/V2BT/Xreadme.md" 
serverlj_8 = "/zzz/V2BT/Xv2ctl.exe.sig" 
serverlj_9 = "/zzz/V2BT/Xv2ray.exe.sig" 
serverlj_10 = "/zzz/V2BT/Xwv2ray.exe.sig" 
serverlj_11 = "/zzz/V2BT/Xsm.txt"

bdlj_1 = os.path.join(gzlj,"config.json")
bdlj_2 = os.path.join(gzlj,"geosite.dat")
bdlj_3 = os.path.join(gzlj,"v2ctl.exe")
bdlj_4 = os.path.join(gzlj,"v2ray.exe")
bdlj_5 = os.path.join(gzlj,"wv2ray.exe")
bdlj_6 = os.path.join(gzlj,"geoip.dat")
bdlj_7 = os.path.join(gzlj,"readme.md")
bdlj_8 = os.path.join(gzlj,"v2ctl.exe.sig")
bdlj_9 = os.path.join(gzlj,"v2ray.exe.sig")
bdlj_10 = os.path.join(gzlj,"wv2ray.exe.sig")
bdlj_11 = os.path.join(gzlj,"说明.txt")

try:
	transport = paramiko.Transport(('60.205.221.103', 22))
	transport.connect(username='root', password='LUCYCOREx2002')
	sftp = paramiko.SFTPClient.from_transport(transport)
except:
	print("服务器连接失败！")
	input("按下回车退出程序")
	sys.exit()

print("正在下载V2ray")
print("由于传输方式的限制")
print("下载速度会受到影响")
print("这可能需要5分钟时间")
try:
	sftp.get(serverlj_1,bdlj_1)
	sftp.get(serverlj_2,bdlj_2)
	sftp.get(serverlj_3,bdlj_3)
	sftp.get(serverlj_4,bdlj_4)
	sftp.get(serverlj_5,bdlj_5)
	sftp.get(serverlj_6,bdlj_6)
	sftp.get(serverlj_7,bdlj_7)
	sftp.get(serverlj_8,bdlj_8)
	sftp.get(serverlj_9,bdlj_9)
	sftp.get(serverlj_10,bdlj_10)
	sftp.get(serverlj_11,bdlj_11)
	
except:
	print("下载失败！")
	input("按下回车退出程序")
	sys.exit()
	
os.system(jdlj_2)
