if __name__ == '__main__':
    apel = int(input('masukan jumlah apel:'))
    jeruk = int(input('masukan jumlah jeruk:'))
    anggur = int(input('masukan jumlah anggur:'))
    hargaApel = apel * 10000
    hargaJeruk = jeruk * 15000
    hargaAnggur = anggur * 20000
    total = hargaApel + hargaAnggur + hargaJeruk
    print(f'Total harga = {total}')