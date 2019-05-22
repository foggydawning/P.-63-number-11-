def fib(max, list_fib=[0,1]):
    if list_fib[-1]>max:
        del list_fib[-1]
        return list_fib
    list_fib.append(list_fib[-2]+list_fib[-1])
    return fib(max,list_fib)

def fib_list (list, list_new=[], i=0):
    if i>=len(list):
        return list_new
    if list[i]==0:
        list_new.append(0)
        return fib_list(list,list_new,i+1)
    if list[i]==1:
        list_new.append(1)
        return fib_list(list,list_new,i+1)
    list_fib= fib(list[i])
    if list[i]==list_fib[-1]:
        list_new.append(list[i])
        return fib_list(list,list_new,i+1)
    else:
        return fib_list(list,list_new,i+1)

list=[4,3,1,2,5,6,7,233,8,9,10,11,12,13,14,89,144,1,2,144,56]
print("Ваш список:", list, sep="\n")
print("\n")

list_new=fib_list(list)
print("Все числа Фибоначчи в Вашем списке:", list_new, sep="\n")
