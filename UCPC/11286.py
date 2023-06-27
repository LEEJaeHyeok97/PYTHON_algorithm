import sys
import heapq

n = int(sys.stdin.readline())


heap = []

for i in range(n):
    tmp = int(sys.stdin.readline())

    if tmp == 0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)

    else:
        heapq.heappush(heap, (abs(tmp), tmp))
#힙(heap)은 첫 번째 파라미터를 기준으로 정렬을 수행합니다. 그러나 첫 번째 파라미터가 동일한 경우에는 두 번째 파라미터를 비교하여 정렬합니다. 따라서, 힙에 추가되는 요소는 (abs(tmp), tmp) 형태의 튜플로 이루어져 있고, 첫 번째 파라미터로는 절댓값인 abs(tmp)을 사용하여 정렬을 수행하며, 두 번째 파라미터인 tmp는 첫 번째 파라미터가 동일한 경우 정렬의 조건으로 사용됩니다.
#힙(heap)은 파라미터의 개수에 상관없이 첫 번째 파라미터부터 비교하여 정렬을 수행합니다. 파라미터가 많을 경우에는 앞의 파라미터부터 순서대로 비교하며, 동일한 경우에만 다음 파라미터를 비교하여 정렬 조건으로 사용합니다. 따라서, 앞의 파라미터가 동일한 경우에는 다음 파라미터를 비교하여 정렬 우선순위를 결정합니다.
