import java.util.*;

public class SortedFreqs {

	public int[] freqs(String[] data) {

		Arrays.sort(data);
		
		ArrayList<String> set = new ArrayList<String>();
		
		for(int i=0;i<data.length;i++){
			if(set.contains(data[i])==false){
				set.add(data[i]);
			}
		}
		
		ArrayList<Integer> frequency = new ArrayList<Integer>();

		int freq = 0;
		for(String word:set){
			for(int i=0;i<data.length;i++){
				if(word.equals(data[i])){
					freq ++;
				}
			}
			frequency.add(freq);
			freq = 0;
		}

		int [] frequencies = new int[set.size()];

		for(int i = 0; i<frequencies.length;i++){
			frequencies[i] = frequency.get(i);
		}
		return frequencies;
	}
}