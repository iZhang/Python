import java.util.*;

public class PrefixCode { 
	public String isOne(String[] words) {
		String no = "No, %d";
		for(int i=0;i<words.length;i++){
			for(int j=0;j<words.length;j++){
				if(words[i].length() < words[j].length()){
					if(words[i].equals(words[j].substring(0,words[i].length()))){
						return String.format(no, i);
					}
				}
		}
		}
	return "Yes";
	}
}