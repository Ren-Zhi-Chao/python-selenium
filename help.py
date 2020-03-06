#! /usr/bin/env python
# -*- coding: utf-8 -*-
kh = '\n      '
jt = '\n   => '

print('\n  【*】 Create Time. 2019-4-21 \n  【*】 个人经历有限，无法做到各个操作系统适配，有兴趣的大手子可以一同完善 (*^_^*)')
print('  【*】 核心宗旨，懒懒懒懒懒懒懒懒懒懒懒懒懒懒懒懒懒懒懒懒懒！ 解放双手~')
print('%s说明'%jt)
print('%s1. 使用Python3 + Selenium进行自动化测试，可做流程、回归测试，生成用户手册等'%kh)
print('%s2. 本程序是基于Python3.7.0编写，检查 python -V 是否是3.X'%kh)
print('%s3. Selenium基于当前最新版本3.141.0进行开发'%kh)

print('%s操作系统'%jt)
print('%s|    操作系统    |    是否适配    |'%kh)
print('      |    Windows     |       √       |')
print('      |     Linux      |       ×       |')
print('      |      Mac       |       ×       |')

print('%s浏览器类型 | 自动化'%jt)
print('%s|   浏览器名称   |   浏览器类型   |  支持自动化测试  |  自动化安装驱动  |   驱动地址'%kh)
print('      |      谷歌      |     CHROME     |        √        |        √        | https://npm.taobao.org/mirrors/chromedriver/')
print('      |      火狐      |     FIREFOX    | 理论支持，未测试 |        ×        | https://npm.taobao.org/mirrors/geckodriver/')
print('      |      欧朋      |     OPERA      | 理论支持，未测试 |        ×        | https://npm.taobao.org/mirrors/operadriver/')
print('      |  屎一般的浏IE  |       IE       |      未测试      |        ×        | http://selenium-release.storage.googleapis.com/index.html')
print('      |     MS Edge    |      EDGE      |      未测试      |        ×        | https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/')
print('      |    PhantomJS   |    PhantomJS   | 理论支持，未测试 |        ×        | http://phantomjs.org/')
print('%s 【说明】IE 浏览器使用Selenium需要设置浏览器的安全项，请自行Google'%kh)
print('%s 【说明】PhantomJS 测试常用浏览器，官方内部问题，暂时已不对其维护，期待有卷土重来之时。'%kh)

print('%s使用方法'%jt)
print('%s1. 进入程序文件目录`X:/QuickPySm`'%kh)
print('%s2. 安装Py依赖，执行 pip install -r requirements.txt '%kh)
print('%s   如果安装/程序运行时出错，打开requirements.txt，将文件中提及的插件卸载： pip uninstall ${name} '%kh)
print('%s3. 浏览器驱动配置 【自动配置直接看3-②】'%kh)
print('%s   ① 手动配置教程 '%kh)
print('%s      1) 查看浏览器版本，根据浏览器版本下载对应的浏览器驱动。(如果驱动版本号与当前浏览器版本不一致时，选择大版本号一致，驱动版本号小编号为小于浏览器版本小编号最为接近的一个)'%kh)
print('            2) 配置环境变量：在环境变量中新建环境变量名BROWSER_DIVER_${浏览器类型}，添加驱动路(所在文件夹层) 【注意：环境变量名大写】')
print('            3) 将 %BROWSER_DIVER_${浏览器类型}% 添加至PATH中')
print('%s   ② 程序配置教程 '%kh)
print('%s      1) 编辑文件 config/config.ini '%kh)
print('               [drive] 项下方添加 type=${浏览器类型}')
print('               [drive] 项下方添加 version=${浏览器版本号} (由于自动检测识别版本号，此时可能会出现选择驱动版本错误问题，如果出现使用上的错误，请移至3-①进行手动安装)')
print('            2) 进入 X:/QuickPySm 目录，执行 python install.py')
print('%s3. 编写测试脚本'%kh)

print('%s其它'%jt)
print('%s1. 自动下载驱动，会安装在install.py同级的目录下，如果想要卸载驱动，删除环境变量配置和该文件夹即可'%kh)
print('%s2. config.ini 文件说明'%kh)
print('%s     ----------------------------------------------------------------------'%kh)
print('           |    属性名称    |     属性等级     |       说明      ')
print('           |---------------------------------------------------------------------')
print('           |     drive      |        1         | 浏览器相关驱动设置')
print('           |      type      |        2         | 浏览器类型(用于打开相应浏览器驱动)')
print('           |     version    |        2         | 浏览器版本(用于自动安装驱动版本)')
print('           |---------------------------------------------------------------------')
print('           |     window     |        1         | 测试弹出的浏览器窗口设置')
print('           |      size      |        2         | 默认打开时窗口大小：max(最大); 100x200(宽100, 高200); 不设置为默认(size这个key不可以删除)')
print('           |    frequency   |        2         | 读取元素时的显示等待时间对应的检测间隔时长，默认0.5s')
print('           |   implicitly   |        2         | 读取元素时的隐式等待时间对应的检测间隔时长，默认为空，不设置值时不使用该设置')
print('           |---------------------------------------------------------------------')
print('           |      file      |        1         | 测试脚本配置')
print('           |      path      |        2         | 执行测试的脚本存放位置（程序会扫描该位置获取脚本，默认`X:/QuickPySm/script`）')
print('           |      name      |        2         | 将要测试的脚本名称（多个用`,`隔开）【还未开发多个】')
print('           |     output     |        2         | 测试结果文件输出位置（默认`X:/QuickPySm/output`）, 设置为`false`则关闭输出')
print('           ----------------------------------------------------------------------')