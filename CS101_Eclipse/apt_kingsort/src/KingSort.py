'''
Created on Apr 3, 2013

@author: Jimmy
'''
import operator

def getSortedList(kings):
    
    numerals = {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
    numerals2 = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500, 'M':1000}
    
    dictionary = {}
    
    for king in kings:
        
        result = 0
        
        #number is the roman numeral part
        
        number = king.split()[1]
        
        #find IV or IX before we count I or V, otherwise IV would be counted as 6
        
        for key in numerals.keys():
            if number.count(key) > 0:
                result += numerals[key]*number.count(key)
                number = number.replace(key,'')
        
        #now we count I and V and so on.
        
        for key in numerals2.keys():
            if number.count(key) > 0:
                result += numerals2[key]*number.count(key)
                number = number.replace(key,"")
                
        #assign each king to it's number
        
        dictionary[king] = dictionary.get(king,0) + result
    
    x = sorted(dictionary.items(),key=operator.itemgetter(1)) #kingSort
    y = sorted(x,key=lambda(name,num):(name.rsplit(None,1)[0],num)) #nameSort
    
    print dictionary
    
    list = []
    for thing in y:
        list.append(thing[0])
            
    return list

print getSortedList(['Anne XIV', 'Anne XLIX', 'Anne XXXIII', 'Ilya VIII', 'Ilya X', 'Ilya XI', 'Ilya XLVIII', 'Ilya XXV', 'Ilya XXVI', 'Ilya XXVIII', 'Ilya XXX', 'Janq XI', 'Janq XLIII', 'Janq XVI', 'Janq XXV', 'Janq XXVIII', 'Mary II', 'Mary IX', 'Mary VI', 'Mary X', 'Mary XV', 'Mary XXIII', 'Mary XXIV', 'Philip III', 'Philip VI', 'Philip XIX', 'Philip XV', 'Philip XX', 'Philip XXXV', 'Robert III', 'Robert VIII', 'Robert X', 'Robert XLIII', 'Robert XV', 'Robert XVII', 'Robert XXVIII', 'Robert XXXI', 'Robert XXXII', 'Robert XXXIII', 'Usamec IV', 'Usamec VII', 'Usamec XL', 'Usamec XLII', 'Usamec XLIX', 'Usamec XXIII', 'Usamec XXXIV', 'Zemco III', 'Zemco X', 'Zemco XXVII', 'Zemco XXXI'])