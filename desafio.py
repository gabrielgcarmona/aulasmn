a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))
t = float(input('treinamento: '))
val=[1,1,1]


x1 = a
x2 = b
x3 = c
val[0] = 0
ordem = [0,1,2]
if b > c and b > a:
        x1 = b
        x2 = a
        x3 = c
        val[1] = 0
        ordem = [1,0,2]
elif c > b and c > a:
    x1 = c
    x2 = b
    x3 = a
    val[2] = 0
    ordem = [2,1,0]
else:
    if a == b:
        val[0],val[1] = 0,0
    elif a == c:
        val[0],val[2] = 0,0
    else:
        val[2],val[1] = 0,0
  
m = (x1 * val[ordem[0]] + x2 * val[ordem[1]] + x3 * val[ordem[2]] + t) / (val[0] + val[1] + val[2])



print("estrategia: ")
print('a: %.2f' % (abs(m - a) * val[0]))  
print('b: %.2f' % (abs(m - b) * val[1]))  
print('c: %.2f' % (abs(m - c) * val[2]))  