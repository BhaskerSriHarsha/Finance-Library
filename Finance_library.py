def CompoundInterest(principal, rate, n):
	# Input Arguments:
	#	principal: It is the principal amount
	#	rate: rate of interest
	#	n: number of times the principal is compounded

	# Output: Amount is returned
	previous=principal
	new=0
	
	for i in range(0,n):
		#print(previous)
		#print(float(rate/100)*previous)
		new = previous + (float(rate/100)*previous)
		previous = new
		
	amount = new
	return amount
	
def SimpleInterest(principal, rate, n):
	# Input Arguments:
	#	principal: It is the principal amount
	#	rate: rate of interest
	#	n: number of times interest is added to the principal

	# Output: Amount is returned
	new = 0
	previous = principal
	for i in range(0,n):
		new = new+(float(rate/100)*principal)
		
	return principal+new
	
