'''
Created on Apr 10, 2013

@author: Jimmy
'''
import operator

def get_book_data(books,ratings):
    file = open(books)
    lines = file.readlines()
    
    bookList = []
    for line in lines:
        bookList.append(line)
    file.close()
    
    file = open(ratings)
    lines = file.readlines()
    dictionary = {}
    for i in range(0,len(lines)):
        if "012345".count(lines[i][0]) or "012345".count(lines[i][1]) == 1:
            #User "Don Wang" occurs twice but with same ratings, so no problem. This instantiates a dictionary. 
            dictionary[lines[i-1].strip()] = dictionary.get(lines[i-1],[])
            for rating in lines[i].split():
                dictionary[lines[i-1].strip()].append(int(rating))
    file.close()
    
#   print len(bookList) = 55
#   print len(dictionary.items()) = 86
#   print dictionary.get("Owen") = [3, 5, 0, 0, 0, 0, 5, 0, 0, 3, 0, 5, 3, 5, 3, 3, 0, 3, 5, 5, 0, 0, 0, 3, 0, 5, 0, 0, 0, 0, 3, 5, 3, 0, 0, 0, 0, 3, 3, 0, 3, 0, 5, 5, 0, 0, 3, 0, 0, 5, 5, 0, 0, 0, 0]

    return bookList, dictionary

def get_movie_data(ratings):
    file = open(ratings)
    lines = file.readlines()
    
    movies = set()
    for line in lines:
        movies.add(line.split()[1])
    moviesList = sorted(list(movies))
    #I now have a list of movies sorted alphabetically.
    
    dictionary = {}
    count = 0 
    for movie in moviesList:
        count += 1
        for line in lines:
            #If a user has rated the movie, add his rating to his ratings list.
            dictionary[line.split()[0]] = dictionary.get(line.split()[0],[])
            if line.split()[1]==movie:
                dictionary[line.split()[0]].append(int(line.split()[2]))
        for line in lines:
            #If a user has not rated the movie, add 0 to his ratings list.
            if len(dictionary[line.split()[0]])==count-1:
                dictionary[line.split()[0]].append(0)
    file.close()
    
#   print len(moviesList) = 150
#   print moviesList.index("Thor") = 135
#   print dictionary.get("student1000")[moviesList.index("Thor")] = 1
    return moviesList, dictionary

def average(items, ratings):
    d = {}
    for i in range(0,len(items)):
        averageRating = 0
        for rating in ratings.values():
            averageRating += rating[i]
        d[items[i]] = d.get(items[i],0.0) + float(averageRating)/len(ratings.values())
    return sorted(d.items(),key=operator.itemgetter(1),reverse=True)

def similarities(name, ratings):
    d = {}
    userRatings = ratings.get(name)
    for rating in ratings.items():
        similarity = 0
        for i in range(0,len(userRatings)):
                similarity += rating[1][i]*userRatings[i]
        d[rating[0]] = d.get(rating[0],0) + similarity
    return sorted(d.items(),key=operator.itemgetter(1),reverse=True)

def recommended(items, ratings, similarities, n):
    d = {}
    
    similarityDictionary = {}
    for tup in similarities:
        similarityDictionary[tup[0]] = similarityDictionary.get(tup[0],0) + tup[1]
    
    similarUsers = []
    for similarity in similarities[:n]:
        similarUsers.append(similarity[0])
        
#   print len(similarUsers)
        
    for i in range(0,len(items)):
        score = 0
        for user in similarUsers:
            #BONUS: assuming the user is the first entry in similarities
            if ratings.get(similarities[0][0])[i] == 0:
                score += ratings.get(user)[i]*similarityDictionary.get(user)
                d[items[i]] = d.get(items[i],0) + score
        
    return sorted(d.items(),key=operator.itemgetter(1),reverse=True) 

#print get_book_data("books.txt","bookratings.txt")
#get_movie_data("movieratings.txt")
#print average(["item1","item2"],{"user1":[-1,6],"user2":[4,104]})
#print similarities("Jimmy",{"Jimmy":[2,2,0,3], "Timmy":[2,3,0,4]})
#x,y=get_movie_data("movieratings.txt")
#print recommended(x,y,similarities("student1000",y),3)
#print recommended(["item1","item2","item3","item4"],{"Jimmy":[1,2,3,4], "Timmy":[0,0,0,0],"Dimmy":[-1,-2,-3,-4]},similarities("Jimmy",{"Jimmy":[1,2,3,4], "Timmy":[0,0,0,0],"Dimmy":[-1,-2,-3,-4]}),2)