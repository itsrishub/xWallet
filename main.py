from bit import Key
from bit import wif_to_key
import os
import gc


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def writeKey(content=''):
    with open('key', 'w') as keyfl:
        keyfl.write(content)
        keyfl.close()


def login(firsttime=False):
    if firsttime:
        authkey = input("Enter you auth key: ")
        clear()
        writeKey(content=authkey)
    key = wif_to_key(open('key').read())
    print(f'BTC address: {key.address}\n')
    usd = key.get_balance('usd')
    btc = key.get_balance('btc')
    print(f"Balance: {usd} USD | {btc} BTC")
    # transfer(key, usd, btc)


def register():
    clear()
    key = Key()
    authkey = key.to_wif()
    print(f'Your super secret auth key: {authkey}')
    print('Please save your auth key safely!\n\n')
    writeKey(content=authkey)
    login()

def transfer(key, usd, btc):
    if btc != '0'  or usd != '0':
        targetwallet = input("Enter target wallet: ")
        amountasbtc = input("Amount to send in BTC: ")
        if int(amountasbtc) <= int(btc):
            key = Key(key)
            key.get_unspents()
            x = key.send([(targetwallet, amountasbtc, 'btc')], fee=100)
            print(x)
        else:
            print('Not enough funds in wallet!')


def main():
    if not os.path.isfile('key'):
        writeKey()
    if os.stat('key').st_size == 0:
        opt = input('For login press 1\nFor sign up press 2\n\n>>')
        if opt == '1':
            login(firsttime=True)
        elif opt == '2':
            register()
        else:
            input('Invalid choice!\n\nPress enter to exit..')
    else:
        try:
            login()
        except Exception as e:
            writeKey()
            main()


if __name__ == '__main__':
    main()
    # L3j75QyQjSKZJaMMw3CqmtjHJcZznTbrqYXZWiPwcEKRJMYEcDj5
