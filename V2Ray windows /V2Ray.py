# -- coding:utf-8--
import lucycore.mokuaiku
import lucycore.ydcore
import os
import sys

ljx = os.getcwd()
jdlj = os.path.join(ljx,'lucycore','sym.txt')

print('\nV2Ray启动器 V1.0')
print('作者：呵呵十三太\n')



try:
	with open(jdlj) as zc:
		time = zc.read()
except:
	try:
		lucycore.ydcore.corecopy()
	except:
		pass
	else:
		print('V2Ray 安装完成！')

	try:
		lucycore.ydcore.de()
	except:
		pass
	else:
		print('V2Ray 变量环境调试完成！')
	print('\nV2Ray 未被激活！')
	print('请输入您购买的密钥 用于激活V2Ray')
	my = input('密钥：')
	corez = lucycore.mokuaiku.corez()
	if my == corez:
		print('V2Ray 激活成功！')
		print('请您重新启动程序！')
		lucycore.mokuaiku.put_time()
		input('按下回车关闭程序')
		sys.exit()
	else:
		print('V2Ray 激活密钥输入错误！')
		print('请您重启程序 重新输入！')
		input("按下回车关闭程序")
		sys.exit()
else:
	timeyz = lucycore.mokuaiku.jznow_time()
	if timeyz in time:
		v2lj = lucycore.ydcore.v2lj()
		try:
			print('V2Ray 启动！')
			os.system(v2lj)
		except:
			print('V2Ray 启动失败！')
			print('无效路径')
	else:
		print('您的密钥已过期！')
		print('请您输入新的密钥 用于激活V2Rray')
		my = input('密钥：')
		corez = lucycore.mokuaiku.corez()
		if my == corez:
			print('V2Ray 激活成功！')
			print('请您重新启动程序！')
			lucycore.mokuaiku.put_time()
			input('按下回车关闭程序')
			sys.exit()
		else:
			print('V2Ray 激活密钥输入错误！')
			print('请您重启程序 重新输入！')
			input("按下回车关闭程序")
			sys.exit()





