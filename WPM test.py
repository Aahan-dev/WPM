import time
import random

# List of sentences to use in the WPM test
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Python programming is fun and educational.",
    "Practice makes perfect, but nobody's perfect.",
    "A journey of a thousand miles begins with a single step.",
    "To be or not to be, that is the question."
]

def get_random_sentence(): # Reeturns a random sentence from the list
    
    return random.choice(sentences)

def calculate_wpm(start_time, end_time, typed_text): # Calculates WPM
   
    elapsed_time = end_time - start_time  # Time in seconds
    minutes = elapsed_time / 60
    words = len(typed_text.split())
    wpm = words / minutes if minutes > 0 else 0
    return wpm

def wpm_test(): # Conducts the WPM test
    
    print("Welcome to the WPM Test!")
    print("Type the following sentence as fast as you can:\n")
    
    sentence = get_random_sentence() 
    print(f'Sentence: "{sentence}"')
    
    input("Press Enter when you are ready to start...")
    
    start_time = time.time()  # Start timing
    typed_text = input("\nStart typing: ")
    end_time = time.time()  # End timing
   
    wpm = calculate_wpm(start_time, end_time, typed_text)
   
    print(f"\nYour WPM is: {wpm:.2f}") # Prints WPM
   
    # Check for accuracy
    correct_words = sentence.split()
    typed_words = typed_text.split()
    correct_count = sum(1 for cw, tw in zip(correct_words, typed_words) if cw == tw)
    accuracy = (correct_count / len(correct_words)) * 100 if correct_words else 0
   
    print(f"Accuracy: {accuracy:.2f}%") # Prints accuracy


if __name__ == "__main__":
    wpm_test()  # Run the WPM tests
