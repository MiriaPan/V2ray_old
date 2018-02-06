# -- coding:utf-8--

import core.shatime
import os
import shutil

print('\nV2ray 启动器V0.1')

timepy = core.shatime.times()

lj = '/Users/lucy/Desktop/V2ray/core/time.txt'

try:
	with open(lj) as x:
		zc = x.read()
except:
	print('V2Ray 未被激活！')
	print('请您输入购买的密钥，用于激活V2Ray')
	my = raw_input('密钥：')
	myjs = core.shatime.now_times()
	if my == myjs:
		core.shatime.put_time()
		print('V2Ray 已成功激活！')
		print('请您重新启动')
	else:
		print('密钥输入错误！')
		print('请您重新启动程序！')
else:
	if timepy in zc:
		print('V2Ray 已成功启动！')
		os.system('/Users/lucy/Desktop/V2ray/core/core/v2ray')
	else:
		print('V2Ray 启动失败！')
		print('V2Ray 密钥过期！')
		print('请重新输入新密钥激活！')
		my = raw_input('密钥：')
		myjs = core.shatime.now_times()
		if my == myjs:
			core.shatime.put_time()
			print('V2Ray 已成功激活！')
			print('请您重新启动')
		else:
			print('密钥输入错误！')
			print('请您重新启动程序！')
		
		




