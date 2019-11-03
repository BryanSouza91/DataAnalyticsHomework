Attribute VB_Name = "Module1"
Sub StocksBonus()

Dim WS_Count As Long
Dim ws As Long
Dim OrgWS As Worksheet
Set OrgWS = ActiveSheet
' Set WS_Count equal to the number of worksheets in the active workbook.
WS_Count = ThisWorkbook.Worksheets.Count

' Begin the worksheet loop.
For ws = 1 To WS_Count
 ThisWorkbook.Worksheets(ws).Activate


' Define last row unique list
Dim LastRowUni As LongLong
LastRowUni = Cells(Rows.Count, 12).End(xlUp).Row

Dim GPIval As Double
Dim LPIval As Double
Dim GTVval As LongLong
Dim inarr() As Variant

Cells(1, 18).Value = "Ticker"
Cells(1, 19).Value = "Value"
Cells(2, 17).Value = "Greatest % Increase"
Cells(3, 17).Value = "Least % Increase"
Cells(4, 17).Value = "Greatest Total Volume"

GPIval = WorksheetFunction.Max(ActiveSheet.Range("N2:N" & LastRowUni))
Cells(2, 19).Value = GPIval
LPIval = WorksheetFunction.Min(ActiveSheet.Range("N2:N" & LastRowUni))
Cells(3, 19).Value = LPIval
GTVval = WorksheetFunction.Max(ActiveSheet.Range("O2:O" & LastRowUni))
Cells(4, 19).Value = GTVval

inarr = Range("L2:O" & LastRowUni)
For k = 1 To (LastRowUni - 1)
 If inarr(k, 4) = GTVval Then
  Cells(4, 18).Value = inarr(k, 1)
 ElseIf inarr(k, 3) = LPIval Then
  Cells(3, 18).Value = inarr(k, 1)
 ElseIf inarr(k, 3) = GPIval Then
  Cells(2, 18).Value = inarr(k, 1)
  
 End If
 
Next k

ActiveSheet.Columns("L:S").AutoFit
ActiveSheet.Range("S2").NumberFormat = "0.00%"
ActiveSheet.Range("S3").NumberFormat = "0.00%"
 
Next ws
OrgWS.Activate
End Sub
