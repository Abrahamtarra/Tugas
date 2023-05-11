if __name__ == '__main__':
    x = int(input('masukan jumlah hari:'))
    
    tahun = x / 360
    bulan = x / 30
    minggu= x / 7
    print(f'hasil dari {x} hari jika dijadikan tahun adalah : {tahun}')
    print(f'hasil dari {x} hari jika dijadikan bulan adalah : {bulan}')
    print(f'hasil dari {x} hari jika dijadikan minggu adalah : {minggu}')
    