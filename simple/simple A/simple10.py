# Embedded file name: simple10.py
import string
letters = list(string.letters) + list(string.digits) + ['+', '/']#abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/  一共45个字符
dec = 'FcjTCgD1EffEm2rPC3bTyL5Wu2bKBI9KAZrwFgrUygHN'#44 = 3*14+2  这个很重要

def encode(input_str):
    str_ascii_list = [ '{:0>8}'.format(str(bin(ord(i))).replace('0b', '')) for i in input_str ]#指将input_str的每个字符变为二进制
    output_str = ''                                                                            #且把所有的0b删去然后前面补0，宽度为8，最后变成列表中的元素
    equal_num = 0                                                                              #也就是说将每次字符通过ascii转换成二进制
    while str_ascii_list:#空白为0
        temp_list = str_ascii_list[:3]#取前三个元素放入,循环14次后只剩2个元素
        if len(temp_list) != 3:#长度不为3就进行
            while len(temp_list) < 3:#长度小于3就循环
                equal_num += 1
                temp_list += ['00000000']

        temp_str = ''.join(temp_list)
        temp_str_list = [ temp_str[x:x + 6] for x in [0,6,12,18] ]#将temp_str前24个字符按顺序平分成4份，每一份是都是temp_str_list列表的一个元素
        temp_str_list = [ int(x, 2) for x in temp_str_list ]#将每个二进制元素变成十进制
        if equal_num:#当equal_num变为1时进行，并编码结束返回output_str（只在进行上一个if语句后进行一次）
            temp_str_list = temp_str_list[0:4 - equal_num]#equal_num=1，取前3个元素放入
        output_str += ''.join([ letters[x] for x in temp_str_list ])#以列表元素为下标索引letters里的字符合并成output_str
        str_ascii_list = str_ascii_list[3:]#取第四个到结束所有元素放入，没有就是空白

    output_str = output_str + '=' * equal_num#为0，不管
    return output_str#返回编码后的数据


print "Now let's start the origin of Python!\n"
print 'Plz Input Your Flag:\n'
enc = raw_input()
lst = list(enc)
lst.reverse()
llen = len(lst)
for i in range(llen):
    if i % 2 == 0:
        lst[i] = chr(ord(lst[i]) - 2)
    lst[i] = chr(ord(lst[i]) + 1)

enc2 = ''
enc2 = enc2.join(lst)
enc3 = encode(enc2)
if enc3 == dec:
    print "You're right! "
else:
    print "You're Wrong! "