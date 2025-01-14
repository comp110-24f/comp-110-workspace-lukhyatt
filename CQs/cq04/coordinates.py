def get_choords(xs: str, ys: str) -> None:
    x = 0
    while x < (len(xs)):
        y = 0
        while y < (len(ys)):
            print("(" + xs[x] + "," + ys[y] + ")")
            y += 1
        x += 1
