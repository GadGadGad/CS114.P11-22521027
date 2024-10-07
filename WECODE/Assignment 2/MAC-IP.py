import re, sys
# Format lay tu https://stackoverflow.com/questions/4260467/what-is-a-regular-expression-for-a-mac-address
macFormat = re.compile(r'^([0-9A-F]{2}[:-]){5}([0-9A-F]{2})$')

while True:
        choose = sys.stdin.readline().strip()
        if choose == '.' or choose == '':
            break
        result = macFormat.match(choose)
        print('true' if result is not None else 'false')
        
    