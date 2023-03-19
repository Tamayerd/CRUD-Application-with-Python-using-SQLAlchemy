from school import Student, session, engine

#veri tabanı ile iletişim sağlanıyor.
local_session = session(bind = engine)

#Veri tabanından istenilen verinin id'si girilerek bir query filtresi oluşturulur ve session yardımıyla bu veri silinir
student_delete=local_session.query(Student).filter(Student.id == input("Id giriniz:")).first() 

local_session.delete(student_delete)

local_session.commit()