yob = int(input("Năm sinh của bạn?"))
age = 2018 - yob
if age < 10:
    print("Baby")
elif age < 18:
    print("teenager")
else:
    print("adult")