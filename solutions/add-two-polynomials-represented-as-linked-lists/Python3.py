# Definition for polynomial singly-linked list.
class PolyNode:
    def __init__(self, x=0, y=0, next=None):
        self.coefficient = x
        self.power = y
        self.next = next

class Solution:
    def addPoly(self, poly1: 'PolyNode', poly2: 'PolyNode') -> 'PolyNode':
        dummy = PolyNode()
        current = dummy

        while poly1 and poly2:
            if poly1.power == poly2.power:
                coeff_sum = poly1.coefficient + poly2.coefficient
                if coeff_sum != 0:
                    current.next = PolyNode(coeff_sum, poly1.power)
                    current = current.next
                poly1 = poly1.next
                poly2 = poly2.next
            elif poly1.power > poly2.power:
                current.next = PolyNode(poly1.coefficient, poly1.power)
                current = current.next
                poly1 = poly1.next
            else:
                current.next = PolyNode(poly2.coefficient, poly2.power)
                current = current.next
                poly2 = poly2.next

        while poly1:
            current.next = PolyNode(poly1.coefficient, poly1.power)
            current = current.next
            poly1 = poly1.next

        while poly2:
            current.next = PolyNode(poly2.coefficient, poly2.power)
            current = current.next
            poly2 = poly2.next

        return dummy.next