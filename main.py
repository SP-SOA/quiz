import random
 
def random_fact_quiz():
    # Define facts and whether they are true or false
    facts = [
        ("Zaid", "True"),
        ("Zaid", "False"),
        ("Sanjana"", "True"),
        ("Sanjana", "False")
    ]
    # Shuffle the list of facts to present them in random order
    random.shuffle(facts)
    # Present each fact to the user and ask if it's true or false
    for fact, truth in facts:
        print(f"Fact: {fact}")
        user_guess = input("True or False? ").capitalize()
        if user_guess == truth:
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is {truth}.")
        print("")  # Blank line for spacing
 
random_fact_quiz()
