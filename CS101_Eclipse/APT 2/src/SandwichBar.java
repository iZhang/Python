import java.util.*;

public class SandwichBar{
	public int whichOrder(String[] available, String[] orders){

		for(int i=0;i<orders.length;i++){

			boolean isSubset = Arrays.asList(available).containsAll(Arrays.asList(orders[i].split(" ")));
			if(isSubset==true){
				return i;
			}
		}
		return -1;
	}
}