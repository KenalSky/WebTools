import requests
from bs4 import BeautifulSoup
import re
import urllib.request
import socket
import math
import time
import datetime
import os
import sys

def report_hook(count, block_size, total_size):
  btrate = 100.0 * count * block_size/ total_size
  if btrate > 100.0:
    btrate =100.0
  print( "\r",'%02d%%'%(btrate) , end= " ")


if __name__ == "__main__":
  print("\nDownloadYizhiboTool Alpha v1.30    \nAuthor:@Kenal_Sky  ©2020  \n")
  url = input("一直播下载网址格式示例:http://www.yizhibo.com/l/IgNfGeZabgI2egsR.html\n正在直播的网址会等到直播结束后自动开始下载.\n输入网址按回车开始下载:")  
  headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
  req = urllib.request.Request(url, headers=headers)

  timesi = 1
  while True:
    timesi = timesi + 1
    page = urllib.request.urlopen(req).read()
    page = page.decode('utf-8')
    # print(page)
    link = re.findall("http://alcdn.hls.xiaoka.tv.*?.m3u8", page)
    if link:
      resrc = link[0][:-10]
      print("\n已获取视频地址:\n" + resrc + "*.ts\n即将开始下载...")
      break
    else:
      for i in range(10):
        print("\r","直播尚未结束!"+str("%02d" %(10-i)) + "秒后第" + str(timesi) + "次重试...", end="")
        time.sleep(1)

  if not os.path.exists("Temp/"):
    os.mkdir("Temp/")
  exec_str = r'del ' + r'Temp\*.ts '
  os.system(exec_str) # 先清理的文件
  i = 0
  print("若长时间无响应,重启程序再试.")
  while True:
    dsrc = resrc + str(i) + ".ts"
    # print (dsrc)
    print("\r","     " + str(i) + ".ts is downloading...", end = "")
    if not os.path.exists("Temp/"):
      os.mkdir("Temp/")
    try:
      urllib.request.urlretrieve(dsrc, "Temp/" + str(i) + ".ts",  reporthook=report_hook)
    except:     #无法连接当前视频片段，则判定下载完毕。
      print("\r","共下载了" + str(i) + "个文件.                          ", )
      print("All fragments have downloaded!")
      break
    else:
      print(str(i) + ".ts has downloaded.      " )
    i=i+1
  # print (i)

  try:
    path = "Temp/"
    for file in os.listdir(path) :  #文件名补零
      name = file.split('.')[0]
      length = len(str(i-1))
      ld = "%0" + str(length) + "d"
      os.rename(os.path.join(path, file), os.path.join(path, ld % int(name) + ".ts"))

    print("\nStart merging...")
    #获取直播开始时间
    starttime = re.findall("直播开始时间.{16}", page)
    starttime = re.sub(r"\D","", starttime[0])
    
    filename = "Done\\"  + starttime
    # for x in range(1,10):
    #   filename = "Done\\"  + starttime + str('%02d' % x)
    #   if not os.path.exists(filename + ".ts"):
    #     break
    path = os.path.abspath(os.curdir) + "\\Done"
    
    print(path + "\\" + starttime + ".ts")
    if os.path.exists(filename + ".ts"):
      print("该文件(" + path + "\\" + starttime + ".ts" + ")已存在,请注意备份您的文件!" )
      while True:
        ifcover = input("是否覆盖(y覆盖当前同名文件,n退出程序)(y/n)?")
        if ifcover == "y":
          break
        else:
          if ifcover == "n":
            sys.exit(0)
          else:
            print("非法输入!")

    if not os.path.exists("Done/"):
      os.mkdir("Done/")
    # print(filename)
    exec_str = r'copy /b ' + r'Temp\*.ts ' + filename + '.ts'
    # print(exec_str)
    os.system(exec_str) # 使用cmd命令将资源整合
    exec_str = r'del ' + r'Temp\*.ts '
    os.system(exec_str) # 删除原来的文件
  except:
    print("Merge failed.请重启软件再试!")
  else:
    os.system("explorer.exe %s" % path)
    print("下载成功!请在该目录下查看(文件名为该直播的开始时间):\n" + path + "\\" + starttime + ".ts")
    
  input("\nPress any key to exit.")