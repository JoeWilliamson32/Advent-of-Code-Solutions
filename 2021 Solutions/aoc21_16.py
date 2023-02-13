data = open('input.txt').read().strip()

# Test Cases 
# data = 'D2FE28'
# data = '38006F45291200'
# data = 'EE00D40C823060'
# data = '8A004A801A8002F478'
# data = '620080001611562C8802118E34'
# data = 'C0015000016115A2E0802F182340'
# data = 'A0016C880162017C3686B18A3D4780'
# data = '04005AC33890'

hex_conv = {
            '0' :'0000',
            '1' : '0001',
            '2' : '0010',
            '3' : '0011',
            '4' : '0100',
            '5' : '0101',
            '6' : '0110',
            '7' : '0111',
            '8' : '1000',
            '9' : '1001',
            'A' : '1010',
            'B' : '1011',
            'C' : '1100',
            'D' : '1101',
            'E' : '1110',
            'F' : '1111'
}

def hex_to_binary(string):
    string = str(string)
    output = ''
    for char in string:
        hex = hex_conv[char]
        output += str(hex)

    return output

# Part 1 
binary = hex_to_binary(data)
binary = list(binary)

def decode(binary):    
    version = int(''.join(binary[:3]), 2)
    binary[:] = binary[3:]
    id = int(''.join(binary[:3]), 2)
    binary[:] = binary[3:]

    if id == 4:
        num = ''
        while True:
            leading_bit = binary.pop(0)
            num += ''.join(binary[:4])
            binary[:] = binary[4:]

            if leading_bit == '0':
                break

        num = int(num, 2)
        return (version, id, num)

    
    else:
        stack = []
        len_id = binary.pop(0)

        if len_id == '0':
            subpack = ''.join(binary[:15])
            subpack_len = int(subpack,2)
            binary[:] = binary[15:]
            temp = binary[:subpack_len]
            binary[:] = binary[subpack_len:]

            while temp:
                stack.append(decode(temp))
    

        else:
            subpack = ''.join(binary[:11])
            subpack_num = int(subpack, 2)
            binary[:] = binary[11:]
            for _ in range(subpack_num):
                stack.append(decode(binary))
            
        return (version, id, stack)


def version_sum(output):
    version, id, stack = output
    if id == 4:
        return version
    else:
        return version + sum(map(version_sum, stack))


part1 = version_sum(decode(binary))


# Part 2 
binary = hex_to_binary(data)
binary = list(binary)

def version_sum2(output):
    version, id, stack = output

    if id == 0:
        return sum(map(version_sum2, stack))

    if id == 1:
        product = 1
        for elem in stack:
            product *= version_sum2(elem)
        return product

    if id == 2:
        return min(map(version_sum2, stack))

    if id == 3:
        return max(map(version_sum2, stack))

    if id == 4:
        return stack

    if id == 5:
        return version_sum2(stack[0]) > version_sum2(stack[1])
    
    if id == 6:
        return version_sum2(stack[0]) < version_sum2(stack[1])

    if id == 7:
        return version_sum2(stack[0]) == version_sum2(stack[1])


part2 = version_sum2(decode(binary))


print(part1)
print(part2)