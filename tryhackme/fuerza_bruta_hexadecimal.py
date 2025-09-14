import itertools
import string

# Texto cifrado recibido (como ejemplo)
cifrado_hex = "2d2d090e184804281b1c3c1d30341c0d51271e0b380b36460915293d1d3d0b113d451d0b1d0b0715"
cifrado_bytes = bytes.fromhex(cifrado_hex)

# Caracteres permitidos en la clave
chars = string.ascii_letters + string.digits  # a-zA-Z0-9

def xor_decrypt(ciphertext, key):
    key_len = len(key)
    return bytes([ciphertext[i] ^ ord(key[i % key_len]) for i in range(len(ciphertext))])

def es_texto_valido(texto):
    # Función heurística para validar si el texto descifrado parece correcto, 
    # por ejemplo: contiene caracteres imprimibles y comienza con 'THM{'
    if texto.startswith(b'THM{') and all(32 <= c < 127 for c in texto):
        return True
    return False

# Fuerza bruta recorriendo todas las combinaciones posibles
for posible_key in itertools.product(chars, repeat=5):
    key_str = ''.join(posible_key)
    descifrado = xor_decrypt(cifrado_bytes, key_str)
    if es_texto_valido(descifrado):
        print(f'Llave encontrada: {key_str}')
        print(f'Mensaje descifrado: {descifrado.decode()}')
        break
