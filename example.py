
with open('new_file.txt','w') as f:
    for i in range(101):
        f.write(str(i) + '\n')

f.close()