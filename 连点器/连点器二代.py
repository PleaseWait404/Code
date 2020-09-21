import pyautogui
import time
import sys

print('本连点器出自陈玉洁之手！@陈玉洁')

def 连点():
    #玩家选择↓
    k = int(input('左键还是右键，按1或2:'))
    e = float(input('次数：'))
    s = float(input('等待：'))
    
    #提示玩家不要玩火↓
    if s < 0.005:
        z = int(input('你输入的指数过小，请考虑您的计算机是否能承受,1或2:'))
        if z == 1:
            print('准备电脑爆炸吧！')
        else:
            连点()
            
        #开始部分↓
    if k == 1:
        b = 0
    if k == 2:
        b = 1
    try:
        i = 0
        while i<e:
            time.sleep(s)
            if b == 0:
                pyautogui.doubleClick()  
            if b == 1:
                pyautogui.rightClick()
            i+=1
    except KeyboardInterrupt:
        sys.exit(0)
        
    print('..........已完成任务.........')
    input()
    连点() #妙啊~,巧用函数，直接无限循环~芜湖~

time.sleep(1)
#启动↓
连点()

