import math
import argparse
import sys


def incorrect():
    print("Incorrect parameters")

parser = argparse.ArgumentParser()
parser.add_argument("--type", type=str)
parser.add_argument("--principal", type=int)
parser.add_argument("--interest", type=float)
parser.add_argument("--periods", type=int)
parser.add_argument("--payment", type=int)
args = parser.parse_args()


if len(sys.argv) < 4 or args.interest is None:
    incorrect()

elif args.type == "annuity":
    interest = (args.interest / 100) / 12
    if not args.principal and args.payment:
        loan_principal = math.floor(
            args.payment / (
                        (interest * math.pow(1 + interest, args.periods)) / (math.pow(1 + interest, args.periods) - 1)))
        print(f"Your loan principal = {loan_principal}")
        total_payment = args.payment * args.periods
        print(f"Overpayment = {total_payment - loan_principal}")
    elif args.principal and not args.payment:
        annuity = math.ceil(args.principal * ((interest * math.pow(1 + interest, args.periods)) /
                                            (math.pow(1+interest, args.periods) - 1)))
        total_p = annuity * args.periods
        print(f"Your annuity payment = {annuity}")
        print(f"Overpayment = {total_p - args.principal}")

    else:
        base = 1 + interest
        x = args.payment / (args.payment - interest * args.principal)
        months = math.ceil((math.log(x, base)))

        years = months // 12
        and_months = months - (years * 12)

        if years == 0:
            if months == 1:
                print(f"It will take {and_months} month to repay this loan!")
            else:
                print(f'It will take {and_months} months to repay this loan!')
        elif years == 1:
            if months == 0:
                print(f"It will take {years} year to repay this loan!")
            elif months == 1:
                print(f"It will take {years} year and\n{and_months} month"
                      f" to repay this loan!")
            else:
                print(f"It will take {years} year and\n{and_months} months"
                      f" to repay this loan")
        else:
            if and_months == 0:
                print(f"It will take {years} years to repay this loan!")
            elif and_months == 1:
                print(f"It will take {years} years and\n{and_months} month"
                      f" to repay this loan!")
            else:
                print(f"It will take {years} years and\n{and_months} months"
                      f" to repay this loan!")
        total_payment = months * args.payment
        print(f"Overpayment = {total_payment - args.principal}")


elif args.type == "diff" and args.periods and args.principal:
    interest = (args.interest / 100) / 12
    total_payment = 0
    for i in range(1, args.periods + 1):
        m_payment = math.ceil((args.principal / args.periods) + interest * (
                args.principal - ((args.principal * (i - 1)) / args.periods)))
        total_payment += m_payment
        print(f"Month {i}: payment is {m_payment}\n")

    print(f"Overpayment = {total_payment - args.principal}")


else:
    incorrect()
