# 1bit と 2bit のシフトを観察する
MOV A, 0 # A = 0
MOV B, 0
# shift 1 bit
ADD A, 1
ADD A, A
ADD A, A
MOV B, A # shore A to B
ADD A, A
ADD A, A
# shift 2 bit
ADD A, 1
ADD A, 2
ADD A, A
ADD A, A
ADD A, A
ADD A, A