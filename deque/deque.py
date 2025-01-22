from collections import deque 
queue = deque(["eric","john","michael"])
queue.append("terry")
queue.append("graham")
print("After append all :- ",queue)
queue.popleft()
print("After popleft1:- ",queue)
queue.pop() # it pop form right
print("After pop :- ",queue)
