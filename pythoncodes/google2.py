t=int(input())
while(t!=0):
    list1 = list(map(int, input().split(",")))
    result = []
    for i in range(0, len(list1)):
        current_no = list1[i]
        indexofc_no = list1.index(current_no)
        print(current_no,indexofc_no)

        before_sum = sum(list1[0:i])

        after_sum = sum(list1[i + 1:])

        if before_sum == after_sum:
            result.append(str(list1[i]) + f"and is present at {indexofc_no + 1}")
    if len(result) == 0:
        print("no such number in the given input list")
    print(" ".join(result))
    t-=1