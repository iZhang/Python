import java.util.*;

public class GridGame {
    char[][] myGrid;
    public int winningMoves(String[] grid){
        myGrid = new char[4][4];
        int row = 0;
        for(String s : grid){
            for(int col = 0; col < 4; col++){
                myGrid[row][col] = s.charAt(col);
            }
            row++;
        }
        return winCount();
    }
    
    public int winCount(){
        int wins = 0;
        ArrayList<int[]> list = findLegalMoves();
        if (list.size() == 0) return 0;
        
        for(int[] a : list){
            myGrid[a[0]][a[1]] = 'X';

            if (winCount() == 0){
		    wins++;
	    }
	    myGrid[a[0]][a[1]] = '.';
        }
        return wins;
    }
    
    /**
     * Find legal moves on global myGrid and return a list of these
     * moves where each move is int[] with [0] = row and [1] = col
     * @return list of all open/legal moves in gridgame
     */
    private ArrayList<int[]> findLegalMoves(){
        ArrayList<int[]> list = new ArrayList<int[]>();
        for(int r=0; r < 4; r++){
            for(int c=0; c < 4; c++){
                if (myGrid[r][c] == '.' && neighborsClear(r,c)){
                    int[] t = new int[2];
                    t[0] = r; t[1] = c;
                    list.add(t);
                }
            }
        }
        return list;
    }
    /**
     * Return true if and only if myGrid[r][c] is a '.', i.e.,
     * returns false if not on board or an 'X'
     * @param r is row being checked
     * @param c is col being checked
     * @return true iff myGrid[r][c] == '.'
     */
    private boolean isDot(int r, int c){
        if (r >= 0 && r < 4 && c >= 0 && c < 4){
            return myGrid[r][c] == '.';
        }
        return true;
    }
    
    /**
     * return true if and only if myGrid[r][c] is open for a move, i.e.,
     * myGrid[r][c] is not adjacent to an 'X'
     * @param r is row being checked
     * @param c is col being checked
     * @return true iff myGrid[r][c] can hold an 'X', i.e., is not adjacent to an 'X'
     */
    
    private boolean neighborsClear(int r, int c) {
        return 
            isDot(r+1,c) &&
            isDot(r-1,c) &&
            isDot(r,c+1) &&
            isDot(r,c-1);
    }
    
    public static void main(String[] args){
        String[] s = {
                "....",
                "....",
                ".X..",
                "...."
        };
        GridGame gg = new GridGame();
        int w = gg.winningMoves(s);
        System.out.println(w);
    }
}