import java.util.*;

public class MedalTable {
	public String[] generate(String[] results) {

		ArrayList<Medal> medalvalues = new ArrayList<Medal>();

		HashMap<String, int[]> medals = new HashMap<String, int[]>();
		String[] result = new String[3];

		for(String element:results){
			result = element.split(" ");
			if(!medals.containsKey(result[0]))
				medals.put(result[0], new int[3]);
			if(!medals.containsKey(result[1]))
				medals.put(result[1], new int[3]);
			if(!medals.containsKey(result[2]))
				medals.put(result[2], new int[3]);
			int[] g=medals.get(result[0]);
			g[0]=g[0]+1;
			medals.put(result[0], g);
			
			int[] s=medals.get(result[1]);
			s[1]=s[1]+1;
			medals.put(result[1], s);
			
			int[] b=medals.get(result[2]);
			b[2]=b[2]+1;
			medals.put(result[2], b);
		}
		medalvalues.clear();
		//assume medals counts are correct
		for(String c: medals.keySet())
		{
			medalvalues.add(new Medal(c,medals.get(c)));
		}
		Collections.sort(medalvalues);
		Collections.reverse(medalvalues);
		String[] output=new String[medalvalues.size()];
		for(int x=0;x<medalvalues.size();x++)
		{
			output[x]=medalvalues.get(x).toString();
		}
		return output;
	}

	public class Medal implements Comparable<Medal>{
		public String country;
		public int gold;
		public int silver;
		public int bronze;

		public Medal(String medal, int[] medalcounts){
			country=medal;
			gold=medalcounts[0];
			silver=medalcounts[1];
			bronze=medalcounts[2];
		}

		public String toString(){
			return country+" "+gold+" "+silver+" "+bronze;
		}

		@Override
		public int compareTo(Medal other) {

			///return -1 if this is less than other
			if(this.gold<other.gold)
				return -1;
			if(this.gold>other.gold) return 1;
				
			if(this.silver<other.silver)
				return -1;
			if(this.silver>other.silver) return 1;
			
			if(this.bronze<other.bronze)
				return -1;
			if(this.bronze>other.bronze) return 1;
			
			return -this.country.compareTo(other.country);
		}
	}
}





