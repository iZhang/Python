import java.util.*;

public class Dirsort {
	public String[] sort(String[] dirs) {
		ArrayList<Directory> directories = new ArrayList<Directory>();
		ArrayList<String> directories2 = new ArrayList<String>();

		for(String dir:dirs){
			directories.add(new Directory(dir));
		}

		Collections.sort(directories);

		for(Directory element:directories){
			directories2.add(element.toString());
		}
		String[] arr = directories2.toArray(new String[directories2.size()]);
		return arr;
	}

	public class Directory implements Comparable<Directory>{

		String superdirectory;

		public Directory(String directory){
			superdirectory = directory;
		}

		public String toString(){
			return superdirectory;
		}

		@Override
		public int compareTo(Directory other) {
			int superdashcount = 0;
			for(int i=0;i<superdirectory.length();i++){
				if(superdirectory.charAt(i)=='/'){
					superdashcount ++;
				}
			}

			int otherdashcount = 0;
			for(int i=0;i<other.superdirectory.length();i++){
				if(other.superdirectory.charAt(i)=='/'){
					otherdashcount ++;
				}
			}

			if(superdashcount < otherdashcount){
				return -1;
			}
			if(superdashcount > otherdashcount){
				return 1;
			}
			if(superdashcount == otherdashcount){
				return superdirectory.compareTo(other.superdirectory);
			}
			return 0;
		}
	}
}

