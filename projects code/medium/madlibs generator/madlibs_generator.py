# reading story from file
with open("story.txt","r") as file:
    story = file.read()
    print(story)

words= set()

start_of_word = -1

# Define placeholder delimiters
word_start_targrt = "<"
word_end_targrt = ">"
 
# extracting placeholders
for i, char in enumerate(story):
    if char == word_start_targrt:
        start_of_word = i

    if char == word_end_targrt and start_of_word !=-1:    
        word = story[start_of_word: i+1]
        words.add(word)
        start_of_word = -1

answers ={}

# collecting inouts form user
for word in words:
    answer = input(f"Enter compatible word for {word} :")
    answers[word] = answer
print(answers) 

