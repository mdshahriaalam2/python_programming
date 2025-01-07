# Find double spaces

srt = "This is a string with double  string"
doubSp = srt.find("  ")

if doubSp != -1:
    srt = srt.replace("  ", " ")
    print(srt)
else: 
    print("Not Found")