import java.util.*; 
public class IsomorphicWords {

	public static void main(String[] args){
		IsomorphicWords a = new IsomorphicWords();
		String[] words = {"aa", "ab", "bb", "cc", "cd" };
		System.out.println(a.countPairs(words));
	}
	
	public int countPairs(String[] words) {
		int isomorphic =0;

		for(int i=0;i<words.length;i++){

			for(int j=0;j<words.length;j++){

				HashMap<Character,Character> key = new HashMap<Character,Character>();
				StringBuffer translated = new StringBuffer();

				if(words[i].length() == words[j].length()){
					
					if(i!=j){
						
						for(int k=0;k<words[i].length();k++){
							//make sure only one key can be assigned to a value
							if(!key.containsValue(words[j].charAt(k))){
								key.put(words[i].charAt(k),words[j].charAt(k));
						}
						}
						
						for(int k=0;k<words[i].length();k++){
							if(key.get(words[i].charAt(k))!=null){
								translated.append(key.get(words[i].charAt(k)));
							}
						}
					}
					}

//				System.out.println(key);
//				System.out.println(translated.toString());
//				System.out.println(words[j]);
				
				if(translated.toString().equals(words[j])){
					isomorphic ++;
//					System.out.println("Equal");
				}
			}
		}
		return isomorphic/2;
	}
}