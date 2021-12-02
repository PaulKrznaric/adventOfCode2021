def day1():
    depth_list = []
    depth_increase = 0
    window_increase = 0
    last_window = None

    f = open('day1.txt', 'r')
    for line in f.readlines():
        depth_list.append(int(line))
    f.close()

    n = len(depth_list)
    for i in range(1, n):
        if depth_list[i - 1] < depth_list[i]:
            depth_increase += 1
    for i in range(2, n):
        current_window = calculate_depth_window(i, depth_list)
        if last_window is not None and current_window > last_window:
            window_increase += 1
        last_window = current_window

    return [depth_increase, window_increase]


def calculate_depth_window(index, list):
    return list[index - 2] + list[index - 1] + list[index]


print(day1())
