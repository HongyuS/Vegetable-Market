def strToList(s):
    l = list()
    for i in range(len(s)):
        l.append(s[i])
    return l

def isAnagram(s1, s2):
    l1 = strToList(s1)
    l2 = strToList(s2)
    l1.sort()
    l2.sort()
    if l1 == l2:
        return True
    else:
        return False

def main():
    s1 = input('The 1st word >')
    s2 = input('The 2nd word >')
    if isAnagram(s1, s2):
        print('----------\nThey are anagrams!\n----------')
    else:
        print('----------\nThey are not anagrams!\n----------')

if __name__ == "__main__":
    print('Enter two words to see if they are anagrams ...')
    main()
