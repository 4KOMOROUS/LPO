# verifica se in una stringa sono presenti 2 caratteri uguali

def find_double(s):
    l = len(s)
    i = 0
    j = 1
    while i < l:
        while j < l:
            if s[i] == s[j]:
                return True
            j += 1
        i += 1
        j = i + 1    
    return False

string = input("type a string: ")
r = find_double(string)
if(r):
    print("double!")
else:
    print("nothing...")