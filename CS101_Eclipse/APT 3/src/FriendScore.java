import java.util.*;

public class FriendScore {

	public int highestScore(String[] friends) {
		int twofriends = 0;

		for (int i = 0; i < friends.length; i++){

			Set<Integer> set = new HashSet<Integer>();

			for (int j = 0; j < friends.length; j++){
				if (friends[i].charAt(j) == 'Y'){
					set.add(j);	

					for (int k = 0; k < friends.length; k++){
						if (friends[j].charAt(k) == 'Y'){
							set.add(k);
						}
					}
				}
			}
			twofriends = Math.max(set.size() - 1, twofriends);
		}
		return twofriends;
	}
}
