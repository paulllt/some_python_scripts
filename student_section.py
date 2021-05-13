category = {
            'BSIT-2A':['John','David','Mary'],
            'BSIT-2B':['Joe','Diana','Susan'],
            'BSIT-2C':['Alex','Carla','Haley'],
            'BSIT-2D':['Dorothy','Athena','Darwin']
           }


student = input("Enter student name: ")

section = [k for k, v in category.items() if student in v]
print(section)

# for k, v in category.items():
#     if student in v:
#         print(k)