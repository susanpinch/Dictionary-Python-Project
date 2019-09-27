"""
Written by: Susan Pinchiaroli
Professor Gochfeld
Assignment 10

"""
import time#import time function
name = 'movie_reviews.txt'#create variable to hold file name
l=0#this is number of unique numbers
words_dictionary = {}#create a dictionary that's empty
number=0#create accumulator variable to increase by one. this will tell us how many lines wereanalyzed
fileobject= open(name,'r')#open the file to 'read'
data = fileobject.read()#store the fileobject in a variable so we cal split it at some point
fileobject.close()#close the file
lines = data.split('\n')#split the read file by line breaks. this will split a string and make it into a list. so lines holds a list of lines. so each items is an entire line
time_before = time.time()#start time before
for line in lines:#create for loop to iterate through the lines variable, which holds each line of the movie reviews as an item
    if len(line)==0:#if the length of the line is zero, meaning that if theres an empty line, just skip it. so use continue statement. 
        continue
    words=line.split()#then split the target variable line by (), which divides items by spaces. this works so that we can iterate through each word now
    number+=1#accumulate number, this tells us how many lines we're iterating through. increase by one after each iteration of the outer loop
    num = words[0]#then assign a variable name num to words[0]. this is going to represent the review value. we can assign it in outer loop because the outer loop represents iterating through each line
    #and each line has a number at the beginning of it. 
    for word in words:#now iterate through each word in the words list, as each item is now a word. 
        if len(word)==0:#again, if the length of the word is zero, continue. 
            continue
        word=word.lower()#translate all words into lower case by using the string method .lower()
        if word not in words_dictionary:#use if/else statement to see if the word is in the dictionary already. this way we know if we need to use 1 as the number of times we've seen it or if we need to accumulate
            count=1#if the word is not in dictionary, a variable called count will equal 1, because we've only seen this word once. and count represents the number of times we've seen a word. 
            value = [count,num]#then create a variable called value and equal it to a list of count, num. again, count is number of times we've seen the word. num is the review score. 
            words_dictionary[word]=[value]#then equal the dictionary at the key word to the value [value] 
        else:
            words_dictionary[word][0][0]+=1#if the word is in the dictionary, then we have to increase the first value, count, by one. because we've now seen this word another time. so we increase by 1
            c=words_dictionary[word][0][1]#then create a variable called c and assign it to the second value in the list, which is the current review of the word.
            value = int(c)+int(num)#then, translate c and num into integers and add them together. this is the total value that this word has from reviews. we are making it a total so that we
            #cancompute the average later in the program. 
            words_dictionary[word][0][1]=value#then equate the second value in the list, num, to the variable value, which holds the total of all reviews. 
           #need to add one to the count that's held in the zero place of list
            
            

time_after = time.time()#end time. 
time= time_after-time_before#calculate the time it took 
l = len(words_dictionary)#l equals the length of the dictionary which tells us how many unique words have been analyzed. 
print("Initializing sentiment database.")#print out all this information
print("Sentiment database initialization complete.")
print("Read",number,"lines.")#print how many lines we've read
print("Total unique words analyzed:",l)#print number of unique words analyzed
print("Analysis took",format(time,'.3f'),"seconds to complete")
print()
while True:#now create a while loop that continues to prompt the user to enter a phrase
    total=0#create variables inside the while loop so that each time the loop repeats, we start over fresh.
    #total is going to hold the averages of each word in phrase so we can compute if the phrase is positive or negative
    iterate=0#iterate is going to hold amount of times we we find a word in dictionary
    phrase = input("Enter a phrase to test: ")#ask user to input a phrase
    if phrase.lower() == 'quit':#test if the phrase is anything other than 'quit', if it isn't, then we know the user wants to quit the program, so we break. 
        print('Quitting.')
        break
    phrase=phrase.lower()#make the entire phrase lower case

    list_of_phrase = phrase.split()    #then split the phrase by spaces so we can analyze each word    
    for word in list_of_phrase:#iterate through the list that holds each word as an item
        if not word.isalnum():#test if there is punctuation in the word
            for punctuation in word:#then iterate through the string
                if not punctuation.isalnum():#if the character in the string is not a number or a letter, then replace it with an empty string. 
                    word = word.replace(punctuation,'')
                    
        if word in words_dictionary:#if the word is in the dictionary, we are going to compute the average.
            average = int(words_dictionary[word][0][1])/int(words_dictionary[word][0][0])#compute the average by dividing the total review amount by the number of unique words. 
            print("* '",word,"'"" appears ",words_dictionary[word][0][0]," times with an average ",average,sep='' )#then print out this average
            total+=average#then accumulate thie average into variable total
            iterate+=1#accumulate iterate by 1. this tells us how many times we've seen words from the phrase in the dictionary. 
        else:#if word is not in dictionary, tell the user. 
            print("* '",word,"'"," Does not appear in any movie reviews.",sep='')
    if total==0:#if the total equals zero then we know none of the words are in the dictionary, so we print that there weren't enough words to determine the sentiment.
        print("Not enough words to determine sentiment")
        print()
        continue#continue so we go back to top of loop. 
    total_=total/iterate#then create variabe called total_ and it stores the total average of the entire phrase. calculate this by dividing total by iterate. 
    print("Average score for this phrase is:",total_)#print out average score
    if total_>2:#if total is greater than 2 then it is positive
        print("This is a POSITIVE phrase.")
    elif total_<2:#else, it is negative. 
        print("This is a NEGATIVE phrase")
    print()
        
            
        

