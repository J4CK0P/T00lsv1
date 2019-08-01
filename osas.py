import os, sys

print ("\033[1;32mSilahkan Masukkan Username & Password Anda")

Nick = 'J4CKOP'

Password = 'ikehikeh'


def restart():

        ngulang = sys.executable

        os.execl(ngulang, ngulang, *sys.argv)



def main():

        uname = raw_input("Nick: ")

        if uname == Nick :

                pwd = raw_input('Password: ')



                if pwd == Password :
                        print "\033[1;32mAlhmdllh sudah masuk juga..",

                        sys.exit()




                else:

                        print "\033[1;32mMaaf Masukkan Password  Anda salah... [?]\033[00m"
                        print "Silahkan segera log-in kembali...!!\n"

                        restart()



        else:

                print "\033[1;32mMaaf Masukkan Nick Anda salah... [?]\033[00m"

                print "Silahkan segera log-in kembali...!!\n"

                restart()



try:

        main()

except KeyboardInterrupt:

        os.system('sh login.sh')


clear
