def AND_gate(x1, x2):
    W = [0.5, 0.5]
    b = -0.7
    result = x1*W[0] + x2*W[1] + b
    if result <= 0:
        return 0
    else:
        return 1


def NAND_gate(x1, x2):
    W = [-0.5, -0.5]
    b = 0.7
    result = x1*W[0] + x2*W[1] + b
    if result <= 0:
        return 0
    else:
        return 1


def OR_gate(x1, x2):
    W = [0.6,  0.6]
    b = -0.5
    result = x1*W[0] + x2*W[1] + b
    if result <= 0:
        return 0
    else:
        return 1


X = [(0, 0), (0, 1), (1, 0), (1, 1)]
and_result = [AND_gate(x1, x2) for x1, x2 in X]
nand_result = [NAND_gate(x1, x2) for x1, x2 in X]
or_result = [OR_gate(x1, x2) for x1, x2 in X]

print("AND  게이트:", and_result)
print("NAND 게이트:", nand_result)
print("OR   게이트:", or_result)


def XOR_gate(x1, x2):
    # 은닉층
    nand_gate_result = NAND_gate(x1, x2)
    or_gate_result = OR_gate(x1, x2)
    S = (nand_gate_result, or_gate_result)

    # 출력층
    result = AND_gate(S[0], S[1])
    if result <= 0:
        return 0
    else:
        return 1


xor_result = [XOR_gate(x1, x2) for x1, x2 in X]
print("XOR  게이트:", xor_result)
