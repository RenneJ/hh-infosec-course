def simple_xor(a, b):
    c = a ^ b
    return c

def char_frequency(s: str):
    char_freq = {}
    for char in s:
        if char.isalpha():
            char_freq.setdefault(char, 0)
            char_freq[char] += 1
    return char_freq

def decrypt_text(s: str, freq_mapping: dict):
    vals = list(freq_mapping.values())
    vals.sort()
    vals.reverse()
    print(vals)
    p = ""
    for char in s:
        if char == "D":
            char = "H"
        elif char == "H":
            char = "T"
        elif char == "P":
            char = "P"
        elif char == "O":
            char = "C"
        elif char == "W":
            char = "O"
        elif char == "G":
            char = "M"
        elif char == "I":
            char = "E"
        elif char == "M":
            char = "A"
        """ elif char == "B":
            char = "S"
        elif char == "T":
            char = "I"
        elif char == "K":
            char = "Y"
        elif char == "Y":
            char = "R"
        elif char =="V":
            char = "R"
        elif char == "L":
            char = "K"
        elif char == "C":
            char = "V"
        elif char == "A":
            char = "N"
        elif char == "J":
            char = "L"
        elif char == "S":
            char = "F"
        elif char == "Q":
            char = "D"
        elif char == "N":
            char = "B"
        elif char == "E":
            char = "Q"
        elif char == "R":
            char = "W" """
        p += char  
    return p


#print(simple_xor(15, 16))
#print(simple_xor(True, True))
c = "HDMH'B TH. KWU'YI AWR WSSTOTMJJK M OWQINYIMLIY! MB KWU BII, BTGPJI BUNBHTHUHTWA OTPDIYB OMA NI NYWLIA RTHD SYIEUIAOK MAMJKBTB. BII KWU MH DHHP://HIYWLMYCTAIA.OWG"
freqs = char_frequency(c)
print(freqs)
p = decrypt_text(c, freqs)
print(p)