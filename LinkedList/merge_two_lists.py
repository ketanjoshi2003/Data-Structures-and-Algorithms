class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


def build_list(values):
    head = ListNode(values[0])
    current = head
    for v in values[1:]:
        current.next = ListNode(v)
        current = current.next
    return head


def merge_two_lists(l1, l2):
    dummy = ListNode(0)
    tail = dummy
    while l1 is not None and l2 is not None:
        if l1.value < l2.value:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 if l1 else l2
    return dummy.next


if __name__ == "__main__":
    list1 = build_list([1, 4])
    list2 = build_list([2, 3])

    merged = merge_two_lists(list1, list2)

    current = merged
    while current is not None:
        print(current.value, end=" -> ")
        current = current.next
    print("None")