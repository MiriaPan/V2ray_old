import paramiko
import os
import sys

gzlj = os.getcwd()
jdlj_1 = os.path.join(gzlj,"download.exe")
jdlj_2 = os.path.join(gzlj,"del.exe")

print("正在连接服务器...")
try:
	transport = paramiko.Transport(('60.205.221.103', 22))
	transport.connect(username='root', password='LUCYCOREx2002')
	sftp = paramiko.SFTPClient.from_transport(transport)
except:
	print("服务器连接失败！请检查网络连接！")
	input("按下回车退出程序")
	sys.exit()

print("正在拷贝下载目录")
print("这可能需要3分钟时间")
try:
	sftp.get('/zzz/az/xz.exe', jdlj_1)
	sftp.get('/zzz/az/sc.exe', jdlj_2)
except:
	print("下载失败！")
	input("按下回车退出程序")
	sys.exit()
	
print("正在启动下载主体")
try:
	os.system(jdlj_1)
except:
	print("下载核心启动失败！")
	input("按下回车退出程序")
	sys.exit()

transport.close()
