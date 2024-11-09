class Solution:
    def make_dict(self, strs):
        str1 = strs.split()
        sum_v = {}
        
        for i in range(0,len(str1),2):
            k = str1[i]
            v = int(str1[i+1])
            
            if k in sum_v:
                sum_v[k] += v
            else:
                sum_v[k] = v
            
        return sum_v
        
def main():
    text = """
        item1 10
        item2 27
        item1 -5
        item3 21
        item3 -7
        item2 5
        item4 22
        """
    obj = Solution().make_dict(text)
    print(obj)
    
if __name__ == "__main__":
    main()
            