class Etudiant:
    def __init__(self, name, num,programe,age):

        self.name = name
        self.num = num
        self.programe = programe
        self.age = age


    def __str__(self):
        output = ""
        output += "****************************************************\n"
        output += "\n"
        output += f"le numéro de l'étudiant: {self.num}\n"
        output += f"le nom de l'étudiant: {self.name}\n"
        output += f"le programe de l'étudiant: {self.programe}\n"
        output += f"l'age' de l'étudiant: {self.age}\n"
        output += "\n"
        output += "****************************************************\n"
        output += "\n"
        output += "\n"

        return output

