import itertools
import string
from tqdm import tqdm

cifrado_hex = "0401242b456128053e4115311d1141247d0a3b5611271b63543c05103860223d1060402231262248"
cifrado_bytes = bytes.fromhex(cifrado_hex)

chars = string.ascii_letters + string.digits  # a-zA-Z0-9

def xor_decrypt(ciphertext, key):
    key_len = len(key)
    return bytes([ciphertext[i] ^ ord(key[i % key_len]) for i in range(len(ciphertext))])

def es_texto_valido(texto):
    if texto.startswith(b'THM{') and all(32 <= c < 127 for c in texto):
        return True
    return False

# Envolver itertools.product con tqdm para mostrar progreso
for posible_key in tqdm(itertools.product(chars, repeat=5), total=len(chars)**5):
    key_str = ''.join(posible_key)
    descifrado = xor_decrypt(cifrado_bytes, key_str)
    if es_texto_valido(descifrado):
        print(f'Llave encontrada: {key_str}')
        print(f'Mensaje descifrado: {descifrado.decode()}')
        break
