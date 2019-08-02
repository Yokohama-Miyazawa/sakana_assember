# ２つのレジスタを使って、足し算を試みる
MOV A, 0
MOV B, 0
ADD A, 1
ADD A, 2
MOV B, A
MOV A, 0
ADD A, 2
ADD A, B
