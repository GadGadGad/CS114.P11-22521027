import sys
input = sys.stdin.read().strip()

if input == \
'''
    #.
    .#
    '''.strip() \
    or input == \
    '''
    .#
    #.
    '''.strip() or input.count('#') < 2: print("No")
else : print("Yes")