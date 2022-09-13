#정석 이분검색 

n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

def binary_search(lst, target):
    n = len(lst)
    lt = 0
    rt = n-1
    while lt <= rt:
        mid = (lt+rt)//2
        if lst[mid] == target:
            print(mid+1)
            break
        elif lst[mid] > target:
            rt = mid - 1
        else:
            lt = mid + 1
    else:
        print("찾는 값이 없습니다")

binary_search(lst, m)
