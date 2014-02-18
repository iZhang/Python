import java.util.*;

public class SimpleWordGame {
      public int points(String[] player, String[] dictionary) {
    	  int score = 0;
    	  Set<String> words = new LinkedHashSet<String>();
    	  for(String remembered:player){
    		  if(Arrays.asList(dictionary).contains(remembered)){
    		  words.add(remembered);
    		  }
    	  }

    	  for(String word:words){
    		  score += Math.pow(word.length(),2);
    	  }
      return score;
      }
}