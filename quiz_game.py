

questions = [ 
    {
        "question" : "when is Ganesh Chaturthi celebrated ?",
        "options"  : ["A. Kartika ", "B. Ashwin", "C. Bhadrapada ", "D. Magha"],
        "answer"   : "C"
    },
    { 
        "question" : "what is the capital of India ?", 
        "options"  : ["A. Delhi ", "B. Mumbai", "C. Kolkata", "D. Chennai"],
        "answer"   : "A"
    },
    {
        "question" : "Which language is used for Data Science ?",
        "options"  : ["A. Python", "B. HTML", "C. CSS", "D. C"], 
        "answer"   : "A"
    },
    {
        "question" : "Which planet is known as the Red Planet ?",
        "options"  : ["A. Earth", "B. Venus", "C. Mars", "D. Jupiter"],
        "answer"   : "C"
    },
    {
        "question" : "Prime Minister of India ?",
        "options"  : ["A.  Mamta Banerjee", "B. Rahul Gandhi", "C. Arvind Kejriwal", "D. Narendra Modi"],
        "answer"   : "D"
    }, 
    {
        "question" : "world Sanskrit day is celebrated on which day",
        "options"  : ["A. 20th August ", "B. 21st September", "C. 28th August", "D. 22nd October"],
        "answer"   : "C"
    },
    {
        "question" : " Which of the three banks will be merged with the other two to create India third-largest bank?",
        "options"  : ["A. Punjab National Bank ", "B.  Indian Bank", "C. Bank of Baroda ", "D. Dena Bank"],
        "answer"   : "B"
    },
    {
        "question" : " Where was India’s first national Museum opened?",
        "options"  : ["A. Delhi ", "B.  Hyderabad", "C. Rajasthan ", "D. Mumbai"],
        "answer"   : "D"
    },
    {
        "question" : " The father of Indian missile technology is _________________?",
        "options"  : ["A.Dr Homi Bhabha ", "B.  Dr Chidambaram", "C. Dr U.R. Rao ", "D.Dr A.P.J. Abdul Kalam"],
        "answer"   : "D"
    },
    {
        "question" : " The sixth avatars of Goddess Durga?",
        "options"  : ["A.  Katyayani ", "B.  Kushmanda", "C. Shailaputri ", "D. Brahmacharini"],
        "answer"   : "A"
    }
]
import random

# Suffle the questions to ensure a different order each time the game is played 
random.shuffle(questions)

print("Welcome to the Python Quiz Game!")
print("You will be asked", len(questions), "questions.")
print("Type A, B, C or D to answer.\n")

score = 0 

for q in questions :
    print ( "\n" + q["question"])

    for option in q ["options"] :
        print (option)
    
    user_answer = input("Enter your answer (A/B/C/D) : " ).upper()
    
    if user_answer == q["answer"]:
        print("Correct answer!!!")
        score += 1
        print("Current Score:", score)
 
    else : 
        print ("Wrong Answer!!!!")
        score -= 1
        print("Current Score:", score)
        
        correct_option = q["options"][ord(q["answer"]) - ord('A')]
        print ("Correct answer is : " , correct_option)


print ("-----------------------------------------------")


print("\n Quiz Completed!!!")
print("Your score is :", score, "out of", len(questions))
percentage = (score / len(questions)) * 100
print("Percentage:", percentage, "%")

if percentage >= 80:
    print("Excellent performance!")
elif percentage >= 50:
    print("Good job!")
else:
    print("Keep practicing!")

