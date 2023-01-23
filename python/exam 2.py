sentence = str(input())
frequent_word = ""
frequency = 0  
words = []
  
# Traversing file line by line 
for line in sentence:
    line_word = line.lower().replace(',','').replace('.','').split(" ");  
      
    
    for w in line_word:  
        words.append(w);  
          
# Finding the max occured word
for i in range(0, len(words)):  
      
    # Declaring count
    count = 1;  
      
    # Count each word in the file  
    for j in range(i+1, len(words)):  
        if(words[i] == words[j]):  
            count = count + 1;  
  
    # If the count value is more
    # than highest frequency then
    if(count > frequency):  
        frequency = count;  
        frequent_word = words[i];  
  
print("Most repeated word: " + frequent_word)
print("Frequency: " + str(frequency))