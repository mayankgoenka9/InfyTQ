"""
HackerRank Designer DoorMat
Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

Mat size must be N X M. (N is an odd natural number, and M is 3 times N.)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.
"""

def top_cone(n,m):
    for i in range(mid):
        print((design*((i*2)+1)).center(m,'-'))

def bottom_cone(n,m):
    for i in range(1,mid+1):
        print((design*(n-(i*2))).center(m,'-'))
def center_message(n,m):
    print(word.center(m,'-'))

if __name__ == '__main__':
    n,m = map(int, input().split(' '))
    mid = n//2
    word = 'WELCOME'
    design = '.|.'
    top_cone(n,m)
    center_message(n,m)
    bottom_cone(n,m)