def test(a=[]):
    a += [0] 
    print(a)

list_obj = []
for i in range(5):
    list_obj.append(i)
    test(list_obj)