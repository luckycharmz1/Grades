def assign_grades(scores):
    best_score = max(scores)
    grades = []
    
    for score in scores:
        if score >= best_score - 10:
            grades.append('A')
        elif score >= best_score - 20:
            grades.append('B')
        elif score >= best_score - 30:
            grades.append('C')
        elif score >= best_score - 40:
            grades.append('D')
        else:
            grades.append('F')
    
    return grades

# Example usage
scores = [75, 80, 90, 60, 85]
grades = assign_grades(scores)
print(grades)
