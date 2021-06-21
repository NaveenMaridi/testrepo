def contains(df,word):
    for i in df:
        if(word==i):
            return i
        elif(i.__contains__(word) or word.__contains__(i)):
            x=input(f'Do you mean {i}?if yes press y else n')
            x=x.lower()
            if(x=='y'):
                return i
            else:
                return 'not found'
        else:
            return 'not found'

print(contains())




