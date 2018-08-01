from random import randint 


def main():
 l = []
 for i in range (3):
  film = input("Vnesi film: ")
  l.append(film)
 print (result(l))
	
def result(l):
 return l[randint(0,2)]	

main()
