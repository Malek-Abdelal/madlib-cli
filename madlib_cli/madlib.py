import re

print('''
    ******************************

      Welcom to the Madlib game !

    ******************************
      ''')



def read_template(path):
    with open(path, 'r') as f :
        res= f.read()
    return res
        
firstTxt = read_template("assets/dark_and_stormy_night_template.txt")   
 
def parse_template(firstTxt):
    regex = r'\{(.*?)\}'
    stripped = re.sub(regex,'{}',firstTxt)
    partsList = re.findall(regex,firstTxt)
    parts = tuple(partsList)
    return stripped, parts
 
stripped = [parse_template(firstTxt)][0][0]
parts = [parse_template(firstTxt)][0][1]

def merge(stripped,parts):    
    txt = stripped.format(*parts)
    return txt

def userInputs(parts):   
        counter=len(parts) 
        arr=[]
        p=0
        while p <counter:    
            i = input(f'Inter {parts[p]} > ')
            arr.append(i)
            p=p+1    
        return  tuple(arr)


if __name__ == '__main__':

    read_template('assets/make-me-a-game.txt')
    firstTxt = read_template('assets/make-me-a-game.txt') 
    parse_template(firstTxt)
    stripped = [parse_template(firstTxt)][0][0]
    parts = [parse_template(firstTxt)][0][1]
       
    userinputs = userInputs(parts)
        
    print(merge(stripped,userinputs))