
def testPrime(Number):
	tester = 2
	while tester*tester < Number+1:
		if Number % tester == 0:
			return False
		tester = tester + 1
	return True

def findPrimeFactor(Number):
	Factor = 2
	biggestPrime = 1
	while Factor < Number/2:
		if Number%Factor== 0:
			if testPrime(Factor) == True:
				biggestPrime = Factor
		Factor = Factor + 1
	return biggestPrime
def findDigit(Number, Place):
	# 1 is for the highest digit but with the value it originally had, 2 is for the rest of the number and 3 is for the first digit as a 1 digit number isolated
	totalPower = pow(10, findDigitCount(Number) -1)
	N = Number
	digitCount = 1
	count = 0
	digitEstimate = findDigitCount(Number)
	unit = totalPower
	while digitCount > Place - 1:
		digitEstimate = 0
		while digitEstimate * unit + unit < N:
			digitEstimate = digitEstimate + 1
		N = N - digitEstimate * unit
		print(digitEstimate)
		digitCount = digitCount - 1
		unit = unit/10
	return digitEstimate	





def square(Number):
	return pow(Number, 3)

def sumSquare(Minimum, Maximum):
	N = Minimum
	newSum = 0
	while N < Maximum + 1:
		newSum = newSum + square(N)
		N = N + 1
	return newSum

def squareSum(Minimum, Maximum):
	N = Minimum
	currentSum = 0
	while N < Maximum+ 1:
		currentSum = currentSum + N
		N = N + 1
	return square(currentSum)
def generatePrimes(Number):
	N = 1
	counter = 0
	while counter < Number + 1:
		if testPrime(N):
			print(N)
			counter = counter + 1
		N = N + 1
def testPythagrean(a, b, c):
	if a*a + b*b == c*c:
		return True
	else:
		return False
def findPythagreanWithDigitSum():
	a = 1
	while a < 1000:
		b = 1
		while b < 1000:
			c = 1
			while c < 1000:
				if testPythagrean(a, b, c):
					print(a + b + c)
					if a + b + c == 1000:
						print(a)
						print (b)
						print (c)
						return True
				c = c + 1
			b = b + 1
		a = a + 1
def sumPrimes(Maximum):
	N = 2
	total = 0
	while N < Maximum:
		if testPrime(N):
			total = total + N
			print(N)
		N = N + 1
	return total
def factorial(Number):
	N = Number
	subtractor = 1
	currentNumber = Number
	while Number > subtractor:
		currentNumber = currentNumber *(Number - subtractor)
		subtractor = subtractor + 1
	return currentNumber
def countDivisers(Number):
	factor = 2
	primeFactorsSoFar = 0
	squareFactors = 0
	N = Number
	factorPower = []
	divisors = 1

	while factor< N+1 :
		if N%factor == 0:
			currentPower = 1
			N = N / factor
			while N%factor == 0:
				N = N / factor
				currentPower = currentPower + 1
			factorPower.append(currentPower + 1)
			primeFactorsSoFar = primeFactorsSoFar + 1
		else:
			factor = factor + 1
	for x in range(0, len(factorPower)):
		divisors = divisors * factorPower[x]
	return divisors

def slowCountDivisers(Number):
	N = Number
	factor = 1
	divisors = 0
	while factor < Number + 1:
		if Number%factor == 0:
			divisors = divisors + 1
		factor = factor + 1
	return divisors
def findNumberWithFactors(Factors):
	N = 1
	while countDivisers(N) < Factors:
		N = N+1
		print(countDivisers(N))
	return N
def findTriangularWithFactors():
	infiniteLoop = True
	currentTriangle = 0
	currentNumber = 1
	while currentNumber < 10000000:
		currentTriangle = currentNumber + currentTriangle
		currentNumber = currentNumber + 1
		if countDivisers(currentTriangle) > 500:
			return currentTriangle
def countCollatz(Number):
	N = Number
	count = 1
	while N != 1:
		if N%2 == 0:
			N = N/2
			count = count + 1
		else:
			N = 3*N + 1
			count = count  + 1
	return count
def millionCollatz():
	N = 1
	count = 0
	currentHighest = 1
	while N < 1000000:
		if countCollatz(N) > count:
			count = countCollatz(N)
			currentHighest = N
			print(countCollatz(N))
		N = N + 1
	return currentHighest
def digitHighestFind(Number, highest):
	unit = pow(10, highest -1)
	counter = 0
	while counter + unit < Number + 1:
		counter = counter + unit
	N = counter/unit
	return N 
def findDigitCount(Number):
	digits = 0
	while pow(10, digits) < Number + 1 :
		digits = digits + 1
	return digits

print("e")