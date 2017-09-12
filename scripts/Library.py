
def testPrime(Number):
	if Number == 1:
		return False
	tester = 2
	while tester*tester <= Number:
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

def square(Number):
	return pow(Number, 2)

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

def findTopDigit(Number):
	
	return (digit(Number, findDigitCount(Number)))

def findDigitCount(Number):
	digits = 0
	while pow(10, digits) < Number + 1 :
		digits = digits + 1
	return digits

def convertToBaseTen(Number, OldBase):
	newNumber = 0
	while Number > 0:
		power = findDigitCount(Number)-1
		topDigit = findTopDigit(Number)
		removedDigit = topDigit * (10**(power))
		difference = topDigit *(OldBase**power)
		newNumber = newNumber + difference
		Number = Number-removedDigit
	return newNumber

def convertToAlternateDigit(Number, NewBase):
	newNumber = 0
	while(Number > 0):
		newDigit = 1
		power = 0
		while(NewBase**(power+1)<= Number):
			power = power + 1
		while((newDigit +1) * (NewBase**power) <Number):
			newDigit = newDigit + 1
		newNumber = newNumber + ((10**power) * newDigit)
		Number = Number - ((NewBase**power) * newDigit)
	return newNumber
x = 0

def convertBase(Number, NewBase, OldBase):
	#only workable in bases under 10
	return convertToAlternateDigit(convertToBaseTen(Number,OldBase), NewBase)

def concatinate(FirstNumber, SecondNumber):
	FirstNumber = FirstNumber * (10**findDigitCount(SecondNumber))
	return (FirstNumber + SecondNumber)


 def digit(Number, Place):
 	# 0 being the ones place, 1 being the 10's place, and -1 being the 0.1s place
 	Number = ((Number%(10**Place)) - (Number%(10**(Place-1))))/(10**(Place-1))
 	Number =Number - (Number % 1)
 	return Number
	
def digits(Number, StartPlace, Length):
	#start place is the right most digit, while length proceeds leftwards in the number
	Number = ((Number%(10**(StartPlace+Length))) - (Number%(10**(StartPlace))))/(10**(StartPlace))
	Number =Number - (Number % 1)
	return Number

def rounded(Number, Place):
# 0 being the ones place, 1 being the 10's place, and -1 being the 0.1s place
	Number = ((Number%(10**Place)) - (Number%(10**(Place-1))))
	Number =Number - (Number % 1)
	return Number


def testTruncatableRight(Number):
	truncatablePrime = True
	while Number > 0 and truncatablePrime == True:
		truncatablePrime = testPrime(Number)
		digitCount = findDigitCount(Number)
		Number = Number - (rounded(Number, digitCount))
	return truncatablePrime

def testTruncatableLeft(Number):
	truncatablePrime = True
	digitCount = findDigitCount(Number)
	while (digitCount) > 0 and truncatablePrime == True:
		truncatablePrime = testPrime(Number)
		Number = digits(Number, 1, (digitCount-1))
		digitCount = digitCount - 1
	return truncatablePrime


def massTruncatableTest():
	number = 11
	amountOfPrimes = 0
	adder = 0
	while amountOfPrimes <= 10:
		if testTruncatableRight(number) and testTruncatableLeft(number):
			adder = adder + number
			print(number)
			print(adder)
			amountOfPrimes = amountOfPrimes + 1
		number = number + 1
	return "I hope that was sufficient"

def rotateNumber(Number):
	digitCount = findDigitCount(Number)
	shiftingDigit = digit(Number, 0)
	Number = Number/10
	Number = Number%1
	Number = Number + (shiftingDigit *(10**digitCount))
	return Number