


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
