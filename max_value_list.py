class Solution:
    def max_list(self,list1):
        first = 0
        second = 0
        max_value = 0
        
        for i in range(len(list1)-1):
            first = list1[i]
            second = list1[i+1]
            if first > second:
                max_value = first
                
        """Second Way"""
        a = 0
        b = 0
        for i in list1:
            if i > a:
                a = i
            if i < b:
                b = i
        print("max:",a)
        print("min:",b)
        
        return max_value
        
def main():
    list1 = [1,2,0,-1,5,9,10,-5]
    obj = Solution().max_list(list1)
    print(obj)
    
if __name__ == "__main__":
    main()
        