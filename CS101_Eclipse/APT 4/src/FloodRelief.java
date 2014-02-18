public class FloodRelief {
        private char[][] myGrid;
        private int myRows, myCols, minRows = -1, minCols = -1;
        private char min;

        public int minimumPumps(String[] heights){

                myRows = heights.length;
                myCols = heights[0].length();
                myGrid = new char[myRows][myCols];
                int ret = 0;
 
                for(int r =0; r < myRows; r++){
                        for(int c=0; c < myCols; c++){
                                myGrid[r][c] = heights[r].charAt(c);
                        }
                }
                while(detectLow()){
                        bFill(min,minRows,minCols);
                        ret++;
                }
                return ret;
        }

        public void bFill(char m, int row, int col){
                if(inRange(row,col)){
                        if(myGrid[row][col]!='*'&&myGrid[row][col]>=m){
                                char n = myGrid[row][col];
                                myGrid[row][col]='*';
                                bFill(n,row+1,col);
                                bFill(n,row-1,col);
                                bFill(n,row,col+1);
                                bFill(n,row,col-1);
                        }
                }
        }

        public boolean detectLow(){
                int i = myRows * myCols;
                min = '{';
                for(int r =0; r < myRows; r++){
                        for(int c=0; c < myCols; c++){
                                if(myGrid[r][c]=='*')i--;
                                else if(myGrid[r][c]<min){
                                        min=myGrid[r][c];
                                        minRows = r;
                                        minCols = c;
                                }
                        }
                }
                if(i == 0)return false;
                return true;
        }
        private boolean inRange(int row, int col) {
                return 0 <= row && row < myGrid.length && 0 <= col&& col < myGrid[0].length;
        }

        public static void main(String[] args){
                String[] args1={
                                "ccccccccccc",
                                 "caaaaaaaaac",
                                 "caaaaaaaaac",
                                 "caazpppzaac",
                                 "caapdddpaac",
                                 "caapdddpaac",
                                 "caapdddpaac",
                                 "caazpppzaac",
                                 "caaaaaaaaac",
                                 "caaaaaaaaac",
                                 "ccccccccccc"
                };
                FloodRelief ss = new FloodRelief();
                System.out.println(ss.minimumPumps(args1));
        }
}