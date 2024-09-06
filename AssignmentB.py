def calculate_gross_salary_from_net(net_monthly_salary):
    # Calculate the medical allowance (10% of gross salary)
    def get_medical_allowance(gross_monthly_salary):
        return gross_monthly_salary * 0.1
    
    # Tax calculation function
    def calculate_tax(gross_yearly_salary):
        if gross_yearly_salary <= 600000:
            return 0
        elif gross_yearly_salary <= 1200000:
            return (gross_yearly_salary - 600000) * 0.05
        elif gross_yearly_salary <= 2200000:
            return 30000 + (gross_yearly_salary - 1200000) * 0.15
        elif gross_yearly_salary <= 3200000:
            return 180000 + (gross_yearly_salary - 2200000) * 0.25
        elif gross_yearly_salary <= 4100000:
            return 430000 + (gross_yearly_salary - 3200000) * 0.30
        else:
            return 700000 + (gross_yearly_salary - 4100000) * 0.35
    
    # Use a more accurate iterative approach to find the gross monthly salary
    low = 0
    high = 1000000
    tolerance = 0.01
    
    while (high - low) > tolerance:
        mid = (low + high) / 2
        Ma = get_medical_allowance(mid)
        gross_yearly_salary = mid * 12
        tax = calculate_tax(gross_yearly_salary)
        net_yearly_salary = gross_yearly_salary - tax
        calculated_net_monthly_salary = (net_yearly_salary / 12) - Ma
        
        if calculated_net_monthly_salary < net_monthly_salary:
            high = mid
        else:
            low = mid
    
    gross_monthly_salary = (low + high) / 2
    gross_yearly_salary = gross_monthly_salary * 12
    final_tax = calculate_tax(gross_yearly_salary)
    
    return gross_monthly_salary, final_tax

# Input value
net_monthly_salary = 299666.67
gross_monthly_salary, tax = calculate_gross_salary_from_net(net_monthly_salary)

print(f"Gross monthly salary before tax deduction: {gross_monthly_salary:.2f}")
print(f"Total tax: {tax:.2f}")
