def isPrime(num):
    if num <= 1:
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

string = input()
let = []
list_cont = []
for i in range(len(string)):
    letra = string[i]
    if(let == []):
        let.append(letra)
        cont = 1
        list_cont.append(cont)
    else:
        j = 0
        encontre = False
        while (j < (len(let))) and (not(encontre)):
            if let[j] == letra:
                list_cont[j] += 1
                encontre = True
            else:
                j += 1
        if(encontre == False):
            let.append(letra)
            cont = 1
            list_cont.append(cont)
print(let)
print(list_cont)
list = []
for i in range(len(let)):
    n = str(list_cont[i])
    print("la letra: ",let[i], " aparece ", n , " veces")
    if isPrime(list_cont[i]):
        list.append(let[i])
print("las letras: ")
print(list)
print("aparecen un numero primo de veces")