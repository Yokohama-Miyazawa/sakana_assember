import sys


def asm_to_bin(asm):
    inst = asm[0:3]
    if inst == "NOP":
        return "0000\n"
    elif inst == "MOV":
        arg0, arg1 = asm[4], asm[7]
        if arg0 == "A" and arg1 == "0":
            return "0100\n"
        elif arg0 == "B" and arg1 == "0":
            return "0101\n"
        elif arg0 == "A" and arg1 == "B":
            return "0110\n"
        elif arg0 == "B" and arg1 == "A":
            return "0111\n"
        else:
            raise Exception
    elif inst == "ADD":
        arg0, arg1 = asm[4], asm[7]
        if arg0 == "A" and arg1 == "1":
            return "1000\n"
        elif arg0 == "A" and arg1 == "2":
            return "1001\n"
        elif arg0 == "A" and arg1 == "A":
            return "1010\n"
        elif arg0 == "A" and arg1 == "B":
            return "1011\n"
        else:
            raise Exception
    else:
        raise Exception


def assemble(input_file_name):
    try:
        f = open(input_file_name)
        o = open("out.txt", "w", encoding="UTF-8")
    except FileNotFoundError:
        print("{}というファイルは存在しません．".format(input_file_name))
    else:
        try:
            for line in f:
                if '#' == line[0]:
                    print('comment:',line, end='')
                    continue
                if '#' in line:
                    tmp = line.split('#')
                    line, comment = tmp[0], tmp[1]
                    print('comment:' ,comment, end='')
                else:
                    pass
                bin_code = asm_to_bin(line)
                print(bin_code[:-1], end=' ')
                print(line[:-1])
                o.write(bin_code)
                bin_code = asm_to_bin(line)
                print(bin_code[:-1], end=' ')
                print(line, end='')
                o.write(bin_code)
        finally:
            f.close()
            o.close()


if __name__ == '__main__':
    args = sys.argv

    try:
        input_file_name = args[1]
    except IndexError:
        print("入力ファイルが指定されていません．\n例: python sakana_assembler.py code.asm")
    else:
        print(input_file_name)
        assemble(input_file_name)
