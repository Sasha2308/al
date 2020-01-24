def read(f):
    for line in f:
        line_split = line.split('*')
        for i in line_split:
            print(i)
        ID = int(line_split[0])
    return ID
    
f = open('file.txt', 'r')
read = read(f)+1
read = str(read)
f.close()

inp = input("Хотите добавить элемент? (y,n) ")

if inp == 'y':
    f = open('file.txt', 'a')
    wr = []
    #wr.append('\n')
    #wr.append(read)
    wr.append(input('назваание книги: '))
    wr.append(input('автор: '))
    wr.append(input('жанр: '))
    wr.append(input('год издания: '))
    wr.append(input('издатель: '))
    wr.append(input('Цена: '))
    
    wr2 = '\n' + read + '*' + '*'.join(wr)
    print(wr2)
    f.write(wr2)
 
f.close()



