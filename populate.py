from models import Students, session

students = [
    Students(id = 1, name="Max Verstappen", age=27, emailid="max.vroom@redbull.com", contact=7894561230),
    Students(id = 2, name="Lewis Hamilton", age=33, emailid="lewis.vroom@amg.com", contact=4567891230),
    Students(id = 3, name="Sergio Perez", age=24, emailid="perez.vroom@redbull.com", contact=3216549870),
    Students(id = 4, name="Lando Norris", age=29, emailid="norris.vroom@mclaren.com", contact=7891234560),
    Students(id = 5, name="George Russell", age=30, emailid="george.vroom@mercedes.com", contact=9874563210),
    Students(id = 6, name="Carlos Sainz", age=21, emailid="carlos.vroom@ferrari.com", contact=1237890564),
    Students(id = 7, name="Fernando Alonso", age=29, emailid="alonso.vroom@astonmartin.com", contact=6541329872)
]

session.add_all(students)
session.commit()
print("Database has been populated !!!")

