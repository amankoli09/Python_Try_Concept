try:
    f=open("amankifile.txt","w")
    try:
        f.write("heyy Buddy! We provide you best services.")
    except:
        print("Something went wrong while writing to the file.")
    finally:
     f.close()
except:
    print("Something went wrong while opening the file.")