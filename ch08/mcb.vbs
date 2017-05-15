cmd = "cmd /c pythonw.exe mcb.pyw"

Set args = WScript.Arguments
For i = 0 to args.Count - 1
  cmd = cmd & " " & args(i)
Next

Set s = CreateObject("Wscript.Shell")
s.CurrentDirectory = "C:\mcb"
s.Run cmd, 0, false
