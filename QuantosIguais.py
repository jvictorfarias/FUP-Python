entrada = [input(), input(), input()]
contador = 0
if(entrada[0] == entrada[1] or entrada[0] == entrada[2]):
    contador += 1
if(entrada[1] == entrada[0] or entrada[1] == entrada[2]):
    contador += 1
if(entrada[2] == entrada[1] or entrada[2] == entrada[0]):
    contador += 1
    
print(contador)