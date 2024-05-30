# Function to convert decimal to binary
def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]
    return binary.zfill(8)

# Initialize the header for the table
header = ["Decimal", "Hex", "Binary", "UTF-8"]

# Print header
print("|".join(header))

# Print separator
print("-" * (len("|".join(header)) + 4))

# Populate the table with ASCII characters
for i in range(128):
    decimal = str(i)
    hex_value = hex(i)[2:].upper().zfill(2)
    binary = decimal_to_binary(i)
    utf8 = chr(i)
    row = [decimal, hex_value, binary, utf8]
    print("|".join(row))