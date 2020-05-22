import wmi
import os
import time
import sys
from threading import Timer

global Timeout
Timeout = False
def iftimeout():
    global Timeout
    Timeout = True
    print("\n您已超时,输入任意内容退出.")

if __name__ == "__main__":
    
    c = wmi.WMI()
    mbid = c.Win32_BaseBoard()[0].SerialNumber.strip()      #获取主板序列号
    cpuid = c.Win32_Processor()[0].ProcessorId.strip()      #获取CPU序列号 
    coid = mbid + cpuid
    cokey = ""
    for co in coid:
        ikey = (int(ord(co))*13) % 7
        cokey = cokey + str(ikey)
    # print(cokey)                                                             #生成通行证字符串

    iflicense = False
    if os.path.exists("Temp/license.alan"):                                  #若通行证文件存在
        with open("Temp/license.alan","r",encoding='utf-8') as f:
            content = f.read()
        if content == cokey:                                                 #通行证匹配成功
            iflicense = True
            print("pass")
        else:                                                                #通行证文件存在但不匹配
            print("license error")
            for i in range(5):
                print("\r", str("%01d" %(5-i)) + "秒后进行答题认证...", end="")
                time.sleep(1)
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
        ans5 = str(input("\n5.您有" + str(timecount) + "秒钟时间回答此问题，超时后需重启程序再试.\n你配看阿兰的直播吗(提示:答案唯一,共三个字)?:"))    
        t.cancel()
        if Timeout ==True:
            sys.exit(0)
        
        answer = ans1 + ans2 + ans3 + ans4 + ans5
        print(answer)
        if answer == "1987-07-25f兰草宝宝关你P事我不配":
            print("\n恭喜您全部回答正确")
            iflicense = True
            with open("Temp/license.alan", "w", encoding='utf-8') as f:         #写入通行证
                f.write(cokey)
                f.close()
        else:
            print("\n您至少有一道题目回答错误或未按规范回答.")
            time.sleep(5)
            sys.exit(0)
        

        
