def reading(string, versions):
    while len(string) >= 11:
        cur_version, type_id, string = int(string[:3], 2), int(string[3:6], 2), string[6:]
        versions += cur_version
        # print(versions, cur_version, string)
        if type_id == 4:
            islast = False
            while not islast:
                islast = string[0] == '0'
                string = string[5:]
        else:
            length_type_id, string = int(string[0]), string[1:]
            if length_type_id == 0:
                total_length, string = int(string[:15], 2), string[15:]
            else:
                n_packets, string = int(string[:11], 2), string[11:]
    return string, versions


# with open('test16.txt', 'r') as f:
with open('input16.txt', 'r') as f:
    inpt = f.read().strip()
print(inpt)

hex_bin = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'
    }

bint = [hex_bin[char] for char in inpt]
bint = ''.join(bint)
print(bint)

r, sum_versions = reading(bint, 0)
print(f'Version: {sum_versions}')
