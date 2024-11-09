class Solution:

    def twoSum(self, num_list, target):
    
        for i in range(len(num_list)):
            for j in range(i+1, len(num_list)):
                if num_list[i] + num_list[j] == target:
                    return [i, j]
                    
def main():

    num_list = [9,3,6,3,5,2,7,3]
    target = 10
    obj = Solution()
    obj1 = obj.twoSum(num_list, target)
    print(obj1)
    
if __name__ == "__main__":
    main()