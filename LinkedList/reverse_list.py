def reverse(self):
    previous = None
    current = self.head

    while current is not None:
        next_node = current.next    # Step 1: save
        current.next = previous     # Step 2: flip
        previous = current          # Step 3: advance previous
        current = next_node         # Step 4: advance current

    self.head = previous            # previous ends up at the new first node