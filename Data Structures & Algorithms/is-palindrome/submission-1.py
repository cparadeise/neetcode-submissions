class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        cleaned_text = "".join(char for char in s.lower() if char.isalnum())
        text_len = len(cleaned_text)
        r = text_len - 1

        for i in range(text_len // 2):
            if cleaned_text[l] != cleaned_text[r]:
                return False
            l += 1
            r -= 1
        
        return True