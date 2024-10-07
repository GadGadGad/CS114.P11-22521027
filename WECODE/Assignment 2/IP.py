# Code lay y tuong tu bai tap backtracking cua mon PTTKTT

def is_valid(s):
    if not s or len(s) > 3:
        return False
    if len(s) == 3 and int(s) > 255:
        return False
    if len(s) > 1 and s[0] == '0':
        return False
    return True

def check_final(u, v):
    return u.replace('.', '') == v

def output_solution(solution):
    print(solution)

def ip_address(i, start, ip, solution):
    if i == 4:
        if check_final(solution, ip):
            output_solution(solution[:-1])
        return

    for j in range(start, min(start + 3, len(ip))):
        check_string = ip[start:j + 1]
        if is_valid(check_string):
            temp = solution
            solution += check_string + '.'
            ip_address(i + 1, j + 1, ip, solution)
            solution = temp

ip = input().strip()
ip_address(0, 0, ip, "")

