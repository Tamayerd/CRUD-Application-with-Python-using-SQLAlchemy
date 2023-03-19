from school import Student, session, engine

local_session = session(bind = engine)

while(True):
    print(""""""""""
1- İsim Değiştir
2- Sınıf değiştir
3- Öğretmen değiştir
4- Not değiştir
""""""""")
    numara = int(input("Yapmak istediğiniz işlem numarasını giriniz:"))
    #Veri tabanından istenilen verinin id'si girilerek bir query filtresi oluşturulur ve session yardımıyla bu veri eklenir
    Student_update = local_session.query(Student).filter(Student.id == input("Id giriniz:")).first() #yalnızca bir satır değişir. = first()

    if numara == 1 :
        
        Student_update.name = input("İsim giriniz:")
        break
    elif numara == 2  :
        
        Student_update.student_class = input("Sınıf giriniz:")
        local_session.commit()
        break

    elif numara == 3:
        
        Student_update.teacher_name = input("Öğretmen adı giriniz:")
        local_session.commit()
        break
    elif numara == 4:
        
        Student_update.student_not = input("Öğrenci notu giriniz:")
        local_session.commit()
        break
    else:
        
       print("Geçersiz sayı girdiniz, tekrar seçiniz:")
    continue
