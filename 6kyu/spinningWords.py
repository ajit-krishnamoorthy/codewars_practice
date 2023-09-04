#Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.
def spin_words(sentence):
    # Your code goes here
    sentenceList = sentence.split()
    for i in range(len(sentenceList)):
        if len(sentenceList[i]) >= 5:
            sentenceList[i] = sentenceList[i][::-1]
    newSentence = ' '.join(sentenceList)
    return newSentence