import story_start;
choose = input("Selamat datang di cerita fantasi, Ingin bermain ? \n")

# ternary di python harus mengassign sebuah value ke variabel 
# di python tidak ada variabel yang bertipe bool 

isPlaying = 1 if choose == 'y' or choose == 'Y' else 0


if(isPlaying):
    story_start.mulai_cerita()
else: 
    print("oke, selamat tinggal")








