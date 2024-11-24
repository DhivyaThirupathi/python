student=(40,"Shree",21,8.57,"MCA")
print(student)
#a. problem
mod=list(student)
mod[3]=9.5
student=tuple(mod)
print(student)
#b. problem
mod_1=list(student)
mod_1[4]="CS"
stud1=tuple(mod_1)
print(stud1)
# c problem
new=(2024,)
print(stud1+new)
