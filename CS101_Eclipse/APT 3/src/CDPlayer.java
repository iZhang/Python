public class CDPlayer {
        public int isRandom(String[] songlist, int n) {
                String s = "";
                for (int i = 0; i < songlist.length; i++)
                        s += songlist[i];

                int i = 0;
                for (i = 0; i < n; i++) {
                        boolean[] used = new boolean[n];
                        int j;
                        for (j = 0; j < i; j++) {
                                if (used[s.charAt(j) - 'A'])
                                        break;
                                used[s.charAt(j) - 'A'] = true;
                        }
                        // System.out.println(i + " " + j);
                        if (j < i)
                                continue;
                        for (; j < s.length(); j++) {
                                if (j % n == i)
                                        used = new boolean[n];
                                if (used[s.charAt(j) - 'A'])
                                        break;
                                used[s.charAt(j) - 'A'] = true;
                        }
                        if (j < s.length())
                                continue;
                        return i;
                }
                return -1;
        }
}