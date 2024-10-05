class Solution:
    def reverseBetween(self, head, left, right):
        if not head:
            return None

        pre, cur = None, head
        while left > 1:
            pre = cur
            cur = cur.next
            left, right = left - 1, right - 1

        tail, con = cur, pre
        while right:
            third = cur.next
            cur.next = pre
            pre = cur
            cur = third
            right -= 1

        if con:
            con.next = pre
        else:
            head = pre

        tail.next = cur
        return head