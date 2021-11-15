nums = []
print("Input numbers one at a time and stop by entering \'STOP\' when your done we will calculate the average of the numbers")
while True:
    try:
        num = int(input(""))
        nums.append(num)
    except:
        break
for i in range(nums):
    print(i)