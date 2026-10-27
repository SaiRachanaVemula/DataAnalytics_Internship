#9.Mutations
#https://www.hackerrank.com/challenges/python-mutations/problem

def mutate_string(string, position, character):
    string=list(string) 
    string[position]=character 
    result="" 
    for k in string: 
        result+=k 
    return result

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
