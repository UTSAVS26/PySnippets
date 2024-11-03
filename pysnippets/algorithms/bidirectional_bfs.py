from collections import deque
def bidirectional_search(graph, start, target):
    queue_start = deque([[start]])
    queue_target = deque([[target]])
