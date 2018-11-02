import xlrd
import matplotlib.pyplot as plt
file_location = "/home/dl108/g1/ex.xlsx"
workbook = xlrd.open_workbook(file_location)
first_sheet = workbook.sheet_by_index(0)
for col in range(first_sheet.ncols):
	x = [first_sheet.cell_value(i, 0) for i in range(first_sheet.ncols)]
	y = [first_sheet.cell_value(i,1) for i in range(first_sheet.ncols)]
	z = [first_sheet.cell_value(i,2) for i in range(first_sheet.ncols)]
plt.plot(x,y,z)
plt.show()