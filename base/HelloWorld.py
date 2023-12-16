from openpyxl import Workbook  
wb = Workbook()

planilha = wb.worksheets[0]

planilha['A1'] = "Banana"
planilha['B1'] = "Paçoca"

planilha.title = "Planilha de Frutas"

wb.save("C:\Script\meuarquivo.xlsx")
