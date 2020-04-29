numbers = [x for x in range(10)]
numbers = [x for x in range(10) if x%3==0] # önce seçer sonra x ' e atar
numbers = [x if x%3==0 else 'üçün katı değil' for x in range(10) ] # önce x e atar sonra seçmeye çalışır. olumsuz durumda ne yapacağını mutlaka yazmalıyız (else)
numbers = [(x,y,z) for x in range(3) for y in range(3) for z in range(3)]
print(numbers)