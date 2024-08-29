data_strukture =[
[1,2,3],
{'a':4,"b":5},
(6,{"cube":7,"drum":8}),
"Hello",
((),[{(2,"Urban",("Urban2",35))}])
]

def calculate_strukture_sum(*args):
    summa = 0
    for arg in args:
        if isinstance(arg,(list,tuple,set)):
            summa += calculate_strukture_sum(*arg)
        elif isinstance(arg,dict):
            for key,value in arg.items():
                summa += calculate_strukture_sum(key)
                summa += calculate_strukture_sum(value)
        elif isinstance(arg,(int,float)):
             summa += arg
        elif isinstance(arg,str):
            summa += len(arg)
    return summa

result = calculate_strukture_sum(data_strukture)
print(result)











