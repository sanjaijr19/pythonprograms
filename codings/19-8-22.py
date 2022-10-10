class mystore:
	__prod_code=[]
	__prod_name=[]
	__cost_price=[]
	__prod_quant=[]


	def getdata(self):
		self.p=int(input("enter the no.of product to store:"))
		for x in range(self.p):
			self.__prod_code.append(int(input("enter the  product code : ")))

			self.__prod_name.append(input("enter the product name : "))
			self.__cost_price.append(int(input("enter the cost price : ")))
	def display(self):
		print("stocks in stores")
		print("________________________________________________________________________________________________________")
		print("product code \t product name \t cost price  ")
		print("______________________________________________________________________________________________,,__________")
		for x in range(self.p):
			print(self.__prod_code[x],"\t\t\t",self.__prod_name[x],"\t\t\t",self.__cost_price[x])
			print("____________________________________________________________________________________________________")
	def printbill(self):
		total_price=0
		for x in range(self.p):
			print("enter the quantities")
			q=int(input(self.__prod_code[x] ))
			self.__prod_quant.append(q)
			total_price = total_price + self.__cost_price[x]*self.__prod_quant[x]
		print("     \t\t\t INVOICE RECEIPT   ")
		print("____________________________________________________________________________________________________")
		print("product code \t\t productname \t\t costprice \t quantity \t totalamount")
		print("____________________________________________________________________________________________________")
		for x in range(self.p):
			print(self.__prod_code[x], "\t\t\t\t", self.__prod_name[x], "\t\t\t\t", self.__cost_price[x], "\t\t\t\t",
				  self.__prod_quant[x], "\t\t\t\t", self.__prod_quant[x] * self.__cost_price[x])
			print("____________________________________________________________________________________________________")
		print("                                                   totalamount=", total_price)

		amount=int(input("enter the amount given"))
		rem_amount=amount-total_price
		print("balance amount to be given ",rem_amount)



s=mystore()
s.getdata()
s.display()
s.printbill()

import django
print(django.VERSION)