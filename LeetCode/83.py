class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, head: ListNode | None) -> ListNode | None:

        current = head

        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head


# ========== 測試 ==========

def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_array(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

def test_case(input_values):
    head = create_linked_list(input_values)
    
    solution = Solution()
    result = solution.mergeTwoLists(head)
    
    print(linked_list_to_array(result))
    

# 執行測試
test_case([1, 1, 2])
test_case([1, 1, 2, 3, 3])
test_case([1, 1, 1])
test_case([1, 2, 3])
test_case([1])
test_case([])
test_case([1, 1, 1, 2, 2, 3])