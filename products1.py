import os # 代表載入operating system 就代表可以與電腦詢問是否內有檔案

def read_file(filename):
	products = []
	with open(filename, 'r') as f:
		for line in f:
			if '商品,價格' in line:
				continue # 繼續, 代表跳過跳到下一回, 但仍在迴圈內
			name, price =line.strip().split(',') 
			# 這個字串先把尾巴的\n去掉後，只要遇到逗點就幫我切一刀
			# 切割完直接存成name 和 price
			# 若有2個逗點，就需要有3個變數在前面, 以此類推
			products.append([name, price]) #把name和price裝到product清單內
	return products

# 只給檔名=> 相對路徑(同樣的資料夾內)

# 讀取檔案
# products = []
# with open('products.csv', 'r') as f:
# 	for line in f:
# 		if '商品,價格' in line:
# 			continue # 繼續, 代表跳過跳到下一回, 但仍在迴圈內
# 		name, price =line.strip().split(',') 
# 		# 這個字串先把尾巴的\n去掉後，只要遇到逗點就幫我切一刀
# 		# 切割完直接存成name 和 price
# 		# 若有2個逗點，就需要有3個變數在前面, 以此類推
# 		products.append([name, price]) #把name和price裝到product清單內
# print(products)

# Step 1 讓使用者輸入
def user_input(products):
	while True:
		name = input('請輸入商品名稱: ')
		if name == 'q' : # q代表quit
			break
		price = input('請輸入商品價格: ') #如果輸入商品才輸價格
		# price = int(price)
		products.append([name, price]) #代替整個
	print(products)
	return products
# print(products[0][0]) # 代表products中的第一個商品及價格中的商品。

# Step 2 印出所有購買紀錄
def print_products(products):
	for product in products: # 印出清單中的每一個東西(小清單)
		print(product[0], '的價格是', product[1])

# Step 3 寫入檔案
def write_file(filename, products):
	with open(filename, 'w') as f: #打開檔案 (檔案已存在也沒關係會覆蓋)
	# with 有自動close的功能
	# encoding(編碼) ='utf-8' (最廣義使用的編碼)
		f.write('商品,價格\n' ) #在寫入商品價格前有個抬頭
		for product in products:
			f.write(product[0] + ',' + product[1] + '\n') # write為寫入的動作

def main(): # 主要執行程式碼
	filename = 'products.csv'
	if os.path.isfile(filename): # 檢查檔案在不在
		print('yeah! 找到檔案了!')
		products = read_file(filename)
	else:
		print('找不到檔案...')

	products = user_input(products)
	print_products(products)
	write_file('products.csv' , products)

main()