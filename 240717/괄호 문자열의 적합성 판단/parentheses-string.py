import sys
input = sys.stdin.readline

line = list(input())

def pair(line):
    stack = []
    for s in line:
        if s == "(":
            stack.append(s)
        
        else:
            if not stack:
                return "No"
            stack.pop()
        
    if stack:
        return "No"
    return "Yes"

print(pair(line))