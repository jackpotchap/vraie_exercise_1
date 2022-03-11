class Etudiant:
    def __init__(self, name, num):

        self.name = name
        self.num = num


    def __str__(self):
        output = ""
        output += "****************************************************\n"
        output += "\n"
        output += f"le numéro de l'étudiant: {self.num}\n"
        output += f"le nom de l'étudiant: {self.name}\n"
        output += "\n"
        output += "****************************************************\n"
        output += "\n"
        output += "\n"

        return output

