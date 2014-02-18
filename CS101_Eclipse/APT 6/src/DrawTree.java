import java.util.*;
public class DrawTree {
          List<String> ls = new ArrayList<String>();
          int[] par;
          String[] ns;
          public String[] draw(int[] parents, String[] names) {
            par = parents; ns = names;
            addChildren(-1, "");
            return ls.toArray(new String[0]);
          }
          public void addChildren(int up, String prefix) {
            int n = 0;
            for(int i=par.length;i-->0;) if(par[i]==up) n++;
            for(int i=0; i<par.length;i++) {
              if(par[i] != up) continue;
              n--;
              ls.add(prefix + "+-" + ns[i]);
              addChildren(i, prefix + (n==0 ? "  " : "| "));
            }
          }
}