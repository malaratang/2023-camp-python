# a=int(input())
# if a%3==0:
#     print(f'{a}는 3의 배수입니다!')
# else:
#     print(f'{a}는 3의 배수가 아닙니다!')
#------------------------------------------------
# for i in range(1, 11, 1):
#     print(i, end=' ')
# b=int(input())
# if b%2==0:
#     print(f'{b}는 짝수입니다')
# else:
#     print(f'{b}은 짝수가 아닌 홀수입니다')
#------------------------------------------------
# c=int(input())
# d=int(input())
# e=int(input())
# o=c
# if c<d:
#     o=d
# if e>o:
#     o=e
# print(o)
#------------------------------------------------
# for i in range(6):
#     for j in range(i):
#         print('*', end='')
#     print()
#------------------------------------------------
# for i in range(6, 0, -1):
#     for j in range(i):
#       print('*', end='')
#     print()
#------------------------------------------------
# a=int(input())
# b=int(input())
# for i in range(a, b+1):
#     if i%2!=0:
#         print(i)
#------------------------------------------------
# u=int(input())
# for i in range(1, u+1):
#     if i%3==0:
#         print('-', end=' ')
#     else:
#         print(i, end=' ')
#------------------------------------------------
a=int(input())
b=int(input())
l=str(input())
if l=="+":
    print(a+b)
elif l=="-":
    print(a-b)
elif l=="/":
    print(a/b)
elif l=="*":
    print(a*b)