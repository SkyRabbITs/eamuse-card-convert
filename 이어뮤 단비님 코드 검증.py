from multiprocessing import Pool
from multiprocessing import shared_memory
from eamu_lib import *

def on_error(result):
    pass

def on_done(result):
    pass

if __name__ == '__main__':
    mode = int(input('모드 선택 (1 검증 2 SSID) : '))
    if mode == 1:
        errorlist = ['문제가 있는 카드 번호']
        while True:
            cardID = input('카드 번호 입력 : ')
            if cardID == 'q':
                print('\n'.join(errorlist))
                break
            cardID = cardID.upper()
            cardID = cardID.replace(':','')
            cardID = cardID.replace(' ','')
            cardID = cardID.replace('-','')
            cardID = cardID.replace('I','1')
            cardID = cardID.replace('O','0')
            if cardID != encodeCardID(decodeCardID(cardID)):
                errorlist.append('cardID')
    else:
        ssidlist = ['SSID 목록']
        while True:
            cardID = input('카드 번호 입력 : ')
            if cardID == 'q':
                print('\n'.join(ssidlist))
                break
            cardID = cardID.upper()
            cardID = cardID.replace(':','')
            cardID = cardID.replace(' ','')
            cardID = cardID.replace('-','')
            cardID = cardID.replace('I','1')
            cardID = cardID.replace('O','0')
            ssid = decodeCardID(cardID)
            ssidlist.append(f'{ssid[0:4]}:{ssid[4:8]}:{ssid[8:12]}:{ssid[12:16]}')