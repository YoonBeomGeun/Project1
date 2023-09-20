
## 함수(=메서드) 선언부
def add_func(n1, n2):
    return n1 + n2

def sub_func(n1, n2):
    return n1 - n2

def gob_func(n1, n2):
    return n1 * n2

def div_func(n1, n2):
    return n1 / n2

def jaegop_func(n1, n2):
    return n1 ** n2

## 전역 변수부
num1 = 100
num2 = 200

## 메인 코드부
res = add_func(num1, num2)
print(num1, "+", num2, "=", res)

res = sub_func(num1, num2)
print(num1, "-", num2, "=", res)

res = gob_func(num1, num2)
print(num1, "*", num2, "=", res)

res = div_func(num1, num2)
print(num1, "/", num2, "=", res)

res = jaegop_func(num1, num2)
print(num1, "**", num2, "=", res)
