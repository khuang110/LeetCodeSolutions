from src.types.node import ListNode


def add_two_numbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    def list_to_llist(n: list) -> ListNode:
        if len(n) == 1:
            return ListNode(val=n[0])
        return ListNode(val=n[0], next=list_to_llist(n[1:]))

    n1 = []
    n2 = []
    sol = []
    i1, i2 = 0, 0

    while l1 is not None:
        n1.append(l1.val)
        l1 = l1.next
        i1 += 1
    while l2 is not None:
        n2.append(l2.val)
        l2 = l2.next
        i2 += 1
    while True:
        if i1 == 0 or i2 == 0:
            sol += n1 + n2
            ln = len(sol)
            print(sol)
            for i in range(ln):
                if sol[i] >= 10:
                    t = (sol[i] % 10) + 1
                    sol[i] -= 10
                    if i < ln - 1:
                        sol[i + 1] += 1
                    elif i == ln - 1:
                        sol.append(1)
            return list_to_llist(sol)
        if i1 <= i2:
            ln = len(n1)
            for i in range(ln):
                i1 -= 1
                i2 -= 1
                sol.append(n1.pop(0) + n2.pop(0))
        elif i1 > i2:
            print("i1 > i2")
            ln = len(n2)
            for i in range(ln):
                i1 -= 1
                i2 -= 1
                sol.append(n1.pop(0) + n2.pop(0))