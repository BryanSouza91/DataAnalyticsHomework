Attribute VB_Name = "Module10"
Sub Stocks()

Dim WS_Count As Long
Dim ws As Long
Dim OrgWS As Worksheet
Set OrgWS = ActiveSheet
' Set WS_Count equal to the number of worksheets in the active workbook.
WS_Count = ThisWorkbook.Worksheets.Count

' Begin the worksheet loop.
For ws = 1 To WS_Count
 ThisWorkbook.Worksheets(ws).Activate


' Define last row variable
 Dim LastRowNon As Long
 LastRowNon = Cells(Rows.Count, 1).End(xlUp).Row

' Define ranges for loops
 Dim i As Long
 Dim j As Long
 Dim OpDate As Long
 Dim ClDate As Long
 OpDate = WorksheetFunction.Min(ActiveSheet.Range("B2:B" & LastRowNon))
 ClDate = WorksheetFunction.Max(ActiveSheet.Range("B2:B" & LastRowNon))

' Define variable for cumulative total volume
 Dim TotalVol As LongLong
 TotalVol = 0

' Filter for unique
ActiveSheet.Range("A1:A" & LastRowNon).AdvancedFilter _
    Action:=xlFilterCopy, _
    CopyToRange:=ActiveSheet.Range("L1"), _
    Unique:=True

' Define last row unique list
Dim LastRowUni As Long
LastRowUni = Cells(Rows.Count, 12).End(xlUp).Row

' Begin the cell loop.
 For i = 2 To LastRowUni
  For j = 2 To LastRowNon
   If Cells(i, 12).Value = Cells(j, 1).Value Then
' Zero handling below
    If Cells(j, 2).Value = OpDate And Cells(j, 3).Value <> 0 Then
     Op = Cells(j, 3).Value
    ElseIf Cells(j, 2).Value = ClDate Then
     Cl = Cells(j, 6).Value
     If Op <> 0 Then
      Cells(i, 13).Value = Cl - Op
      Cells(i, 14).Value = ((Cl - Op) / Op)

     Else
      Cells(i, 13).Value = 0
      Cells(i, 14).Value = 0
     End If
    End If
' Calculate volume cumulative total
     TotalVol = TotalVol + Cells(j, 7).Value
    
   Else
' Store cumulative volume total
    Cells(i, 15).Value = TotalVol
' Reset to 0 before next ticker
    TotalVol = 0
' Reset Cl and Op
    Cl = 0
    Op = 0
' Adjust loop variables
    j = j - 1
    i = i + 1

   End If
   
  Next j
 Next i


 
' Format worksheet here.
' Add % to percent column with colors

ActiveSheet.Cells(1, 15).Value = "Total Volume"
ActiveSheet.Cells(1, 14).Value = "Percent Change"
ActiveSheet.Cells(1, 13).Value = "Yearly Change"
ActiveSheet.Cells(1, 12).Value = "Ticker"
ActiveSheet.Range("M2:M" & LastRowUni).Style = "Currency"
ActiveSheet.Range("N2:N" & LastRowUni).NumberFormat = "0.000%"

Dim rng As Range
Set rng = ActiveSheet.Range("M2:M" & LastRowUni)
For Each cell In rng
    If cell.Value > 0 Then
        cell.Interior.Color = vbGreen
    Else
        cell.Interior.Color = vbRed
    End If
Next cell

' Do bonus stuff here
Dim GPIval As Double
Dim LPIval As Double
Dim GTVval As LongLong
Dim inarr() As Variant

' Setup Table
ActiveSheet.Cells(1, 18).Value = "Ticker"
ActiveSheet.Cells(1, 19).Value = "Value"
ActiveSheet.Cells(2, 17).Value = "Greatest % Increase"
ActiveSheet.Cells(3, 17).Value = "Greatest % Decrease"
ActiveSheet.Cells(4, 17).Value = "Greatest Total Volume"

' Find values for table
GPIval = WorksheetFunction.Max(ActiveSheet.Range("N2:N" & LastRowUni))
ActiveSheet.Cells(2, 19).Value = GPIval
LPIval = WorksheetFunction.Min(ActiveSheet.Range("N2:N" & LastRowUni))
ActiveSheet.Cells(3, 19).Value = LPIval
GTVval = WorksheetFunction.Max(ActiveSheet.Range("O2:O" & LastRowUni))
ActiveSheet.Cells(4, 19).Value = GTVval

' Find tickers for table
inarr = Range("L2:O" & LastRowUni)
For k = 1 To (LastRowUni - 1)
 If inarr(k, 4) = GTVval Then
  ActiveSheet.Cells(4, 18).Value = inarr(k, 1)
 ElseIf inarr(k, 3) = LPIval Then
  ActiveSheet.Cells(3, 18).Value = inarr(k, 1)
 ElseIf inarr(k, 3) = GPIval Then
  ActiveSheet.Cells(2, 18).Value = inarr(k, 1)
  
 End If
 
Next k

' Formatting
ActiveSheet.Range("S2").NumberFormat = "0.00%"
ActiveSheet.Range("S3").NumberFormat = "0.00%"
ActiveSheet.Columns("L:S").AutoFit

Next ws
OrgWS.Activate
End Sub