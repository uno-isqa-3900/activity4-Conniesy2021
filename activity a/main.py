# "Connie"
# "ISQA 3900 Web Application Development"
# "Data: 2/14/2021"
# "list unique name"


def list_name():
     # First list
     names = ['maria', 'maria', 'will', 'sam', 'maria', 'kahn', 'sam', 'barry', 'george', 'hank', 'belinda', 'maria', 'karthik']
     names.sort()
     print("Intial list of Namme:\n" + str(names))

     # Second list
     names1 = []
     for i in names:
         if i not in names1:
            names1.append(i)
     print("\nList of unique names:\n" + str(names1))

list_name()




