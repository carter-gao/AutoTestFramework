#!/usr/bin/env python
# coding:utf-8

# @Author:  Carter.Gao
# @Email:   gaoxx9527@163.com
# @Date:    2019/8/27 20:33
# @IDE:     PyCharm
# @About:   Appium服务器初始化参数（Capability）


class DesiredCaps:
    """
    定义Android，IOS平台Appium服务器初始化参数，全部定义默认配置，在代码中修改参数
    """

    # 安卓虚拟机
    caps_android_simulator = {
        "automationName": "Appium",     # 自动化测试的引擎，Appium（默认）或者 Selendroid
        "platformName": "Android",      # 手机操作系统，iOS, Android, 或者 FirefoxOS
        "platformVersion": "",          # 手机操作系统的版本
        "deviceName": "",               # 设备名或连接真机的唯一设备号，安卓通过‘adb devices’获取
        # "udid": "",                     # 连接真机的唯一设备号，此参数直接传给deviceName也可以
        "app": "",                      # 安装包路径，与appPackage 和 appActivity指定其一即可
        "noReset": True,                # 在当前 session 下不会重置应用的状态。默认值为 false
        "androidScreenshotPath": "/data/local/tmp",  # 在设备中截图被保存的目录名。默认值为 /data/local/tmp
        "autoGrantPermissions": True,   # 让Appium自动确定您的应用需要哪些权限，并在安装时将其授予应用。默认设置为 false
        # "unicodeKeyboard": True,        # 使用 Unicode 输入法。 默认值为 false
        # "resetKeyboard": True,          # 在设定了 unicodeKeyboard 关键字的 Unicode 测试结束后，重置输入法到原有状态。如果单独使用，将会被忽略。默认值为 false
        "noSign": True,                 # 跳过检查和对应用进行 debug 签名的步骤。仅适用于 UiAutomator，不适用于 selendroid。 默认值为 false
        # "appActivity": "",              # Activity 的名字是指从你的包中所要启动的 Android Activity，如MainActivity, .Settings
        # "appPackage": "",               # 运行的 Android 应用的包名，如com.example.android.myApp, com.android.settings
        # "appWaitActivity": "",          # 用于等待启动的 Android Activity 名称
        # "appWaitPackage": "",           # 用于等待启动的 Android 应用的包
        "appWaitDuration": 20000,       # 用于等待 appWaitActivity 启动的超时时间（以毫秒为单位）（默认值为 20000)
        "deviceReadyTimeout": 10,       # 用于等待模拟器或真机准备就绪的超时时间，如 5
        "androidDeviceReadyTimeout": 10,    # 用于等待设备在启动应用后准备就绪的超时时间。以秒为单位。
        "androidInstallTimeout": 90000,     # 用于等待在设备中安装 apk 所花费的时间（以毫秒为单位）。默认值为 90000
        "ignoreUnimportantViews": True,     # 调用 uiautomator 的函数 setCompressedLayoutHierarchy()。由于 Accessibility 命令在忽略部分元素的情况下执行速度会加快，这个关键字能加快测试执行的速度。被忽略的元素将不能够被找到，因此这个关键字同时也被实现成可以随时改变的 设置 ( settings )。 默认值为 false
        "disableAndroidWatchers": True,     # 禁用 android 监视器（watchers）。监视器用于见识应用程序的无响应状态（anr）和崩溃（crash），禁用会降低 Android 设备或模拟器的 CPU 使用率。该 capability 仅在使用 UiAutomator 时有效，不适用于 selendroid，默认设置为 false。
        # "browserName": "",              # 浏览器，'Safari' 对应 iOS，'Chrome', 'Chromium', 或 'Browser' 则对应 Android
        # "enablePerformanceLogging": False,  # （仅适用于 Chrome 与 webview）开启 Chromedriver 的性能日志。（默认值为 false）
        # "chromeOptions": "",            # 允许对 ChromeDriver 传 chromeOptions 的参数。例如 chromeOptions: {args: ['--disable-popup-blocking']}
        # "recreateChromeDriverSessions": False,  # 当移除非 ChromeDriver webview时，终止掉 ChromeDriver 的 session。默认设置为 false
        # "nativeWebScreenshot": False,   # 在 web 的上下文（context），使用原生（native）的方法去截图，而不是用过代理的 ChromeDriver。默认值为 false
        # "androidDeviceSocket": "",      # 开发工具的 socket 名称。只有在被测应用是一个使用 Chromium 内核的浏览器时才需要。socket 会被浏览器打开，然后 Chromedriver 把它作为开发者工具来进行连接。例如 chrome_devtools_remote
        # "chromedriverExecutable": "",   # webdriver 可执行文件的绝对路径（如果 Chromium 内嵌一个自己提供的 webdriver，则应使用他去替换掉 Appium 自带的 chromedriver）,例如 /abs/path/to/webdriver
        # "autoWebview": False,           # 直接转换到 Webview 上下文（context），默认值为 false
        # "autoWebviewTimeout": 2000,     # 用于等待 Webview 上下文（context）激活的时间（以毫秒为单位）。默认值为 2000
        # "fullReset": False,             # (Android) 要清除 app 里的数据，请将应用卸载才能达到重置应用的效果。在 Android, 在 session 完成之后也会将应用卸载掉。默认值为 false
        # "newCommandTimeout": None,      # 用于客户端在退出或者结束 session 之前，Appium 等待客户端发送一条新命令所花费的时间（秒为单位）
        # "language": None,               # (Sim/Emu-only) 为模拟器设置语言，例如 fr
        # "locale": None,                 # (Sim/Emu-only) 为模拟器设置所在区域，例如 fr_CA
        # "orientation": None,            # (Sim/Emu-only) 模拟器当前的方向，竖屏 或 横屏
        # "androidCoverage": "",          # 用于执行测试的 instrumentation 类。如 com.my.Pkg/com.my.Pkg.instrumentation.MyInstrumentation
        # "adbPort": 5037,                # 用来连接 ADB 服务器的端口（默认值为 5037）
        # "avd": "",                      # 被启动 avd 的名字，例如 api19
        # "avdLaunchTimeout": 120000,     # 用于等待 avd 启动并连接 ADB 的超时时间（以毫秒为单位），默认值为 120000。
        # "avdReadyTimeout": 120000,      # 用于等待 avd 完成启动动画的超时时间（以毫秒为单位），默认值为 120000。
        # "avdArgs": "",                  # 启动 avd 时使用的额外参数。例如 -netfast
        # "useKeystore": False,           # 使用自定义的 keystore 给 apk 签名，默认值为 false
        # "keystorePath": "~/.android/debug.keystore",    # 自定义 keystore 的路径, 默认路径为 ~/.android/debug.keystore
        # "keystorePassword": "",         # 自定义 keystore 的密码
        # "keyAlias": "",                 # key 的别名	例如 androiddebugkey
        # "keyPassword": "",              # key 的密码	例如 foo
        # "intentAction": "android.intent.action.MAIN",   # 用于启动 activity 的 intent action（默认值为 android.intent.action.MAIN)
        # "intentCategory": "android.intent.category.LAUNCHER",   # 用于启动 activity 的 intent category。（默认值为 android.intent.category.LAUNCHER)
        # "intentFlags": 0x10200000,      # 用于启动 activity 的标识（flags）（默认值为 0x10200000）
        # "optionalIntentArguments": "",  # 用于启动 activity 的额外 intent 参数。例如 --esn <EXTRA_KEY>, --ez <EXTRA_KEY> <EXTRA_BOOLEAN_VALUE>, 等等。
        # "dontStopAppOnReset": False,    # 在使用 adb 启动应用之前，不要终止被测应用的进程。如果被测应用是被其他钩子(anchor)应用所创建的，设置该参数为 false 后，就允许钩子(anchor)应用的进程在使用 adb 启动被测应用期间仍然存在。换而言之，设置 dontStopAppOnReset 为 true 后，我们在 adb shell am start 的调用中不需要包含 -S标识（flag）。忽略该 capability 或 设置为 false 的话，就需要包含 -S 标识（flag）。默认值为 false
    }

    # 安卓真机
    caps_android_machine = {
        "automationName": "Appium",         # 自动化测试的引擎，Appium（默认）或者 Selendroid
        "platformName": "Android",          # 手机操作系统，iOS, Android, 或者 FirefoxOS
        "platformVersion": "",              # 手机操作系统的版本
        "deviceName": "",                   # 设备名或连接真机的唯一设备号，安卓通过‘adb devices’获取
        # "udid": "",                       # 连接真机的唯一设备号，此参数直接传给deviceName也可以
        "app": "",                          # 安装包路径，与appPackage 和 appActivity指定其一即可
        "noReset": True,                    # 在当前 session 下不会重置应用的状态。默认值为 false
        "androidScreenshotPath": "/data/local/tmp",  # 在设备中截图被保存的目录名。默认值为 /data/local/tmp
        "autoGrantPermissions": True,       # 让Appium自动确定您的应用需要哪些权限，并在安装时将其授予应用。默认设置为 false
        # "unicodeKeyboard": True,            # 使用 Unicode 输入法。 默认值为 false
        # "resetKeyboard": True,              # 在设定了 unicodeKeyboard 关键字的 Unicode 测试结束后，重置输入法到原有状态。如果单独使用，将会被忽略。默认值为 false
        "noSign": True,                     # 跳过检查和对应用进行 debug 签名的步骤。仅适用于 UiAutomator，不适用于 selendroid。 默认值为 false
        # "appActivity": "",                  # Activity 的名字是指从你的包中所要启动的 Android Activity，如MainActivity, .Settings
        # "appPackage": "",                   # 运行的 Android 应用的包名，如com.example.android.myApp, com.android.settings
        # "appWaitActivity": "",              # 用于等待启动的 Android Activity 名称
        # "appWaitPackage": "",               # 用于等待启动的 Android 应用的包
        "appWaitDuration": 20000,           # 用于等待 appWaitActivity 启动的超时时间（以毫秒为单位）（默认值为 20000)
        "deviceReadyTimeout": 10,           # 用于等待模拟器或真机准备就绪的超时时间，如 5
        "androidDeviceReadyTimeout": 10,    # 用于等待设备在启动应用后准备就绪的超时时间。以秒为单位。
        "androidInstallTimeout": 90000,     # 用于等待在设备中安装 apk 所花费的时间（以毫秒为单位）。默认值为 90000
        "ignoreUnimportantViews": True,     # 调用 uiautomator 的函数 setCompressedLayoutHierarchy()。由于 Accessibility 命令在忽略部分元素的情况下执行速度会加快，这个关键字能加快测试执行的速度。被忽略的元素将不能够被找到，因此这个关键字同时也被实现成可以随时改变的 设置 ( settings )。 默认值为 false
        "disableAndroidWatchers": True,     # 禁用 android 监视器（watchers）。监视器用于见识应用程序的无响应状态（anr）和崩溃（crash），禁用会降低 Android 设备或模拟器的 CPU 使用率。该 capability 仅在使用 UiAutomator 时有效，不适用于 selendroid，默认设置为 false。
        # "browserName": "",                  # 浏览器，'Safari' 对应 iOS，'Chrome', 'Chromium', 或 'Browser' 则对应 Android
        # "enablePerformanceLogging": False,  # （仅适用于 Chrome 与 webview）开启 Chromedriver 的性能日志。（默认值为 false）
        # "chromeOptions": "",                # 允许对 ChromeDriver 传 chromeOptions 的参数。例如 chromeOptions: {args: ['--disable-popup-blocking']}
        # "recreateChromeDriverSessions": False,  # 当移除非 ChromeDriver webview时，终止掉 ChromeDriver 的 session。默认设置为 false
        # "nativeWebScreenshot": False,       # 在 web 的上下文（context），使用原生（native）的方法去截图，而不是用过代理的 ChromeDriver。默认值为 false
        # "androidDeviceSocket": "",          # 开发工具的 socket 名称。只有在被测应用是一个使用 Chromium 内核的浏览器时才需要。socket 会被浏览器打开，然后 Chromedriver 把它作为开发者工具来进行连接。例如 chrome_devtools_remote
        # "chromedriverExecutable": "",       # webdriver 可执行文件的绝对路径（如果 Chromium 内嵌一个自己提供的 webdriver，则应使用他去替换掉 Appium 自带的 chromedriver）,例如 /abs/path/to/webdriver
        # "autoWebview": False,               # 直接转换到 Webview 上下文（context），默认值为 false
        # "autoWebviewTimeout": 2000,         # 用于等待 Webview 上下文（context）激活的时间（以毫秒为单位）。默认值为 2000
        # "fullReset": False,                 # (Android) 要清除 app 里的数据，请将应用卸载才能达到重置应用的效果。在 Android, 在 session 完成之后也会将应用卸载掉。默认值为 false
        # "newCommandTimeout": None,          # 用于客户端在退出或者结束 session 之前，Appium 等待客户端发送一条新命令所花费的时间（秒为单位）
        # "androidCoverage": "",              # 用于执行测试的 instrumentation 类。如 com.my.Pkg/com.my.Pkg.instrumentation.MyInstrumentation
        # "adbPort": 5037,                    # 用来连接 ADB 服务器的端口（默认值为 5037）
        # "avd": "",                          # 被启动 avd 的名字，例如 api19
        # "avdLaunchTimeout": 120000,         # 用于等待 avd 启动并连接 ADB 的超时时间（以毫秒为单位），默认值为 120000。
        # "avdReadyTimeout": 120000,          # 用于等待 avd 完成启动动画的超时时间（以毫秒为单位），默认值为 120000。
        # "avdArgs": "",                      # 启动 avd 时使用的额外参数。例如 -netfast
        # "useKeystore": False,               # 使用自定义的 keystore 给 apk 签名，默认值为 false
        # "keystorePath": "~/.android/debug.keystore",  # 自定义 keystore 的路径, 默认路径为 ~/.android/debug.keystore
        # "keystorePassword": "",             # 自定义 keystore 的密码
        # "keyAlias": "",                     # key 的别名	例如 androiddebugkey
        # "keyPassword": "",                  # key 的密码	例如 foo
        # "intentAction": "android.intent.action.MAIN",  # 用于启动 activity 的 intent action（默认值为 android.intent.action.MAIN)
        # "intentCategory": "android.intent.category.LAUNCHER",   # 用于启动 activity 的 intent category。（默认值为 android.intent.category.LAUNCHER)
        # "intentFlags": 0x10200000,          # 用于启动 activity 的标识（flags）（默认值为 0x10200000）
        # "optionalIntentArguments": "",      # 用于启动 activity 的额外 intent 参数。例如 --esn <EXTRA_KEY>, --ez <EXTRA_KEY> <EXTRA_BOOLEAN_VALUE>, 等等。
        # "dontStopAppOnReset": False,        # 在使用 adb 启动应用之前，不要终止被测应用的进程。如果被测应用是被其他钩子(anchor)应用所创建的，设置该参数为 false 后，就允许钩子(anchor)应用的进程在使用 adb 启动被测应用期间仍然存在。换而言之，设置 dontStopAppOnReset 为 true 后，我们在 adb shell am start 的调用中不需要包含 -S标识（flag）。忽略该 capability 或 设置为 false 的话，就需要包含 -S 标识（flag）。默认值为 false
    }

    # IOS虚拟机
    caps_ios_simulator = {
        "automationName": "Appium",     # 自动化测试的引擎，Appium（默认）或者 Selendroid
        "platformName": "iOS",          # 手机操作系统，iOS, Android, 或者 FirefoxOS
        "platformVersion": "",          # 手机操作系统的版本
        "deviceName": "",               # 设备名或连接真机的唯一设备号，iOS通过 Instruments 的 instruments -s devices 命令获取
        "udid": "",                     # 连接真机的唯一设备号，此参数直接传给deviceName也可以
        "app": "",                      # 安装包路径
        "noReset": False,               # 在当前 session 下不会重置应用的状态。默认值为 false
        "browserName": "",              # 浏览器，'Safari' 对应 iOS，'Chrome', 'Chromium', 或 'Browser' 则对应 Android
        "newCommandTimeout": None,      # 用于客户端在退出或者结束 session 之前，Appium 等待客户端发送一条新命令所花费的时间（秒为单位）
        "autoWebview": False,           # 直接转换到 Webview 上下文（context），默认值为 false
        "fullReset": False,             # (iOS)删除所有的模拟器文件夹。(Android) 要清除 app 里的数据，请将应用卸载才能达到重置应用的效果。在 Android, 在 session 完成之后也会将应用卸载掉。默认值为 false
        "language": None,               # (Sim/Emu-only) 为模拟器设置语言，例如 fr
        "locale": None,                 # (Sim/Emu-only) 为模拟器设置所在区域，例如 fr_CA
        "orientation": None,            # (Sim/Emu-only) 模拟器当前的方向，竖屏 或 横屏
        "customSSLCert": "",            # (Sim/Emu-only) 给模拟器添加一个 SSL 证书。例如 -----BEGIN CERTIFICATE-----MIIFWjCCBEKg  -----END CERTIFICATE-----
        "calendarFormat": "",           # （仅支持模拟器） 为iOS的模拟器设置日历格式。例如 gregorian
        "locationServicesEnabled": False,       # （仅支持模拟器）强制打开或关闭定位服务。默认值是保持当前模拟器的设定
        "locationServicesAuthorized": False,    # （仅支持模拟器）通过修改 plist 文件设定是否允许应用使用定位服务，从而避免定位服务的警告出现。默认值是保持当前模拟器的设定。请注意在使用这个关键字时，你同时需要使用 bundleId 关键字来发送你的应用的 bundle ID。
        "nativeWebTap": False,          # （仅支持模拟器）在Safari中允许“真实的"，非基于 javascript 的 web 点击 (tap) 。 默认值：false。注意：取决于 viewport 大小/比例， 点击操作不一定能精确地点中对应的元素。
        "safariInitialUrl": "",         # （仅支持模拟器） (>= 8.1) 初始化 safari 的时使用的地址。默认是一个本地的欢迎页面
        "safariAllowPopups": False,     # （仅支持模拟器）允许 javascript 在 Safari 中创建新窗口。默认保持模拟器当前设置。
        "safariIgnoreFraudWarning": False,      # （仅支持模拟器）阻止 Safari 显示此网站可能存在风险的警告。默认保持浏览器当前设置。
        "safariOpenLinksInBackground": False,   # （仅支持模拟器）Safari 是否允许链接在新窗口打开。默认保持浏览器当前设置。
        "keepKeyChains": False,         # （仅支持模拟器）当 Appium 会话开始/结束时是否保留存放密码存放记录 (keychains) 库(Library)/钥匙串(Keychains))
        "bundleId": "",                 # 被测应用的 bundle ID 。用于在真实设备中启动测试，也用于使用其他需要 bundle ID 的关键字启动测试。在使用 bundle ID 在真实设备上执行测试时，你可以不提供 app 关键字，但你必须提供 udid 。例如 io.appium.TestApp
        "launchTimeout": None,          # 以毫秒为单位，在 Appium 运行失败之前设置一个等待 instruments 的时间
        "autoAcceptAlerts": False,      # 当警告弹出的时候，都会自动去点接受。包括隐私访问权限的警告（例如 定位，联系人，照片）。默认值为 false。不支持基于 XCUITest 的测试。
        "autoDismissAlerts": False,     # 当警告弹出的时候，都会自动去点取消。包括隐私访问权限的警告（例如 定位，联系人，照片）。默认值为 false。不支持基于 XCUITest 的测试。
        "nativeInstrumentsLib": False,  # 使用原生 intruments 库（即关闭 instruments-without-delay）。
        "localizableStringsDir": "en.lproj",    # 从哪里查找本地化字符串。默认值为 en.lproj
        "interKeyDelay": 100,           # 以毫秒为单位，按下每一个按键之间的延迟时间,例如 100
        "showIOSLog": False,            # 是否在 Appium 的日志中显示设备的日志。默认值为 false
        "sendKeyStrategy": "",          # 输入文字到文字框的策略。模拟器默认值：oneByOne(一个接着一个)。真实设备默认值：grouped (分组输入)，例 oneByOne, grouped或setValue
        "screenshotWaitTimeout": 10,    # 以秒为单位，生成屏幕截图的最长等待时间。默认值为：10
        "waitForAppScript": "",         # 用于判断 "应用是否被启动” 的 iOS 自动化脚本代码。默认情况下系统等待直到页面内容非空。结果必须是布尔类型。例如 true;, target.elements().length > 0;, $.delay(5000); true;
        "webviewConnectRetries": 8,     # 用于获取 webview 失败时，发送连接信息到远程调试器的次数。默认次数为: 8
        "appName": "",                  # 被测应用的名字。 用于支持 iOS 9 以上系统的应用的自动化。
    }

    # IOS真机
    caps_ios_machine = {
        "automationName": "Appium",     # 自动化测试的引擎，Appium（默认）或者 Selendroid
        "platformName": "iOS",          # 手机操作系统，iOS, Android, 或者 FirefoxOS
        "platformVersion": "",          # 手机操作系统的版本
        "deviceName": "",               # 设备名或连接真机的唯一设备号，iOS通过 Instruments 的 instruments -s devices 命令获取
        "udid": "",                     # 连接真机的唯一设备号，此参数直接传给deviceName也可以
        "app": "",                      # 安装包路径
        "noReset": False,               # 在当前 session 下不会重置应用的状态。默认值为 false
        "browserName": "",              # 浏览器，'Safari' 对应 iOS，'Chrome', 'Chromium', 或 'Browser' 则对应 Android
        "newCommandTimeout": None,      # 用于客户端在退出或者结束 session 之前，Appium 等待客户端发送一条新命令所花费的时间（秒为单位）
        "autoWebview": False,           # 直接转换到 Webview 上下文（context），默认值为 false
        "fullReset": False,             # (iOS)删除所有的模拟器文件夹。(Android) 要清除 app 里的数据，请将应用卸载才能达到重置应用的效果。在 Android, 在 session 完成之后也会将应用卸载掉。默认值为 false
        "bundleId": "",                 # 被测应用的 bundle ID 。用于在真实设备中启动测试，也用于使用其他需要 bundle ID 的关键字启动测试。在使用 bundle ID 在真实设备上执行测试时，你可以不提供 app 关键字，但你必须提供 udid 。例如 io.appium.TestApp
        "launchTimeout": None,          # 以毫秒为单位，在 Appium 运行失败之前设置一个等待 instruments 的时间
        "autoAcceptAlerts": False,      # 当警告弹出的时候，都会自动去点接受。包括隐私访问权限的警告（例如 定位，联系人，照片）。默认值为 false。不支持基于 XCUITest 的测试。
        "autoDismissAlerts": False,     # 当警告弹出的时候，都会自动去点取消。包括隐私访问权限的警告（例如 定位，联系人，照片）。默认值为 false。不支持基于 XCUITest 的测试。
        "nativeInstrumentsLib": False,  # 使用原生 intruments 库（即关闭 instruments-without-delay）。
        "localizableStringsDir": "en.lproj",    # 从哪里查找本地化字符串。默认值为 en.lproj
        "interKeyDelay": 100,           # 以毫秒为单位，按下每一个按键之间的延迟时间,例如 100
        "showIOSLog": False,            # 是否在 Appium 的日志中显示设备的日志。默认值为 false
        "sendKeyStrategy": "",          # 输入文字到文字框的策略。模拟器默认值：oneByOne(一个接着一个)。真实设备默认值：grouped (分组输入)，例 oneByOne, grouped或setValue
        "screenshotWaitTimeout": 10,    # 以秒为单位，生成屏幕截图的最长等待时间。默认值为：10
        "waitForAppScript": "",         # 用于判断 "应用是否被启动” 的 iOS 自动化脚本代码。默认情况下系统等待直到页面内容非空。结果必须是布尔类型。例如 true;, target.elements().length > 0;, $.delay(5000); true;
        "webviewConnectRetries": 8,     # 用于获取 webview 失败时，发送连接信息到远程调试器的次数。默认次数为: 8
        "appName": "",                  # 被测应用的名字。 用于支持 iOS 9 以上系统的应用的自动化。
    }

    # IOS虚拟机（使用 XCUITest）
    caps_ios_XCUITest_simulator = {
        "automationName": "Appium",     # 自动化测试的引擎，Appium（默认）或者 Selendroid
        "platformName": "iOS",          # 手机操作系统，iOS, Android, 或者 FirefoxOS
        "platformVersion": "",          # 手机操作系统的版本
        "deviceName": "",               # 设备名或连接真机的唯一设备号，iOS通过 Instruments 的 instruments -s devices 命令获取
        "udid": "",                     # 连接真机的唯一设备号，此参数直接传给deviceName也可以
        "app": "",                      # 安装包路径
        "noReset": False,               # 在当前 session 下不会重置应用的状态。默认值为 false
        "browserName": "",              # 浏览器，'Safari' 对应 iOS，'Chrome', 'Chromium', 或 'Browser' 则对应 Android
        "newCommandTimeout": None,      # 用于客户端在退出或者结束 session 之前，Appium 等待客户端发送一条新命令所花费的时间（秒为单位）
        "autoWebview": False,           # 直接转换到 Webview 上下文（context），默认值为 false
        "fullReset": False,             # (iOS)删除所有的模拟器文件夹。(Android) 要清除 app 里的数据，请将应用卸载才能达到重置应用的效果。在 Android, 在 session 完成之后也会将应用卸载掉。默认值为 false
        "language": None,               # (Sim/Emu-only) 为模拟器设置语言，例如 fr
        "locale": None,                 # (Sim/Emu-only) 为模拟器设置所在区域，例如 fr_CA
        "orientation": None,            # (Sim/Emu-only) 模拟器当前的方向，竖屏 或 横屏
        "customSSLCert": "",            # (Sim/Emu-only) 给模拟器添加一个 SSL 证书。例如 -----BEGIN CERTIFICATE-----MIIFWjCCBEKg  -----END CERTIFICATE-----
        "calendarFormat": "",           # （仅支持模拟器） 为iOS的模拟器设置日历格式。例如 gregorian
        "locationServicesEnabled": False,       # （仅支持模拟器）强制打开或关闭定位服务。默认值是保持当前模拟器的设定
        "locationServicesAuthorized": False,    # （仅支持模拟器）通过修改 plist 文件设定是否允许应用使用定位服务，从而避免定位服务的警告出现。默认值是保持当前模拟器的设定。请注意在使用这个关键字时，你同时需要使用 bundleId 关键字来发送你的应用的 bundle ID。
        "nativeWebTap": False,          # （仅支持模拟器）在Safari中允许“真实的"，非基于 javascript 的 web 点击 (tap) 。 默认值：false。注意：取决于 viewport 大小/比例， 点击操作不一定能精确地点中对应的元素。
        "safariInitialUrl": "",         # （仅支持模拟器） (>= 8.1) 初始化 safari 的时使用的地址。默认是一个本地的欢迎页面
        "safariAllowPopups": False,     # （仅支持模拟器）允许 javascript 在 Safari 中创建新窗口。默认保持模拟器当前设置。
        "safariIgnoreFraudWarning": False,      # （仅支持模拟器）阻止 Safari 显示此网站可能存在风险的警告。默认保持浏览器当前设置。
        "safariOpenLinksInBackground": False,   # （仅支持模拟器）Safari 是否允许链接在新窗口打开。默认保持浏览器当前设置。
        "keepKeyChains": False,         # （仅支持模拟器）当 Appium 会话开始/结束时是否保留存放密码存放记录 (keychains) 库(Library)/钥匙串(Keychains))
        "bundleId": "",                 # 被测应用的 bundle ID 。用于在真实设备中启动测试，也用于使用其他需要 bundle ID 的关键字启动测试。在使用 bundle ID 在真实设备上执行测试时，你可以不提供 app 关键字，但你必须提供 udid 。例如 io.appium.TestApp
        "launchTimeout": None,          # 以毫秒为单位，在 Appium 运行失败之前设置一个等待 instruments 的时间
        "nativeInstrumentsLib": False,  # 使用原生 intruments 库（即关闭 instruments-without-delay）。
        "localizableStringsDir": "en.lproj",    # 从哪里查找本地化字符串。默认值为 en.lproj
        "interKeyDelay": 100,           # 以毫秒为单位，按下每一个按键之间的延迟时间,例如 100
        "showIOSLog": False,            # 是否在 Appium 的日志中显示设备的日志。默认值为 false
        "sendKeyStrategy": "oneByOne",  # 输入文字到文字框的策略。模拟器默认值：oneByOne(一个接着一个)。真实设备默认值：grouped (分组输入)，例 oneByOne, grouped或setValue
        "screenshotWaitTimeout": 10,    # 以秒为单位，生成屏幕截图的最长等待时间。默认值为：10
        "waitForAppScript": "",         # 用于判断 "应用是否被启动” 的 iOS 自动化脚本代码。默认情况下系统等待直到页面内容非空。结果必须是布尔类型。例如 true;, target.elements().length > 0;, $.delay(5000); true;
        "webviewConnectRetries": 8,     # 用于获取 webview 失败时，发送连接信息到远程调试器的次数。默认次数为: 8
        "appName": "",                  # 被测应用的名字。 用于支持 iOS 9 以上系统的应用的自动化。
        "processArguments": "",         # 通过 instruments 传递到 AUT 的参数	例如 -myflag
        "wdaLocalPort": "",             # 如果这个值被指定了，Mac 主机就会使用这个端口，通过 USB 发送数据到 iOS 设备中。默认的端口与 iOS 设备中 WDA 的端口号是一致的。
        "showXcodeLog": False,          # 是否显示运行测试时 Xcode 的输出日志，如果值设置为 true ，则会在启动的时候产生大量的额外日志。默认设置为 false。
        "iosInstallPause": 0,           # 安装应用程序与启动 WebDriverAgent 之间停止的间隔时间（以毫秒为单位），特别适用于体积较大的包。默认是设置为 0。
        "scaleFactor": "",              # 模拟器缩放因子。这对于默认分辨率是大于实际分辨的模拟器来说非常有用。因此，你不用上下滑动模拟器的屏幕就能看到所有模拟器显示的内容了。可接受的值为: '1.0', '0.75', '0.5', '0.33' 和 '0.25'。 这些值都应该是一个字符串
        "preventWDAAttachments": True,  # 设置 WebDriverAgent 项目中的 DerivedData 文件夹的权限为仅可读。为了防止 XCTest 框架产生大量无用的截屏与日志，该设置是非常必要的，因为这是不可能通过 Apple 提供的接口去关闭的。设置 capabilitity 为 true 将会设置 Posix 的文件夹的权限为 555，设置为 false 则会将权限重置回 755
        "webDriverAgentUrl": "",        # 若提供了 URL，Appium 将在这 URL 上连接现有的 WebDriverAgent 实例，而不是重新启动一个。
        "useNewWDA": False,             # 若设置为 true，则直接卸载设备上现存的所有 WebDriverAgent 客户端。在某些情况，该做法可以提高稳定性。默认设置为 false。
        "wdaLaunchTimeout": 60000,      # 等待 WebDriverAgent 可 ping 通的时间（以毫秒为单位）。默认设置为 60000ms。
        "calendarAccessAuthorized": True,   # 若设置为 true，则允许在 iOS 模拟器上访问日历。若设置为 false，则不被允许。否则，日历的 authorizationStatus 会保持不变。
    }

    # IOS真机（使用 XCUITest）
    caps_ios_XCUITest_machine = {
        "automationName": "Appium",     # 自动化测试的引擎，Appium（默认）或者 Selendroid
        "platformName": "iOS",          # 手机操作系统，iOS, Android, 或者 FirefoxOS
        "platformVersion": "",          # 手机操作系统的版本
        "deviceName": "",               # 设备名或连接真机的唯一设备号，iOS通过 Instruments 的 instruments -s devices 命令获取
        "udid": "",                     # 连接真机的唯一设备号，此参数直接传给deviceName也可以
        "app": "",                      # 安装包路径
        "noReset": False,               # 在当前 session 下不会重置应用的状态。默认值为 false
        "browserName": "",              # 浏览器，'Safari' 对应 iOS，'Chrome', 'Chromium', 或 'Browser' 则对应 Android
        "newCommandTimeout": None,      # 用于客户端在退出或者结束 session 之前，Appium 等待客户端发送一条新命令所花费的时间（秒为单位）
        "autoWebview": False,           # 直接转换到 Webview 上下文（context），默认值为 false
        "fullReset": False,             # (iOS)删除所有的模拟器文件夹。(Android) 要清除 app 里的数据，请将应用卸载才能达到重置应用的效果。在 Android, 在 session 完成之后也会将应用卸载掉。默认值为 false
        "bundleId": "",                 # 被测应用的 bundle ID 。用于在真实设备中启动测试，也用于使用其他需要 bundle ID 的关键字启动测试。在使用 bundle ID 在真实设备上执行测试时，你可以不提供 app 关键字，但你必须提供 udid 。例如 io.appium.TestApp
        "launchTimeout": None,          # 以毫秒为单位，在 Appium 运行失败之前设置一个等待 instruments 的时间
        "nativeInstrumentsLib": False,  # 使用原生 intruments 库（即关闭 instruments-without-delay）。
        "localizableStringsDir": "en.lproj",    # 从哪里查找本地化字符串。默认值为 en.lproj
        "interKeyDelay": 100,           # 以毫秒为单位，按下每一个按键之间的延迟时间,例如 100
        "showIOSLog": False,            # 是否在 Appium 的日志中显示设备的日志。默认值为 false
        "sendKeyStrategy": "grouped",   # 输入文字到文字框的策略。模拟器默认值：oneByOne(一个接着一个)。真实设备默认值：grouped (分组输入)，例 oneByOne, grouped或setValue
        "screenshotWaitTimeout": 10,    # 以秒为单位，生成屏幕截图的最长等待时间。默认值为：10
        "waitForAppScript": "",         # 用于判断 "应用是否被启动” 的 iOS 自动化脚本代码。默认情况下系统等待直到页面内容非空。结果必须是布尔类型。例如 true;, target.elements().length > 0;, $.delay(5000); true;
        "webviewConnectRetries": 8,     # 用于获取 webview 失败时，发送连接信息到远程调试器的次数。默认次数为: 8
        "appName": "",                  # 被测应用的名字。 用于支持 iOS 9 以上系统的应用的自动化。
        "processArguments": "",         # 通过 instruments 传递到 AUT 的参数	例如 -myflag
        "wdaLocalPort": "",             # 如果这个值被指定了，Mac 主机就会使用这个端口，通过 USB 发送数据到 iOS 设备中。默认的端口与 iOS 设备中 WDA 的端口号是一致的。
        "showXcodeLog": False,          # 是否显示运行测试时 Xcode 的输出日志，如果值设置为 true ，则会在启动的时候产生大量的额外日志。默认设置为 false。
        "iosInstallPause": 0,           # 安装应用程序与启动 WebDriverAgent 之间停止的间隔时间（以毫秒为单位），特别适用于体积较大的包。默认是设置为 0。
        "xcodeConfigFile": "",          # 一个可选的 Xcode 可配置文件的完整路径，用于指定在真机上运行 WebDriverAgent 的个人身份或者团队身份的代码签名。
        "keychainPath": "",             # 从系统的 keychain 中导出私有开发秘钥的完整路径。在真机测试时与 keychainPassword 配合使用。
        "keychainPassword": "",         # 在 keychainPath 中指定 keychain 的解锁密码。
        "preventWDAAttachments": True,  # 设置 WebDriverAgent 项目中的 DerivedData 文件夹的权限为仅可读。为了防止 XCTest 框架产生大量无用的截屏与日志，该设置是非常必要的，因为这是不可能通过 Apple 提供的接口去关闭的。设置 capabilitity 为 true 将会设置 Posix 的文件夹的权限为 555，设置为 false 则会将权限重置回 755
        "webDriverAgentUrl": "",        # 若提供了 URL，Appium 将在这 URL 上连接现有的 WebDriverAgent 实例，而不是重新启动一个。
        "useNewWDA": False,             # 若设置为 true，则直接卸载设备上现存的所有 WebDriverAgent 客户端。在某些情况，该做法可以提高稳定性。默认设置为 false。
        "wdaLaunchTimeout": 60000,      # 等待 WebDriverAgent 可 ping 同的时间（以毫秒为单位）。默认设置为 60000ms。
    }


if __name__ == '__main__':
    import pprint
    pprint.pprint(DesiredCaps.caps_ios_XCUITest_simulator)
