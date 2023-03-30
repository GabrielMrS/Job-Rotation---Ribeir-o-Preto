# Definindo a String
string = '!tegraT an rahlabart rezarp mu res iaV ,leirbaG é emon ueM !álO'

# Laço para inverter a string
string_invertida = ''
for i in range(len(string)-1, -1, -1):
    string_invertida += string[i]

# Imprimindo a string invertida
print(string_invertida)
