import java.util.*;

public class AllWordLadders {
    Map<String, int[]> myMap;
    Set<String> used;       
    String to;
    String[] words;
    
    public int[] solve(String[] words, String from, String to) {
        myMap = new HashMap<String, int[]>();
        used = new TreeSet<String>();
        this.to = to;
        this.words = words;
        
        //find first rungs
        Queue<String> currentRungs = new LinkedList<String>();
        for (String s: words){
            if (oneAway(from, s)){
                currentRungs.add(s);
                used.add(s);
                int[] temp = new int[2];
                temp[0] = 1; //initial length of the route
                temp[1] = 1; //no. of words point to it on the route from the beginning
                myMap.put(s, temp);             
            }
        }
        
        String lastRung = findRoute(currentRungs);
        if (lastRung.equals("")){
            int[] temp = new int[2];  //when there is no ladder
            temp[0]=temp[1]=0;
            return temp;
        }       
        return myMap.get(lastRung);     
    }
    
    /**
     * Called to find the shortest path, record the length and the route during searching
     * @param q is the rungs in current hop
     * @return the last rung
     */
    
    public String findRoute(Queue<String> q){
        //mark all the rungs in this level as used
        Iterator<String> it = q.iterator();
        if (!it.hasNext()) return "";
        while(it.hasNext()){
            used.add(it.next());
        }
        
        Queue<String> nextRungs = new LinkedList<String>();
        while (q.size()!=0){
            String current = q.remove();
            
            //base case
            if (oneAway(current, to)){
                myMap.get(current)[0]+=2;  //include length of itself and the to word
                while (q.size()!=0){
                    String s =q.remove();
                    if (oneAway(s, to)){
                        myMap.get(current)[1] += myMap.get(s)[1];                       
                    }                                       
                }
                return current;
            }
            
            //find next level's rungs, store in maps and update the length and route
            for (String s : words) {
                if (!used.contains(s) && oneAway(current, s)) {
                    if (!myMap.containsKey(s)) {
                        nextRungs.add(s);
                        int[] temp = new int[2];
                        temp[0] = myMap.get(current)[0] + 1; // add length
                        temp[1] = myMap.get(current)[1]; // pass the route no.                      
                        myMap.put(s, temp);
                    } else {
                        myMap.get(s)[1] += myMap.get(current)[1]; //pass the route no.                      
                    }
                }
            }
        }       
        return findRoute(nextRungs);
    }

    /**
     * Check if the two strings have distance of 1 
     * @param from
     * @param to
     * @return whether the distance equals to 1
     */
    private boolean oneAway(String from, String to) {
        if (from.length() != to.length())
            return false;

        int diff = 0;
        for (int k = 0; k < from.length(); k++) {
            if (from.charAt(k) != to.charAt(k))
                diff++;
        }
        return diff == 1;
    }
}