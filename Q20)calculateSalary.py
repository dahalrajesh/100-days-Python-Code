def calculate_in_hand_salary():
    try:
        # Input the annual salary
        salary = float(input("Enter your annual salary: "))

        # Calculate HRA (10%), DA (5%), and PF (3%)
        hra_deduction = 0.1 * salary
        da_deduction = 0.05 * salary
        pf_deduction = 0.03 * salary

        # Calculate taxable income after HRA, DA, and PF deductions
        taxable_income = salary - (hra_deduction + da_deduction + pf_deduction)

        # Determine tax percentage based on salary slabs
        if 0 <= salary <= 1_00_000:
            print("Salary too low to calculate deductions. Print K.")
            return

        if 5_00_000 < Taxable brackets applied .


