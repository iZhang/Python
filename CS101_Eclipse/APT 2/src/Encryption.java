import java.util.*;
import java.io.*;

public class Encryption {
	public String encrypt(String message){
		
		HashMap<Character,Character> translation = new HashMap<Character,Character>();
		
		StringBuffer result = new StringBuffer();
		
		char[] alphabet = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
		
		int n = 0;
		
		for(int i=0;i<message.length();i++){
			if(translation.get(message.charAt(i)) !=null){
				n += 1;
			}
			if(translation.get(message.charAt(i)) == null){
				translation.put(message.charAt(i), alphabet[i-n]);
			}
		}
		for(int i=0;i<message.length();i++){
			result.append(translation.get(message.charAt(i)));
		}
		return result.toString();
	}
}