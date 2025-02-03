def grade(score):
    if score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"

score = float(input("กรุณากรอกคะแนนสอบของคุณ: "))
print(f"เกรดของคุณคือ: {grade(score)}")