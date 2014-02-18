import java.util.*;

public class FamilyTree {
	private HashMap<String, Integer> name2id;
	private boolean[][] parent;
	private boolean[][] desc;
	private boolean[][] diff;

	private int[] gender;
	private int[] color;
	ArrayList<String> names = new ArrayList<String>();

	private boolean colordfs(int i, int c) {
		if (color[i] != 0) {
			return (color[i] == c);
		}
		color[i] = c;
		for (int j = 0; j < parent.length; j++) {
			if (diff[i][j]) {
				if (!colordfs(j, 3 - c)) {
					return false;
				}
			}
		}
		return true;
	}

	private boolean checkAndUpdate() {
		for (int i = 0; i < parent.length; i++) {
			int count = 0;
			int tmp = -1;

			for (int j = 0; j < parent.length; j++) {
				if (parent[i][j]) {
					count++;
					if (tmp == -1) {
						tmp = j;
					} else {
						diff[tmp][j] = true;
						diff[j][tmp] = true;
					}

					if (desc[j][i] || (i == j)) {
						return false;
					}
				}
			}

			if (count > 2) {
				return false;
			}
		}

		for (int i = 0; i < parent.length; i++) {
			color[i] = 0;
		}
		for (int i = 0; i < parent.length; i++) {
			if (gender[i] != 0) {
				if (!colordfs(i, gender[i])) {
					return false;
				}
			}
		}
		for (int i = 0; i < parent.length; i++) {
			if (color[i] == 0) {
				if (!colordfs(i, 1)) {
					return false;
				}
			}
		}

		for (int i = 0; i < parent.length; i++) {
			for (int j = 0; j < parent.length; j++) {
				desc[i][j] = parent[i][j];
			}
		}

		for (int k = 0; k < parent.length; k++) {
			for (int i = 0; i < parent.length; i++) {
				for (int j = 0; j < parent.length; j++) {
					desc[i][j] |= (desc[i][k] && desc[k][j]);
				}
			}
		}

		return true;
	}

	public int firstBad(String[] data) {
		name2id = new HashMap<String, Integer>();

		for (int i = 0; i < data.length; i++) {
			Scanner scanner = new Scanner(data[i]);
			while (scanner.hasNext()) {
				String name = scanner.next();
				if (name.equals("m") || name.equals("f")) {
					continue;
				}
				if (name2id.containsKey(name)) {
					continue;
				}
				int id = name2id.size();
				name2id.put(name, id);
				names.add(name);
			}
		}

		parent = new boolean[name2id.size()][name2id.size()];
		desc = new boolean[name2id.size()][name2id.size()];
		diff = new boolean[name2id.size()][name2id.size()];
		gender = new int[name2id.size()];
		color = new int[name2id.size()];

		for (int i = 0; i < data.length; i++) {
			Scanner scanner = new Scanner(data[i]);
			String first = scanner.next();
			String second = scanner.next();

			if (second.equals("m") || second.equals("f")) {
				boolean isMale = second.equals("m");
				int which = name2id.get(first);

				if (gender[which] != 0) {
					if (isMale != (gender[which] == 1)) {
						return i;
					}
				}
				gender[which] = isMale ? 1 : 2;
			} else {
				parent[name2id.get(first)][name2id.get(second)] = true;
			}

			if (!checkAndUpdate()) {
				return i;
			}
		}

		return -1;
	}
}