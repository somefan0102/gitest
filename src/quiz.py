def start(quiz):
    total_correct = 0
    total_length = len(quiz)

    for qna in quiz:
        answer = input(qna[0]).lower()
        if answer == qna[1]:
            print("Correct!")
            total_correct += 1
        else:
            print(f"Incorrect, the correct answer was \"{qna[1]}\".")
        print()
    
    print(f"Verbal score: {total_correct} out of {total_length}.")
    print(f"Percentage score: {(total_correct/total_length):.2%}")

    if total_correct == total_length:
        print(f"\U0001f389")