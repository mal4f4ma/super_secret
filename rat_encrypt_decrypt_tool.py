import numpy as np
from FlagHostPort import key, secret
import sys

def encryptFlagHostPort():
    data_encoded = []

    for i in range(10):
        x = 0
        for j in range(i * 8, (i * 8) + 8):
            al = np.uint8(ord(secret[j]))
            bl = np.uint8(ord(key[x]))
            res_xor = np.uint8(bl ^ al)
            res_sub = np.uint8(res_xor - x)
            data_encoded.append(hex(res_sub))
            x += 1
            pass
        pass
    print(data_encoded)
    return ''.join(data_encoded)
    
def decryptFlagHostPort():
    #Recordatorio IMPORTANTE:
    #   Debo hacer la funcion para decryptar y poder
    #   obtener el host y port para que el RAT se conecte
    #   al panel de control, despues de codificar el resultado
    #   se escribe en ZGVjcnlwdGVkRmxhZ0hvc3RBbmRQb3J0   
    pass

if __name__ == "__main__":
    if len(sys.argv) == 2:
        decryptFlagHostPort(sys.argv[1])
    else:
        print("Nop =(")
