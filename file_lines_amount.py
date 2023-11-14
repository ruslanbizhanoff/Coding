def file_lines_amount(filename: str) -> int:
    import re
    '''
    Calculates the number of non-empty lines in a file.
    '''
    with open(filename, 'r') as f:
        return len(re.findall(r".+\n*", f.read()))


if __name__ == "__main__":
    import os
    # Update the directory with the script.
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)
    print(file_lines_amount('translate.txt'))