def	ft_count_harvest_recursive():
	days = int(input("Days until harvest: "))
	def nova_funcao(n):
		if (n > days):
			print("Harvest time!")
			return
		print("Day: {n}")
		nova_funcao(n+1)

ft_count_harvest_recursive()