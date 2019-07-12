import csv

# variables
# Entrez le @NomDeDomaine.extension exemple: @exemple.org
suitemail = "@domaine.extension"

# Entrez la base que les mots de passe auront
suitepass = "password"
quota = 10
comptes = []
listNoms = []

# Mettez le nom de votre fichier text des noms des employees
with open("fichierDeNoms.txt", "r") as f:
    for line in f:
        newnom = line.lower().replace(" ", "")
        newnom = newnom.replace("\n", "")
        email = newnom + suitemail
        password = newnom + suitepass
        acces = [email, password, quota]
        listNoms.append(acces)

with open('FichierDesAccess.csv', 'w', newline='', encoding='utf-8') as f:
    thewriter = csv.writer(f)
    thewriter.writerow(["Email", "Password", "Quota"])
    for acces in listNoms:
        thewriter.writerow(acces)
        """f.write(email)
        f.write("\n")"""
