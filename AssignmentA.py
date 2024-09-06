# Assignment A
salary = int(input("eneter monthly salary: "))
Ma = salary * 0.1
yearly = (salary - Ma) * 12
net = 0
tax = 0
exceeding = 0

if (yearly <= 600000):
    net = yearly
elif (yearly > 600000 and yearly <= 1200000 ):
    exceeding = yearly - 600000
    tax = exceeding * 0.05
    net = yearly - tax
elif (yearly > 1200000 and yearly <= 2200000):
    exceeding = yearly - 1200000
    tax = 30000 + (exceeding *0.15)
    net = yearly - tax
elif (yearly > 2200000 and yearly <= 3200000):
    exceeding = yearly - 2200000
    tax = 180000 + (exceeding * 0.25)
    net = yearly - tax
elif (yearly > 3200000 and yearly <= 4100000):
    exceeding = yearly - 3200000
    tax = 430000 + (exceeding * 0.3)
    net = yearly - tax
else :
    exceeding = yearly - 4100000
    tax = 700000 + (exceeding * 0.35)
    net = yearly - tax

netMonthly = (net / 12) + Ma

print("Net monthly salary after tax deduction: ", netMonthly)
