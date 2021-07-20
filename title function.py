txt="welcome to navgurukul"
i=0
while i<len(txt):
    if i==0:
        text=""+txt[i].upper()
    else:
        if txt[i]==" ":
            i=i+1
            text=text+" "+txt[i].upper()
        else:
            text=text+txt[i]
    i=i+1
print(text)