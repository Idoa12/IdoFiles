def section_count(ba, num, b):
    # checks number of sections needed to be made and if there is none, it creates the file
    if num == b:
        # create files
        with open('file.txt', 'wb') as bf:
            bf.write(ba)
            bf.close()
    else:
        section(ba[:], num, b)


def section(ba, num, b):
    # goes over all possible tags for specific section
    for tag in range(0, 256):
        ba += bytes([tag])
        section_length(ba[:], num, b)


def section_length(ba, num, b):
    # goes over all lengths possible for the section
    for length in range(0, 256):
        ba += bytes([length])
        if length == 0:
            section_count(ba[:], num, b + 1)
        else:
            section_value_recursive(ba[:], length, 0, num, b)
        ba.pop()


def section_value_recursive(ba, length, a, num, b):
    # creates sections with all possible combinations with the given length
    if length == a:
        section_count(ba[:], num, b + 1)
    else:
        for v in range(0, 256):
            section_value_recursive(ba[:] + bytes([v]), length, a + 1, num, b)


def main():
    # creates the header with 'magic'
    magic = 'fee1900d'
    magic = bytearray.fromhex(magic)
    magic = magic[::-1]

    for i in range(0, 256):
        # main loop that goes by the number of sections
        magic_temp = magic[:]
        magic_temp += bytes([i])
        section_count(magic_temp[:], i, 0)


if __name__ == '__main__':
    main()
