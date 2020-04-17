def main():
    global count,penentu
    count = 0
    penentu = 0
    while True:
        f = open('file_to_dec.py').read()
        if 'marshal.loads' in f:
            count += 1
            f = f.replace('exec','x = ')
            d = open('marshall.py','w')
            d.write('from uncompyle6.main import decompile')
            d.write('\nfrom sys import stdout\n')
            d.write(f)
            d.write('\ndecompile(3.7,x,stdout)')
            d.close()
            os.system('python3 marshall.py > file_to_dec.py')
        elif 'exec base64' in f or 'exec(base64' in f:
            count += 1
            x = f.replace('exec','print')
            open('file_base64.py','w').write(x)
            os.system('python3 file_base64.py > file_to_dec.py')
        else:
            penentu += 1
            try:
                os.mkdir('decompile')
            except: pass
            a = open('file.py').read().split('\n')
            x = open('decompile/final.py','w')
            x.write('# AUTO DECOMPILE MARSHAL BY XIUZSEC\n')
            for c in a:
                if '#' not in c:
                    x.write(c)
            x.write('\n# okay, decompile by zettamus ')
            x.close()
            break
def animasi():
    while True:
        for x in list('\ |/-'):
            print(f'\r[{x}] Decompile : {count} ',end='');time.sleep(0.1)
        if penentu == 1:
            break
    print()
    sys.exit()
def chek(data):
    try:
        asw = open(data).read()
    except FileNotFoundError:
        print('[!] File not found ')
        exit()
    if 'marshal.loads' in asw or 'base64' in asw:
        return asw
    else:
        exit('[!] File not support ')
try:
    import os,time,sys
    from threading import *
    print('\n\n\t[ DECOMPILE MARSHALL and BASE64 ]')
    data = input('\n[*] file to dec : ')
    cek = chek(data)
    open('file_to_dec.py','w').write(cek)
    x = Thread(target=main)
    z = Thread(target=animasi)
    x.start()
    z.start()
    sys.exit()
except IOError: pass
