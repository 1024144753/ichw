import turtle

def isable(s, a, b):
    for i in range(int(s) // int(a) + 1):
        if (int(s) - i * int(a)) % int(b) == 0:
            return True
    return False


def isok(m, n, a, b):
    alist = [m, n, a, b]
    if (int(m) *int(n)) % (int(a) *int(b)) == 0 and isable(m, a, b) and isable(n, a, b):
        return True
    else:
        print('无法完整铺满')
        return False


def brick(x, a, b, m, wall, k):
    for i in range(b):
        for p in range(a):
            wall[x + i * m + p] = k
    return wall


def judge(x, a, b, m, n, wall):
    if x % m + a > m or  x // m + b > n:
        return False
    else:
        num = 0
        for i in range(b):
            for p in range(a):
                num = wall[x + i * m + p] + num
        if num > 0:
            return False
        else:
            return True


def filling(m, n, a, b, mywall, k, blist):
    global number
    if a == b:
        for pos in range(int((m*n)/(a*b))):
            mywall = brick(int(((pos % (m / a)) * a + (pos // (m / a)) * (m * a))), a, b, m, mywall, pos + 1)
        ans = [[n for (n, m) in enumerate(mywall) if m == x] for x in range(1, int((m * n) / (a * b) + 1))]
        answer.append(ans)
        print(mywall)
        number = 1
        print("铺法：")
        print(ans)
        return

    if 0 not in mywall:
        ans = [[n for (n, m) in enumerate(mywall) if m == x] for x in range(1, int((m * n) / (a * b) + 1))]
        answer.append(ans)
        number = number + 1
        print('铺法', number, ":")
        print(ans)
        return
    q = mywall.index(0)
    for r in range(2):
        if judge(q, blist[r], blist[-r - 1], m, n, mywall):
            mywall = brick(q, blist[r], blist[-r - 1], m, mywall, k)
            filling(m, n, a, b, mywall, k + 1, blist)
            mywall = brick(q, blist[r], blist[-r - 1], m, mywall, 0)
    return


def comeout_wall(length, width):
    t.up()
    t.speed(0)
    for w in range(width):
        for l in range(length):
            t.goto(l, w)
            t.write(l + w * length, False, "center")

    for w in range(width + 1):
        t.up()
        t.goto(-0.5, w - 0.5)
        t.down()
        t.fd(length)

    t.left(90)
    for l in range(length + 1):
        t.up()
        t.goto(l - 0.5, -0.5)
        t.down()
        t.fd(width)


def comeout_brick(f, o, m):
    t.speed(0)
    t.up()
    t.goto(f % m - 0.5, f // m - 0.5)
    t.down()
    t.goto(f % m - 0.5, o // m + 0.5)
    t.goto(o % m + 0.5, o // m + 0.5)
    t.goto(o % m + 0.5, f // m - 0.5)
    t.goto(f % m - 0.5, f // m - 0.5)


if __name__ == "__main__":
    wall_length = int(input("墙长"))
    wall_width = int(input("墙宽"))
    brick_length = int(input("砖长"))
    brick_width = int(input("砖宽"))
    while isok(wall_length, wall_width, brick_length, brick_width) is False:
        wall_length = int(input("墙长"))
        wall_width = int(input("墙宽"))
        brick_length = int(input("砖长"))
        brick_width = int(input("砖宽"))
    number = 0
    answer = []
    blist = [brick_length, brick_width]
    wall = [0] * (wall_length * wall_width)
    filling(wall_length, wall_width, brick_length, brick_width, wall, 1, blist)
    unity = dict(enumerate(answer))
    num = int(input("请选择方案(1到%d)进行可视化"%len(answer)))
    t = turtle.Turtle()
    wn = turtle.Screen()
    wn.setworldcoordinates(-2, -2, 1.2*wall_length, 1.2*wall_width)
    wn.setup(0.8, 0.8)
    comeout_wall(wall_length, wall_width)
    for i in unity[int(num) - 1]:
        comeout_brick(i[0], i[-1], wall_length)
    
