class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r = 0, len(s) - 1 # left and right pointer
        while l<r:
            while l<r and not self.alphaNum(s[l]):
                l+=1 # increment the left pointer if it is not alpha numeric character
            while r > l and not self.alphaNum(s[r]):
                r -= 1 # decrement the right pointer if it is not alpha numeric, here r > l is to make sure that it is not passing each other when doing comparison
            if s[l].lower() != s[r].lower():#lowercase in case running into uppercase
                return False
            l, r= l+1, r-1 #update left and right pointer after each loop
        return True #here if the loop successfully passed, meaning the string is a valid palindrome, return true

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or #check uppercase
                ord('a') <= ord(c) <= ord('z') or #check lowercase
                ord('0') <= ord(c) <= ord('9')) #check numers