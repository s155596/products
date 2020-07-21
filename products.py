products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q' : # q代表quit
		break
	price = input('請輸入商品價格: ') #如果輸入商品才輸價格
	p = []
	p.append(name)
	p.append(price)
	# p = [name, price] 可用此行代替上述兩行
	products.append(p)
	# 最後可用 products.append([name, price]) 代替整個
print(products)
print(products[0][0]) # 代表products中的第一個商品及價格中的商品。