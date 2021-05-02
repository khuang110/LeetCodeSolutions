from src.types.node import ListNode


def is_palindrome(head: ListNode) -> bool:
    x = ''
    ln = 0
    while head is not None:
        x += f'{head.val}'
        ln += 1
        head = head.next

    def palindrome(_ln: int, _x: str) -> bool:
        for i in range(_ln):
            if _x[i] != _x[ln - i - 1]:
                return False
        return True

    return palindrome(ln, x)
