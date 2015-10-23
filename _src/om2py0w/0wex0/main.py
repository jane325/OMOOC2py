# -*- coding: UTF-8 -*-  # 中文符号输入显示
import os  # 模块可自定义使用

def main():
    print 'hello world!' # 一行命令，清晰整洁
    print "这是 Alice\'的问候。" # 声明单行字符 单双引号 逃逸处理
    print "这是Bob\'的问候。"   # 紧跟着函数定义的代码缩进4格，函数间最好上下行隔开

    foo(5, 10)

    print '=' * 10 # * 字符可乘
    print '这将直接执行' + os.getcwd()  # 调用os模块中的函式

    counter = 0
    counter += 1 # 变量需要实例化

    food = ['苹果','杏子','李子','梨']
    for i in food:
        print '俺就爱整只:'+i  # 在循环中，i 指代列表中每个循环的事物

    print '数到10'
    for i in range(10):  # 从0 开始，不包括最后一位（显示0到9），应用函数必定以冒号结尾
        print i

def foo(paraml,secondParam):
    res = paraml + secondParam
    print '%s 加 %s 等于 %s' %(paraml,secondParam,res)
    if res<50:
        print '这个'
    elif (res>=50) and ((paraml==42) or (secondParam==24)):  # 逻辑运算符，使用英文单词
        print '那个'
    else:
        print '嗯...' 
    return res

if __name__ == '__main__': # 在最后调用主函式,用内置脚本名判定，运行当前脚本，__name ==__main,否则当做模块导入时，不运行main
    main()
