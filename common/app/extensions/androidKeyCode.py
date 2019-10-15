#!/usr/bin/env python
# coding:utf-8

# @Author:  Carter.Gao
# @Email:   gaoxx9527@163.com
# @Date:    2019/9/11 0:57
# @IDE:     PyCharm
# @About:   安卓键码


class AndroidKeyCode:
    """
    appium包没有自带安卓keycode，在此自定义
    """
    # 基本按键
    KEYCODE_0 = 7   # 按键'0'
    KEYCODE_1 = 8   # 按键'1'
    KEYCODE_2 = 9   # 按键'2'
    KEYCODE_3 = 10  # 按键'3'
    KEYCODE_4 = 11  # 按键'4'
    KEYCODE_5 = 12  # 按键'5'
    KEYCODE_6 = 13  # 按键'6'
    KEYCODE_7 = 14  # 按键'7'
    KEYCODE_8 = 15  # 按键'8'
    KEYCODE_9 = 16  # 按键'9'
    KEYCODE_A = 29  # 按键'A'
    KEYCODE_B = 30  # 按键'B'
    KEYCODE_C = 31  # 按键'C'
    KEYCODE_D = 32  # 按键'D'
    KEYCODE_E = 33  # 按键'E'
    KEYCODE_F = 34  # 按键'F'
    KEYCODE_G = 35  # 按键'G'
    KEYCODE_H = 36  # 按键'H'
    KEYCODE_I = 37  # 按键'I'
    KEYCODE_J = 38  # 按键'J'
    KEYCODE_K = 39  # 按键'K'
    KEYCODE_L = 40  # 按键'L'
    KEYCODE_M = 41  # 按键'M'
    KEYCODE_N = 42  # 按键'N'
    KEYCODE_O = 43  # 按键'O'
    KEYCODE_P = 44  # 按键'P'
    KEYCODE_Q = 45  # 按键'Q'
    KEYCODE_R = 46  # 按键'R'
    KEYCODE_S = 47  # 按键'S'
    KEYCODE_T = 48  # 按键'T'
    KEYCODE_U = 49  # 按键'U'
    KEYCODE_V = 50  # 按键'V'
    KEYCODE_W = 51  # 按键'W'
    KEYCODE_X = 52  # 按键'X'
    KEYCODE_Y = 53  # 按键'Y'
    KEYCODE_Z = 54  # 按键'Z'

    # 符号
    KEYCODE_PLUS = 81           # 按键'+'
    KEYCODE_MINUS = 69          # 按键'-'
    KEYCODE_STAR = 17           # 按键'*'
    KEYCODE_SLASH = 76          # 按键'/'
    KEYCODE_EQUALS = 70         # 按键'='
    KEYCODE_AT = 77             # 按键'@'
    KEYCODE_POUND = 18          # 按键'#'
    KEYCODE_APOSTROPHE = 75     # 按键'''(单引号)
    KEYCODE_BACKSLASH = 73      # 按键'\'
    KEYCODE_COMMA = 55          # 按键','
    KEYCODE_PERIOD = 56         # 按键'.'
    KEYCODE_LEFT_BRACKET = 71   # 按键'['
    KEYCODE_RIGHT_BRACKET = 72  # 按键']'
    KEYCODE_SEMICOLON = 74      # 按键';'
    KEYCODE_GRAVE = 68          # 按键'`'
    KEYCODE_SPACE = 62          # 空格键

    # 小键盘
    KEYCODE_NUMPAD_0 = 144              # 小键盘按键'0'
    KEYCODE_NUMPAD_1 = 145              # 小键盘按键'1'
    KEYCODE_NUMPAD_2 = 146              # 小键盘按键'2'
    KEYCODE_NUMPAD_3 = 147              # 小键盘按键'3'
    KEYCODE_NUMPAD_4 = 148              # 小键盘按键'4'
    KEYCODE_NUMPAD_5 = 149              # 小键盘按键'5'
    KEYCODE_NUMPAD_6 = 150              # 小键盘按键'6'
    KEYCODE_NUMPAD_7 = 151              # 小键盘按键'7'
    KEYCODE_NUMPAD_8 = 152              # 小键盘按键'8'
    KEYCODE_NUMPAD_9 = 153              # 小键盘按键'9'
    KEYCODE_NUMPAD_ADD = 157            # 小键盘按键'+'
    KEYCODE_NUMPAD_SUBTRACT = 156       # 小键盘按键'-'
    KEYCODE_NUMPAD_MULTIPLY = 155       # 小键盘按键'*'
    KEYCODE_NUMPAD_DIVIDE = 154         # 小键盘按键'/'
    KEYCODE_NUMPAD_EQUALS = 161         # 小键盘按键'='
    KEYCODE_NUMPAD_COMMA = 159          # 小键盘按键','
    KEYCODE_NUMPAD_DOT = 158            # 小键盘按键'.'
    KEYCODE_NUMPAD_LEFT_PAREN = 162     # 小键盘按键'('
    KEYCODE_NUMPAD_RIGHT_PAREN = 163    # 小键盘按键')'
    KEYCODE_NUMPAD_ENTER = 160          # 小键盘按键回车

    # 功能键
    KEYCODE_F1 = 131    # 按键F1
    KEYCODE_F2 = 132    # 按键F2
    KEYCODE_F3 = 133    # 按键F3
    KEYCODE_F4 = 134    # 按键F4
    KEYCODE_F5 = 135    # 按键F5
    KEYCODE_F6 = 136    # 按键F6
    KEYCODE_F7 = 137    # 按键F7
    KEYCODE_F8 = 138    # 按键F8
    KEYCODE_F9 = 139    # 按键F9
    KEYCODE_F10 = 140   # 按键F10
    KEYCODE_F11 = 141   # 按键F11

    # 电话按键
    KEYCODE_CALL = 5            # 拨号键
    KEYCODE_ENDCALL = 6         # 挂机键
    KEYCODE_HOME = 3            # 按键Home
    KEYCODE_MENU = 82           # 菜单键
    KEYCODE_BACK = 4            # 返回键
    KEYCODE_SEARCH = 84         # 搜索键
    KEYCODE_CAMERA = 27         # 拍照键
    KEYCODE_FOCUS = 80          # 拍照对焦键
    KEYCODE_POWER = 26          # 电源键
    KEYCODE_NOTIFICATION = 83   # 通知键
    KEYCODE_MUTE = 91           # 话筒静音键
    KEYCODE_VOLUME_MUTE = 164   # 扬声器静音键
    KEYCODE_VOLUME_UP = 24      # 音量增加键
    KEYCODE_VOLUME_DOWN = 25    # 音量减小键

    # 控制按键
    KEYCODE_ENTER = 66          # 回车键
    KEYCODE_ESCAPE = 111        # ESC键
    KEYCODE_DPAD_CENTER = 23    # 导航键-确定键
    KEYCODE_DPAD_UP = 19        # 导航键-向上
    KEYCODE_DPAD_DOWN = 20      # 导航键-向下
    KEYCODE_DPAD_LEFT = 21      # 导航键-向左
    KEYCODE_DPAD_RIGHT = 22     # 导航键-向右
    KEYCODE_MOVE_HOME = 122     # 光标移动到开始键
    KEYCODE_MOVE_END = 123      # 光标移动到末尾键
    KEYCODE_PAGE_UP = 92        # 向上翻页键
    KEYCODE_PAGE_DOWN = 93      # 向下翻页键
    KEYCODE_DEL = 67            # 退格键
    KEYCODE_FORWARD_DEL = 112   # 删除键
    KEYCODE_INSERT = 124        # 插入键
    KEYCODE_TAB = 61            # Tab键
    KEYCODE_NUM_LOCK = 143      # 小键盘锁
    KEYCODE_CAPS_LOCK = 115     # 大写锁定键
    KEYCODE_BREAK = 121         # Break/Pause键
    KEYCODE_SCROLL_LOCK = 116   # 滚动锁定键
    KEYCODE_ZOOM_IN = 168       # 放大键
    KEYCODE_ZOOM_OUT = 169      # 缩小键

    # 组合键
    KEYCODE_ALT_LEFT = 57       # Alt+Left
    KEYCODE_ALT_RIGHT = 58      # Alt+Right
    KEYCODE_CTRL_LEFT = 113     # Control+Left
    KEYCODE_CTRL_RIGHT = 114    # Control+Right
    KEYCODE_SHIFT_LEFT = 59     # Shift+Left
    KEYCODE_SHIFT_RIGHT = 60    # Shift+Right

    # # 多媒体键(不常用)
    # KEYCODE_MEDIA_PLAY = 126            # 多媒体键-播放
    # KEYCODE_MEDIA_STOP = 86             # 多媒体键-停止
    # KEYCODE_MEDIA_PAUSE = 127           # 多媒体键-暂停
    # KEYCODE_MEDIA_PLAY_PAUSE = 85       # 多媒体键-播放/暂停
    # KEYCODE_MEDIA_FAST_FORWARD = 90     # 多媒体键-快进
    # KEYCODE_MEDIA_REWIND = 89           # 多媒体键-快退
    # KEYCODE_MEDIA_NEXT = 87             # 多媒体键-下一首
    # KEYCODE_MEDIA_PREVIOUS = 88         # 多媒体键-上一首
    # KEYCODE_MEDIA_CLOSE = 128           # 多媒体键-关闭
    # KEYCODE_MEDIA_EJECT = 129           # 多媒体键-弹出
    # KEYCODE_MEDIA_RECORD = 130          # 多媒体键-录音

    # # 手柄按键(不常用)
    # KEYCODE_BUTTON_1 = 188      # 通用游戏手柄按钮#1
    # KEYCODE_BUTTON_2 = 189      # 通用游戏手柄按钮#2
    # KEYCODE_BUTTON_3 = 190      # 通用游戏手柄按钮#3
    # KEYCODE_BUTTON_4 = 191      # 通用游戏手柄按钮#4
    # KEYCODE_BUTTON_5 = 192      # 通用游戏手柄按钮#5
    # KEYCODE_BUTTON_6 = 193      # 通用游戏手柄按钮#6
    # KEYCODE_BUTTON_7 = 194      # 通用游戏手柄按钮#7
    # KEYCODE_BUTTON_8 = 195      # 通用游戏手柄按钮#8
    # KEYCODE_BUTTON_9 = 196      # 通用游戏手柄按钮#9
    # KEYCODE_BUTTON_10 = 197     # 通用游戏手柄按钮#10
    # KEYCODE_BUTTON_11 = 198     # 通用游戏手柄按钮#11
    # KEYCODE_BUTTON_12 = 199     # 通用游戏手柄按钮#12
    # KEYCODE_BUTTON_13 = 200     # 通用游戏手柄按钮#13
    # KEYCODE_BUTTON_14 = 201     # 通用游戏手柄按钮#14
    # KEYCODE_BUTTON_15 = 202     # 通用游戏手柄按钮#15
    # KEYCODE_BUTTON_16 = 203     # 通用游戏手柄按钮#16
    # KEYCODE_BUTTON_A = 96       # 游戏手柄按钮A
    # KEYCODE_BUTTON_B = 97       # 游戏手柄按钮B
    # KEYCODE_BUTTON_C = 98       # 游戏手柄按钮C
    # KEYCODE_BUTTON_X = 99       # 游戏手柄按钮X
    # KEYCODE_BUTTON_Y = 100      # 游戏手柄按钮Y
    # KEYCODE_BUTTON_Z = 101      # 游戏手柄按钮Z
    # KEYCODE_BUTTON_L1 = 102     # 游戏手柄按钮L1
    # KEYCODE_BUTTON_L2 = 104     # 游戏手柄按钮L2
    # KEYCODE_BUTTON_R1 = 103     # 游戏手柄按钮R1
    # KEYCODE_BUTTON_R2 = 105     # 游戏手柄按钮R2
    # KEYCODE_BUTTON_MODE = 110   # 游戏手柄按钮Mode
    # KEYCODE_BUTTON_SELECT = 109   # 游戏手柄按钮Select
    # KEYCODE_BUTTON_START = 108    # 游戏手柄按钮Start
    # KEYCODE_BUTTON_THUMBL = 106   # Left Thumb Button
    # KEYCODE_BUTTON_THUMBR = 107   # Right Thumb Button

    # # 其他(不常用)
    # KEYCODE_NUM = 78                # 按键Number_modifier
    # KEYCODE_INFO = 165              # 按键Info
    # KEYCODE_APP_SWITCH = 187        # 按键App_switch
    # KEYCODE_BOOKMARK = 174          # 按键Bookmark
    # KEYCODE_AVR_INPUT = 182         # 按键A/V Receiver input
    # KEYCODE_AVR_POWER = 181         # 按键A/V Receiver power
    # KEYCODE_CAPTIONS = 175          # 按键Toggle captions
    # KEYCODE_CHANNEL_DOWN = 167      # 按键Channel down
    # KEYCODE_CHANNEL_UP = 166        # 按键Channel up
    # KEYCODE_CLEAR = 28              # 按键Clear
    # KEYCODE_DVR = 173               # 按键DVR
    # KEYCODE_ENVELOPE = 65           # 按键Envelope special function
    # KEYCODE_EXPLORER = 64           # 按键Explorer special function
    # KEYCODE_FORWARD = 125           # 按键Forward
    # KEYCODE_FUNCTION = 119          # 按键Function modifier
    # KEYCODE_GUIDE = 172             # 按键Guide
    # KEYCODE_HEADSETHOOK = 79        # 按键Headset Hook
    # KEYCODE_META_LEFT = 117         # 按键Left Meta modifier
    # KEYCODE_META_RIGHT = 118        # 按键Right Meta modifier
    # KEYCODE_PICTSYMBOLS = 94        # 按键Picture Symbols modifier
    # KEYCODE_PROG_BLUE = 186         # 按键Blue “programmable”
    # KEYCODE_PROG_GREEN = 184        # 按键Green “programmable”
    # KEYCODE_PROG_RED = 183          # 按键Red “programmable”
    # KEYCODE_PROG_YELLOW = 185       # 按键Yellow “programmable”
    # KEYCODE_SETTINGS = 176          # 按键Settings
    # KEYCODE_SOFT_LEFT = 1           # 按键Soft Left
    # KEYCODE_SOFT_RIGHT = 2          # 按键Soft Right
    # KEYCODE_STB_INPUT = 180         # 按键Set-top-box input
    # KEYCODE_STB_POWER = 179         # 按键Set-top-box power
    # KEYCODE_SWITCH_CHARSET = 95     # 按键Switch Charset modifier
    # KEYCODE_SYM = 63                # 按键Symbol modifier
    # KEYCODE_SYSRQ = Screen          # 按键System Request/Print
    # KEYCODE_TV = 170                # 按键TV
    # KEYCODE_TV_INPUT = 178          # 按键TV input
    # KEYCODE_TV_POWER = 177          # 按键TV power
    # KEYCODE_WINDOW = 171            # 按键Window
    # KEYCODE_UNKNOWN = 0             # 未知按键
