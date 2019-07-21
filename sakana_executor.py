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

def bin_exe(A, B, binary_code='0000'):
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
        bin_to_result = (A+1, B) # A = A + 1
    elif binary_code == '1001':
        bin_to_result = (A+2, B) # A = A + 2
    elif binary_code == '1010':
        bin_to_result = (A*2, B) # A = A * 2
    elif binary_code == '1011':
        bin_to_result = (A+B, B) # A = A + B

    return bin_to_result

def show_command_and_registers(A, B, line, option='number'):
    if option == 'number':
        print(line,'A:',A,'B:',B)



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("source_file", type=str,
                                help="入力ファイルのファイル名を指定")
    args = parser.parse_args()

    try:
        lines = read_file(args.source_file)
    except IndexError:
        print("入力ファイルが指定されていません．\n例: python sakana_executor.py output_file.out")
    A, B = None, None
    show_command_and_registers(A, B, lines[0])
    try:
        for i, line in enumerate(lines):
            A, B = bin_exe(A, B, line)
            show_command_and_registers(A, B, line)
    except:
        print('File"'+args.source_file+'", Line',i,'in command',line)
        
