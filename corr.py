
# 관계 값이 양수 일 때 ex
x_1 = [1,2,3,4]
y_1 = [1,2,3,4]
# 관계 값이 음수 일 때 ex
x_2 = [1,2,3,4]
y_2 = [4,3,2,1]
# 관계 값이 0일 때 ex 샘플 구상 중
x_3 = []
y_3 = []
def spearman(*args):
    box = []
    for key in range(len(args)):
        box2 = []
        val_sort = sorted(args[key])
        for idx in range(len(args[key])):
            [box2.append(i + 1) for i in range(len(args[key])) if args[key][idx] == val_sort[i] and idx >= len(box2)]
        box.append(box2)
        print(box)
        print(box2)
    p = [6 * ((box[0][idx] - box[1][idx]) ** 2) for idx in range(len(box[0]))]
    return 1 - (sum(p) / ((len(args[0]) ** 3) - len(args[0])))
print(spearman(x_1,y_1))


# def kendall(*args):
#     box = []
#     for idx in range(len(args[0])):
#         box.append([args[0][idx],args[1][idx]])
#     box = sorted(box , key = lambda box : box[0])
#     con_count, discon_count = 0, 0
#     for num in range(len(args[0])):
#         for idx in range(num+1,len(args[0])):
#             # print(args[0][num],args[0][idx])
#             if box[num][0] < box[idx][0] and box[num][1] < box[idx][1]:
#                 con_count += 1
#             else: discon_count += 1
#     return (con_count - discon_count) / (con_count + discon_count)
#
# print(kendall(x_2,y_2))