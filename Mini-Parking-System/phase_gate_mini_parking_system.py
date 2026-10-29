def main():

	while True:
	
		menu = """
			===================================================
				WELCOME TO CATALYST PARKING LOT
			===================================================
			WHAT WOULD YOU LIKE TO DO TODAY?
		
			1. PARK MY CAR
			2. CHECK AVAILABLE SPACES
			3. TAKE MY CAR
			0. End
			"""
			
		user_choice  =  input(f"{menu} \nEnter Option: ")
		
		match user_choice:
		
			case "1": 
						park_car  =  input("Where would you like to park your car? ")
						
						
						print("Car Parked Successfully!", f"Your Car is parked in {account['account_number']}")
						
			case "2": 
						
						check_spaces  =  print(f"All Available Spaces are? \n{availabe_spaces()}")
						
						
						
						
			case "3": 
						take_car  =  input("Where did you park your car? ")
						print(f"Alright! You can Take you car. \n{availabe_spaces()}")
						

			
			case "0": 		break
			
			case _: 		print("Invalid input")
					
					



if __name__ == "__main__":

	main()

