    ********************************************************************
    About： 集成API/WEB_UI/APP_UI测试框架
    Author：Carter Gao
    Date：  2019-10-15 23:00
    ********************************************************************

    目录结构：
    ----apps            app测试包存放及备份目录
    ----common          公共类
        ...
        ----api         api公共类
        ----app         app应用公共类
        ----web         web应用公共类
    ----config          存放配置文件
    ----data            存放测试数据文件
    ----logs            存放日志文件
    ----packages        一些第三方包
    ----page            web/app UI页面类
    ----results         存放测试结果excel、测试报告、截图文件等
    ----tools           存放一些工具，浏览器驱动等
    ----ts_pytest       pytest测试框架用例目录
    ----ts_unittest     unittest测试框架用例目录
        ...
        ----runAll.py   执行用例主程序
        ...
    
    说明：
    1.python版本：3.7
    2.测试框架：unittest，pytest
    3.第三方库：
        pip install requests                requests请求库
        pip install cx_Oracle               Oracle库
        pip install PyMySQL                 MySQL库
        pip install redis                   redis库
        pip install openpyxl                excel文件处理库
        pip install PyYAML                  yaml文件处理库
        pip install Faker                   随机数据生成库
        pip install selenium                WEB_UI测试库
        pip install Appium-Python-Client    APP_UI测试库
        pip install pytest                  pytest测试框架
        pip install allure-pytest           allure定制化测试报告库
        pip install jsonpath                JSON嵌套取值工具

    测试用例命名规范：
        1.unittest默认按照ASCII码顺序执行用例，故所有用例文件及用例方法以test打头，下划线加小写字母或数字，升序命名。
        2.pytest无顺序要求，只要按照pytest命名要求编写用例即可
