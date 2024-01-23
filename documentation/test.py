#this is for another class but figured I'd use it here as a placeholder

def affine_caesar_cipher(a, b, plaintext):
    #apply the affine Caesar cipher formula
    c = (a * plaintext + b) % 26

    return c

#loop through all possible combinations of a, b, and plaintext
for a in range(1, 26):
    for b in range(26):
        conversions = set()
        duplicates_found = False

        for plaintext in range(26):
            result = affine_caesar_cipher(a, b, plaintext)
            if result in conversions:
                duplicates_found = True
                break
            conversions.add(result)

        if duplicates_found:
            print("Duplicates found for a =", a, "and b =", b, "    == ", result)
