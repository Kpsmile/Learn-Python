import xlrd
import xlwt
from xlrd import open_workbook
import os
import stat

# import arcpy

wb_Infibeam = open_workbook ("F:\\home_test_1\\Mobiles-Infibeam.xls")
wb_master = open_workbook ("F:\\home_test_1\\Mobiles-Master-Data.xls")

sheet_infibeam = wb_Infibeam.sheet_by_index(0)
s1=sheet_infibeam.cell_value(0,0)


sheet_master = wb_master.sheet_by_index(0)
s2=sheet_master.cell_value(0,0)

print(s1)
# print(sheet_infibeam.nrows)
no_of_rows_infibeam=sheet_infibeam.nrows
print(no_of_rows_infibeam)
print(sheet_infibeam.ncols)

print(s2) 
print(sheet_master.nrows)
no_of_rows_master=sheet_master.nrows
print(sheet_master.ncols)



# for row in range(sheet.nrows):
# #     print sheet.cell_value(row,0)
#     s1=sheet.cell_value(row,0)
#     print(s1)
    
# Infibeam = [sheet_infibeam.cell_value(row,0) for row in range(sheet_infibeam.nrows)]
Infibeam =[ [sheet_infibeam.cell_value(row,col) for col in range(sheet_infibeam.ncols)] for row in range(sheet_infibeam.nrows) ]
print Infibeam
print Infibeam[1][0]
print Infibeam[1][1]

# master = [sheet_master.cell_value(row,0) for row in range(sheet_master.nrows)]
master =[ [sheet_master.cell_value(row,col) for col in range(sheet_master.ncols)] for row in range(sheet_master.nrows) ]
print master

wb=xlwt.Workbook(encoding="utf-8")
ws =wb.add_sheet("sheet78")
# ws.write(0,0,Infibeam[0][0])
k=0
# n=1
while k<no_of_rows_infibeam:
#     k=k+1
#     print k
#     if l<3:
      
    ws.write(k,0,Infibeam[k][0])
    wb.save("F:\\home_test_1\\Writing_test20.xls")
    ws.write(k,1,Infibeam[k][1])
     
     
    wb.save("F:\\home_test_1\\Writing_test20.xls")
    st = os.stat('F:\\home_test_1\\Writing_test20.xls')    
    os.chmod('F:\\home_test_1\\Writing_test20.xls', st.st_mode | stat.S_IWOTH)
    k=k+1
    print k
k=0
while k<sheet_master.nrows:
      
    ws.write(k,2,master[k][0])
    wb.save("F:\\home_test_1\\Writing_test20.xls")
    ws.write(k,3,master[k][1])
    wb.save("F:\\home_test_1\\Writing_test20.xls")
    k=k+1
    print k
#     st = os.stat('F:\\home_test_1\\Writing_test20.xls')    
#     os.chmod('F:\\home_test_1\\Writing_test20.xls', st.st_mode | stat.S_IWOTH)



X=[]
Y=[]

for mylist_1 in Infibeam:
    X.append(mylist_1[0])
    # print (mylist_1[0])
    
print X


for mylist_2 in master:
    Y.append(mylist_2[0])
    
print Y
    
l=0


for each_1 in X:
    for each_2 in Y:
        while l<16:
            if each_1 == each_2:
                print l
                print each_2
                print("updating")
#                 print X.index(each_2)
                ws.write(l,4,"MATCH")
                wb.save("F:\\home_test_1\\Writing_test20.xls")
                l=l+1
                print l
            else:
                print l
                print each_2
#                 print X.index(each_2)
#                 print "NO MATCH"
                ws.write(l,4,"NO MATCH")
                wb.save("F:\\home_test_1\\Writing_test20.xls")
                l=l+1
                print l