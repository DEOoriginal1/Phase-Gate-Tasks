import java.util.Arrays;
public class ArraySorting{
	public static void main(String ... args){
	
	int[][] matrix = {{1,2,3},{4,5,6},{7,8,9}};
	
	int[][] result = multipleArrays(matrix);	
	
	System.out.println(Arrays.deepToString(result));
	
	}
	
	
	
	public static int[][] multipleArrays(int[][] numbers){
		int[][] result = new int [numbers.length][];	
		for(int index = 0; index < numbers.length; index++){
			result[index] = swap(numbers[index]);
		}
					return result ;
	}
		
		
		
		
	public static int[] swap(int[] numbers){
		int[] reverse = new int[numbers.length];
		for(int index = 0; index < numbers.length; index++){
			reverse[index] = numbers[numbers.length - 1 - index];
		}
				return reverse;
	}		
}
