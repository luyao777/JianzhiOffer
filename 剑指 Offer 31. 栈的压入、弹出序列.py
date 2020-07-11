class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        push_i = 0
        pop_i = 0
        while(push_i < len(pushed)):
            if push_i < len(pushed):
                stack.append(pushed[push_i])
                push_i += 1
            while(pop_i < len(popped) and len(stack)>0 and popped[pop_i] == stack[-1]):
                stack = stack[:-1]
                pop_i += 1
                if pop_i >= len(popped):
                    break
        if pop_i < len(popped):
                return False
        return True
