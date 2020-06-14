def geo_dist(n, p):
    return (1-p)**(n-1) * p

nu, dn = map(int, input().split())
p = nu/dn
n = int(input())
print(round(sum([geo_dist(i, p) for i in range(1,n+1)]),3))