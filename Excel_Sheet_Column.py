def excel_sheet(s):
    a='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    st='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'
    while s:
        i=(s-1)%26
        s=(s-1)//26
        st=a[i]+st
    return st
n=int(input())
print(excel_sheet(n))