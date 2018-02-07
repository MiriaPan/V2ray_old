# -- coding:utf-8--

import core.shatime
import os
import shutil

xlj = os.getcwd()

print('\nV2ray 启动器V0.3'.decode("utf-8").encode("gb2312"))

timepy = core.shatime.times()

lj = 'core/time.txt'

try:
	with open(lj) as x:
		zc = x.read()
except:
	print('V2Ray 未被激活！'.decode("utf-8").encode("gb2312"))
	print('请您输入购买的密钥，用于激活V2Ray'.decode("utf-8").encode("gb2312"))
	my = raw_input('密钥：'.decode("utf-8").encode("gb2312"))
	myjs = core.shatime.now_times()
	if my == myjs:
		core.shatime.put_time()
		print('V2Ray 已成功激活！'.decode("utf-8").encode("gb2312"))
		print('请您重新启动'.decode("utf-8").encode("gb2312"))
		raw_input('输入回车键继续'.decode("utf-8").encode("gb2312"))
	else:
		print('密钥输入错误！'.decode("utf-8").encode("gb2312"))
		print('请您重新启动程序！'.decode("utf-8").encode("gb2312"))
		raw_input('输入回车键继续'.decode("utf-8").encode("gb2312"))
else:
	if timepy in zc:
		try:
			print('V2Ray 已成功启动！'.decode("utf-8").encode("gb2312"))
			os.system(xlj + '\core\core\\v2ray.exe')
			raw_input('按下回车键继续'.decode("utf-8").encode("gb2312"))
		except:
			print('错误:未能成功启动 V2Ray请检查文件路径与文件是否存在！'.decode("utf-8").encode("gb2312"))
			raw_input('按下回车键继续'.decode("utf-8").encode("gb2312"))
	else:
		print('V2Ray 启动失败！'.decode("utf-8").encode("gb2312"))
		print('V2Ray 密钥过期！'.decode("utf-8").encode("gb2312"))
		print('请重新输入新密钥激活！'.decode("utf-8").encode("gb2312"))
		my = raw_input('密钥：'.decode("utf-8").encode("gb2312"))
		myjs = core.shatime.now_times()
		if my == myjs:
			core.shatime.put_time()
			print('V2Ray 已成功激活！'.decode("utf-8").encode("gb2312"))
			print('请您重新启动'.decode("utf-8").encode("gb2312"))
			raw_input('输入回车键继续'.decode("utf-8").encode("gb2312"))
		else:
			print('密钥输入错误！'.decode("utf-8").encode("gb2312"))
			print('请您重新启动程序！'.decode("utf-8").encode("gb2312"))
			raw_input('输入回车键继续'.decode("utf-8").encode("gb2312"))
		
		




