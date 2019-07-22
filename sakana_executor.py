import os
import sys
import argparse

def read_file(input_file_name):
    #if input_file_name in os.dir():
    #    print('file in dir')
    try:
        with open(input_file_name) as f:
            lines = []
            for line in f:
                lines.append(line[:-1])
            return lines
    #else:
    except:
        print("{}というファイルは存在しません．".format(input_file_name))
        raise FileNotFoundError

def bin_exe(A, B, binary_code='0000', A_size=4, B_size=4):
    # defalut register size is 4 bit
    A_size = 2**A_size
    B_size = 2**B_size
    if binary_code == '0000':
        bin_to_result = (A, B)
    elif binary_code == '0001':
        bin_to_result = (A, B)
    elif binary_code == '0010':
        bin_to_result = (A, B)
    elif binary_code == '0011':
        bin_to_result = (A, B)   # 以上の４つは何もしない
    elif binary_code == '0100':
        bin_to_result = (0, B)   # A = 0
    elif binary_code == '0101':
        bin_to_result = (A, 0)   # B = 0
    elif binary_code == '0110':
        bin_to_result = (A, A)   # B = A
    elif binary_code == '0111':
        bin_to_result = (B, B)   # A = B
    elif binary_code == '1000':
        if A+1 > A_size:
            print('register overflow:',A,'+ 1 >',A_size,
                    'register was reset to',(A+1)%A_size)
        bin_to_result = ((A+1)%A_size, B) # A = A + 1
    elif binary_code == '1001':
        if A+2 > A_size:
            print('register overflow:',A,'+ 2 >',A_size,
                    'register was reset to',(A+2)%A_size)
        bin_to_result = ((A+2)%A_size, B) # A = A + 2
    elif binary_code == '1010':
        if A*2 > A_size:
            print('register overflow:',A,'* 2 >',A_size,
                    'register was reset to',(A*2)%A_size)
        bin_to_result = ((A*2)%A_size, B) # A = A * 2
    elif binary_code == '1011':
        if A+B > A_size:
            print('register overflow:',A,'*', B, '>', A_size,
                    'register was reset to',(A+B)%A_size)
        bin_to_result = ((A+B)%A_size, B) # A = A + B

    return bin_to_result

def to_color(s):
    if s == '0':
        return '\x1b[0;37;47m'+s+'\x1b[0m' # white
    elif s == '1':
        return '\x1b[0;31;41m'+s+'\x1b[0m' # red
    else:
        return '\x1b[0;33;43m'+s+'\x1b[0m' # yellow

def to_bin(num):
    return bin(num)[2:]

def to_color_bin(num, size=4):
    # defalut register size is 4 bit
    if num != None:
        return ''.join([to_color(i) for i in to_bin(num).rjust(size, '0')])
    else:
        return ''.join([to_color('*') for i in range(size)])

def show_command_and_registers(A, B, line, option='', size=4):

    if option == 'number':
        if line == 'init':
            print('      A:', A, '\tB:', B)
        else:
            print(line,' A:', A, '\tB:', B)
    elif option == 'color':
        if line == 'init':
            print('      A:',to_color_bin(A, size), '\tB:',to_color_bin(B, size))
        else:
            print(line, ' A:',to_color_bin(A, size), '\tB:',to_color_bin(B, size))
    else:
        if line == 'init':
            print('      A:'+str(A).rjust(5, ' '),'|',to_color_bin(A, size),
                    '\tB:'+str(B).rjust(5, ' '), '|',to_color_bin(B, size))
        else:
            print(line, ' A:'+str(A).rjust(5, ' '), '|', to_color_bin(A, size),
                    '\tB:'+str(B).rjust(5, ' ') ,'|' ,to_color_bin(B, size))



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("source_file", type=str,
                                help="入力ファイルのファイル名を指定")
    parser.add_argument("-f","--format", type=str,
                                help="入力ファイルのファイル名を指定")
    args = parser.parse_args()

    try:
        lines = read_file(args.source_file)
    except IndexError:
        print("入力ファイルが指定されていません．\n例: python sakana_executor.py output_file.out")
    A, B = None, None
    print('init: ',end='')
    show_command_and_registers(A, B, 'init', args.format)
    try:
        for i, line in enumerate(lines):
            A, B = bin_exe(A, B, line)
            print(str(i).rjust(3),': ',end='')
            show_command_and_registers(A, B, line, args.format)
    except:
        print('File"'+args.source_file+'", Line',i,'in command',line)
        
