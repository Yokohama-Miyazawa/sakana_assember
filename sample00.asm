MOV A, 0 # line end comment
# line comment
MOV B, 0
ADD A, 1
ADD A, A
ADD A, 1
ADD A, A
MOV B, A # copy A register bit pattern to B
ADD A, 1
ADD A, A
ADD A, 1
ADD A, A
ADD A, 1
ADD A, 1
ADD A, 1
MOV B, A
ADD A, 1
ADD A, 1
MOV A, B # copy B register bit pattern to A

