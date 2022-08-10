a, b = map(int, input().split())
c = int(input())

hour = a
minute = b + c

hour += minute // 60
minute %= 60

if hour >= 24:
    hour -= 24
    
print(hour, minute)