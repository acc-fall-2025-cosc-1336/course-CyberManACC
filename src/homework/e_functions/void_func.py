from value_return import (
    get_gross_pay,
    get_fica_tax,
    get_federal_tax,
)

def display_payroll_check(hours, rate):
    """
    Prints the paycheck lines using the required labels.
    Formatting to 2 decimals; spacing similar to the example.
    """
    gross = get_gross_pay(hours, rate)
    fica = get_fica_tax(gross)
    fed = get_federal_tax(gross)
    net = gross - fica - fed

    # Match the example’s labels; numeric formatting to 2 decimals.
    print(f"Gross Pay:{gross:>14.2f}\n")
    print(f"FICA:{fica:>20.2f}\n")
    print(f"Federal Tax:{fed:>13.2f}\n")
    print(f"Net Pay:{net:>16.2f}\n")
