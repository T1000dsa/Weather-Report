def dgr_chr(x:int|float,y="k",z="c"):
	"""
	Changes degrees and return changed variable.
	Function takes three argument's: required argument x and two optional argument's y and z. 
	y - > z
	"""
	base = {"f":{"c":((x-32)*5)/9,"k":((x-32)*5)/9 + 273.15},"c":{"f":(x*1.8)+32,"k":x+273.15},"k":{"c":x-273.15,"f":(x-273.15)*9/5+32}}
	try:
		return round(base[y][z],4)
	except(KeyError) as err:
		return "Wrong name of the variable"