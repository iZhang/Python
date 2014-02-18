import java.util.*;

public class GalaxyTrip 
{
	Map<String, List<String>> myGraph = new TreeMap<String, List<String>>();

	public int[] possibleValues(String[] dependencies) 
	{
		//Map<String, List<String>> myGraph = new TreeMap<String, List<String>>();
		int vertex = 0;
		for(String s : dependencies)
		{
			String sv = ""+vertex;
			vertex++;

			List<String> list = new ArrayList<String>();
			myGraph.put(sv, list);

			if (s.equals("")) continue;           // no vertices, don't parse
			String[] a = s.split(" ");

			for (String nextv : a)
			{
				list.add(nextv);
			}
		}

		List<Integer> sizes = new ArrayList<Integer>();

		for (int k = 0; k < dependencies.length; k++)
		{
			int s = dfs(k+"");
			if (s != 0)
			{
				sizes.add(s);
			}
		}

		boolean[] possible = new boolean[100];
		possible[0] = true;

		for (int p = 0; p < sizes.size(); p++)
		{
			for (int k = possible.length-1; k >= 0; k--)
			{
				if (possible[k])
				{
					possible[k+sizes.get(p)] = true;
				}
			}
		}

		List<Integer> answer = new ArrayList<Integer>();

		for (int i =1; i <= dependencies.length; i++)
		{
			if (possible[i])
			{
				answer.add(i);
			}
		}

		int[] answerArray = new int[answer.size()];

		for (int k = 0; k < answer.size(); k++)
		{
			answerArray[k] = answer.get(k);
		}

		return answerArray;
	}

	Set<String> myVisited = new TreeSet<String>();
	private int dfs(String vertex)
	{	
		if (myVisited.contains(vertex)) return 0;

		myVisited.add(vertex);

		int total = 1;   // count myself

		for(String adj : myGraph.get(vertex))
		{
			total += dfs(adj);
		}

		return total;
	}

}