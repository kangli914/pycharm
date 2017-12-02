#imagine this is the data you've just scraped off of some social media web site 
dirty_data = "You're your own best friend. But Doug's awsme! #dougisawesome" 

#create a dictionary of possible ambiguous apostrophies and their less ambiguous counterparts 
APOSTROPHES = {"'s" : " is", "'re" : " are"} #there are many more apostrophy uses in both English slang and grammar that you'd have to check for 

#chop up the words 
words = dirty_data.split() 

#create a blank list to hold modified words 

new_words = [] 

#loop through each word 
for word in words: 
	for key in APOSTROPHES.keys(): 
		if key in word: 
			word = word.replace(key, APOSTROPHES[key]) 
		new_words.append(word) 
		
#reassemble the string from the new words
clean_data = " ".join(new_words) 

#to prove to you that we fixed the text: 
print(clean_data)