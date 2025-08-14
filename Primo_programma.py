# Il nostro primo programma in Python

robot_name = "Chappie"
robot_age = 1
print("Ciao, sono " + robot_name + " e ho " + str(robot_age) + " anno.")

user_name = input("Come ti chiami? ")
print("Ciao " + user_name + ", piacere di conoscerti!")

user_age = input("Quanti anni hai? ")
age_difference = user_age - int(robot_age)
print("La differenza di età tra noi è di " + str(age_difference) + " anni.")
print("Grazie per aver interagito con me, " + user_name + "!")
print("Arrivederci!")
print("Spero di rivederti presto!")
