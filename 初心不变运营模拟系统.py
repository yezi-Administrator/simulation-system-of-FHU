print("初心不变运营模拟系统\n初心不变 超级管理员 叶子\n保留所有权利")
print("加载模块......")
print("\t初始化日志记录模块......")

try:
    import logging
    运行日志=logging.getLogger("运行日志")
    格式器=logging.Formatter('%(asctime)s %(levelname)-8s %(message)s')
    输出器=logging.FileHandler("运行日志.log")
    输出器.setFormatter(格式器)
    运行日志.addHandler(输出器)
    输出器.setFormatter(格式器)
    运行日志.setLevel(logging.DEBUG)
    运行日志.info("日志记录初始化成功")
    事件日志=logging.getLogger("事件日志")
    格式器=logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    输出器=logging.FileHandler("事件日志.log")
    输出器.setFormatter(格式器)
    事件日志.addHandler(输出器)
    输出器.setFormatter(格式器)
    事件日志.setLevel(logging.DEBUG)
except:
    print("关键错误：缺少日志记录模块 logging，该模块用于支持日志记录功能，请先安装此模块")
finally:
    print("\t日志记录模块加载成功......")
    
def 错误处理(错误原因):
        print("程序遇到了一个严重错误：",错误原因,"，导致其被迫中止")
        print("请跟随以下指导尝试排除故障：")
        print("\t<1>如果您修改过源代码，请尝试访问项目主页下载最新版本")
        print("\t<2>如果报错信息指向日志文件，请确认您的磁盘空间充足，且您有创建文件的权限")
        print("\t<3>如果报错信息指向模块，请运行 pip 重新安装报错模块")
        print("\t<4>如果您下载的版本是非稳定版，请尝试下载最新稳定版")
        print("\t<5>如果您无法解决该问题，请访问 Gihub 项目主页：https://github.com/FHU-yezi/simulation-system-of-FHU/")
        print("\t在其中新建一个 Issues 报告问题，并上传本目录中的 运行日志.log 文件，以方便让我们排查问题")

try:
    pass
except:
    运行日志.critical("缺少必要组件")
    错误处理("缺少必要组件")
else:
    print("\t必要组件加载成功......")
    运行日志.debug("必要组件加载成功")
try:
    from random import random,randint,choice
except:
    运行日志.critical("缺少 random 模块")
    错误处理("缺少 random 模块")
else:
    运行日志.debug("\trandom 模块加载成功")
try:
    from time import time,sleep
except:
    运行日志.critical("缺少 time 模块")
    错误处理("缺少 time 模块")
else:
    运行日志.debug("\ttime 模块加载成功")

print("所有模块加载成功......")
运行日志.info("所有模块加载成功")

print("初始化类......")
运行日志.info("初始化类")

print("初始化基础数值......")######应该取代

随机数=0
运行天数=0
警告次数=0

print("数值初始化成功......")

try:
    class 部门():
        def __init__(self):
            self.人数=0
            self.人员列表=[]
            self.能力=0
        def 部门成员加入(self,编号):
            if 编号 in 人力资源部.群成员列表:
                self.人员列表.append(编号)
                print("操作执行成功！")
            else:
                print("操作执行失败！原因：编号不存在’")
        def 部门成员退出(self,编号):
            if 编号 in 人力资源部.群成员列表 and 编号 in self.人员列表:
                self.人员列表.remove(编号)
                print("操作执行成功！")
            else:
                print("操作执行失败！原因：编号不存在")
        def __str__(self):
            return "一个未定义名称的部门：\n\t人数："+str(self.人数)+"\n\t能力："+str(self.能力)+"\n\t人员列表："+str(self.人员列表)

    class 群组运营部(部门):
        def __str__(self):
            return "群组运营部：\n\t人数："+str(self.人数)+"\n\t能力："+str(self.能力)+"\n\t人员列表："+str(self.人员列表)

    class 人力资源部(部门):
        def __init__(self):
            self.人数=0
            self.人员列表=[]
            self.群成员列表=[]
            self.能力=0
            self.当前群人数=1#人数上限为 500，与真实情况相同
            self.成员编号列表=["0"]
            self.未分配部门人员=[]
        def 群成员加入(self):
            for i in range(500):
                进入=None
                exec("if 用户"+str(i)+".满意度>=60 and 用户"+str(i)+".活跃度>=3 and 用户"+str(i)+".在群中==False and randint(0,11)==1:进入=True",globals())
                if 进入!=None:
                    exec("用户"+str(i)+".在群中=True",globals())
                    exec("self.群成员列表.append(i)",globals())
                    exec("self.当前群人数+=1",globals())
                    print("有 1 个成员进入了初心不变，他的成员编号是",i,"。")
        def 群成员退出(self):
            for i in range(500):
                退出=None
                exec("if 用户"+str(i)+".满意度>=30 and 用户"+str(i)+".活跃度<=5 and 用户"+str(i)+".在群中==True and randint(0,11)==1:进入=True",globals())
                if 退出!=None and i !=0:
                    exec("用户"+str(i)+".在群中=False",globals())
                    exec("self.群成员列表.remove(i)",globals())
                    exec("self.当前群人数-=1",globals())
            print("有 1 个成员退出了初心不变，他的成员编号是",i,"。")
        def __str__(self):
            return "人力资源部：\n\t人数："+str(self.人数)+"\n\t能力："+str(self.能力)+"\n\t人员列表："+str(self.人员列表)+"\n\t当前群人数："+str(self.当前群人数)

    class 文案宣传部(部门):
        def __init__(self):
            self.人数=0
            self.人员列表=[]
            self.能力=0
            self.文案列表=[]
            self.当前进行文案="无"
            self.总文案数量=0
            self.当前文案进度=0
        def 新文案(self):
            self.当前进行文案=input("请输入文案名称：")
            self.文案列表.append(文案名称)
            self.总文案数量+=1
            print("名为",文案名称,"的文案已成功创建！")
        def 文案处理(self):
            self.当前文案进度+=self.能力
            print("名为",self.当前进行文案,"的文案进度增加了",self.能力,"点")
        def 文案完成度检测(self):
            if self.当前进行文案=="":
                print("您当前没有文案，请先创建文案！")
            elif self.文案完成度>=100:
                文案质量=randint(0,101)
                print("您完成了一篇新的文案，其质量为",文案质量,"，全体成员活跃度与满意度上升！")
                for i in range(500):
                    exec("用户"+i+".活跃度+=int(文案质量/10)",globals())
                    exec("用户"+i+".满意度+=文案质量",globals())
                    self.当前进行文案="无"
                    self.当前文案进度=0
        def __str__(self):
            return "文案宣传部：\n\t人数："+str(self.人数)+"\n\t能力："+str(self.能力)+"\n\t人员列表："+str(self.人员列表)+"\n\t当前进行文案："+str(self.当前进行文案)+"\n\t当前文案进度："+str(self.当前文案进度)

    class 舆情分析部(部门):
        def __init__(self):
            self.人数=0
            self.人员列表=[]
            self.能力=0
            self.舆情事件进行中=False
            self.当前进行舆情事件编号=0
            self.舆情事件等级="无"
            self.舆情事件产生者="无"
            self.总舆情事件数量=0
            self.舆情事件编号列表=[]
        def 新舆情事件(self):
            if len(人力资源部.群成员列表)!=0:
                self.舆情事件产生者=choice(人力资源部.群成员列表)#随便选一个人中招
                self.舆情事件进行中=True
                self.总舆情事件数量+=1#舆情数量+1
                self.当前舆情事件编号=randint(0,501)#随机产生编号
                while True:#判断编号是否存在于列表中
                    if (self.当前舆情事件编号 in self.舆情事件编号列表)==False:
                        self.舆情事件编号列表.append(self.当前舆情事件编号)
                        break
                    else:
                        self.当前舆情事件编号=randint(0,501)
                if self.舆情分析部能力==0:
                    self.舆情事件等级="重要"
                elif self.舆情分析部能力<=5:
                    self.舆情事件等级="一般"
                elif self.舆情分析部能力<=10:
                    self.舆情事件等级="微弱"
                elif self.舆情分析部能力>10:
                    self.舆情事件等级="微不足道"
                print("产生了一个新的舆情事件，该事件的编号为",当前舆情事件编号,"，该事件是由",舆情事件产生者,"产生的。该事件的等级为：",舆情事件等级,"\n该事件导致成员加入概率降低了",本次buff)
        def 舆情事件处理(self):#这里还有一些 bug
            回答=""
            while True:
                回答=input("请选择您要进行的操作：\n<1>发布声明\n<2>不予理睬\n<3>停止运营")
        def __str__(self):
            return "舆情分析部：\n\t人数："+str(self.人数)+"\n\t能力："+str(self.能力)+"\n\t人员列表："+str(self.人员列表)+"\n\t当前舆情事件状态："+str(self.舆情事件进行中)+"\n\t当前舆情事件产生者："+str(self.舆情事件产生者)

    运行日志.debug("初始化部门类成功")

    class 用户():
        def __init__(self,编号):
            self.编号=编号
            self.满意度=randint(30,71)
            self.活跃度=randint(0,11)
            self.在群中=False
    运行日志.debug("初始化用户类成功")

    class 管理组():
        def __init__(self):
            self.人数=0
            self.人员列表=[]
except:
    运行日志.critical("初始化类失败")
    错误处理("初始化类失败")
else:
    print("初始化类成功......")
    运行日志.info("初始化类成功")

运行日志.info("初始化对象")

群组运营部=群组运营部()
人力资源部=人力资源部()
文案宣传部=文案宣传部()
舆情分析部=舆情分析部()
运行日志.debug("初始化部门对象成功")

try:
    for i in range(500):
        exec("用户"+str(i)+"=用户("+str(i)+")")
except:
    运行日志.critical("初始化对象失败")
    错误处理("初始化对像失败")
else:
    运行日志.info("初始化对象成功")
    print("初始化对象成功......")

print("初始化函数......")
#函数初始化开始

def 用户操作():
    回答=input("请选择您的操作：\n\t<1>查看运营情况\n\t:")
    if 回答=="1": 
        print(群组运营部)
        print(文案宣传部)
        print(舆情分析部)
        print(人力资源部)
        input("按下 Enter 键继续")
        运行日志.debug("用户查看了运营情况")
    else:
        print("您跳过了查询")

def 结束(原因):
    print("您结束了长达",运行天数,"个虚拟天的初心之旅，因为",原因,"。")
    print("但是，初心不变的种子仍在，它将重新启动，再次开始在这个神秘莫测的环境中进化，欢迎您再次使用。")
    运行日志.info("结束")
    input("按下 Enter 键退出......")
    exit()
    
#函数初始化结束
print("函数初始化成功......")
print("即将开始模拟......")
sleep(1)
#主程序
while True:
    运行天数+=1
    print("今天是第",运行天数,"天")
    if randint(0,11)<=3:
        舆情分析部.新舆情事件()
        运行日志.debug("触发新舆情事件")
    if randint(0,11)<=5:
        人力资源部.群成员加入()
        运行日志.debug("触发成员加入事件")
    if randint(0,11)<=5:
        人力资源部.群成员退出()
        运行日志.debug("触发成员退出事件")
    if 舆情分析部.舆情事件进行中==True:
        舆情分析部.舆情事件处理()
        运行日志.debug("触发舆情处理事件")
    用户操作()
    if 人力资源部.当前群人数<=10:
        警告次数+=1
        print("警告：人数不足！（如连续出现此警告 10 次将结束）")
        运行日志.info("触发人数不足事件")
    else:
        警告次数=0
        运行日志.debug("警告次数归零")
    if 警告次数>=10:
        结束("人数不足")
