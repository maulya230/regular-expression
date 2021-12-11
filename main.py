import re # import regular expressions
text = open("data.txt")
numbers = []
Total = 0
for line in text:
    nmbrs = re.findall('[0-9]+', line)
    numbers = numbers + nmbrs 
for n in numbers:
    Total = Total + float(n)
print ("Total = ", Total )