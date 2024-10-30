class Person:
    def __init__(self, name,age,gender,):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        return f"i am {self.name} , {self.age} years old,{self.gender}"


class Member(Person):
    def __init__(self, name,age,gender,membership_id):
        Person.__init__(self,name,age,gender)
        self.membership_id = membership_id


    def introduce(self):
        return f"i am {self.name} , {self.age} years old,with membership ID : {self.membership_id}."

class Author(Person):
    def __init__(self, name,age,gender,books_written):
        self.books_written = books_written
        super().__init__(name,age,gender)

    def listofbooks(self):
        return f"The books written are {self.books_written}"

class AuthorMember(Member, Author):
    def __init__(self, name, age, gender, membership_id, books_written):

        Member.__init__(self, name, age, gender, membership_id)
        Author.__init__(self, name, age, gender, books_written)

        self.books_written = books_written


    def introduce(self):
        return f" I am {self.name} , {self.age} years old,{self.gender}, with membership ID : {self.membership_id}, Books written:{self.books_written}."
author_and_members = []
member1 = AuthorMember("Yoona", 23, "Female", "1234", "Hopps , Corals ")
author_and_members.append(member1)
member2 = AuthorMember("Haroon", 75, "Male", "1235", "Me and who , Divergent ")
author_and_members.append(member2)
member3 = AuthorMember("Sheena", 38, "Female", "1236",  "Born in 1986")
author_and_members.append(member3)

for member in author_and_members:
    print(member.introduce())








