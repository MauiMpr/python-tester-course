
def word_frequency_counter (text):
    if not text:
        return{}
    
    text = text.lower().split()

    frequency = {}

    def process_words(text, index):
        if index == len(text):
            return
        
        
        word = text[index]

        if word in frequency:
          frequency[word] += 1
        else:
          frequency[word] = 1

        process_words(text, index + 1)

    process_words(text, 0)

    return frequency
    
text = ("Hello this is a piece of text to test the word counts")
frequency_dict = word_frequency_counter(text)

for word, count in frequency_dict.items():
    print(f"{word}: {count}")