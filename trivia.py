import csv
def populate_dict(filename):
    questions = {}
    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            question = line[0]
            answer = line[1] 
            questions[question] = [answer]        
    return questions

filename = "sports_trivia.csv"
questions = populate_dict(filename)
while True:
    try:
        play = int(input("Welcome to Sports Trivia! Press 1 to begin and enter for your next challenge! "))
        if play != 1:
            raise ValueError("Invalid input. Please enter '1' to play.")
        break
    except ValueError as e:
        print(e)

num_correct = 0
if play == 1:
    for question, answer in questions.items():
        user_answer = input(question)
        if user_answer.lower() == answer[0].lower():
            print("Correct!")
            num_correct += 1
            print("\tScore:", num_correct)
        else: 
            print("Incorrect!")
            print("\tCorrect Answer is: ", answer[0])
        quit = input("\tType 'quit' to end or press enter to continue: ")
        if quit.lower() == 'quit':
            print("Final Score: ", num_correct)
            break
    
    
    




