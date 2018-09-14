# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        # print(head.val)
        if not head:
            return
        if not head.next:
            return TreeNode(head.val)
        fast = head.next.next
        slow = head
        pre = None
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            pre = slow
        second = slow.next
        slow.next = None
        ans = TreeNode(second.val)
        ans.left = self.sortedListToBST(head)
        ans.right = self.sortedListToBST(second.next)
    
        return ans
        
            
        