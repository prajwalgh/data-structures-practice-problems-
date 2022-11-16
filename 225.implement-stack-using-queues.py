#
# @lc app=leetcode id=225 lang=python
#
# [225] Implement Stack using Queues
#

# @lc code=start
 class MyStack(object):

    def __init__(self):
            self.q=deque()

    def push(self, x):
        self.q.append(x)
        

    def pop(self):
        for i in range(len(self.q)-1):
            self.push(self.q.popleft())
        return self.q.popleft()
        

    def top(self):
        return self.q[-1]
        

    def empty(self):
        return len(self.q)==0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()      


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end

