def analisador(codigo):
	estado = 0
	p=0
	fim = 0
	ult_position = (len(codigo)-1)
	print_v = []
	while (fim == 0):
		if(estado == 0):
			if (codigo[p] == 'p'):
			    estado = 1
			    print_v.append(codigo[p])
			elif(codigo[p] == 'i'):
				estado = 7
				print_v.append(codigo[p])
			elif(codigo[p] == 'a' or codigo[p] == 'b' or codigo[p] == 'c' or codigo[p] == 'd' or codigo[p] == 'f' or codigo[p] == 'g' or codigo[p] == 'h' or codigo[p] == 'j' or codigo[p] == 'k' or codigo[p] == 'l' or codigo[p] == 'm' or codigo[p] == 'n' or codigo[p] == 'o' or codigo[p] == 'q' or codigo[p] == 'r' or codigo[p] == 's' or codigo[p] == 't'or codigo[p] == 'u'or codigo[p] == 'v'or codigo[p] == 'w'or codigo[p] == 'x'or codigo[p] == 'y'or codigo[p] == 'z'or codigo[p] == 'A'or codigo[p] == 'B'or codigo[p] == 'C'or codigo[p] == 'D'or codigo[p] == 'E'or codigo[p] == 'F'or codigo[p] == 'G'or codigo[p] == 'H'or codigo[p] == 'I'or codigo[p] == 'J'or codigo[p] == 'K'or codigo[p] == 'L'or codigo[p] == 'M'or codigo[p] == 'N'or codigo[p] == 'O'or codigo[p] == 'P'or codigo[p] == 'Q'or codigo[p] == 'R'or codigo[p] == 'S'or codigo[p] == 'T'or codigo[p] == 'U'or codigo[p] == 'V'or codigo[p] == 'W'or codigo[p] == 'X'or codigo[p] == 'Y'or codigo[p] == 'Z' or codigo[p] == '_'):
			    estado = 18
			    print_v.append(codigo[p])
			elif(codigo[p] == 'e'):
			    estado = 13
			    print_v.append(codigo[p])
			elif(codigo[p] == '"'):
			    estado = 20
			    print_v.append(codigo[p])
			elif(codigo[p] == '0' or codigo[p] ==  '1' or codigo[p] ==  '2' or codigo[p] ==  '3' or codigo[p] ==  '4' or codigo[p] ==  '5' or codigo[p] ==  '6' or codigo[p] ==  '7' or codigo[p] ==  '8' or codigo[p] ==  '9'):
				estado = 23
				print_v.append(codigo[p])  
			elif(codigo[p] == '('):
				estado = 28
				print_v.append(codigo[p])
			elif(codigo[p] == ')'):
				estado = 29
				print_v.append(codigo[p])
			elif(codigo[p] == '{'):
			    estado = 30
			    print_v.append(codigo[p])
			elif(codigo[p] == '}'):
			    estado = 31
			    print_v.append(codigo[p])
			elif(codigo[p] == '['):
			    estado = 32
			    print_v.append(codigo[p])
			elif(codigo[p] == ']'):
			    estado = 33
			    print_v.append(codigo[p])
			elif(codigo[p] == ';'):
			    estado = 34
			    print_v.append(codigo[p])
			elif(codigo[p] == ','):
			    estado = 35
			    print_v.append(codigo[p])
			elif(codigo[p] == '&'):
			    estado = 38
			    print_v.append(codigo[p])
			elif(codigo[p] == '|'):
			    estado = 39
			    print_v.append(codigo[p])
			elif(codigo[p] == '<'):
			    estado = 40
			    print_v.append(codigo[p])
			elif(codigo[p] == '>'):
			    estado = 41
			    print_v.append(codigo[p])
			elif(codigo[p] == '!'):
			    estado = 42
			    print_v.append(codigo[p])
			elif(codigo[p] == '='):
			    estado = 43
			    print_v.append(codigo[p])
			elif(codigo[p] == '%'):
			    estado = 52
			    print_v.append(codigo[p])
			elif(codigo[p] == '+'):
			    estado = 53
			    print_v.append(codigo[p])
			elif(codigo[p] == '-'):
			    estado = 54
			    print_v.append(codigo[p])
			elif(codigo[p] == '*'):
			    estado = 55
			    print_v.append(codigo[p])
			elif(codigo[p] == '/'):
			    estado = 57
			    print_v.append(codigo[p])
			elif(codigo[p] == ' ' or codigo[p] == '\n' or codigo[p] == '\t'):
				p=p+1
				estado = 0

		if(estado == 1):
			if ((p == ult_position)):
				estado = 18
			else:
				p=p+1

				if(codigo[p] == 'r'):
				 	estado = 2
				 	print_v.append(codigo[p])
				 	if (p == ult_position):
				 		estado = 18
				else:
					estado = 18
					print_v.append(codigo[p])

		if(estado == 2):
			p=p+1

			if(codigo[p] == 'i'):
			 	estado = 3
			 	print_v.append(codigo[p])
			 	if (p == ult_position):
			 		estado = 18
			else:
				estado = 18
				print_v.append(codigo[p])

		if(estado == 3):
			p=p+1
			
			if(codigo[p] == 'n'):
			 	estado = 4
			 	print_v.append(codigo[p])
			 	if (p == ult_position):
			 		estado = 18
			else:
				estado = 18
				print_v.append(codigo[p])
			
		if(estado == 4):
			p=p+1
			
			if(codigo[p] == 't'):
			 	estado = 5
			 	print_v.append(codigo[p])
			else:
				estado = 18
				print_v.append(codigo[p])
			
		if(estado == 5):
			if ((p == ult_position)):
				estado = 6
			else:
				p=p+1

				if(codigo[p] == ' ' or codigo[p] == '\n' or codigo[p] == '\t' or codigo[p] == '(' or codigo[p] == ')' or codigo[p] == '{' or codigo[p] == '}' or codigo[p] == '[' or codigo[p] == ']' or codigo[p] == ';' or codigo[p] == ','):
				 	estado = 6
				else:
					estado = 18
					print_v.append(codigo[p])
			
		if(estado == 6):
			if(codigo[p] == '(' or codigo[p] == ')' or codigo[p] == '{' or codigo[p] == '}' or codigo[p] == '[' or codigo[p] == ']' or codigo[p] == ';' or codigo[p] == ','):
				p=p-1
				for z in print_v:
					print(z, end='')
				print(" -> Palavra Reservada")
				print_v.clear()
				if (p == ult_position):
					break
				else:
					p=p+1
					estado = 0
			else:
				for z in print_v:
					print(z, end='')
				print(" -> Palavra Reservada")
				print_v.clear()
				if (p == ult_position):
					break
				else:
					estado = 0

		if(estado == 7):
			if ((p == ult_position)):
				estado = 18
			else:
				p=p+1

				if(codigo[p] == 'n'):
				 	estado = 8
				 	print_v.append(codigo[p])
				 	if (p == ult_position):
				 		estado = 18

				elif(codigo[p] == 'f'):
					estado = 11
					print_v.append(codigo[p])

				else:
					estado = 18
					print_v.append(codigo[p])

		if(estado == 8):
			p=p+1
			if(codigo[p] == 't'):
			 	estado = 9
			 	print_v.append(codigo[p])
			else:
				estado = 18
				print_v.append(codigo[p])

		if(estado == 9):
			if ((p == ult_position)):
				estado = 10
			else:
				p=p+1

				if(codigo[p] == ' ' or codigo[p] == '\n' or codigo[p] == '\t' or codigo[p] == '(' or codigo[p] == ')' or codigo[p] == '{' or codigo[p] == '}' or codigo[p] == '[' or codigo[p] == ']' or codigo[p] == ';' or codigo[p] == ','):
				 	estado = 10
				else:
					estado = 18
					print_v.append(codigo[p])

		if(estado == 10):
			if(codigo[p] == '(' or codigo[p] == ')' or codigo[p] == '{' or codigo[p] == '}' or codigo[p] == '[' or codigo[p] == ']' or codigo[p] == ';' or codigo[p] == ','):
				p=p-1
				for z in print_v:
					print(z, end='')
				print(" -> Palavra Reservada")
				print_v.clear()
				if (p == ult_position):
					break
				else:
					p=p+1
					estado = 0
			else:
				for z in print_v:
					print(z, end='')
				print(" -> Palavra Reservada")
				print_v.clear()
				if (p == ult_position):
					break
				else:
					estado = 0

		if(estado == 11):
			if ((p == ult_position)):
				estado = 12
			else:
				p=p+1

				if(codigo[p] == ' ' or codigo[p] == '\n' or codigo[p] == '\t' or codigo[p] == '(' or codigo[p] == ')' or codigo[p] == '{' or codigo[p] == '}' or codigo[p] == '[' or codigo[p] == ']' or codigo[p] == ';' or codigo[p] == ','):
				 	estado = 12
				else:
					estado = 18
					print_v.append(codigo[p])


		if(estado == 12):
			if(codigo[p] == '(' or codigo[p] == ')' or codigo[p] == '{' or codigo[p] == '}' or codigo[p] == '[' or codigo[p] == ']' or codigo[p] == ';' or codigo[p] == ','):
				p=p-1
				for z in print_v:
					print(z, end='')
				print(" -> Palavra Reservada")
				print_v.clear()
				if (p == ult_position):
					break
				else:
					p=p+1
					estado = 0
			else:
				for z in print_v:
					print(z, end='')
				print(" -> Palavra Reservada")
				print_v.clear()
				if (p == ult_position):
					break
				else:
					estado = 0

		if(estado == 13):
			if ((p == ult_position)):
				estado = 18
			else:
				p=p+1

				if(codigo[p] == 'l'):
				 	estado = 14
				 	print_v.append(codigo[p])
				 	if (p == ult_position):
				 		estado = 18
				else:
					estado = 18
					print_v.append(codigo[p])

		if(estado == 14):
			p=p+1

			if(codigo[p] == 's'):
			 	estado = 15
			 	print_v.append(codigo[p])
			 	if (p == ult_position):
			 		estado = 18
			else:
				estado = 18
				print_v.append(codigo[p])

		if(estado == 15):
			p=p+1
			
			if(codigo[p] == 'e'):
			 	estado = 16
			 	print_v.append(codigo[p])
			else:
				estado = 18
				print_v.append(codigo[p])

		if(estado == 16):
			if ((p == ult_position)):
				estado = 17
			else:
				p=p+1

				if(codigo[p] == ' ' or codigo[p] == '\n' or codigo[p] == '\t' or codigo[p] == '(' or codigo[p] == ')' or codigo[p] == '{' or codigo[p] == '}' or codigo[p] == '[' or codigo[p] == ']' or codigo[p] == ';' or codigo[p] == ','):
				 	estado = 17
				else:
					estado = 18
					print_v.append(codigo[p])

		if(estado == 17):
			if(codigo[p] == '(' or codigo[p] == ')' or codigo[p] == '{' or codigo[p] == '}' or codigo[p] == '[' or codigo[p] == ']' or codigo[p] == ';' or codigo[p] == ','):
				p=p-1
				for z in print_v:
					print(z, end='')
				print(" -> Palavra Reservada")
				print_v.clear()
				if (p == ult_position):
					break
				else:
					p=p+1
					estado = 0
			else:
				for z in print_v:
					print(z, end='')
				print(" -> Palavra Reservada")
				print_v.clear()
				if (p == ult_position):
					break
				else:
					estado = 0

		if(estado == 18):
			if ((p == ult_position)):
				estado = 19
			else:
				p=p+1

				if(codigo[p] == 'A'or codigo[p] == 'B'or codigo[p] == 'C'or codigo[p] == 'D'or codigo[p] == 'E'or codigo[p] == 'F'or codigo[p] == 'G'or codigo[p] == 'H'or codigo[p] == 'I'or codigo[p] == 'J'or codigo[p] == 'K'or codigo[p] == 'L'or codigo[p] == 'M'or codigo[p] == 'N'or codigo[p] == 'O'or codigo[p] == 'P'or codigo[p] == 'Q'or codigo[p] == 'R'or codigo[p] == 'S'or codigo[p] == 'T'or codigo[p] == 'U'or codigo[p] == 'V'or codigo[p] == 'W'or codigo[p] == 'X'or codigo[p] == 'Y'or codigo[p] == 'Z'or codigo[p] == 'a'or codigo[p] == 'b'or codigo[p] == 'c'or codigo[p] == 'd'or codigo[p] == 'e'or codigo[p] == 'f'or codigo[p] == 'g'or codigo[p] == 'h'or codigo[p] == 'i'or codigo[p] == 'j'or codigo[p] == 'k'or codigo[p] == 'l'or codigo[p] == 'm'or codigo[p] == 'n'or codigo[p] == 'o'or codigo[p] == 'p'or codigo[p] == 'q'or codigo[p] == 'r'or codigo[p] == 's'or codigo[p] == 't'or codigo[p] == 'u'or codigo[p] == 'v'or codigo[p] == 'w'or codigo[p] == 'x'or codigo[p] == 'y'or codigo[p] == 'z'or codigo[p] == '0' or codigo[p] ==  '1' or codigo[p] ==  '2' or codigo[p] ==  '3' or codigo[p] ==  '4' or codigo[p] ==  '5' or codigo[p] ==  '6' or codigo[p] ==  '7' or codigo[p] ==  '8' or codigo[p] ==  '9' or codigo[p] == '_'):
				 	estado = 18
				 	print_v.append(codigo[p])
				 	if (p == ult_position):
				 		estado = 19

				elif(codigo[p]==" " or codigo[p]=="\n" or codigo[p]=="\t" or codigo[p]=="(" or codigo[p]==")" or codigo[p]=="{" or codigo[p]=="}" or codigo[p]=="[" or codigo[p]=="]" or codigo[p]==";" or codigo[p]=="," or codigo[p]=="+" or codigo[p]=="-" or codigo[p]=="*" or codigo[p]=="/" or codigo[p]=="%" or codigo[p]=="&" or codigo[p]=="|" or codigo[p]=="!"  or codigo[p]=="="  or codigo[p]==">" or codigo[p]=="<"):
					estado = 19
				else:
					estado = 18
					print_v.append(codigo[p])

		if(estado == 19):
			if(codigo[p]=="(" or codigo[p]==")" or codigo[p]=="{" or codigo[p]=="}" or codigo[p]=="["or codigo[p]=="]" or codigo[p]==";" or codigo[p]=="," or codigo[p]=="+" or codigo[p]=="-" or codigo[p]=="*" or codigo[p]=="/" or codigo[p]=="%" or codigo[p]=="&" or codigo[p]=="|" or codigo[p]=="!"  or codigo[p]=="="  or codigo[p]==">" or codigo[p]=="<"):
				p=p-1
				for z in print_v:
					print(z, end='')
				print(" -> Identificador")
				print_v.clear()
				if (p == ult_position):
					break
				else:
					p=p+1
					estado = 0
			else:
				for z in print_v:
					print(z, end='')
				print(" -> Identificador")
				print_v.clear()
				if (p == ult_position):
					break
				else:
					estado = 0

		if(estado == 20):
			if ((p == ult_position)):
				estado = 22
			else:
				p=p+1

				if(codigo[p] != '"'):
				 	estado = 20
				 	print_v.append(codigo[p])
				 	if (p == ult_position):
				 		estado = 22
				else:
					estado = 21
					print_v.append(codigo[p])

		if(estado == 21):
			for z in print_v:
				print(z, end='')
			print(" -> String")
			print_v.clear()
			if (p == ult_position):
				break
			else:
				p=p+1
				estado = 0

		if(estado == 22):
			for z in print_v:
				print(z, end='')
			print (' -> ERRO: abriu aspas mas não fechou')
			print_v.clear()
			break

		if(estado == 23):
			if ((p == ult_position)):
				estado = 25
			else:
				p=p+1

				if(codigo[p] == '0' or codigo[p] ==  '1' or codigo[p] ==  '2' or codigo[p] ==  '3' or codigo[p] ==  '4' or codigo[p] ==  '5' or codigo[p] ==  '6' or codigo[p] ==  '7' or codigo[p] ==  '8' or codigo[p] ==  '9'):
				 	estado = 23
				 	print_v.append(codigo[p])
				 	if (p == ult_position):
				 		estado = 25

				elif(codigo[p]=="."):
					estado = 27
					print_v.append(codigo[p])
					if (p == ult_position):
						print("ERRO: o '.' não pode ser o ultimo valor")
						break

				elif(codigo[p]==" " or codigo[p]=="\n" or codigo[p]=="\t" or codigo[p]=="(" or codigo[p]==")" or codigo[p]=="{" or codigo[p]=="}" or codigo[p]=="[" or codigo[p]=="]" or codigo[p]==";" or codigo[p]=="," or codigo[p]=="+" or codigo[p]=="-" or codigo[p]=="*" or codigo[p]=="/" or codigo[p]=="%" or codigo[p]=="&" or codigo[p]=="|" or codigo[p]=="!"  or codigo[p]=="="  or codigo[p]==">" or codigo[p]=="<"):
					estado = 25
				else:
					estado = 18
					print_v.append(codigo[p])

		if(estado == 24):
			if(codigo[p]=="(" or codigo[p]==")" or codigo[p]=="{" or codigo[p]=="}" or codigo[p]=="["or codigo[p]=="]" or codigo[p]==";" or codigo[p]=="," or codigo[p]=="+" or codigo[p]=="-" or codigo[p]=="*" or codigo[p]=="/" or codigo[p]=="%" or codigo[p]=="&" or codigo[p]=="|" or codigo[p]=="!"  or codigo[p]=="="  or codigo[p]==">" or codigo[p]=="<"):
				p=p-1
				for z in print_v:
					print(z, end='')
				print(" -> Número Decimal")
				print_v.clear()
				if (p == ult_position):
					break
				else:
					p=p+1
					estado = 0
			else:
				for z in print_v:
					print(z, end='')
				print(" -> Número Decimal")
				print_v.clear()
				if (p == ult_position):
					break
				else:
					estado = 0

		if(estado == 25):
			if(codigo[p]=="(" or codigo[p]==")" or codigo[p]=="{" or codigo[p]=="}" or codigo[p]=="["or codigo[p]=="]" or codigo[p]==";" or codigo[p]=="," or codigo[p]=="+" or codigo[p]=="-" or codigo[p]=="*" or codigo[p]=="/" or codigo[p]=="%" or codigo[p]=="&" or codigo[p]=="|" or codigo[p]=="!"  or codigo[p]=="="  or codigo[p]==">" or codigo[p]=="<"):
				p=p-1
				for z in print_v:
					print(z, end='')
				print(" -> Número Inteiro")
				print_v.clear()
				if (p == ult_position):
					break
				else:
					p=p+1
					estado = 0
			else:
				for z in print_v:
					print(z, end='')
				print(" -> Número Inteiro")
				print_v.clear()
				if (p == ult_position):
					break
				else:
					estado = 0

		if(estado == 26):
			if ((p == ult_position)):
				estado = 24
			else:
				p=p+1

				if(codigo[p] == '0' or codigo[p] ==  '1' or codigo[p] ==  '2' or codigo[p] ==  '3' or codigo[p] ==  '4' or codigo[p] ==  '5' or codigo[p] ==  '6' or codigo[p] ==  '7' or codigo[p] ==  '8' or codigo[p] ==  '9'):
				 	estado = 26
				 	print_v.append(codigo[p])
				 	if (p == ult_position):
				 		estado = 24

				elif(codigo[p]==" " or codigo[p]=="\n" or codigo[p]=="\t" or codigo[p]=="(" or codigo[p]==")" or codigo[p]=="{" or codigo[p]=="}" or codigo[p]=="["or codigo[p]=="]" or codigo[p]==";" or codigo[p]=="," or codigo[p]=="+" or codigo[p]=="-" or codigo[p]=="*" or codigo[p]=="/" or codigo[p]=="%" or codigo[p]=="&" or codigo[p]=="|" or codigo[p]=="!"  or codigo[p]=="="  or codigo[p]==">" or codigo[p]=="<"):
					estado = 24
				else:
					estado = 18

		if(estado == 27):
			p=p+1
			if(codigo[p] == '0' or codigo[p] ==  '1' or codigo[p] ==  '2' or codigo[p] ==  '3' or codigo[p] ==  '4' or codigo[p] ==  '5' or codigo[p] ==  '6' or codigo[p] ==  '7' or codigo[p] ==  '8' or codigo[p] ==  '9'):
				estado = 26
				print_v.append(codigo[p])
			else:
				estado = 18
				print_v.append(codigo[p])
		if(estado == 28):
			for z in print_v:
				print(z, end='')
			print(" -> Delimitador")
			print_v.clear()
			if (p == ult_position):
				break
			else:
				p=p+1
				estado = 0

		if(estado == 29):
			for z in print_v:
				print(z, end='')
			print(" -> Delimitador")
			print_v.clear()
			if (p == ult_position):
				break
			else:
				p=p+1
				estado = 0

		if(estado == 30):
			for z in print_v:
				print(z, end='')
			print(" -> Delimitador")
			print_v.clear()
			if (p == ult_position):
				break
			else:
				p=p+1
				estado = 0

		if(estado == 31):
			for z in print_v:
				print(z, end='')
			print(" -> Delimitador")
			print_v.clear()
			if (p == ult_position):
				break
			else:
				p=p+1
				estado = 0
			
		if(estado == 32):
			for z in print_v:
				print(z, end='')
			print(" -> Delimitador")
			print_v.clear()
			if (p == ult_position):
				break
			else:
				p=p+1
				estado = 0
			
		if(estado == 33):
			for z in print_v:
				print(z, end='')
			print(" -> Delimitador")
			print_v.clear()
			if (p == ult_position):
				break
			else:
				p=p+1
				estado = 0
			
		if(estado == 34):
			for z in print_v:
				print(z, end='')
			print(" -> Delimitador")
			print_v.clear()
			if (p == ult_position):
				break
			else:
				p=p+1
				estado = 0
			
		if(estado == 35):
			for z in print_v:
				print(z, end='')
			print(" -> Delimitador")
			print_v.clear()
			if (p == ult_position):
				break
			else:
				p=p+1
				estado = 0
			
		if(estado == 36):
			for z in print_v:
				print(z, end='')
			print(" -> Operador Lógico")
			print_v.clear()
			if (p == ult_position):
				break
			else:
				p=p+1
				estado = 0
				
			
		if(estado == 37):
			for z in print_v:
				print(z, end='')
			print(" -> Operador Lógico")
			print_v.clear()
			if (p == ult_position):
				break
			else:
				p=p+1
				estado = 0
			
		if(estado == 38):
			if ((p == ult_position)):
				estado = 18
			else:
				p=p+1

				if(codigo[p] == '&'):
				 	estado = 36
				 	print_v.append(codigo[p])
				else:
					estado = 18
					print_v.append(codigo[p])

		if(estado == 39):
			if ((p == ult_position)):
				estado = 18
			else:
				p=p+1

				if(codigo[p] == '|'):
				 	estado = 37
				 	print_v.append(codigo[p])
				else:
					estado = 18
					print_v.append(codigo[p])

		if(estado == 40):
			if ((p == ult_position)):
				estado = 44
			else:
				p=p+1

				if(codigo[p] == '='):
				 	estado = 45
				 	print_v.append(codigo[p])
				else:
					estado = 44

		if(estado == 41):
			if ((p == ult_position)):
				estado = 46
			else:
				p=p+1

				if(codigo[p] == '='):
				 	estado = 47
				 	print_v.append(codigo[p])
				else:
					estado = 46

		if(estado == 42):
			if ((p == ult_position)):
				estado = 48
			else:
				p=p+1

				if(codigo[p] == '='):
				 	estado = 49
				 	print_v.append(codigo[p])
				else:
					estado = 48

		if(estado == 43):
			if ((p == ult_position)):
				estado = 50
			else:
				p=p+1

				if(codigo[p] == '='):
				 	estado = 51
				 	print_v.append(codigo[p])
				else:
					estado = 50

		if(estado == 44):
			if(codigo[p] == '<'):
				for z in print_v:
					print(z, end='')
				print(" -> Operador Relacional")
				print_v.clear()
				break
			else:
				p=p-1
				for z in print_v:
					print(z, end='')
				print(" -> Operador Relacional")
				print_v.clear()
				if (p == ult_position):
					break
				else:
					p=p+1
					estado = 0


		if(estado == 45):
			for z in print_v:
				print(z, end='')
			print(" -> Operador Relacional")
			print_v.clear()
			if (p == ult_position):
				break
			else:
				p=p+1
				estado = 0
			
		if(estado == 46):
			if(codigo[p] == '>'):
				for z in print_v:
					print(z, end='')
				print(" -> Operador Relacional")
				print_v.clear()
				break
			else:
				p=p-1
				for z in print_v:
					print(z, end='')
				print(" -> Operador Relacional")
				print_v.clear()
				if (p == ult_position):
					break
				else:
					p=p+1
					estado = 0

		if(estado == 47):
			for z in print_v:
				print(z, end='')
			print(" -> Operador Relacional")
			print_v.clear()
			if (p == ult_position):
				break
			else:
				p=p+1
				estado = 0
			
		if(estado == 48):
			if(codigo[p] == '!'):
				for z in print_v:
					print(z, end='')
				print(" -> Operador Lógico")
				print_v.clear()
				break
			else:
				p=p-1
				for z in print_v:
					print(z, end='')
				print(" -> Operador Lógico")
				print_v.clear()
				if (p == ult_position):
					break
				else:
					p=p+1
					estado = 0

		if(estado == 49):
			for z in print_v:
				print(z, end='')
			print(" -> Operador Relacional")
			print_v.clear()
			if (p == ult_position):
				break
			else:
				p=p+1
				estado = 0
			
		if(estado == 50):
			if(codigo[p] == '='):
				for z in print_v:
					print(z, end='')
				print(" -> Operador de Atribuição")
				print_v.clear()
				break
			else:
				p=p-1
				for z in print_v:
					print(z, end='')
				print(" -> Operador de Atribuição")
				print_v.clear()
				if (p == ult_position):
					break
				else:
					p=p+1
					estado = 0

		if(estado == 51):
			for z in print_v:
				print(z, end='')
			print(" -> Operador Relacional")
			print_v.clear()
			if (p == ult_position):
				break
			else:
				p=p+1
				estado = 0
			
		if(estado == 52):
			for z in print_v:
				print(z, end='')
			print(" -> Operador Aritimético")
			print_v.clear()
			if (p == ult_position):
				break
			else:
				p=p+1
				estado = 0
			
		if(estado == 53):
			for z in print_v:
				print(z, end='')
			print(" -> Operador Aritimético")
			print_v.clear()
			if (p == ult_position):
				break
			else:
				p=p+1
				estado = 0
			
		if(estado == 54):
			for z in print_v:
				print(z, end='')
			print(" -> Operador Aritimético")
			print_v.clear()
			if (p == ult_position):
				break
			else:
				p=p+1
				estado = 0
			
		if(estado == 55):
			for z in print_v:
				print(z, end='')
			print(" -> Operador Aritimético")
			print_v.clear()
			if (p == ult_position):
				break
			else:
				p=p+1
				estado = 0
			
		if(estado == 56):
			if(codigo[p] == '/'):
				for z in print_v:
					print(z, end='')
				print(" -> Operador Aritimético")
				print_v.clear()
				break
			else:
				p=p-1
				for z in print_v:
					print(z, end='')
				print(" -> Operador Aritimético")
				print_v.clear()
				if (p == ult_position):
					break
				else:
					p=p+1
					estado = 0

		if(estado == 57):
			if ((p == ult_position)):
				estado = 56
			else:
				p=p+1

				if(codigo[p] == '/'):
				 	estado = 58
				 	print_v.append(codigo[p])
				else:
					estado = 56
		if(estado == 58):
			if(p == ult_position):
				for z in print_v:
					print(z, end='')
				print(" -> Comentário")
				print_v.clear()
				break
			else:
				p=p+1

				if(codigo[p] != '\n'):
				 	estado = 58
				 	print_v.append(codigo[p])
				else:
					estado = 59

		if(estado == 59):
			for z in print_v:
				print(z, end='')
			print(" -> Comentário")
			print_v.clear()
			if (p == ult_position):
				break
			else:
				p=p+1
				estado = 0

analisador('''int x = 2;
if(x==2){
	print("kaue brabo")
}else{
	print("kaue n é brabo :( ")
}''')