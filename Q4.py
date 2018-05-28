def truefalse(correct,id,answers):
    correct=[]
    answers=[]
    for x in answers:
        answers.append(x)
    for x in correct:
        correct.append(x)

    Score=0
    if id == 999:
        return
    else:
        for x in range(0,len(answers)):
            print(x)
            # print(answer[x]==correct[x])
            # print(Score)
            if answers[x] == "x":
                Score+=0
            elif answers[x] == correct[x]:
                Score+=1
            elif answers[x] != correct[x]:
                Score-=1
        print(id, " ", Score, " marks")

        # for x,y in zip(correct,answers):
        #     if y == 'x':
        #         Score=Score
        #     elif x==y:
        #         Score+=1
        #     else:
        #         Score-=1


# print("t"=="t")

truefalse("T F T F T F T F T F T F T F T F T F T F T F T F T F T F T F",100," T F T T F F T F T F T F T F T T T F F F x F T x T F T F x F")



