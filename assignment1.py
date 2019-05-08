print(           "Marksheet")
English = int(input( "Enter marks of English: ")) 
Pst = int(input( "Enter marks of Pst: "))
Sindhi = int(input( "Enter marks of Sindhi: "))
Chemistry = int(input( "Enter marks of Chemistry: "))
Computer_Science = int(input( "Enter marks of Computer-Science: "))
Marks_Obtained =  English + Pst + Sindhi + Chemistry + Computer_Science
print(Marks_Obtained)
Percentage = (Marks_Obtained/500*100)
print(Percentage)
if (Percentage >= 80) :
    print("Grade A+")
elif (Percentage >=70) :
    print("Grade A")
elif (Percentage >=60) :
    print("Grade B")
elif (Percentage >=50) :
    print("Grade C")
elif (Percentage >=40) :
     print("Grade D")
else :
    print(Fail)