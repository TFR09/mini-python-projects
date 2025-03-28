def cumulative():
    num = 0
    nums = []
    while num >= 0:
        num = int(input("Enter an unsigned integer (or -1 to finish): "))
        nums.append(num)
        if num < 0:
        nums.remove(num)
    
    print("Cumulative Values:")
    total = 0
    for i in range(len(nums)):
        total += nums[i]
        print(total)


if __name__ =="__main__":
    cumulative()