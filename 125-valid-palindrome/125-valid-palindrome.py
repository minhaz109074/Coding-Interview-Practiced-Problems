class Solution:
    def isPalindrome(self, s: str) -> bool:
        news = ""
        for ch in s:
            if ch.isalnum():
                if ch.isupper():
                    news += ch.lower()
                else:
                    news += ch
        
        l, r = 0, len(news)-1
        while(l<r):
            if news[l] != news[r]:
                return False
            l += 1
            r -= 1
        return True