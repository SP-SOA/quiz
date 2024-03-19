import random

def python_concepts_quiz():
    # Define facts 
    facts = [
        # Placeholder facts  
        ("Fact 1: Placeholder description", "True"),
        ("Fact 2: Placeholder description", "True"),
        ("Fact 3: Placeholder description", "True"),
        ("Fact 4: Placeholder description", "True")
    ]
    
    # Shuffle the list of facts to present them in random order
    random.shuffle(facts)
    
    # Initialize score
    score = 0
    
    # Enumerate and present each fact to the user, asking if it's true or false
    for index, (fact, truth) in enumerate(facts, start=1):
        print(f"Python Statement {index}: {fact}")
        user_guess = input("Is this statement True or False? ").capitalize()
        if user_guess == truth:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer is {truth}.")
        print("")  

    # Final score
    print(f"Your final score is {score}/{len(facts)}")

# Call the function
python_concepts_quiz()
