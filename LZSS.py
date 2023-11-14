def LZSS(text):
    buffer = [i for i in text[:5]]
    _dict = ['' for i in range(8)]
    pos = 0
    code = []
    while pos < len(text):
        buffer = [i for i in text[pos:pos+5]]
        code.append((0, text[pos]))
        pos += 1
        _dict
        print(buffer)
    return buffer, code
def main():
    text = input()
    print((LZSS(text)))

if __name__ == "__main__":
    main()