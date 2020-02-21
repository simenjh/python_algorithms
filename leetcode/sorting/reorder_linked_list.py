import math as m
import random as r


# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

# You may not modify the values in the list's nodes, only nodes itself may be changed.

# Example 1:

# Given 1->2->3->4, reorder it to 1->4->2->3.
# Example 2:

# Given 1->2->3->4->5, reorder it to 1->5->2->4->3.






# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
        

def reorderList(head):
    if head is not None:
        second = split_list_in_half(head)
        second_reversed = reverse_second(second)
        insert_second_into_first(head, second_reversed)


def split_list_in_half(head):
    first_length = list_length(head)
    return produce_second_list(head, first_length)


def list_length(node):
    l = 0
    while node is not None:
        l += 1
        node = node.next
    return l


def produce_second_list(head, first_length):
    half_of_length = m.floor(first_length / 2)
    current = head
    second = head
    count = 0
    while count <= half_of_length:
        if count == half_of_length:
           second = current.next
           current.next = None
        else:
            current = current.next
        count += 1
    return second


def reverse_second(head):
    prev = None
    current = head
    while current is not None:
        nex = current.next
        current.next = prev
        prev = current
        current = nex
    return prev
    

def insert_second_into_first(first, second):
    first_pointer = first
    second_pointer = second

    while (first_pointer is not None) and (second_pointer is not None):
        first_next = first_pointer.next
        second_next = second_pointer.next

        first_pointer.next = second_pointer
        second_pointer.next = first_next
        
        first_pointer = first_next
        second_pointer = second_next


    




# Helper functions
def print_list_vals(node):
    while node is not None:
        print(node.val)
        node = node.next
        

def make_linked_list(length):
    head = ListNode(r.randint(0, 100))
    current = head
    count = 0
    while count < length-1:
        current.next = ListNode(r.randint(0, 100))
        current = current.next
        count += 1
    return head
