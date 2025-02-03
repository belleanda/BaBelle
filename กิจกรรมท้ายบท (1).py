def check_CreditCard(money):
    if money < 15000:
        return "คุณไม่มีสิทธิ์ทำบัตรเครดิต"
    elif money < 70000:
        return "คุณได้ทำบัตรเงิน"
    elif money < 100000:
        return "คุณได้ทำบัตรทอง"
    else:
        return "คุณได้ทำบัตร Platinum"

money = float(input("กรุณากรอกเงินเดือนของคุณ: "))
print(check_CreditCard(money))