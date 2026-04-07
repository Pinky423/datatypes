def digit_sum(n):
    if n < 10:
        return n
    
    s = 0
    while n > 0:
        s = s + (n % 10)   # last digit add
        n = n // 10        # last digit remove
    
    return digit_sum(s)

print(digit_sum(987))