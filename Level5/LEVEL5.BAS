' LEVEL5.FRM
Option Explicit

Sub cmdLogin_Click ()
If  edtUsername = Mid(gc0006, 56, 1) & Mid(gc0006, 28, 1) & Mid(gc0006, 35, 1) & Mid(gc0006, 3, 1) & Mid(gc0006, 44, 1) & Mid(gc0006, 11, 1) & Mid(gc0006, 13, 1) & Mid(gc0006, 21, 1) Then
  If  edtPassword = Mid(gc0006, 45, 1) & Mid(gc0006, 48, 1) & Mid(gc0006, 25, 1) & Mid(gc0006, 32, 1) & Mid(gc0006, 15, 1) & Mid(gc0006, 40, 1) & Mid(gc0006, 25, 1) & Mid(gc0006, 14, 1) & Mid(gc0006, 19, 1) Then
    MsgBox "Level 6 can be found at: " & Left$(gc000A, 37) & Mid(gc0006, 21, 1) & Mid(gc0006, 14, 1) & Mid(gc0006, 29, 1) & Mid(gc0006, 32, 1) & Mid(gc0006, 12, 1) & Mid(gc0006, 14, 1) & Mid(gc000A, 44, 6), 0, "Horray!"
    End
  End If
End If
MsgBox "Invalid username and/or password!", 0, "ERROR!"
End Sub

Sub Form_Load ()
Me.Move (Screen.Width - Me.Width) / 2, (Screen.Height - Me.Height) / 2
End Sub
