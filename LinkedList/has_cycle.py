class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def build_list(values):
    """Creates a simple linked list from a Python list of values, returns head."""
    head = Node(values[0])
    current = head
    for v in values[1:]:
        current.next = Node(v)
        current = current.next
    return head



def has_cycle(head):
    fast = head
    slow = head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    return False 


# ---- Test it ----
if __name__ == "__main__":
    head = build_list([10, 20, 30, 40])

    # Test 1: no cycle
    print(has_cycle(head))   # should print False

    # Test 2: create a cycle manually (40 points back to 20)
    head.next.next.next.next = head.next
    print(has_cycle(head))   # should print True