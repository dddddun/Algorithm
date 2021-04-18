# 경로 압축 기법
def find_parent_path_compression(parent, x):
    if parent[x] != x:
        parent[x] = find_parent_path_compression(parent, parent[x])
    return parent

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent_path_compression(parent, a)
    b = find_parent_path_compression(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(union 연산)의 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v + 1)

# 부모 테이블에서, 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

# 사이클 발생 여부
cycle = False

for i in range(e):
    a, b = map(int, input().split())

    # 사이클이 발생한 경우 종료
    if find_parent_path_compression(parent, a) == find_parent_path_compression(parent, b):
        cycle = True
        break

    # 사이클이 발생하지 않은 경우 합집합(union) 수행
    else:
        union_parent(parent, a, b)
