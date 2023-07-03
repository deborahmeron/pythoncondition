marks = float(input("marks"))

if marks > 100:
    print("error")
elif marks > 81 < 100:
    print("Grade A plain")
elif marks > 76 < 80:
    print("Grade A-")
elif marks > 70 < 75:
    print("Grade B+")
elif marks > 65 < 69:
    print("Grade B plain")
elif marks > 60 < 64:
    print("Grade B-")
elif marks > 55 < 59:
    print("Grade C+")
elif marks > 50 < 54:
    print("Grade C plain")
elif marks > 45 < 49:
    print("Grade D+")
elif marks > 40 < 44:
    print("Grade D")
elif marks > 0 < 39:
    print("Grade D-")
 else:print("error")

