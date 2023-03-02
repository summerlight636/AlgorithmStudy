# 입력

# 알고리즘


# import operator
#
#
# def solution(genres, plays):
#     dic = dict()
#     n = len(genres)
#     plays.append(-1)
#     for i, x in enumerate(genres):
#         if x not in dic.keys():
#             dic[x] = [plays[i], i, n]
#         else:
#             sum_value = dic[x][0]
#             m1 = dic[x][1]
#             m2 = dic[x][2]
#             if plays[m2] < plays[i]:
#                 dic[x][2] = i
#                 if plays[m1] < plays[i]:
#                     dic[x][1], dic[x][2] = dic[x][2], dic[x][1]
#             dic[x][0] = sum_value + plays[i]
#
#     sdic = sorted(dic.items(), key=operator.itemgetter(0), reverse=True)
#
#     answer = []
#     for key, value in sdic:
#         answer.append(value[1])
#         if value[2] != n:
#             answer.append(value[2])
#     return answer