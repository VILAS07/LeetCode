class Solution(object):
	# We need to sort the distinct nodes of the BST by using inorder traversal
    def balanceBST(self, root):
        def inorder(root):
            if not root:
                return []
            return inorder(root.left) + [root.val] + inorder(root.right)
        
        nums = inorder(root) # Because the function returns a list, we assign that list to variable nums for later uses
        
        def constructBST(nums):
            if len(nums) == 0: # Our list is empty
                return None
            if len(nums) == 1: # Our list has only one element
                return TreeNode(nums[0])
				
			# Here is one illustration before the code:
			# Assuming that we already have a sorted list : [1, 2, 5, 7, 9, 12, 14]
			# The middle value is 7, which is also our very first root
			# root.left will apply the same thought recursively with a sorted list: [1, 2, 5]
			# root.right will apply the same thought recursively with a sorted list: [9, 12, 14]
			# Below is the final code:
			
            mid = len(nums) // 2
            new_node = TreeNode(nums[mid])
            new_node.left = constructBST(nums[:mid])
            new_node.right = constructBST(nums[mid+1:])
            return new_node
        
        return constructBST(nums)