print("WELCOME TO KON BANEGA CROREPATI😎😎\n")
print("The  round contains three questions and if u solved three correctly u will be earning one crore \n")

print(" Round begin---best of luck--WARM REGARDS FROM CRORE PATI\n")
questions=["who is the prime minister of india","when we multiply a number by zero what is the answer","national bird of india"]
answers=["Narendra modi","0","peacock"]
won=True
for i in range(len(questions)):
    print(questions[i])
    user_answer=input("your answer: ")
    if user_answer==answers[i].lower():
        print("CORRECT👌👌")
    else:
        print("OOPS  WRONG ANSWER OUT OF THE GAME NO MONEY EARNED")
        won= False
        break
if won:
    print("congratulations u earned one crore ❤️")
    i
    

    
    


