def calc_median(nums):
    if( (len(nums) / 2) == 1):
        return ((len(nums) / 2) + 1)
    else:
        return round(((len(nums) / 2 ) + (len(nums) / 2 + 1)) / 2 )

def work_with_file(nums):
    name_file = str(input())
    f = open(name_file, 'r', encoding='utf-8')
    for i in f: 
        nums.append(int(i))
    f.close()

def main():
    nums = []
    sum = 0

    work_with_file(nums)

    mediana = calc_median(nums)
    
    for i in range(len(nums)):
        sum = sum + abs(nums[i] - mediana)

    print(sum)

main()
