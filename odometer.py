def palindromic():
    for i in range(1000000):
        str_i = str(i).zfill(6)
        if str_i[2:] == str_i[5:1:-1]:
            i += 1
            str_i = str(i).zfill(6)
            if str_i[1:] == str_i[5:0:-1]:
                i += 1
                str_i = str(i).zfill(6)
                if str_i[1:5] == str_i[5:1:-1]:
                    i += 1
                    str_i = str(i).zfill(6)
                    if str_i[:] == str_i[::-1]:
                        print(i)
                        
if __name__ == "__main__":
    palindromic()