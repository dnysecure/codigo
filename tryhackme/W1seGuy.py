cifrado_hex = "código_hex_del_cifrado_aquí"
cifrado_bytes = bytes.fromhex(cifrado_hex)

# Texto que se supone debe salir (por ejemplo los primeros caracteres cleartext conocidos)
texto_conocido = b"THM{"

for llave_int in range(256):
    llave_byte = llave_int.to_bytes(1, byteorder='big')
    
    # XOR del cifrado con la llave repetida para el largo del texto conocido
    resultado = bytes([b ^ llave_int for b in cifrado_bytes[:len(texto_conocido)]])
    
    if resultado == texto_conocido:
        print(f"¡Llave encontrada! Valor hex: {llave_hex}")
        # Con esta llave puedes descifrar todo el mensaje
        mensaje_descifrado = bytes([b ^ llave_int for b in cifrado_bytes])
        print("Mensaje completo descifrado:", mensaje_descifrado.decode())
        break
