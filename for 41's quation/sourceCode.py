"""
            ADDIS ABABA SCIENCE AND TECHNOLOGY UNIVERSITY
             COLLEGE OF ELECTRICAL AND MECHANICAL ENGINEERING
                DEPARTMENTS OF ELECTRICAL AND COMPUTER ENGINEERING
                  (COMPUTER ENGINEERING STREAM)
                     Advanced programing Assignment
                     ===================================
                          Section : C
                             Name : Yosef Emyayu
                               Id : Ets1310/10
                                submitted to Mr. Eyob B.
"""
import math
class Assignment:
    # 1
    def cube(self, num):
        return num ** 3

    # 2
    def triangle(self, h, w):
        area = 0.5 * h * w
        return area

    # 3
    def rectangle(self, h, w):
        area = h * w
        return area

    # 4
    def line(self, m, x, b):
        y = m * x + b
        return y

    # 5
    def intersect(self, m1, b1, m2, b2):
        if m1 == m2:
            # the two line are parallel
            return 0
        # compute the value of x at the intersection
        x = -(b2 - b1) / (m2 - m1)
        # compute the y value for both line
        y1 = m1 * x + b1
        y2 = m2 * x + b2
        if y1 == y2:
            return 1
        else:
            return 0

    # 6
    def facto(self, num):
        facto = 1
        if num > 1:
            facto = num * self.facto(num - 1)
        return facto

    def factorial(self):
        num = int(input('Enter the number:'))
        if num < 0:
            print("input must be  non-negative!!!")
        else:
            print(f"Factorial: {num}! = {self.facto(num)}")

    # 7
    def fibo(self, num):
        if num <= 1:
            return num
        else:
            return (self.fibo(num - 1) + self.fibo(num - 2))

    def fibonacci(self):
        lastTerm = int(input("Enter the last term:"))
        if lastTerm < 0:
            print("input must be positive-integer!!!")
        else:
            fibonacci = []
            for i in range(lastTerm):
                fibonacci.append(self.fibo(i))
            print(f"Fibonacci serious up to {lastTerm} :{fibonacci}")

    # 8A
    def PrimeChecking(self, num):
        result = True
        if num == 1:
            return 'one is neither prime nor composite'
        elif num == 0:
            # Zero is divisible by any number except itself,i.e not prime
            return False
        # search for the factor of the number ,if the number is different from zero and one
        for factor in range(2, num - 1):
            if num % factor == 0:
                result = False
                break
        return result

    # 8B
    def sumOfDigit(self, num):
        sum = 0
        for i in str(num):
            sum += int(i)
        return sum

    # 9
    def ascendingOrder(self, list):
        for i in range(len(list) - 1):
            min = i
            for j in range(i + 1, len(list)):
                if list[j] < list[min]:
                    min = j
            temp = list[i]
            list[i] = list[min]
            list[min] = temp
        return list

    # 10
    def markAbove20(self):

        studentNum = int(input('Enter total number of student:'))
        count = 0
        i = 0
        while i < studentNum:
            mark = int(input(f"Enter mark of student_{i + 1} :"))
            # for validating user input
            if mark >= 0 and mark < 30:
                if int(mark) > 20:
                    count += 1
            else:
                print("Invalid!!!,Mark should be between 0 and 30")
                i -= 1
            i += 1
        print('Number of student who scored above 20 is ', count)

    # 11
    def phoneNumber(self):
        phone = input("Type a 9 digit number :")
        # validate the input
        if len(phone) == 9:
            if int(phone[0]) == 9:
                print("Mobile")
            else:
                print("Fixed Phone")
        else:
            print("Invalid!!!,your input must be 9 digit number")

    # 12
    def maxAndMin(self):
        list = input("Enter your List:\nUse space as a separator:\n").split()

        min = int(list[0])
        max = int(list[1])

        for num in list:
            num = int(num)
            if num < min:
                min = num
            if num > max:
                max = num
        print("Minimum =", min)
        print("Maximum =", max)

    # 13
    def reverse(self):
        num = int(input("Enter a number:"))
        reversedNum = 0
        print("Normal number = ", num)
        while (num > 0):
            reversedNum = reversedNum * 10 + num % 10
            # integer divitione
            num = num // 10
        print("Reversed number = ", reversedNum)

    # 14
    def gcd(self):
        num1 = int(input("Enter the First Number :"))
        num2 = int(input("Enter the Second Number :"))
        smallest = num1
        if num2 < num1:
            smallest = num2
        largestFactor = 1
        for i in range(1, smallest + 1):
            if num1 % i == 0 and num2 % i == 0:
                largestFactor = i
        print(f"Greatest common factor of {num1} and {num2} is {largestFactor}")

    # 15
    def lcm(self):
        num1 = int(input("Enter the First Number :"))
        num2 = int(input("Enter the Second Number :"))
        largest = num1
        if num2 > num1:
            largest = num2
        leastComMul = num1 * num2
        for i in range(1, largest + 1):
            if leastComMul != num1 * num2:
                break
            for j in range(1, largest + 1):
                if num1 * i == num2 * j:
                    leastComMul = num1 * i
                    break
                elif num2 * j > num1 * i:
                    break
        print(f"Least common Multiple of {num1} and {num2} is {leastComMul}")

    # 16
    def sumOfSerious(self):
        sum = 0
        for i in range(1, 97 + 1, 2):
            sum += i / (i + 2)
        print("1/3+3/5+5/9+ . . . +95/97+97/99 = ", sum)

    # 17
    def isbn(self):
        number = input("Enter nine digit number:")
        if len(number) != 9:
            print("Invalid,Input must be nine digit")
            return
        checksum = 0
        temp = int(number)
        for i in range(9, 0, -1):
            digit = temp % 10
            print(digit)
            checksum += digit * i
            print("ch", checksum)
            temp = temp // 10
            print("temp", temp)
        checksum = checksum % 11
        if checksum == 10:
            checksum = "X"
        print("ISBN :" + number + str(checksum))

    # 18
    def exp(self):
        x = int(input("for e^X enter the value of X :"))
        sum = 1
        for i in range(1, 100):
            sum += (x ** i) / self.facto(i)
        print(f"e^{x} = {sum}")

    # 19
    def leapYear(self):
        print("list of leap year in twenty-first century (2001-2100)")
        for year in range(1700, 2100 + 1):
            if (year % 400 == 0 or year % 100 != 0 and year % 4 == 0):
                print(year, end="\t")

    # 20
    def largestAndOccurrence(self):
        numbers = input("Enter numbers:\nUse space as a separator:\n>>").split()
        max = 0
        occurrence = 1
        for num in numbers:
            num = int(num)
            if num > max:
                max = num
                occurrence = 1
            elif num == max:
                occurrence += 1
        print("the largest number is", max)
        print("the occurrence of the largest number is", occurrence)

    # 21
    def numWithDigitCube(self):
        low = 100
        high = 1000
        print("list of numbers that is equal to the sum of cube of its digit ")
        for num in range(low, high):
            digits = []
            tempNum = num
            while tempNum > 0:
                digit = tempNum % 10
                digits.append(digit)
                tempNum = tempNum // 10
            digitSum = 0
            for i in digits:
                digitSum += i ** 3
            if num == digitSum:
                print(num)

    # 22
    def digitcount(self):
        while True:
            num = int(input("Enter a number:"))
            if num < 0:
                return
            count = 0
            while num > 0:
                count += 1
                num = num // 10
            print("Number of digit =", count)

    # 23
    def primeCount(self):
        bound = int(input("Enter the maximum bound:"))
        count = 0
        for num in range(2, bound + 1):
            haveFactor = False
            for factor in range(2, (num // 2) + 1):
                if num % factor == 0:
                    haveFactor = True
                    break
            if not haveFactor:
                count += 1
        print(f"there are {count} prime number between 2 and {bound}")

    # 24
    def isPerfectNUmber(self):
        number = int(input("Enter positive integer:"))
        digitSum = 0
        properDivisor = []
        for i in range(1, (number // 2) + 1):
            if number % i == 0:
                digitSum += i
                properDivisor.append(i)
        if digitSum == number:
            print(f"{number} is Perfect number")
            print(f"proper divisor of {number}:{properDivisor}")
        else:
            print(f"{number} is Not Perfect number")

    # 25
    def countNumAve(self):
        num = int(input("Enter an number,<enter 0 to terminate>: "))
        count_pos = 0
        count_neg = 0
        total = 0
        average = 0
        if (num != 0):
            while (num != 0):
                if (num > 0):
                    count_pos += 1
                elif (num < 0):
                    count_neg += 1
                total += num
                num = int(input("Enter an number,<enter 0 to terminate>: "))
                count = count_pos + count_neg
                average = total / count

            print("The number of positives is", count_pos)
            print("The number of negatives is", count_neg)
            print("The total is", total)
            print("The average is", float(average))
        else:
            print("No input entered")

    # 26
    def tutionCost(self):
        totalCost = 0
        tuition = 10000
        tuition10Year = 0
        for year in range(1, 15):
            # increase tuition by 5% every year
            tuition += tuition * 0.05
            # test for after 10 years
            if year > 10:
                totalCost += tuition
            # cost of tution in ten years
            if year == 10:
                tuitionTenthYear = tuition
        print()
        print("Tuition in ten years: $", tuition10Year)
        print("Total cost for four years' worth of",
              "tuition after ten years: $", totalCost)

    # 27
    def conversion(self):

        while True:
            print("Select your choice .")
            print("     1. TO convert pound to kilogram  ")
            print("     2. TO convert mile to kilometer  ")
            print("     3. TO convert hour to minute ")
            print("     0. To Exit ")

            choice = input(">>selected Conversion: ")
            if choice in ('1', '2', '3', '0'):
                if choice == '1':
                    pounds = int(input("        Enter weight in Pounds: "))
                    kgs = pounds / 2.2046
                    print("     weight in kilogram = ", kgs)
                elif choice == '2':
                    mile = int(input("      Enter distance in mile: "))
                    kilometer = 1.609 * mile
                    print("     distance in kilometer = ", kilometer)
                elif choice == '3':
                    hour = int(input("      Enter time in hour: "))
                    minute = hour * 60
                    print("     time in minute = ", minute)
                elif choice == '0':
                    return
                else:
                    print("Entered input is invalid")

    # 28
    def topTwoStudents(self):

        num = int(input("Enter number of students:"))
        names = []
        marks = []
        for i in range(1, num + 1):
            name = input(f"       Name of students{i}:")
            mark = int(input(f"         Enter Mark :"))
            names.append(name)
            marks.append(mark)
        top1 = marks[0]
        for mark in marks:
            if mark > top1:
                top1 = mark
        top2 = marks[0]
        for mark in marks:
            if mark > top2:
                if mark < top1:
                    top2 = mark
        print(f'Student {names[marks.index(top1)]} has the highest mark')
        print('     The his mark  =', top1)
        print(f'Student {names[marks.index(top2)]} has the second highest mark')
        print('        His mark  =', top2)

    # 29
    def topOneStudent(self):

        num = int(input("Enter number of students:"))
        names = []
        marks = []
        for i in range(1, num + 1):
            name = input(f"       Name of students{i}:")
            mark = int(input(f"         Enter His Mark:"))
            names.append(name)
            marks.append(mark)
        top = marks[0]
        for mark in marks:
            if mark > top:
                top1 = mark

        print(f'Student {names[marks.index(top)]} has the highest mark')
        print('      His mark  =', top1)

    # 30
    def multOf5and6NotBoth(self):
        print("List of number which is divisible by 5 and 6 But not both")
        count = 0
        for num in range(100, 200 + 1):
            if num % 5 == 0 and num % 6 == 0:
                continue
            elif num % 5 == 0 or num % 6 == 0:
                count += 1
                print(num, end="\t")
            if count == 10:
                print()
                count = 0

    # 31
    def ascii(self):
        print("ACCII characters from ! to ~ ")
        count = 0
        for i in range(33, 127):
            print(chr(i), end="\t")
            count += 1
            if count == 10:
                print()
                count = 0

    # 32A pattern
    def patternA(self):
        for i in range(1, 6 + 1):
            for j in range(6, i, -1):
                print(end="\t")
            for j in range(1, i + 1):
                print((i - j + 1), end="\t")
            print()

    # 32B pattern
    def patternB(self):
        for i in range(1, 7):
            for j in range(1, i):
                print(end="\t")
            for j in range(1, 7 - i + 1):
                print(j, end="\t")
            print()

    # 33 pattern
    def patternPyramid(self):
        line = int(input("Enter the number of line:"))
        for i in range(1, line + 1):
            for j in range(line, i, -1):
                print(end="\t")
            for j in range(1, i + 1):
                print((i - j + 1), end="\t")
            for j in range(2, i + 1):
                print((j + 0), end="\t")
            print()

    # 34
    def patternPascal(self):
        for i in range(0, 8):
            for j in range(8, i, -1):
                print(end="\t")
            for j in range(0, i + 1):
                print(2 ** j, end="\t")
            for j in range(i - 1, 0 - 1, -1):
                print(2 ** j, end="\t")
            print()

    # 35
    def loanAmountPeriod(self):
        loanAmount = int(input("Enter loan amount:"))
        numberOfYears = int(input("Enter number of years: "))
        annualInterestRate = 5000.0
        print("Interest Rate", "     ", "Monthly Payment", "         ",
              "Total Payment")
        while (annualInterestRate <= 8000.0):
            monthlyInterestRate = (annualInterestRate / 1000) / 1200
            monthlyPayment = (
                    loanAmount * monthlyInterestRate /
                    (1 - 1 / math.pow(1 + monthlyInterestRate, numberOfYears * 12)) *
                    10)
            totalPayment = (monthlyPayment * numberOfYears * 12)
            print((annualInterestRate / 1000), "              ", monthlyPayment, "        ",
                  totalPayment)
            annualInterestRate = annualInterestRate + 125.0

    # 36
    def toHexadecomal(self):
        decimal = int(input("Enter decimal number:"))
        hexadecimal = ""
        while (1):
            remainder = decimal % 16
            if remainder == 10:
                hexadecimal = 'A' + hexadecimal
            elif remainder == 11:
                hexadecimal = 'B' + hexadecimal
            elif remainder == 12:
                hexadecimal = 'C' + hexadecimal
            elif remainder == 13:
                hexadecimal = 'D' + hexadecimal
            elif remainder == 14:
                hexadecimal = 'E' + hexadecimal
            elif remainder == 15:
                hexadecimal = 'F' + hexadecimal
            else:
                hexadecimal = str(remainder) + hexadecimal

            decimal = decimal // 16
            if decimal == 0:
                break
        print("Hexadecimal Value =", hexadecimal)

    # 37
    def eulers_number(self):
        sum = 1
        for i in range(1, 60 + 1):
            sum += 1 / self.factorials(i)
        print("Euler's number")
        print(f"1 + 1/1! +1/2! +1/3! + . . .!  = {sum}")

    def factorials(self, num):
        facto = 1
        if num > 1:
            facto = num * self.factorials(num - 1)
        return facto

    # 38
    def isPrime(self):
        num = int(input("Enter a Natural number:"))
        if num == 1:
            print('One is neither prime nor composite')
            return
        elif num == 0:
            # Zero is divisible by any number except itself,i.e not prime
            print('Zero is not prime number')
            return
        # search for the factor of the number ,if the number is different from zero and one
        prime = True
        for factor in range(2, num - 1):
            if num % factor == 0:
                prime = False
                break
        if prime:
            print(f"{num} is Prime number")
        else:
            print(f"{num} is Not Prime number")

    # 39
    def isEven(self):
        num = int(input("Enter a number:"))
        if num % 2 == 0:
            print(f"{num} is Even number")
        else:
            print(f"{num} is Not Even number")

    # 40
    def calculator(self):
        print("==============================================\n"
              "Simple calculator documentation\n"
              "It works for only for the FOUR operators(+,-,*,/) \n"
              "Simply put your expression which is combination of operator and operands like\n "
              "       Enter your Excretion:3+4\n"
              "       output 4+4 = 7\n"
              "====================================================")
        expression = input("Enter your Excretion:")

        if '*' in expression:
            result = self.product(expression)
            print(f"{expression} = {result}")
        elif '/' in expression:
            result = self.quationt(expression)
            print(f"{expression} = {result}")
        elif '+' in expression:
            result = self.sum(expression)
            print(f"{expression} = {result}")
        elif '-' in expression:
            result = self.difference(expression)
            print(f"{expression} = {result}")
        else:
            print("Invalid input not expression!")
            return

    def product(self, expression):
        operand1, operand2 = expression.split("*")
        product = int(operand1) * int(operand2)
        return product

    def quationt(self, expression):
        operand1, operand2 = expression.split("/")
        quationt = int(operand1) / int(operand2)
        return quationt

    def sum(self, expression):
        operand1, operand2 = expression.split("+")
        sum = int(operand1) + int(operand2)
        return sum

    def difference(self, expression):
        operand1, operand2 = expression.split("-")
        difference = int(operand1) - int(operand2)
        return difference

    # 41
    def factrialsum(self):
        n = int(input("Enter the value of  'n' :"))
        sum = 0
        for i in range(1, n + 1):
            sum += self.facto(i)
        print(f"1!+2!+3!+ ... +{n}! = {sum}")

