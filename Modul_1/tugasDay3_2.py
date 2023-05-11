fibonacci = int(input("masukan jumlah :"))

bilangan1 = 0
bilangan2 = 1
count = 0

if fibonacci <=0:
    print("Harus lebih dari 0")
elif fibonacci ==1:
    print("Penjumlahan hanya sampai", fibonacci,":")
    print(bilangan1)
else:
    print("Fibonacci:")
    while count < fibonacci:
        print(bilangan1)
        jumbil = bilangan1 + bilangan2
        bilangan1 = bilangan2
        bilangan2 = jumbil
        count += 1