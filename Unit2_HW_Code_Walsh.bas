Attribute VB_Name = "Module11"
'Sub WS_easy()
'
'' Setting variable types
'Dim Stock_Name As String
'Dim Total_Stock_Volumn As Double
'Dim Sum_Table_Row As Long
'Dim i As Long
'Dim LastRow As Long
'
'' Setting initial variable values
'Sum_Table_Row = 2
'
'' Determining number of last row
'LastRow = Range("A" & Rows.Count).End(xlUp).Row
'
'' Proving rows were counted
'' MsgBox (LastRow)
'
'' Loop for finding names and volumn
'For i = 2 To LastRow
'If Cells(i + 1, 1).Value <> Cells(i, 1).Value Then
'Stock_Name = Cells(i, 1).Value
'Total_Stock_Volumn = Total_Stock_Volumn + Cells(i, 7).Value
'
'Range("I" & Sum_Table_Row).Value = Stock_Name
'Range("L" & Sum_Table_Row).Value = Total_Stock_Volumn
'
'Sum_Table_Row = Sum_Table_Row + 1
'
'Total_Stock_Volumn = 0
'
'Else
'
'Total_Stock_Volumn = Total_Stock_Volumn + Cells(i, 7).Value
'
'End If
'
'Next i
'
'
'
'End Sub

Sub WS_Challenge()
    Dim xSh As Worksheet
    Application.ScreenUpdating = False
    For Each xSh In Worksheets
        xSh.Select
        Call WS_moderate
    Next
    Application.ScreenUpdating = True
End Sub
Sub WS_moderate()

' Setting variable types
Dim Stock_Name As String
Dim Total_Stock_Volumn As Double
Dim Sum_Table_Row As Long
Dim i As Long
Dim LastRow As Long

Dim Year_Opening_Price As Double
Dim Year_Closing_Price As Double
Dim Yearly_Change As Double
Dim Percent_Change As Double

Dim MaxPercent As Double
Dim MinPercent As Double
Dim MaxVolumn As Double


' Setting initial variable values
Sum_Table_Row = 2
YearOpenFlag = False
Year_Opening_Price = Cells(2, 3).Value


' Determining number of last row
LastRow = Range("A" & Rows.Count).End(xlUp).Row

' ' Proving rows were counted
' MsgBox (LastRow)

    ' Add output Column Header
     Range("I:L").EntireColumn.AutoFit
       Cells(1, 9).Value = "Ticker"
       Cells(1, 10).Value = "Yearly Change"
       Cells(1, 11).Value = "Percent Change"
       Cells(1, 12).Value = "Total Stock Volumn"
       
     ' Add output labels
     Range("N:P").EntireColumn.AutoFit
       Cells(2, 14).Value = "Greatest % Increase"
       Cells(3, 14).Value = "Greatest % Decrease"
       Cells(4, 14).Value = "Greatest Total Volumn"
       
       ' Adds last two column headers
       Cells(1, 15).Value = "Ticker"
       Cells(1, 16).Value = "Value"

' Loop for finding names and volumn
For i = 2 To LastRow

If Cells(i + 1, 1).Value <> Cells(i, 1).Value Then

    Stock_Name = Cells(i, 1).Value
       
   ' Setting the stock's year opening price
    If Not YearOpenFlag Then
    
        Year_Opening_Price = Cells(i + 1, 3).Value
        
    ' Account for first year opening price
        If i = 2 Then
    
             Year_Opening_Price = Cells(2, 3).Value
    
        End If
           
        YearOpenFlag = True
    
    End If
    ' End of first time loop code
    
Total_Stock_Volumn = Total_Stock_Volumn + Cells(i, 7).Value

Range("I" & Sum_Table_Row).Value = Stock_Name
Range("L" & Sum_Table_Row).Value = Total_Stock_Volumn

Sum_Table_Row = Sum_Table_Row + 1

Total_Stock_Volumn = 0

Else

    Year_Closing_Price = Cells(i + 1, 6).Value

    Total_Stock_Volumn = Total_Stock_Volumn + Cells(i, 7).Value

    Yearly_Change = Year_Closing_Price - Year_Opening_Price
    Range("J" & Sum_Table_Row).Value = Yearly_Change
    
    'Add coloring formatter
    If Yearly_Change < 0 Then
    Range("J" & Sum_Table_Row).Interior.ColorIndex = 3
    
    ElseIf Yearly_Change > 0 Then
    Range("J" & Sum_Table_Row).Interior.ColorIndex = 4
    
    End If
      
' ***
' *** The following error handling needs work
If i = 2 Then
        Year_Opening_Price = Cells(2, 3).Value
        
        End If
        
    ' Calculate percent change
    If Year_Opening_Price = 0 Or IsEmpty(Year_Opening_Price) Then
        Percent_Change = 0 ' "Null" Or "NA" or whatever you'd like
    Else
        Percent_Change = Yearly_Change / Year_Opening_Price
    End If

    
    ' Times 100 and then enters percent into spreadsheet
    Range("K" & Sum_Table_Row).Value = Round(Percent_Change * 100, 2) & "%"


    ' Resetting Flags
        YearOpenFlag = False


End If

Next i

' Determining number of last row of output
LastRowOfOutput = Range("I" & Rows.Count).End(xlUp).Row

' Temporary show output row count
' MsgBox (LastRowOfOutput)

    ' Application.worksheetfunction.max(range("a:a"))
    MaxPercent = Application.WorksheetFunction.Max(Range("K:K"))

    ' Do not multiply times 100 - already reading converted numbers
    Range("P" & 2).Value = Round(MaxPercent, 2) & "%"


    ' Application.worksheetfunction.max(range("a:a"))
    MinPercent = Application.WorksheetFunction.Min(Range("K:K"))

    ' Do not multiply times 100 - already reading converted numbers
    Range("P" & 3).Value = Round(MinPercent, 2) & "%"


    ' Application.worksheetfunction.max(range("a:a"))
    MaxVolumn = Application.WorksheetFunction.Max(Range("L:L"))

    Range("P" & 4).Value = MaxVolumn


    ' Finding the Ticker
    For i = 2 To LastRowOfOutput

        ' Max Percent Ticker
        If Range("K" & i).Value = MaxPercent Then
        
        Range("O" & 2).Value = Range("I" & i).Value
  
        End If
    
        ' MinPercent Ticker
        If Range("K" & i).Value = MinPercent Then
        
        Range("O" & 3).Value = Range("I" & i).Value
  
        End If
        
        ' Max Volumn Ticker
        
        If Range("L" & i).Value = MaxVolumn Then
        
        Range("O" & 4).Value = Range("I" & i).Value
  
        End If
   
    Next i
  
  
End Sub
