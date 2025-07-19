from ast import Break

print("\n\nTicket Booking System\n")
restart = ('Y')
#ps = "Passenger"
while restart != ('N','NO','n','no'):
	print()
	Name = str(input("Enter your Name: "))
	Email = input("Enter your Emailid: ")
	Number = int(input("Enter your Mobile Number: "))
	print("\nYour Account has been created!!!")
	print("\nSelect the option from below")
	print()
	print("1.Check PNR status")
	print("2.Ticket Reservation")
	print("3.Cancel ticket")
	print("4.Seats availability")
	print()
	option = int(input("\nEnter your option: "))

	if option == 1:
		print("Your PNR status is t3")
		exit(0)

	elif option == 2:
		people = int(input("\nEnter no. of Ticket you want: "))
		name_x = []
		age_y = []
		sex_z = []
		for p in range(people):
			name = str(input("\nName: "))
			name_x.append(name)
			age  = int(input("\nAge : "))
			age_y.append(age)
			sex  = str(input("\nMale or Female: "))
			sex_z.append(sex)
		
		restart = str(input("\nDid you forgot someone? y/n: "))
		if restart in ('y','YES','yes','Yes'):
			restart = ('Y')
		else :
			x = 0
			print("\nTotal Ticket: ",people)
			for p in range(1,people+1):
				print("Ticket: ",p)
				print("Name: ", name_x[x])
				print("Age: ", age_y[x])
				print("Sex: ",sex_z[x])
				x += 1
		exit(0)

	elif option == 3:
		int(input("Enter your Ticket Serial number: "))
		# print("\nEnter your Ticket Serial number:")
		print("Do you want to cancel the ticket??")
		ps=input()
		# if ps == ['y' or 'Y' or 'Yes' or 'yes' or 'YES']:
		print("Enter your reason")
		ps=input()
		print("Half of the amount wiil be refunded")
		print("Click 'Y' if it is Okay")
		ps=input()
		print("Your Ticket cancelled Succesfully.")
		# elif ps == ['n' or 'N' or 'NO' or 'no' or 'No']:
		# print("Your Ticket has not been cancelled.")

		# restart = str(input("\nDo you want to continue? y/n: "))
		# if restart in ('y','YES','yes','Yes'):
		# 	restart = ('Y')
		exit(0)
	elif option == 4:
		Train_number = int(input("\nEnter your Train number: "))
		Seat_number =int(input("\nEnter your Seat number: "))
		
		if Seat_number < 200:
			print("Seats are Availbale")
		else:
			Break("Sorry...No seats available")
		exit(0)