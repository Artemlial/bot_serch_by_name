dict_ascii= {'a': f'[{bytes([224,225,226,227,228,229,230]).decode("windows-1252")}a]',
             'c': f'[{bytes([231]).decode("windows-1252")}c]',
             'd': f'[{bytes([185,240]).decode("iso-8859-10")}d]',
             'e': f'[{bytes([232,233,234,235]).decode("windows-1252")}e]',
             'g': f'[{bytes([179]).decode("iso-8859-10")}g]',  
             'i': f'[{bytes([236,237,238,239]).decode("windows-1252")}i]', 
             'k': f'[{bytes([182]).decode("iso-8859-10")}k]', 
             'n': f'[{bytes([241]).decode("windows-1252")}n]', 
             'o': f'[{bytes([242,243,244,245,246,248]).decode("windows-1252")}o]', 
             's': f'[{bytes([186]).decode("iso-8859-10")}s]', 
             't': f'[{bytes([187]).decode("windows-1252")}t]', 
             'u': f'[{bytes([249,250,251,252]).decode("windows-1252")}u]', 
             'y': f'[{bytes([253,255]).decode("windows-1252")}y]', 
             'z': f'[{bytes([188]).decode("iso-8859-10")}z]', 
             'A': f'[{bytes([192,193,194,195,196,197,198]).decode("windows-1252")}A]', 
             'C': f'[{bytes([199]).decode("windows-1252")}C]', 
             'D': f'[{bytes([208,169]).decode("iso-8859-10")}D]', 
             'E': f'[{bytes([200,201,202,203]).decode("windows-1252")}E]',  
             'G': f'[{bytes([163]).decode("iso-8859-10")}G]',
             'I': f'[{bytes([204,205,206,207]).decode("windows-1252")}I]',
             'K': f'[{bytes([166]).decode("iso-8859-10")}K]', 
             'N': f'[{bytes([209]).decode("windows-1252")}N]', 
             'O': f'[{bytes([210,211,212,213,214,216]).decode("windows-1252")}O]', 
             'S': f'[{bytes([170]).decode("iso-8859-10")}S]', 
             'T': f'[{bytes([171]).decode("iso-8859-10")}T]', 
             'U': f'[{bytes([217,218,219,220]).decode("windows-1252")}U]',
             'Y': f'[{bytes([221]).decode("windows-1252")}Y]', 
             'Z': f'[{bytes([172]).decode("iso-8859-10")}Z]'}
def main():
    print(dict_ascii)
if __name__ == "__main__":
    main()