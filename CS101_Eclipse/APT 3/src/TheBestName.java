import java.util.*;

public class TheBestName{

	public String[] sort(String[] names) {
		ArrayList<Name> list = new ArrayList<Name>();
		ArrayList<String> list2 = new ArrayList<String>();
		for (String s: names){
			list.add(new Name(s));
		}

		Collections.sort(list);
		for(Name element:list){
			list2.add(element.toString());
		}

		String[] arr = list2.toArray(new String[list2.size()]);
		return arr;
	}

	public class Name implements Comparable<Name>{

		String supername;

		public Name(String name){
			supername = name;
		}

		public String toString(){
			return supername;
		}


		@Override
		public int compareTo(Name other) {
			int sum = 0;
			for(int i=0;i<supername.length();i++){
				int value = supername.charAt(i) - 64;
				sum += value;
			}
			int sum2 = 0;
			for(int i=0;i<other.supername.length();i++){
				int value = other.supername.charAt(i) - 64;
				sum2 += value;
			}

			if(supername.equals("JOHN")){
				return -1;
			}
			
			if(other.supername.equals("JOHN")){
				return 1;
			}

			if(sum > sum2){
				return -1;
			}

			if(sum < sum2){
				return 1;
			}

			if(sum == sum2){
				return supername.compareTo(other.supername);
			}
			return 0;
		}
	}
}