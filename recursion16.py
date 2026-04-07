def calculate(lst):
    return sum(lst),max(lst),min(lst)

nums=[10,40,30]
s,mx,mn=calculate(nums)
print("sum:",s)
print("Max:",mx)
print("Min:",mn)