def is_palindrome(s: str) -> bool:
    s = s.lower()
    left, right = 0, len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True

print(is_palindrome("A man, a plan, a canal: Panama"))  # Output: True