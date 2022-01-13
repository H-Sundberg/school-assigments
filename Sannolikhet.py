dates_of_2020_list = []
month_list = [1,2,3,4,5,6,7,8,9,10,11,12]
day_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
year2020 = 20
days_of_seven = []

for month in month_list:
    for day in day_list:
        if month == 2 and day>29:
            break
        if month == 4 and day>30:
            break
        if month == 6 and day>30:
            break
        if month == 9 and day>30:
            break
        if month == 11 and day>30:
            break
        if round(year2020 / 10,0) + year2020 % 10 + round(month / 10,0) + month % 10 + round(day / 10,0) + day % 10 == 7:
            days_of_seven.append(str(month)+"/"+str(day)+"/"+str(year2020))
        else:
            datum = ""
            datum +=str(month)+"/"+str(day)+"/"+str(year2020)
            dates_of_2020_list.append(datum)


print("lista av datum med sju:", days_of_seven)

sannolikhet = (len(days_of_seven)/ 366)*100
print("sannolikheten är:", round(sannolikhet, 4), "%")
print(len(days_of_seven), "chanser av 366")