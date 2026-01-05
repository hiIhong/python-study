T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    dx = x1 - x2
    dy = y1 - y2
    dist_sq = dx*dx + dy*dy

    r_sum_sq = (r1 + r2) ** 2
    r_diff_sq = (r1 - r2) ** 2

    # 같은 위치, 같은 반지름
    if dist_sq == 0 and r1 == r2:
        print(-1)
    # 만나지 않음
    elif dist_sq > r_sum_sq or dist_sq < r_diff_sq:
        print(0)
    # 한 점에서 만남
    elif dist_sq == r_sum_sq or dist_sq == r_diff_sq:
        print(1)
    # 두 점에서 만남
    else:
        print(2)
