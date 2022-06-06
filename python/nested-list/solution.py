if __name__ == '__main__':
    student = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student[name] = score
    
    scores = list(student.values())
    scores = set(scores)
    scores = [n for n in scores]
    scores.sort()
    
    array = [key for key, value in student.items() if value == scores[1]]
    array.sort()
    for _ in array:
        print(_)
        