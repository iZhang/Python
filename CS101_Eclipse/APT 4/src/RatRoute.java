public class RatRoute {
        String[] map;
        
        public int findRoute(int x, int y, int end_x, int end_y) {
                if (x== end_x && y==end_y) {
                        return 1;
                }
                if (map[y].charAt(x) == 'X')
                        return 0;
                int route = 0;
                if (end_x > x)
                         route += findRoute(x+1, y, end_x, end_y);
                if (end_x < x)
                         route += findRoute(x-1, y, end_x, end_y);
                if (end_y > y)
                         route += findRoute(x, y+1, end_x, end_y);
                if (end_y < y)
                         route += findRoute(x, y-1, end_x, end_y);
                
                return route;
        }
        
        public int numRoutes(String[] enc) { 
                map = enc;
                int start_x = 0, start_y = 0, end_x = 0, end_y = 0;
                for (int i = 0; i < enc.length; i++) 
                        for (int j = 0; j < enc[0].length(); j++) {
                                if (enc[i].charAt(j) == 'R') {
                                        start_x = j;
                                        start_y = i;
                                }
                                if (enc[i].charAt(j) == 'C') {
                                        end_x = j;
                                        end_y = i;
                                }
                        }
                return findRoute(start_x, start_y, end_x, end_y);
        }
}