upper_corner = input()
lower_corner = input()

count = len([temp for temp in (upper_corner + lower_corner) if temp == '#'])

if (count == 2 and upper_corner[0] == '#' and lower_corner[1] == '#') or (count == 2 and upper_corner[1] == '#' and lower_corner[0] == '#'): print("No")
else: print("Yes")
