#!/usr/bin/python3


def isWinner(x, nums):
    if not nums or x < 1:
        return None
    n = max(nums)
    List = []
    for _ in range(max(n+1, 2)):
        List.append(True)
    for i in range(2, int(pow(n, 0.5)) + 1):
        if not List[i]:
            continue
        for j in range(i*i, n + 1, i):
            List[j] = False

    List[0] = List[1] = False
    c = 0
    for i in range(len(List)):
        if List[i]:
            c += 1
        List[i] = c

    player1 = 0
    for n in nums:
        player1 += List[n] % 2 == 1
    if player1 * 2 == len(nums):
        return None
    if player1 * 2 > len(nums):
        return "Maria"
    return "Ben"
