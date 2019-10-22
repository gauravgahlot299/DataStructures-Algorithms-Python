s = '({[]})'
def isBalanced(s):
    visited = []
    for i in s:
        if i==')':
            if len(visited) == 0 or visited.pop(-1)!='(':
                return('Unbalanced')
        if i==']':
            if len(visited) == 0 or visited.pop(-1)!='[':
                return('Unbalanced')
        if i=='}':
            if len(visited) == 0 or visited.pop(-1)!='{':
                return('Unbalanced')
        if i=='(' or i=='{' or i=='[':
            visited.append(i)
    if len(visited) > 0:
        return ('Unbalanced')
    else:
        return ('Balanced')
print(isBalanced(s))