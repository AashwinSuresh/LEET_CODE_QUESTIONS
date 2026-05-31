


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        n=len(word)
        count =0
        lower ={}
        upper ={}
        for i in range(n):
            if word[i].islower() :
                lower[word[i]]=i
            elif word[i].isupper() and word[i] not in upper :
                upper[word[i]]=i
        print(f"lower alphabets : {lower}")
        print(f"upper alphabets : {upper}")
        for l,ind in lower.items():
            u=l.upper()
            print(f"converted {l} to {u}")
            if u in upper :
                if upper[u]>ind:
                    count+=1
                    print(f"incremented count : {count}")
        return count

#INPUTS
# Copy and paste these lines into your Python file to test your solution

# Initialize your solution class
sol = Solution()

# Test Case 1: Standard Valid Case
word1 = "aaAbcBC"
print(f"Test 1 Output: {sol.numberOfSpecialChars(word1)}")  # Expected: 3

# Test Case 2: No Uppercase Characters
word2 = "abc"
print(f"Test 2 Output: {sol.numberOfSpecialChars(word2)}")  # Expected: 0

# Test Case 3: Lowercase appearing after Uppercase
word3 = "AbBCab"
print(f"Test 3 Output: {sol.numberOfSpecialChars(word3)}")  # Expected: 0

# Test Case 4: Reverse order of all letters
word4 = "ccBbaA"
print(f"Test 4 Output: {sol.numberOfSpecialChars(word4)}")  # Expected: 0

# Test Case 5: Complex Valid Case
word5 = "dDeEfF"
print(f"Test 5 Output: {sol.numberOfSpecialChars(word5)}")  # Expected: 3