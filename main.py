import random 

  

def python_concepts_quiz(): 

    facts = [ 
        ("Sanjana loves animals and dogs", "False"), 
        ("Sanjana is a black belt in Taekwondo", "True"), 
        ("Zaid is an engineer", "True"), 
        ("Zaid is 50 years old", "False") 

    ] 

     

    random.shuffle(facts) 

     

    score = 0 

     

    for index, (fact, truth) in enumerate(facts, start=1): 

        print(f"Statement {index}: {fact}") 

        user_guess = input("Is this statement True or False? ").capitalize() 

        if user_guess == truth: 

            print("Correct!") 

            score += 1 

        else: 

            print(f"Incorrect. The correct answer is {truth}.") 

        print("")   

  

    print(f"Your final score is {score}/{len(facts)}") 

  

python_concepts_quiz() 
