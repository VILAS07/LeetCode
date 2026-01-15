class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for ch in s:
            if ch in "({[":
                stack.append(ch)
            elif ch in ")}]":
                if not stack:
                    return False  
                top = stack.pop()
                if (ch == ")" and top != "(") or \
                   (ch == "}" and top != "{") or \
                   (ch == "]" and top != "["):
                    return False   
        return not stack  
