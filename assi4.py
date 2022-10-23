def push(s,n):
    s.append(n)
    return
def pop(a):
    if len==0:
        print("Stack is Empty")
    else:
        d = s[len(s)-1]
        del s[len(s)-1]
        return d
stack=[]
print(push(stack,11))
print(push(stack,22))
print(push(stack, 22))
print(pop())
#hacktoberfest
