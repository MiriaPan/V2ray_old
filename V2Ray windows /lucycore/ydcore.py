import os
import shutil

bdlj = os.getcwd()
mblj = r'C:\python\sun36x64'
v2jdlj = os.path.join(bdlj,r'lucycore','v2lucy')


def corecopy():
	shutil.copytree(v2jdlj,mblj)


def de():
	shutil.rmtree(v2jdlj)

def v2lj():
	lj = r'C:\python\sun36x64\v2ray.exe'
	return lj
