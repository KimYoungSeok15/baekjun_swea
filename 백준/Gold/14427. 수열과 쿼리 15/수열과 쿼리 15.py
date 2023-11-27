import heapq
import sys
input = sys.stdin.readline
N = int(input())
sequence = list(map(int, input().split()))

# 초기화된 최소 힙 생성
min_heap = [(value, index) for index, value in enumerate(sequence)]
heapq.heapify(min_heap)

M = int(input())

for _ in range(M):
    query = input().split()
    
    if query[0] == '1':
        i, v = map(int, query[1:])
        sequence[i - 1] = v
        heapq.heappush(min_heap, (v, i - 1))
    elif query[0] == '2':
        while True:
            min_value, min_index = heapq.heappop(min_heap)
            if sequence[min_index] == min_value:
                print(min_index + 1)
                heapq.heappush(min_heap, (min_value, min_index))
                break