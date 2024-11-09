class Solution:
    def second_highest_dict(self, dict1):
        c = 0
        b = 0
        name = []
        
        for k, v in dict1.items():
            if c < v:
                b = c
                c = v
            elif b < v and c != v:
                b = v
                
        for k, v in dict1.items():
            if v == b:
                name.append(k)
        
        n = 0
        m = name[0]
        
        if len(name) > 1:
            while n < len(name):
                if name[n] < 0:
                    m = name[n]
                    n += 1
        return m
        
def main():
    dict1 = {"amol":10, "omkar":9, "omprakash":9, "pallavi":8, "shubham":11}
    obj = Solution()
    obj1 = obj.second_highest_dict(dict1)
    print(obj1)
    
if __name__ == "__main__":
    main()