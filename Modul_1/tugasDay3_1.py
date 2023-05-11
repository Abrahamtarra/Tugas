text = "The Fox and fox"
print(text)

oldText = input('Masukan kata yang ingin dirubah: ')
newText = input('Masukan kata pengganti: ')

ganti = text.replace(oldText,newText)
print(ganti)

# ganti = text.replace("fox", "dog")  #cara yang lebih mudah dan singkat tanpa perlu memasukan kata
# print(ganti)