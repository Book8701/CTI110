
num_of_scores = int(input("How many scores do you want to enter? "))


scores_list = []


for i in range(1, num_of_scores + 1):
  
    while True:
        try:

            score = float(input(f"Enter score #{i}: "))
            
        
            if 0 <= score <= 100:
             
                scores_list.append(score)
                break
            else:
                print("INVALID Score entered!!!!")
                print("Score should be between 0 and 100")
        except ValueError:
            print("Invalid input. Please enter a numerical value.")


lowest_score = min(scores_list)


modified_list = [s for s in scores_list if s != lowest_score]


average_score = sum(modified_list) / len(modified_list)


if 90 <= average_score <= 100:
    grade = 'A'
elif 80 <= average_score < 90:
    grade = 'B'
elif 70 <= average_score < 80:
    grade = 'C'
elif 60 <= average_score < 70:
    grade = 'D'
else:
    grade = 'F'

print("------------Results--------------")
print(f"Lowest Score : {lowest_score}")
print(f"Modified List: {modified_list}")
print(f"Scores Average: {average_score:.2f}")
print(f"Grade : {grade}")
print("---------------------------------")
