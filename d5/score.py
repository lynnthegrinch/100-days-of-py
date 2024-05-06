student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

h_s = 0
for score in student_scores:
  if score > h_s:
    h_s = score
print(f"The highest score in the class is: {h_s}")
