def alternate_gcd(x, y):
    if x == 0:
        return (y, 0, 1)
    else:
        result, a, b = alternate_gcd(y % x, x)
        return (result, b - (y // x) * a, a)
def calculate_modular_inverse(num, modulo):
    gcd, x, _ = alternate_gcd(num, modulo)
    if gcd == 1:
        return (x % modulo + modulo) % modulo
    else:
        return -1  
def create_alternate_identity_matrix(matrix_size):
    identity_matrix = [[0] * matrix_size for _ in range(matrix_size)]
    for i in range(matrix_size):
        identity_matrix[i][i] = 1  
    return identity_matrix
def perform_alternate_gauss_jordan_elimination(data_matrix, inverse_matrix, modulus, matrix_size):
    for col in range(matrix_size):
        col_value = calculate_modular_inverse(data_matrix[col][col], modulus)
        for j in range(matrix_size):
            data_matrix[col][j] = (data_matrix[col][j] * col_value % modulus + modulus) % modulus
            inverse_matrix[col][j] = (inverse_matrix[col][j] * col_value % modulus + modulus) % modulus
        for row in range(matrix_size):
            if row != col:
                factor = data_matrix[row][col]
                for i in range(matrix_size):
                    data_matrix[row][i] = (data_matrix[row][i] - factor * data_matrix[col][i] % modulus + modulus) % modulus
                    inverse_matrix[row][i] = (inverse_matrix[row][i] - factor * inverse_matrix[col][i] % modulus + modulus) % modulus
    return inverse_matrix
def decode_data_with_alternate_approach(data_matrix, inverse_matrix, matrix_size, message_size, modulus):
    decoded_parts = []
    for i in range(matrix_size):
        decoded_part = []
        for j in range(message_size):
            decoded_char = 0
            for k in range(matrix_size):
                decoded_char = (decoded_char + inverse_matrix[i][k] * data_matrix[k][matrix_size + j] % modulus + modulus) % modulus
            decoded_part.append(decoded_char)
        decoded_parts.append(decoded_part)
    return decoded_parts
def convert_to_text_with_alternate_approach(decoded_parts):
    decoded_data = ''
    for part in decoded_parts:
        for cr in part:
            decoded_data += chr(cr)
    return decoded_data
def decrypt_data_with_alternate_approach(matrix_size, message_size, data_matrix, modulus):
    inverse_matrix = create_alternate_identity_matrix(matrix_size)
    inverse_matrix = perform_alternate_gauss_jordan_elimination(data_matrix, inverse_matrix, modulus, matrix_size)
    decoded_parts = decode_data_with_alternate_approach(data_matrix, inverse_matrix, matrix_size, message_size, modulus)
    return convert_to_text_with_alternate_approach(decoded_parts)
def main():
    matrix_size = int(input())
    message_size = int(input())
    data_matrix = []
    for i in range(matrix_size):
        line = input().strip()
        row = [ord(c) for c in line]
        data_matrix.append(row)
    modulus = 127
    decrypted_data = decrypt_data_with_alternate_approach(matrix_size, message_size, data_matrix, modulus)
    print(decrypted_data)
if __name__ == "__main__":
    main()
