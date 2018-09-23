import next_permutation

target = 24
# current = [2,6,6,9],symbol = [0,1,1], parenthesisCom = [0,1,2] 
# a b c d
def Points24(current,symbol,parenthesisCom):
    operated = []
    temp = current.copy()
    for j in range(3):
        i = parenthesisCom[j]
        result = Operation(temp[i],temp[i+1],symbol[j])
        if result == 'Divisor 0':
            return 'Divisor 0'
        if i in operated or i+1 in operated:
            for t in operated:
                temp[t] = result
            
        if i not in operated:
            operated.append(i)
        if i+1 not in operated:
            operated.append(i+1)

        temp[i] = result
        temp[i+1] = result
        # print(temp)
    return result

def Operation(a,b,digit):
    if digit == 0:
        return a+b
    elif digit == 1:
        return a-b
    elif digit == 2:
        return a*b
    else:
        if b != 0:
            return a/b
        else:
            return 'Divisor 0'
    
# print(Points24([1,2,3,4],[0,2,0],[1,2,0]))
# current = [2,6,6,9],symbol = [0,1,1], parenthesisCom = [0,1,2] 
# a b c d
def Expression(current,symbol,parenthesisCom):
    operated = []
    temp = current.copy()
    recursive = 1
    size = len(parenthesisCom)
    for j in range(3):
        i = parenthesisCom[j]
        if recursive < size:
            result = ExpressionUtil(temp[i],temp[i+1],symbol[j],True)
        else:
            result = ExpressionUtil(temp[i],temp[i+1],symbol[j],False)

        if i in operated or i+1 in operated:
            for t in operated:
                temp[t] = result
        if i not in operated:
            operated.append(i)
        if i+1 not in operated:
            operated.append(i+1)
        temp[i] = result
        temp[i+1] = result
        recursive += 1
    return result   

def ExpressionUtil(a,b,digit,flag):
    if flag == True:
        if digit == 0:
            return '({}+{})'.format(str(a),str(b))
        elif digit == 1:
            return '({}-{})'.format(str(a),str(b))
        elif digit == 2:
            return '({}*{})'.format(str(a),str(b))
        else:
            return '({}/{})'.format(str(a),str(b))
    else:
        if digit == 0:
            return '{}+{}'.format(str(a),str(b))
        elif digit == 1:
            return '{}-{}'.format(str(a),str(b))
        elif digit == 2:
            return '{}*{}'.format(str(a),str(b))
        else:
            return '{}/{}'.format(str(a),str(b))


arr = [int(x) for x in input().split()]
arr.sort()
#loop symbols eg[0,0,1] where [0,1,2,3]represents[+,-,*,/]
n = len(arr)
symbols = [[j,k,l] for j in range(4) for k in range(4) for l in range(4)]

solutions = []
while True:
    for symbol in symbols:
        parenthesisCom = [0,1,2]
        while True:
            result = Points24(arr, symbol, parenthesisCom)
            if result != 'Divisor 0':
                if abs(result-target) < 1e-8:
                    solution = Expression(arr,symbol,parenthesisCom)
                    solutions.append(solution)
            if not next_permutation.next_permutation(parenthesisCom):
                break
    if not next_permutation.next_permutation(arr):
        break
for i, solution in enumerate(solutions):
    print("#{}: {} = 24".format(i + 1, solution))

# current = [2,1, 3, 4] 
# symbol = [0,1,3] 
# parenthesisCom = [1,2,0]
# print(current,symbol,parenthesisCom)
# print(Points24(current,symbol,parenthesisCom))
# print(Expression(current,symbol,parenthesisCom))