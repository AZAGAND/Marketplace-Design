class kasir:
    
    def_init_(self): # type: ignore
        Self.keranjang = {} # type: ignore
    
    def tambah_item(self, nama, harga, jumlah):
        if nama in self.keranjang:
            self.keranjang[nama]['jumlah'] += jumlah
        else:
            self.keranjang[nama] = {'harga': harga, 'jumlah': jumlah}
            print(f"{jumlah} {nama} ditambahkan ke keranjang...")

            def tampilkan_keranjang(self):
                print("\n===>Keranjang Belanja")
        if not self.keranjang:
            print("keranjang masih kosong")
            return
        total=0
        for nama, info in self.keranjang.items():
            subtotal = info['harga'] * info['jumlah']
            total += subtotal
            print(f"{nama} - {info['jumlah']} x Rp.{info['harga']:,} = Rp.{subtotal:,}")
        print(f"Total belanja: Rp.{total:,}\n")
        return total
    
    def proses_bayar(self):
        total = self.tampilkan_keranjang()
        if not self.keranjang:
            return
            while True:
                try:
                    uang_bayar = int(input("masukkan jumlah uang: Rp."))
                    if uang_bayar >= total:
                        kembalian = uang_bayar - total
                        print(f"pembayaran berhasil, Kembalian: Rp.{kembalian,}\n")
                        self.keranjang.clear()
                        break
                    else:
                        print("uang tidak cukup, harap coba lagi...")
                except ValueError:
                    print("harap masukkan value yang valid")
kasir = kasir()
