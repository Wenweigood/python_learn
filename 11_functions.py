# 语法参考
# 声明一个函数
def function_name():
    print('do something')


# 调用声明的函数
function_name()


def a_value_returned_function():
    return '123'


print(a_value_returned_function())


def one_parameter_function(i):
    print(i)


one_parameter_function(999)


def two_parameter_function(i, j):
    return i + j


print(two_parameter_function('a', 'b'))
print(two_parameter_function(1, 5))


# 上方只传值的方式必须要严格遵守参数位置顺序。如果想不受限制可以传递带有key和value的参数。
# 使用语法
def function_name(para1, para2):
    return para1 + para2


# 调用方法通过指定key=value
print(function_name(para1='John', para2='Doe'))
print(function_name(para2='Doe', para1='John'))


# 带默认参数的函数
def a_default_value_function(a='a'):
    print(a + 'b')


a_default_value_function('c')


# 函数和变量一样，可以被覆盖
def a_default_value_function(a='a', b=[1, 2, 3]):
    print(a, b)


a_default_value_function('c')


# 任意参数函数
# 语法形式 * 不确定参数
# 本质上是将参数打包成一个tuple（元组）
def any_args_function(*args):
    print(args)


any_args_function(1, 2, 3, '5', 6, ['wen', 'vi'])


# 实参和不定参数
def any_args_function(name, *args):
    print(name, args)


any_args_function('vi')


# 本质上是将参数打包成一个字典
def any_args_function(**kwargs):
    print(kwargs.items())


any_args_function(name='wen', name2='vi')


# 函数作为另一个函数的参数
# 可以将函数作为参数传递
def square_number(n):
    return n ** n


def do_something(f, x):
    return f(x)


print(do_something(square_number, 3))  # 27
print('type of square_number', type(square_number))

print('------exercise------')


def add_two_numbers(i, j):
    return i + j


def convert_celsius_to_fahrenheit(C):
    return (C * 9 / 5) + 32


print(convert_celsius_to_fahrenheit(100))


def reverse_list(l):
    return l[::-1]


print('1,3,5,10,11\'s reverse is:', reverse_list([1, 3, 5, 10, 11]))


def capitalize_list_items(l):
    for i in range(len(l)):
        l[i] = l[i].upper()
    return l


print(capitalize_list_items(['wen', 'vi']))


def add_item(l, obj):
    l.append(obj)
    return l


print(add_item([1, 5, 6], 9))


def sum_all_numbers(*args):
    count = 0
    for arg in args:
        count+=arg
    return count


print(sum_all_numbers(1,2,5,6,10))


def evens_and_odds(p):
    odd = 0
    even = 0
    for i in range(1,p+1,1):
        if(i%2 ==0):
            even+=1
        else:
            odd+=1
    print('odds:',odd)
    print('evens',even)

evens_and_odds(100)
evens_and_odds(101)


def is_prime(p):
    sqrt_p = p**0.5
    for i in range(2,int(sqrt_p)+1):
        if(p%i == 0):
            return False
    return True


print('4 is prime', is_prime(4))
print('23 is prime', is_prime(23))


def is_all_the_same_type(l):
    if(len(l) == 0):
        return True
    t = type(l[0])
    for item in l:
        if(type(item) != t):
            return False
    return True


print('[1,2,3] is all the same type',is_all_the_same_type([1,2,3]))
print('[1,2,3,\'w\',\'v\'] is all the same type',is_all_the_same_type([1,2,3,'w','v']))


