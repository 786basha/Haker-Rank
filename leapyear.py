# def is_leap(year):
#     if year %4==0:
#         if year %100==0:
#             if year %400==0:
#                 return True
#             else: return False
#         else: return False
#     else: return False
# #
# year=int(input("enter the year:"))
# print(is_leap(year))
def is_leap(year):
    leap = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 ==0:
                return True
            else: return False
        else:
            return False
    else:
        return False


year = int(input())
print(is_leap(year))