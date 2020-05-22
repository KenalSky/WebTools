import requests
import re
import urllib.request
import socket
import math
import time
import datetime
import os
import sys
import wmi
from threading import Timer

global Timeout
Timeout = False
def iftimeout():
    global Timeout
    Timeout = True
    print("\n您已超时,输入任意内容按回车退出.")

def report_hook(count, block_size, total_size):
  btrate = 100.0 * count * block_size/ total_size
  if btrate > 100.0:
    btrate =100.0
  print( "\r",'%02d%%'%(btrate) , end= " ")


if __name__ == "__main__":
  iflicense = False
  ifgeturl = False

  print("\nDownloadYizhiboTool    Alpha v1.3126 for alan locked   \nAuthor:@Kenal_Sky   ©2020  \n\n免责声明:对于不当转载或使用本程序而引起的民事纷争,行政处理或其他损失,本人不承担责任.\n警告:严禁分享本工具中相关问题的答案.下载有关[real阿兰]的视频后请勿分享,传播.\n")
  url = input("一直播下载网址格式示例:http://www.yizhibo.com/l/IgNfGeZabgI2egsR.html\n正在直播的网址会等到直播结束后自动开始下载.输入错误地址程序将自动退出.\n输入网址按回车开始下载:")  
  headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
  req = urllib.request.Request(url, headers=headers)
  page = urllib.request.urlopen(req).read()
  page = page.decode('utf-8')
  yiid = re.findall("<title>.*?-一直播</title>", page)
  yiidname = yiid[0][7:-12]
  print("\n您正在试图下载[" + yiidname + "]的一直播")
  if yiid[0][7:-12] == "real阿兰":
    # print("is alan")
    #生成通行证字符串
    c = wmi.WMI()
    mbid = c.Win32_BaseBoard()[0].SerialNumber.strip()      #获取主板序列号
    cpuid = c.Win32_Processor()[0].ProcessorId.strip()      #获取CPU序列号 
    coid = mbid + cpuid
    cokey = ""
    for co in coid:
      ikey = (int(ord(co))*13) % 7
      cokey = cokey + str(ikey)
    # print(cokey) 
    if os.path.exists("Temp/license.alan"):                                  #若通行证文件存在
      with open("Temp/license.alan","r",encoding='utf-8') as f:
        content = f.read()
      if content == cokey:                                                 #通行证匹配成功
        iflicense = True
        ifgeturl = True
        print("\n通行证匹配成功!")
    else:                                                                #通行证文件存在但不匹配
      print("\n通行证不存在或无效.\n")
      for i in range(3):
        print("\r", str("%01d" %(2-i)) + "秒后进行答题认证...", end="")
        time.sleep(1)
  else:
    # print("is not alan")
    iflicense = True
    ifgeturl = True
  
  if not iflicense:
    print("\n请先通过答题验证身份.\n\n共5题,全部答对会生成通行证文件,下次启动可直接进入下载.\n请按照答题规范或提示进行答题,每个题目输入答案后按回车确认.")
    input("\n按下回车开始答题-->")
    #第一题
    timecount = 20
    t = Timer(timecount, iftimeout)   
    t.start()
    ans1 = str(input("\n1.您有" + str(timecount) + "秒钟时间回答此问题，超时后需重启程序再试.\n阿兰的生日是(请按此格式输入:2020-02-02):"))    
    t.cancel()
    if Timeout ==True:
      sys.exit(0)
    #第二题
    timecount = 30
    t = Timer(timecount, iftimeout)   
    t.start()
    ans2 = str(input("\n2.您有" + str(timecount) + "秒钟时间回答此问题，超时后需重启程序再试.\n阿兰以下哪个部位有颗明显的痣?\na.左下巴\nb.右下巴\nc.左鼻翼\nd.右鼻翼\ne.左上眼皮\nf.右上眼皮\ng.左下眼皮\nh.右下眼皮\ni.左太阳穴\nj.右太阳穴\n您的答案(单选,请输入小写字母代号):"))
    t.cancel()
    if Timeout ==True:
      sys.exit(0)
    #第三题
    timecount = 15
    t = Timer(timecount, iftimeout)   
    t.start()
    ans3 = str(input("\n3.您有" + str(timecount) + "秒钟时间回答此问题，超时后需重启程序再试.\n阿兰父亲的微博昵称是:"))    
    t.cancel()
    if Timeout ==True:
      sys.exit(0)
    #第四题
    timecount = 20
    t = Timer(timecount, iftimeout)   
    t.start()
    ans4 = str(input("\n4.您有" + str(timecount) + "秒钟时间回答此问题，超时后需重启程序再试.\n(提示:答案唯一,其中某个字用大写P代替)\n向阿兰提问:你为什么总删直播?\n阿兰:"))    
    t.cancel()
    if Timeout ==True:
      sys.exit(0)
    #第五题
    timecount = 20
    t = Timer(timecount, iftimeout)   
    t.start()
    ans5 = str(input("\n5.您有" + str(timecount) + "秒钟时间回答此问题，超时后需重启程序再试.\n你配下载阿兰的直播吗(提示:答案唯一,共三个字)?:"))    
    t.cancel()
    if Timeout ==True:
      sys.exit(0)
    
    answer = ans1 + ans2 + ans3 + ans4 + ans5
    # print(answer)
    if answer == "1987-07-25f兰草宝宝关你P事我不配":
      iflicense = True
      if not os.path.exists('Temp/'):
        os.mkdir('Temp/')
      with open("Temp/license.alan", "w", encoding='utf-8') as f:         #写入通行证
        f.write(cokey)
        f.close()
      print("\n此时阿兰觉得你配下载的她的直播!\n请妥善保管/Temp/license.alan文件,下次可直接下载阿兰的一直播.\n")
      ifgeturl = True
      for i in range(10):
        print("\r", str("%01d" %(9-i)) + "秒后自动开始下载...", end="")
        time.sleep(1)
    else:
      print("")
      for i in range(8):
        print("\r", "您至少有一道题目回答错误或未按规范回答." + str("%01d" %(7-i)) + "秒后自动退出.", end="")
        time.sleep(1)
      sys.exit(0)
        
  if iflicense:               #若通行证合法，进入下载
    if not ifgeturl:
      url = input("一直播下载网址格式示例:http://www.yizhibo.com/l/IgNfGeZabgI2egsR.html\n正在直播的网址会等到直播结束后自动开始下载.输入错误地址程序将自动退出.\n输入网址按回车开始下载:")  
      headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
      req = urllib.request.Request(url, headers=headers)
      page = urllib.request.urlopen(req).read()
      page = page.decode('utf-8')
      # print(page)
    timesi = 1
    while True:
      timesi = timesi + 1
      link = re.findall("http://alcdn.hls.xiaoka.tv.*?.m3u8", page)
      if link:
        resrc = link[0][:-10]
        print("\n已获取视频地址:\n" + resrc + "*.ts\n即将开始下载...\n")
        break
      else:
        for i in range(10):
          print("\r","直播尚未结束!"+str("%02d" %(10-i)) + "秒后第" + str(timesi) + "次重试...", end="")
          time.sleep(1)

    if not os.path.exists("Temp/"):
      os.mkdir("Temp/")
    exec_str = r'del ' + r'Temp\*.ts '
    os.system(exec_str) # 先清理Temp目录下所有.ts文件
    i = 0
    print("\r","Temp/*.ts文件已清理完毕,开始下载碎片文件...\n若长时间无响应,重启程序再试.")
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
        if file[-3:] != ".ts":        #跳过非.ts文件
          continue
        name = file.split('.')[0]
        length = len(str(i-1))
        ld = "%0" + str(length) + "d"
        os.rename(os.path.join(path, file), os.path.join(path, ld % int(name) + ".ts"))

      print("\nStart merging...")
      #获取直播开始时间
      starttime = re.findall("直播开始时间.{16}", page)
      starttime = re.sub(r"\D","", starttime[0])
      
      filename = "Done\\"  + starttime
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
      os.system(exec_str) # 删除Temp目录下所有.ts文件的文件
    except:
      print("Merge failed.请重启软件再试!")
    else:
      os.system("explorer.exe %s" % path)
      print("\n下载成功!请在该目录下查看(文件名为该直播的开始时间):\n" + path + "\\" + starttime + ".ts")

  input("\nInput any key and press Enter to exit.")
  sys.exit(0)