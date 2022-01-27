import sys


input = sys.stdin.readline

names = []
adj_list_dict = {}
N = int(input())

for _ in range(N):
    raw_input = input().split()
    if raw_input[0] in adj_list_dict.keys():
        adj_list_dict[raw_input[0]].append(raw_input[1])
    else:
        adj_list_dict[raw_input[0]] = raw_input[1:]

for _ in range(10):
    names.append(input().strip())

for name in names:
    cousins = 0
    for mother in adj_list_dict.keys():
        if name in adj_list_dict[mother]:
            for aunts in adj_list_dict.values():
                if mother in aunts:
                    for aunt in aunts:
                        if aunt in adj_list_dict.keys() and aunt != mother:
                            cousins += len(adj_list_dict[aunt])

    print("Cousins:", cousins, end=", ")
    for children in adj_list_dict.values():
        if name in children:
            print("Sisters:",len(children) - 1)
