from school import Student, session, engine


#Öğrenci eklemek için input oluşturdum.
users = [
   {
      "name" : input("name: "),
      "student_class" : input("student_class :"),
      "teacher_name" : input("teacher_name :") ,
      "student_not" : input("student_not :")
    
   }]


local_session = session(bind = engine)

for u in users:
    new_student=Student(name = u["name"], student_class = u["student_class"], teacher_name = u["teacher_name"], student_not =u["student_not"])
    
    local_session.add(new_student)

    local_session.commit()

    print(f"Added {u['name']}")


