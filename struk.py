#  author    : Eko Setiawan
#  github    : github.com/ehkoqtau

key_buka = 'ehkoqtau'
max_wrong = 3
salah = 0
prompt = 'Password : '

while True:
    try:
        import getpass

        key = str(getpass.getpass((prompt)))
    except ValueError:
        continue

    if key == key_buka:
        import os, platform, re

        def clear_screen():
            # clear screen
            if platform.system().upper() == 'WINDOWS':
                os.system('cls')  # For Windows
            elif platform.system().upper() == 'LINUX' or platform.system().upper() == 'OS X':
                os.system('clear')  # For Linux/OS X

        def bon_encrypt():
            prompt = "Masukkan No Bon : "
            while True:
                try:
                    print("-=Aplikasi Encrypt No Bon=-")
                    x = int(input(prompt))
                except ValueError:
                    print("Error! Input harus berupa angka")
                    continue

                if len(str(x)) > 5:
                    print("Error! Input tidak boleh lebih dari 5.")
                    continue
                elif x < 0:
                    print("Error! Inputan tidak boleh lebih kecil dari 0")
                    continue

                else:
                    x = str(x).zfill(4)
                    replace = {'1': 'M', '2': 'K', 'T': 'C', 'S': 'V', 'Y': 'U', 'P': 'A', '7': 'I', '8': 'Z', '9': 'R',
                               '0': 'N'}
                    print("\nNomor Bon : " + "".join([replace.get(c, c) for c in x.upper()]) + "\n")

                    print("1. Lagi")
                    print("0. Kembali")
                    print("------------------")
                    menu = input("Pilih menu> ")
                    clear_screen()

                    if menu == "1":
                        continue
                    elif menu == "0":
                        break
                    else:
                        print("Menu salah!")
                        break

        def show_menu():
            print("=== APLIKASI IT - Create @ehkoqtau with Python ===")
            print("1. Encrypt No Bon")
            print("0. Keluar")
            print("------------------")
            menu = input("Pilih menu> ")

            clear_screen()

            if menu == "1":
                bon_encrypt()
            elif menu == "0":
                exit()
            else:
                print("Menu salah!")

        if __name__ == "__main__":
            clear_screen()
            while (True):
                show_menu()
    else:
        salah += 1
        if salah > 5:
            print('Kamu sudah salah lebih dari 5 kali...')
            input('Tekan Enter untuk keluar')
            break
        else:
            print('Password Salah ', salah, ' kali')
            continue