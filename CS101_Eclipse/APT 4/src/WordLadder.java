public class WordLadder {
        StringWrap[] strList;
        boolean first;

        private class StringWrap {
                String str;
                boolean used;

                public StringWrap(String str) {
                        this.str = str;
                        this.used = false;
                }

                public boolean similar(StringWrap temp) {
                        String t = temp.str;
                        int cnt = 0;
                        for (int i = 0; i < t.length(); i++) {
                                if (t.charAt(i) != str.charAt(i))
                                        cnt++;
                        }
                        return cnt == 1;
                }
        }

        public boolean solve(StringWrap from, StringWrap to) {
                if (from.similar(to) && first)
                        return true;
                first = true;
                for (StringWrap cur : strList) {
                        if (from.similar(cur) && !cur.used) {
                                cur.used = true;
                                if (solve(cur, to))
                                        return true;
                                else
                                        cur.used = false;
                        }
                }
                return false;
        }

        public String ladderExists(String[] words, String from, String to) {
                strList = new StringWrap[words.length];
                first = false;
                for (int i = 0; i < strList.length; i++) {
                        strList[i] = new StringWrap(words[i]);
                }
                return solve(new StringWrap(from), new StringWrap(to)) ? "ladder"
                                : "none";
        }
}