if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    arr.sort(reverse = True)
    for i, a in enumerate(arr):
        if i > 0 and arr[i] < arr[i - 1]:
            print(arr[i])
            break;
