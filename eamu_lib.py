_key = [
    0x20d0d03c, 0x868ecb41, 0xbcd89c84, 0x4c0e0d0d,
    0x84fc30ac, 0x4cc1890e, 0xfc5418a4, 0x02c50f44,
    0x68acb4e0, 0x06cd4a4e, 0xcc28906c, 0x4f0c8ac0,
    0xb03ca468, 0x884ac7c4, 0x389490d8, 0xcf80c6c2,
    0x58d87404, 0xc48ec444, 0xb4e83c50, 0x498d0147,
    0x64f454c0, 0x4c4701c8, 0xec302cc4, 0xc6c949c1,
    0xc84c00f0, 0xcdcc49cc, 0x883c5cf4, 0x8b0fcb80,
    0x703cc0b0, 0xcb820a8d, 0x78804c8c, 0x4fca830e,
    0x80d0f03c, 0x8ec84f8c, 0x98c89c4c, 0xc80d878f,
    0x54bc949c, 0xc801c5ce, 0x749078dc, 0xc3c80d46,
    0x2c8070f0, 0x0cce4dcf, 0x8c3874e4, 0x8d448ac3,
    0x987cac70, 0xc0c20ac5, 0x288cfc78, 0xc28543c8,
    0x4c8c7434, 0xc50e4f8d, 0x8468f4b4, 0xcb4a0307,
    0x2854dc98, 0x48430b45, 0x6858fce8, 0x4681cd49,
    0xd04808ec, 0x458d0fcb, 0xe0a48ce4, 0x880f8fce,
    0x7434b8fc, 0xce080a8e, 0x5860fc6c, 0x46c886cc,
    0xd01098a4, 0xce090b8c, 0x1044cc2c, 0x86898e0f,
    0xd0809c3c, 0x4a05860f, 0x54b4f80c, 0x4008870e,
    0x1480b88c, 0x0ac8854f, 0x1c9034cc, 0x08444c4e,
    0x0cb83c64, 0x41c08cc6, 0x1c083460, 0xc0c603ce,
    0x2ca0645c, 0x818246cb, 0x0408e454, 0xc5464487,
    0x88607c18, 0xc1424187, 0x284c7c90, 0xc1030509,
    0x40486c94, 0x4603494b, 0xe0404ce4, 0x4109094d,
    0x60443ce4, 0x4c0b8b8d, 0xe054e8bc, 0x02008e89
]

_lut_a0 = [
    0x02080008, 0x02082000, 0x00002008, 0x00000000,
    0x02002000, 0x00080008, 0x02080000, 0x02082008,
    0x00000008, 0x02000000, 0x00082000, 0x00002008,
    0x00082008, 0x02002008, 0x02000008, 0x02080000,
    0x00002000, 0x00082008, 0x00080008, 0x02002000,
    0x02082008, 0x02000008, 0x00000000, 0x00082000,
    0x02000000, 0x00080000, 0x02002008, 0x02080008,
    0x00080000, 0x00002000, 0x02082000, 0x00000008,
    0x00080000, 0x00002000, 0x02000008, 0x02082008,
    0x00002008, 0x02000000, 0x00000000, 0x00082000,
    0x02080008, 0x02002008, 0x02002000, 0x00080008,
    0x02082000, 0x00000008, 0x00080008, 0x02002000,
    0x02082008, 0x00080000, 0x02080000, 0x02000008,
    0x00082000, 0x00002008, 0x02002008, 0x02080000,
    0x00000008, 0x02082000, 0x00082008, 0x00000000,
    0x02000000, 0x02080008, 0x00002000, 0x00082008
]

_lut_a1 = [
    0x08000004, 0x00020004, 0x00000000, 0x08020200,
    0x00020004, 0x00000200, 0x08000204, 0x00020000,
    0x00000204, 0x08020204, 0x00020200, 0x08000000,
    0x08000200, 0x08000004, 0x08020000, 0x00020204,
    0x00020000, 0x08000204, 0x08020004, 0x00000000,
    0x00000200, 0x00000004, 0x08020200, 0x08020004,
    0x08020204, 0x08020000, 0x08000000, 0x00000204,
    0x00000004, 0x00020200, 0x00020204, 0x08000200,
    0x00000204, 0x08000000, 0x08000200, 0x00020204,
    0x08020200, 0x00020004, 0x00000000, 0x08000200,
    0x08000000, 0x00000200, 0x08020004, 0x00020000,
    0x00020004, 0x08020204, 0x00020200, 0x00000004,
    0x08020204, 0x00020200, 0x00020000, 0x08000204,
    0x08000004, 0x08020000, 0x00020204, 0x00000000,
    0x00000200, 0x08000004, 0x08000204, 0x08020200,
    0x08020000, 0x00000204, 0x00000004, 0x08020004
]

_lut_a2 = [
    0x80040100, 0x01000100, 0x80000000, 0x81040100,
    0x00000000, 0x01040000, 0x81000100, 0x80040000,
    0x01040100, 0x81000000, 0x01000000, 0x80000100,
    0x81000000, 0x80040100, 0x00040000, 0x01000000,
    0x81040000, 0x00040100, 0x00000100, 0x80000000,
    0x00040100, 0x81000100, 0x01040000, 0x00000100,
    0x80000100, 0x00000000, 0x80040000, 0x01040100,
    0x01000100, 0x81040000, 0x81040100, 0x00040000,
    0x81040000, 0x80000100, 0x00040000, 0x81000000,
    0x00040100, 0x01000100, 0x80000000, 0x01040000,
    0x81000100, 0x00000000, 0x00000100, 0x80040000,
    0x00000000, 0x81040000, 0x01040100, 0x00000100,
    0x01000000, 0x81040100, 0x80040100, 0x00040000,
    0x81040100, 0x80000000, 0x01000100, 0x80040100,
    0x80040000, 0x00040100, 0x01040000, 0x81000100,
    0x80000100, 0x01000000, 0x81000000, 0x01040100
]

_lut_a3 = [
    0x04010801, 0x00000000, 0x00010800, 0x04010000,
    0x04000001, 0x00000801, 0x04000800, 0x00010800,
    0x00000800, 0x04010001, 0x00000001, 0x04000800,
    0x00010001, 0x04010800, 0x04010000, 0x00000001,
    0x00010000, 0x04000801, 0x04010001, 0x00000800,
    0x00010801, 0x04000000, 0x00000000, 0x00010001,
    0x04000801, 0x00010801, 0x04010800, 0x04000001,
    0x04000000, 0x00010000, 0x00000801, 0x04010801,
    0x00010001, 0x04010800, 0x04000800, 0x00010801,
    0x04010801, 0x00010001, 0x04000001, 0x00000000,
    0x04000000, 0x00000801, 0x00010000, 0x04010001,
    0x00000800, 0x04000000, 0x00010801, 0x04000801,
    0x04010800, 0x00000800, 0x00000000, 0x04000001,
    0x00000001, 0x04010801, 0x00010800, 0x04010000,
    0x04010001, 0x00010000, 0x00000801, 0x04000800,
    0x04000801, 0x00000001, 0x04010000, 0x00010800
]

_lut_b0 = [
    0x00000400, 0x00000020, 0x00100020, 0x40100000,
    0x40100420, 0x40000400, 0x00000420, 0x00000000,
    0x00100000, 0x40100020, 0x40000020, 0x00100400,
    0x40000000, 0x00100420, 0x00100400, 0x40000020,
    0x40100020, 0x00000400, 0x40000400, 0x40100420,
    0x00000000, 0x00100020, 0x40100000, 0x00000420,
    0x40100400, 0x40000420, 0x00100420, 0x40000000,
    0x40000420, 0x40100400, 0x00000020, 0x00100000,
    0x40000420, 0x00100400, 0x40100400, 0x40000020,
    0x00000400, 0x00000020, 0x00100000, 0x40100400,
    0x40100020, 0x40000420, 0x00000420, 0x00000000,
    0x00000020, 0x40100000, 0x40000000, 0x00100020,
    0x00000000, 0x40100020, 0x00100020, 0x00000420,
    0x40000020, 0x00000400, 0x40100420, 0x00100000,
    0x00100420, 0x40000000, 0x40000400, 0x40100420,
    0x40100000, 0x00100420, 0x00100400, 0x40000400
]

_lut_b1 = [
    0x00800000, 0x00001000, 0x00000040, 0x00801042,
    0x00801002, 0x00800040, 0x00001042, 0x00801000,
    0x00001000, 0x00000002, 0x00800002, 0x00001040,
    0x00800042, 0x00801002, 0x00801040, 0x00000000,
    0x00001040, 0x00800000, 0x00001002, 0x00000042,
    0x00800040, 0x00001042, 0x00000000, 0x00800002,
    0x00000002, 0x00800042, 0x00801042, 0x00001002,
    0x00801000, 0x00000040, 0x00000042, 0x00801040,
    0x00801040, 0x00800042, 0x00001002, 0x00801000,
    0x00001000, 0x00000002, 0x00800002, 0x00800040,
    0x00800000, 0x00001040, 0x00801042, 0x00000000,
    0x00001042, 0x00800000, 0x00000040, 0x00001002,
    0x00800042, 0x00000040, 0x00000000, 0x00801042,
    0x00801002, 0x00801040, 0x00000042, 0x00001000,
    0x00001040, 0x00801002, 0x00800040, 0x00000042,
    0x00000002, 0x00001042, 0x00801000, 0x00800002
]

_lut_b2 = [
    0x10400000, 0x00404010, 0x00000010, 0x10400010,
    0x10004000, 0x00400000, 0x10400010, 0x00004010,
    0x00400010, 0x00004000, 0x00404000, 0x10000000,
    0x10404010, 0x10000010, 0x10000000, 0x10404000,
    0x00000000, 0x10004000, 0x00404010, 0x00000010,
    0x10000010, 0x10404010, 0x00004000, 0x10400000,
    0x10404000, 0x00400010, 0x10004010, 0x00404000,
    0x00004010, 0x00000000, 0x00400000, 0x10004010,
    0x00404010, 0x00000010, 0x10000000, 0x00004000,
    0x10000010, 0x10004000, 0x00404000, 0x10400010,
    0x00000000, 0x00404010, 0x00004010, 0x10404000,
    0x10004000, 0x00400000, 0x10404010, 0x10000000,
    0x10004010, 0x10400000, 0x00400000, 0x10404010,
    0x00004000, 0x00400010, 0x10400010, 0x00004010,
    0x00400010, 0x00000000, 0x10404000, 0x10000010,
    0x10400000, 0x10004010, 0x00000010, 0x00404000
]

_lut_b3 = [
    0x00208080, 0x00008000, 0x20200000, 0x20208080,
    0x00200000, 0x20008080, 0x20008000, 0x20200000,
    0x20008080, 0x00208080, 0x00208000, 0x20000080,
    0x20200080, 0x00200000, 0x00000000, 0x20008000,
    0x00008000, 0x20000000, 0x00200080, 0x00008080,
    0x20208080, 0x00208000, 0x20000080, 0x00200080,
    0x20000000, 0x00000080, 0x00008080, 0x20208000,
    0x00000080, 0x20200080, 0x20208000, 0x00000000,
    0x00000000, 0x20208080, 0x00200080, 0x20008000,
    0x00208080, 0x00008000, 0x20000080, 0x00200080,
    0x20208000, 0x00000080, 0x00008080, 0x20200000,
    0x20008080, 0x20000000, 0x20200000, 0x00208000,
    0x20208080, 0x00008080, 0x00208000, 0x20200080,
    0x00200000, 0x20000080, 0x20008000, 0x00000000,
    0x00008000, 0x00200000, 0x20200080, 0x00208080,
    0x20000000, 0x20208000, 0x00000080, 0x20008080
]

_valid_chars = "0123456789ABCDEFGHJKLMNPRSTUWXYZ";

def typeFromCardID(cardID:str):
    match cardID[:2]:
        case 'E0':
            return 1
        case '01':
            return 2
        case _:
            return 2

def encodeCardID(cardID:str):
    if len(cardID) != 16:
        raise Exception(f'cardID가 16자가 아닌 {len(cardID)}자입니다. 확인 후 다시 입력해주세요.')
    
    cardType = typeFromCardID(cardID)
    cardint = []
    cardID = int(cardID,16)
    for i in range(8):
        cardint.append(cardID & 0xff)
        cardID >>= 8 
    
    ciphered = encode(cardint)
    
    #print(ciphered)
    
    bits = [0 for i in range(65)]
    for i in range(64):
        bits[i] = (ciphered[i >> 3] >> (~i & 7)) & 1
        
    #print(bits)
    
    groups = [0 for i in range(16)]
    for i in range(13):
        groups[i] = (bits[i*5+0] << 4) | (bits[i*5+1] << 3) | (bits[i*5+2] << 2) | (bits[i*5+3] << 1) | (bits[i*5+4] << 0)
    
    #print(groups)
    
    groups[13] = 1
    groups[0] ^= cardType
    
    #print(groups)
    
    for i in range(14):
        index = len(groups)-1 if i==0 else i-1
        xor_calc = groups[i] ^ groups[index]
        groups[i] = xor_calc
        #print(groups, i, index, xor_calc)
    
    groups[14] = cardType
    groups[15] = checksum(groups)
    
    #print(groups)
    
    result = ''
    for i in range(len(groups)):
        result += _valid_chars[groups[i]]
    
    return result

def decodeCardID(cardID:str):
    if len(cardID) != 16:
        raise Exception(f'cardID가 16자가 아닌 {len(cardID)}자입니다. 확인 후 다시 입력해주세요.')
    
    for i in range(len(cardID)):
        if cardID[i] not in _valid_chars:
            raise Exception(f'{i+1}번째 글자 {cardID[i]}가 유효하지 않은 글자입니다. 확인 후 다시 입력해주세요.')
    
    groups = []
    for chars in cardID:
        groups.append(_valid_chars.find(chars))
    
    if groups[14] != 1 and groups[14] != 2:
        raise Exception(f'카드 번호의 15번째 자리에 있는 카드 종류가 유효하지 않습니다. 1 또는 2여야 하는데 {groups[14]}가 입력되었습니다.')
    
    if groups[15] != checksum(groups):
        raise Exception(f'체크섬이 유효하지 않습니다. 카드 번호가 잘못되었을 가능성이 있습니다. 테스트 중인 경우, 유효한 체크섬은 {checksum(groups)}입니다.')
    
    for i in range(13,0,-1):
        groups[i] ^= groups[i-1]
    groups[0] ^= groups[14]
    
    bits = [0 for i in range(65)]
    for i in range(64):
        bits[i] = (groups[int(i / 5)] >> (4 - (i % 5))) & 1
    
    ciphered = [0 for i in range(8)]
    for i in range(64):
        ciphered[(int(i / 8))] |= int(bits[i] << (~i & 7))
    
    deciphered = decode(ciphered)
    deciphered.reverse()
    
    finalValue = ''
    for i in range(len(deciphered)):
        finalValue += format(deciphered[i],'x').zfill(2)
    
    cardType = typeFromCardID(finalValue)
    if groups[14] != cardType:
        raise Exception('디코딩 이후의 카드 종류가 원래의 카드 종류와 일치하지 않습니다.')
    
    return finalValue

def decodeCardIDFromGroup(groups:str):
    # 카드번호는 내가 잘 입력할 거고 카드번호는 어짜피 여기서 오류날거라 없앰
    if groups[15] != checksum(groups):
        raise Exception(f'체크섬이 유효하지 않습니다. 카드 번호가 잘못되었을 가능성이 있습니다. 테스트 중인 경우, 유효한 체크섬은 {checksum(groups)}입니다.')
    
    for i in range(13,0,-1):
        groups[i] ^= groups[i-1]
    groups[0] ^= groups[14]
    
    bits = [0 for i in range(65)]
    for i in range(64):
        bits[i] = (groups[int(i / 5)] >> (4 - (i % 5))) & 1
    
    ciphered = [0 for i in range(8)]
    for i in range(64):
        ciphered[(int(i / 8))] |= int(bits[i] << (~i & 7))
    
    deciphered = decode(ciphered)
    deciphered.reverse()
    
    finalValue = ''
    for i in range(len(deciphered)):
        finalValue += format(deciphered[i],'x').zfill(2)
    
    #카드타입 체크도 어짜피 앞쪽에서 012e 아니면 걸러서 없앰
    
    return finalValue

def checksum(data):
    checksum = 0;
    for i in range(15):
        checksum += (i % 3 + 1) * data[i]
    
    while checksum >= 0x20:
        checksum = (checksum & 0x1F) + (checksum >> 5)
    
    return checksum;

def encode(inputList):
    if len(inputList) != 8:
        raise Exception(f'encode 함수에서 8바이트 리스트를 받아야 하지만 {len(inputList)} 길이의 리스트를 받았습니다. 카드 번호가 잘못 되었을 가능성이 있습니다.')
    
    output = [None for i in range(8)]
    
    fromInt(output, operatorA(0x00, toInt(inputList)))
    fromInt(output, operatorB(0x20, toInt(output)))
    fromInt(output, operatorA(0x40, toInt(output)))
    
    return output

def decode(inputList):
    if len(inputList) != 8:
        raise Exception(f'decode 함수에서 8바이트 리스트를 받아야 하지만 {len(inputList)} 길이의 리스트를 받았습니다. 카드 번호가 잘못 되었을 가능성이 있습니다.')
    
    output = [None for i in range(8)]
    
    fromInt(output, operatorB(0x40, toInt(inputList)))
    fromInt(output, operatorA(0x20, toInt(output)))
    fromInt(output, operatorB(0x00, toInt(output)))
    
    return output

def toInt(data):
    inX = (data[0] & 0xFF) | ((data[1] & 0xFF) << 8) | ((data[2] & 0xFF) << 16) | ((data[3] & 0xFF) << 24)

    inY = (data[4] & 0xFF) | ((data[5] & 0xFF) << 8) | ((data[6] & 0xFF) << 16) | ((data[7] & 0xFF) << 24)

    v7 = ((((inX ^ (inY >> 4)) & 0xF0F0F0F) << 4) ^ inY) & 0xFFFFFFFF
    v8 = (((inX ^ (inY >> 4)) & 0xF0F0F0F) ^ inX) & 0xFFFFFFFF

    v9 = ((v7 ^ (v8 >> 16))) & 0x0000FFFF
    v10 = (((v7 ^ (v8 >> 16)) << 16) ^ v8) & 0xFFFFFFFF

    v11 = (v9 ^ v7) & 0xFFFFFFFF
    v12 = (v10 ^ (v11 >> 2)) & 0x33333333
    v13 = (v11 ^ (v12 << 2)) & 0xFFFFFFFF

    v14 = (v12 ^ v10) & 0xFFFFFFFF
    v15 = (v13 ^ (v14 >> 8)) & 0x00FF00FF
    v16 = (v14 ^ (v15 << 8)) & 0xFFFFFFFF

    v17 = ROR(v15 ^ v13, 1)
    v18 = (v16 ^ v17) & 0x55555555

    v3 = ROR(v18 ^ v16, 1)
    v4 = (v18 ^ v17) & 0xFFFFFFFF

    result = ((v3 & 0xFFFFFFFF) << 32) | (v4 & 0xFFFFFFFF)
    return result

def fromInt(data, state):
    v3 = (state >> 32) & 0xFFFFFFFF
    v4 = state & 0xFFFFFFFF

    v22 = ROR(v4, 31)
    v23 = (v3 ^ v22) & 0x55555555
    v24 = (v23 ^ v22) & 0xFFFFFFFF

    v25 = ROR(v23 ^ v3, 31)
    v26 = (v25 ^ (v24 >> 8)) & 0x00FF00FF
    v27 = (v24 ^ (v26 << 8)) & 0xFFFFFFFF

    v28 = (v26 ^ v25) & 0xFFFFFFFF
    v29 = ((v28 >> 2) ^ v27) & 0x33333333
    v30 = ((v29 << 2) ^ v28) & 0xFFFFFFFF

    v31 = (v29 ^ v27) & 0xFFFFFFFF
    v32 = (v30 ^ (v31 >> 16)) & 0x0000FFFF
    v33 = (v31 ^ (v32 << 16)) & 0xFFFFFFFF

    v34 = (v32 ^ v30) & 0xFFFFFFFF
    v35 = (v33 ^ (v34 >> 4)) & 0xF0F0F0F

    outY = ((v35 << 4) ^ v34) & 0xFFFFFFFF
    outX = (v35 ^ v33) & 0xFFFFFFFF

    data[0] = int(outX & 0xFF)
    data[1] = int((outX >> 8) & 0xFF)
    data[2] = int((outX >> 16) & 0xFF)
    data[3] = int((outX >> 24) & 0xFF)
    data[4] = int(outY & 0xFF)
    data[5] = int((outY >> 8) & 0xFF)
    data[6] = int((outY >> 16) & 0xFF)
    data[7] = int((outY >> 24) & 0xFF)

def operatorA(off, state):
    v3 = (state >> 32) & 0xFFFFFFFF
    v4 = state & 0xFFFFFFFF
    
    for i in range(0,32,4):
        v20 = ROR(v3 ^ _key[off + i + 1], 28)
        
        v4 ^= _lut_b0[(v20 >> 26) & 0x3F] ^ _lut_b1[(v20 >> 18) & 0x3F] ^ \
              _lut_b2[(v20 >> 10) & 0x3F] ^ _lut_b3[(v20 >> 2) & 0x3F] ^ \
              _lut_a0[((v3 ^ _key[off + i]) >> 26) & 0x3F] ^ _lut_a1[((v3 ^ _key[off + i]) >> 18) & 0x3F] ^ \
              _lut_a2[((v3 ^ _key[off + i]) >> 10) & 0x3F] ^ _lut_a3[((v3 ^ _key[off + i]) >> 2) & 0x3F]
        
        v21 = ROR(v4 ^ _key[off + i + 3], 28);
        
        v3 ^= _lut_b0[(v21 >> 26) & 0x3F] ^ _lut_b1[(v21 >> 18) & 0x3F] ^ \
              _lut_b2[(v21 >> 10) & 0x3F] ^ _lut_b3[(v21 >> 2) & 0x3F] ^ \
              _lut_a0[((v4 ^ _key[off + i + 2]) >> 26) & 0x3F] ^ _lut_a1[((v4 ^ _key[off + i + 2]) >> 18) & 0x3F] ^ \
              _lut_a2[((v4 ^ _key[off + i + 2]) >> 10) & 0x3F] ^ _lut_a3[((v4 ^ _key[off + i + 2]) >> 2) & 0x3F]
    
    result = ((v3 & 0xFFFFFFFF) << 32) | (v4 & 0xFFFFFFFF)
    return result

def operatorB(off, state):
    v3 = (state >> 32) & 0xFFFFFFFF
    v4 = state & 0xFFFFFFFF
    
    for i in range(0,32,4):
        v20 = ROR(v3 ^ _key[off + 31 - i], 28)
        
        v4 ^= _lut_a0[((v3 ^ _key[off + 30 - i]) >> 26) & 0x3F] ^ _lut_a1[((v3 ^ _key[off + 30 - i]) >> 18) & 0x3F] ^ \
              _lut_a2[((v3 ^ _key[off + 30 - i]) >> 10) & 0x3F] ^ _lut_a3[((v3 ^ _key[off + 30 - i]) >> 2) & 0x3F] ^  \
              _lut_b0[(v20 >> 26) & 0x3F] ^ _lut_b1[(v20 >> 18) & 0x3F] ^ \
              _lut_b2[(v20 >> 10) & 0x3F] ^ _lut_b3[(v20 >> 2) & 0x3F]
        
        v21 = ROR(v4 ^ _key[off + 29 - i], 28)
        
        v3 ^= _lut_a0[((v4 ^ _key[off + 28 - i]) >> 26) & 0x3F] ^ _lut_a1[((v4 ^ _key[off + 28 - i]) >> 18) & 0x3F] ^ \
              _lut_a2[((v4 ^ _key[off + 28 - i]) >> 10) & 0x3F] ^ _lut_a3[((v4 ^ _key[off + 28 - i]) >> 2) & 0x3F] ^ \
              _lut_b0[(v21 >> 26) & 0x3F] ^ _lut_b1[(v21 >> 18) & 0x3F] ^ \
              _lut_b2[(v21 >> 10) & 0x3F] ^ _lut_b3[(v21 >> 2) & 0x3F]
        
    return ((v3 & 0xFFFFFFFF) << 32) | (v4 & 0xFFFFFFFF)

def ROR(val, amount):
    return ((val << (32 - amount)) & 0xFFFFFFFF) | ((val >> amount) & 0xFFFFFFFF)