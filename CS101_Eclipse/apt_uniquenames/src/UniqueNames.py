'''
Created on Apr 3, 2013

@author: Jimmy
'''
def namesForYear(courses, year):
    list = []

    for course in courses:
        list += course.split(":")[1:]  

    list2 = []
    
    for i in range(0,len(list)):
        if list[i] == year:
            list2.append(list[i-1])
    
    x = sorted(set(list2))
    
    return " ".join(x).strip()
    
#    return " ".join(sorted(list3).strip()
print namesForYear(['cps6:James:firstyear:Merlin:sophomore:Blake:senior:Yin:senior:Gauf:junior', 'math31:Smith:firstyear:Maxwell:sophomore:Blake:senior:Yin:senior:Gauf:junior', 'french2:Yin:firstyear:Gauf:sophomore:Knuth:senior:Lee:firstyear', 'german1:Gauf:sophomore:Wesley:senior:Lee:firstyear:James:firstyear:Merlin:sophomore'],"senior" )
