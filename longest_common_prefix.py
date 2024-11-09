class Solution:
    def longestCommonPrefix(self, strs):
        result = ""
        str1 = sorted(strs)
        first = str1[0]
        last = str1[-1]
        
        for i in range(min(len(first),len(last))):
            if first[i] != last[i]:
                return result
            result += first[i]
        return result
        
def main():
    strs = ["flower", "flow", "flight"]
    
    obj = Solution().longestCommonPrefix(strs)
    print(obj)

if __name__ == "__main__":
    main()
        
        