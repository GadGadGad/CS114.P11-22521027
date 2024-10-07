import sys

server = {}

while True:
    choose = sys.stdin.readline()
    if choose == '0':
        break
    if choose != '':
        choose = choose.split()
        if choose[0] == '1':
            server[int(choose[1])] = True 
        elif choose[0] == '2':
            print(1 if server.get(int(choose[1]), False) else 0)
        elif choose[0] == '3':
            server[int(choose[1])] = False