def DFS(v):
    if v>7:
        return 
    else:
        print(v, end=" ") # 본연의 일이 위치하는 곳에 따라 전위, 중위, 후위 순회로 나뉜다
        DFS(v*2) #부모 노드 값의 *2 는 왼쪽 노드를 호출한 것
        DFS(v*2 + 1) #오른쪽 자식 노드를 호출한 것
    

DFS(1)