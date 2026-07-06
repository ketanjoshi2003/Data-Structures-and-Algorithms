class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def build_list(values):
    head = Node(values[0])
    current = head
    for v in values[1:]:
        current.next = Node(v)
        current = current.next
    return head


def find_middle(head):
    fast = head
    slow = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        
    return slow


if __name__ == "__main__":
    head = build_list([10, 20, 30, 40, 50])
    result = find_middle(head)
    print(result.value)   # should print 30