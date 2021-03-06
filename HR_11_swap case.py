'''
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase 
letters and vice versa.

For Example:
         Www.HackerRankSolution.in → wWW.hACKERrANKsOLUTION.IN
         Pythonist 2 → pYTHONIST 2
Input Format:
         A single line containing a string S.
Constraints:
         0<len(S)<=1000
Output Format:
        Print the modified string S.
'''

def swap_case(s):
    case_change=[]
    for i in range(len(s)):
        if (s[i].isupper())==True:
            case_change.append(s[i].lower())
        elif (s[i].islower()==True):
            case_change.append(s[i].upper())
        else:
            case_change.append(s[i])    
        stri=''
    return stri.join(case_change)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)