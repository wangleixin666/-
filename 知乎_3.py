# 1(2(4,5(7,8)),3(6))
import sys


class Node:
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

line = sys.stdin.readline()
i = 0
index = 0
while i < len(line) - 1:
    Node(int(line[i]))
    if line[i] == '(':
        index = i
        line[i+1] = Node(int(line[i])).left
        i += 1
    if line[i] == ',':
        line[i+1] = Node(int(line[i-3])).right
        i += 1
    if line[i] == ')' and line[i+1] != ')' and line[i+1] != ',':
        line[i+1] = Node(int(line[index])).right
        i += 1




print line
