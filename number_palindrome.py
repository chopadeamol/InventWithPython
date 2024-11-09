class Solution:
    def is_palindrome_num(self, num):
        if num < 0:
            return False
        if num == 0:
            return True
            
        num = str(num)
        num1 = ""
        
        for i in num[::-1]:
            num1 += i
            
        if num == num1:
            return True
        else:
            return False
            
def main():
    num = 121
    obj = Solution().is_palindrome_num(num)
    print(obj)
    
if __name__ == "__main__":
    main()
    
        
            