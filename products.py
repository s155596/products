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

for product in products: # 印出清單中的每一個東西(小清單)
	print(product[0], '的價格是', product[1])

with open('products.csv', 'w', encoding='utf-8') as f: #打開檔案 (檔案已存在也沒關係會覆蓋)
# with 有自動close的功能
# encoding(編碼) ='utf-8' (最廣義使用的編碼)
	f.write('商品,價格\n' ) #在寫入商品價格前有個抬頭
	for product in products:
		f.write(product[0] + ',' + product[1] + '\n') # write為寫入的動作