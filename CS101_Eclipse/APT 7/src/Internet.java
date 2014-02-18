import java.util.*;

public class Internet {

	Set<Integer> mySet = new HashSet<Integer>();
	Set<Integer> visited = new HashSet<Integer>();
	ArrayList<Set<Integer>> list = new ArrayList<Set<Integer>>();
	int num = 0;

	public int articulationPoints(String[] routers){

		Set<Integer> routerSet = new HashSet<Integer>();

		for(int i = 0; i < routers.length; i++){
			Set<Integer> connections = new HashSet<Integer>();

			String[] split = routers[i].split(" ");
			for(String s : split){
				routerSet.add(Integer.parseInt(s));
				connections.add(Integer.parseInt(s));
			}
			list.add(connections);
		}

		num = routerSet.size();

		int count = 0;
		for(int i = 0; i < list.size(); i++){
			mySet.clear();
			visited.clear();
			if(i == 0) {
				visited.add(i + 1);
				helper(list.get(i + 1), i + 1, i);
			}
			else {
				visited.add(i - 1);
				helper(list.get(i - 1),i - 1, i);
			}
			if (mySet.size() != (routerSet.size()-1)){
				count++;
			}
		}

		return count;
	}

	private void helper(Set<Integer> s, int i, int k){
		if(mySet.size() != (num - 1)){
			mySet.add(i);
			mySet.addAll(s);
			mySet.remove(k);
			for (Integer num : s){
				if(!visited.contains(num) && num != k){
					visited.add(num);
					helper(list.get(num),num,k);
				}
			}
		}
	}
}