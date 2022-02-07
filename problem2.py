input = open('info_security.txt','r')
input_contents = input.read()
#print(input_contents)
input.close()
print(len(input_contents))
encryptor = {'a':'r',
'b':'s',
'c':'t',
'd':'u',
'e':'v',
'f':'w',
'g':'x',
'h':'y',
'i':'z',
'j':'A',
'k':'B',
'l':'C',
'm':'D',
'n':'E',
'o':'F',
'p':'G',
'q':'H',
'r':'I',
's':'J',
't':'K',
'u':'L',
'v':'M',
'w':'N',
'x':'O',
'y':'P',
'z':'Q',
'A':'R',
'B':'S',
'C':'T',
'D':'U',
'E':'V',
'F':'W',
'G':'X',
'H':'Y',
'I':'Z',
'J':'a',
'K':'b',
'L':'c',
'M':'d',
'N':'e',
'O':'f',
'P':'g',
'Q':'h',
'R':'i',
'S':'j',
'T':'k',
'U':'l',
'V':'m',
'W':'n',
'X':'o',
'Y':'p',
'Z':'q'
}
output = ""
for i in range(len(input_contents)):
    if input_contents[i] in encryptor:
        pass_key = input_contents[i]
        output += encryptor[pass_key]
    else:
        output += input_contents[i]
#print(output)

info_security_encrypted = open('info_security_encrypted.txt', 'w')
info_security_encrypted.write(output)
info_security_encrypted.close()




#Below is just a test to ensure that my key worked and was reversible.
encrypted_text = open('info_security_encrypted.txt', 'r')
encrypted_contents = encrypted_text.read()
print(encrypted_contents)
encrypted_text.close()
test = ""
decryptor = {'r':'a',
's':'b',
't':'c',
'u':'d',
'v':'e',
'w':'f',
'x':'g',
'y':'h',
'z':'i',
'A':'j',
'B':'k',
'C':'l',
'D':'m',
'E':'n',
'F':'o',
'G':'p',
'H':'q',
'I':'r',
'J':'s',
'K':'t',
'L':'u',
'M':'v',
'N':'w',
'O':'x',
'P':'y',
'Q':'z',
'R':'A',
'S':'B',
'T':'C',
'U':'D',
'V':'E',
'W':'F',
'X':'G',
'Y':'H',
'Z':'I',
'a':'J',
'b':'K',
'c':'L',
'd':'M',
'e':'N',
'f':'O',
'g':'P',
'h':'Q',
'i':'R',
'j':'S',
'k':'T',
'l':'U',
'm':'V',
'n':'W',
'o':'X',
'p':'Y',
'q':'Z'}

for i in range(len(encrypted_contents)):
    if encrypted_contents[i] in decryptor:
        pass_key_test = encrypted_contents[i]
        test += decryptor[pass_key_test]
    else:
        test += encrypted_contents[i]
print(test)
