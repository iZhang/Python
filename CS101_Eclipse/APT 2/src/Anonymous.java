import java.util.*;

public class Anonymous {
	public static void main(String[] args){
		Anonymous a = new Anonymous();
		String[] headlines = {"Earthquake in San Francisco ", " Burglary at musuem in Sweden ", " Poverty "};
		String[] messages = {"Give me my money back ", " I am the best coder ", " TOPCODER "};
		System.out.println(a.howMany(headlines, messages));
	}

	public int howMany(String[] headlines, String[] messages) {

		char[] alphabet = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
		HashMap<Character,Integer> availableletters = new HashMap<Character,Integer>();
		int possiblemessages = 0;
		
		for(String headline:headlines){
			for(int i =0; i<headline.length();i++){
				for(int j=0; j<alphabet.length;j++){
					if(Character.toLowerCase(headline.charAt(i))==alphabet[j]){
						if(availableletters.get(Character.toLowerCase(headline.charAt(i)))==null){
							availableletters.put(Character.toLowerCase(headline.charAt(i)), 1);
						}else{
							availableletters.put(Character.toLowerCase(headline.charAt(i)), availableletters.get(Character.toLowerCase(headline.charAt(i)))+1);
							}
						}
					}
				}
			}

//		System.out.println(availableletters);

		for(String message:messages){
			HashMap<Character,Integer> lettersneeded = new HashMap<Character,Integer>();

			for(int i =0; i<message.length();i++){
				for(int j=0; j<alphabet.length;j++){
					if(Character.toLowerCase(message.charAt(i))==alphabet[j]){
						if(lettersneeded.get(Character.toLowerCase(message.charAt(i)))==null){
							lettersneeded.put(Character.toLowerCase(message.charAt(i)), 1);
						}else{
						lettersneeded.put(Character.toLowerCase(message.charAt(i)), lettersneeded.get(Character.toLowerCase(message.charAt(i)))+1);	
						}
						}
					}
				}
			
//			System.out.println(lettersneeded);
			
			int count = 0;
			
			for(char letter:alphabet){
				if(lettersneeded.get(letter)!=null && availableletters.get(letter) != null){
					if(lettersneeded.get(letter)<=availableletters.get(letter)){
						count ++;
				}
			}
			}
			if(count==lettersneeded.size()){
				possiblemessages ++;
			}
		}
			return possiblemessages;
			
		}
	}