from src import *
from src.types import node


class Solution:
    @staticmethod
    def is_palindrome(self, x: int) -> bool:
        return palindrome_number_009.is_palindrome(x)

    @staticmethod
    def is_palindrome_list(self, head: node.ListNode) -> bool:
        return palindrome_linked_list_234.is_palindrome(head)

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1 = list(-1 for _ in range(100))
        n2 = list(-1 for _ in range(100))
        num1, num2 = 0, 0
        i1, i2 = 0, 0

        while l1 is not None:
            n1[i1] = l1.val
            l1 = l1.next
            i1 += 1
        while l2 is not None:
            n2[i2] = l2.val
            l2 = l2.val
            i2 += 1

        for i in range(i1):
            num1 += n1[i] * 10 ** i
        for i in range(i2):
            num2 += n2[i] * 10 ** i
        j += k
        sol = list(map(int, str(j)))
        return sol[::-1]