StudentId = input("Enter your Student ID: ")
EmailId = input("Enter your Email ID: ")
Password = input("Enter your Password: ")
ReferralCode = input("Enter Referral Code: ")

is_valid = True

if len(StudentId) != 7 :
    is_valid = False
else:
    if StudentId[0:3] != "CSE":
        is_valid = False
    elif StudentId[3] != '-':
        is_valid = False
    elif not (StudentId[4].isdigit() and StudentId[5].isdigit() and StudentId[6].isdigit()):
        is_valid = False


if EmailId.count('@') < 1 or EmailId.count('.') < 1:
    is_valid = False
elif EmailId[0] == '@':
    is_valid = False
elif EmailId[len(EmailId)-4:] != ".edu":
    is_valid = False


if len(Password) < 8:
    is_valid = False
elif 'a' <= Password[0] <= 'z' :
    is_valid = False
elif Password.count("0") + Password.count("1") + Password.count("2") + Password.count("3") + Password.count("4") + \
     Password.count("5") + Password.count("6") + Password.count("7") + Password.count("8") + Password.count("9") == 0:
    is_valid = False
    


if len(ReferralCode) != 6:
    is_valid = False
else:
    if ReferralCode[0:3] != "REF":
        is_valid = False
    elif not (ReferralCode[3].isdigit() and ReferralCode[4].isdigit()):
        is_valid = False
    elif ReferralCode[5] != '@':
        is_valid = False


if is_valid:
    print("Approved")
else:
    print("Rejected")