def clearall(local_global_var):	
	"""clearall(global()) suprime les variables locales dans la console"""
	all = [var for var in local_global_var if var[0] != "_"]
	for var in all:
		print(var)
		del local_global_var[var]