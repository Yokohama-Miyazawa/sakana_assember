import sys
import argparse


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


def assemble(input_file_name, output_file_name='out.txt'):
    try:
        f = open(input_file_name)
        o = open(output_file_name, "w", encoding="UTF-8")
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
        finally:
            f.close()
            o.close()


if __name__ == '__main__':
    #args = sys.argv
    parser = argparse.ArgumentParser()
    parser.add_argument("source_file", type=str,
                                help="入力ファイルのファイル名を指定")
    parser.add_argument("-o", "--output", type=str,
                                help="出力ファイルのファイル名を指定、指定しない時のデフォルトは`out.txt`")
    args = parser.parse_args()

    print(args)

    try:
        if args.output != None:
            assemble(args.source_file, args.output)
        else:
            assemble(args.source_file)
    except:
        print("形式に沿って実行してください\n例: python sakana_assembler.py code.asm")


