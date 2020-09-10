stock = [
    {'name' : 'iPhone Xs' , 'stock' : 24 , 'price' : 65432.1 , 
        'recomended' : ['Samsung Galaxy s10' , "iPhone 6"]},
    {'name' : "Samsung Galaxy s10" , 'stock' : 8 ,
        'price' : 50000 , "discount" : 5000},
    {'name' : 'Xiaomi Mi8' , 'stock' : 38000.5},    
]
print(type(stock))



print(type(stock[1]))
print(stock[0]['recomended'])