# Sakana Assembler  
簡易的なアセンブラです．

## 命令セット

| | マシンコード | ニーモニック | 意味 |
|---|---|---|---|
|0  |0000 |NOP      | 何もしない |
|1  |0001 |JMP XXXX | XXXXへジャンプ  |
|2  |0010 |JNC XXXX | キャリーフラグが立っていなければXXXXへジャンプ |
|3  |0011 |RND B    | Bレジスタに0~15のランダムな値を入れる |
|4  |0100 |MOV A, 0 | Aレジスタに0を入れる |
|5  |0101 |MOV B, 0 | Bレジスタに0を入れる |
|6  |0110 |MOV A, B | AレジスタにBレジスタの値を入れる |
|7  |0111 |MOV B, A | BレジスタにAレジスタの値を入れる |
|8  |1000 |ADD A, 1 | Aレジスタに1加える |
|9  |1001 |ADD A, 2 | Aレジスタに2加える |
|10 |1010 |ADD A, A | Aレジスタの値を2倍にする |
|11 |1011 |ADD A, B | AレジスタにBレジスタの値を加える |
|12 |1100<br>[1111] |HALT |終了する ※JUMP命令と同じ |
|13 |1101 |未使用    | |
|14 |1110<br>XXXX |LD A, XXXX | Aレジスタに RAM[XXXX] の値を入れる |
|15 |1111<br>XXXX |ST A, XXXX | Aレジスタの値を RAM[XXXX] に入れる |

## `sakana_assembler.py`の使い方
入力するアセンブリファイルを`code.asm`とすると，  
```
$ python sakana_assembler.py code.asm
```  
出力ファイル名が省略されたときは`out.txt`で固定されます。  

出力ファイル名の指定は以下のようにできます
```
$ python sakana_assembler.py code.asm -o output.out
```

### コメント
`#`の後ろは、コメントとして認識されます。
```
MOV A, 0 # line end comment
# line comment
```
以上の二種類のコメントがサポートされています。

### 空行
空行はスキップされます。


## `sakana_executor.py`の使い方
入力するアセンブリファイルを`out.txt`とすると，  
```
$ python sakana_executor.py out.txt
```  

### 表示オプション
デフォルトはレジスタと十進数字をともに表示する

レジスタのビジュアだけを表示したい時
```
$ python sakana_executor.py out.txt --format color
```

レジスタの十進数字だけを表示したい時
```
$ python sakana_executor.py out.txt --format number
```
