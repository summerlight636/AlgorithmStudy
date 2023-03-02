# 큰 값을 항상 가로로 두기로 => 가로: max(x) for x in sizes

def solution(sizes):
    answer = 0

    w_max = 0
    h_max = 0
    for w, h in sizes:
        # 이 부분을 간단히 w = max(sizes), h = min(sizes) 로 생각할 수 있다.
        if w > h:
            if w_max < w:
                w_max = w
            if h_max < h:
                h_max = h
        else:
            if w_max < h:
                w_max = h
            if h_max < w:
                h_max = w
    return w_max * h_max


# 참고 답안
def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)