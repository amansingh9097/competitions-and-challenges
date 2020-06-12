from itertools import combinations

N = int(input())
S = list(input().split())
K = int(input())
if (K < 1) | (K > N):
    print("third argument can't be greater than first argument or less than 1")
    exit(0)

combinations_list = list(combinations(S, K))
list_contains_a = list(map(lambda x: 'a' in x, combinations_list))
total_truth_cases = sum(list_contains_a)
print('{:.4f}'.format(total_truth_cases/len(combinations_list)))