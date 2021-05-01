def isPalindrome(x: int) -> bool:
    # Base case, negative not palindrome
    if x < 0:
        return False

    div = 1
    while x / div >= 10:
        div *= 10
    while x != 0:
        l = x // div
        t = x % 10

        if l != t:
            return False
        x = (x % div) // 10
        div /= 100
    return True