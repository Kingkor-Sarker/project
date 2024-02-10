import random
import time
operartor = ["+", "-", "*"]
min_oparand = 2
max_oparand = 10
total_question = 10
wrong = 0
def generat():
    left = random.randint(min_oparand, max_oparand)
    right = random.randint(min_oparand, max_oparand)
    op = random.choice(operartor)
    question = str(left) + op + str(right)
    sol = eval(question)
    return question, sol
input("press enter to start")
print("---------------------------------")
start = time.time()
for i in range(total_question):
    question, sol = generat()
    while True:
        ans = input(f"Question no {i+1}: {question}:")
        if int(ans) == sol:
            break
        print("Wrong try again")
        wrong += 1
end = time.time()
print("---------------------------------")
print("Nice work")
print(f"Total time: {round(end - start, 2)}sec \nwrong: {wrong} \ntime per question: {round((end - start)/total_question, 2)}")


