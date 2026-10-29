import java.util.Arrays;
import java.util.Scanner;
public class MiniParkingSystem{
	public static void main(String ... args){
	Scanner input = new Scanner(System.in);
	
	char[] park = new char[20];
		
		boolean parkSpace = true;
		
		

      System.out.println("""
===============================================================
                 WELCOME TO CATALYST PARKING LOT
===============================================================
			1. PARK MY CAR
			2. CHECK AVAILABLE SPACES
			3. TAKE MY CAR
			0. End
              
              """);
     System.out.println("Select One: ");
	int menu = input.nextInt();


		switch(menu){
	  
	  case 1 -> {
	  	for(int row = 0; row < park.length; row++){
	  		park[row] = 0;
	  	}
	  	for (int row = 0; row < park.length; row++) {
                System.out.print(park[row]+ " ");
            }
            	System.out.println();
            	
            	boolean parkingLot = true;
            	while(parkingLot){
	  	System.out.print("Enter where you want to park (1-20): ");
        	int parked = input.nextInt();
        	
        	int index = parked - 1;       	
	  	
	  	if (parked >= 0 && parked <= 20) {
	  		if(park[index] == 0){
	  			park[index] = 1;
	  		System.out.print("Updated parking lot.");
	  	for(int count = 0; count < park.length; count++){
	  		System.out.print(park[count] + " ");
	  	}
	  		System.out.println();
	  		}
	  		else{
	  		System.out.println("No Spaces!");
	  		}
	  	}
	  		else{
	  		System.out.println("Invalid!");
	  		}
	  		if(parked == 0){
	  			parkingLot = false;
	  		}
	  	}
	  }
	  	case 2 -> System.out.println("CHECK AVAILABLE SPACES");
       	        case 3 -> System.out.println("TAKE MY CAR");
       	        case 0 -> parkSpace = false;
	        default -> System.out.println("Invalid!");
	  		
	  	
	  	
	  	
	  	}
	}
	
	

}
