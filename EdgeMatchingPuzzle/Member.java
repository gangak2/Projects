import java.util.*;

/**
 * Write a description of class Member here.
 * 
 * @author (Gangaprasad Koturwar) 
 * @version (a version number or a date)
 */
public class Member
{
    // instance variables - replace the example below with your own
    public Tile[][] board = new Tile[16][16];
    public int health=0;
    public boolean properBoundaries=true;

    /**
     * Constructor for objects of class Member
     */
    public Member()
    {
        
    }

    /**
     * An example of a method - replace this comment with your own
     * 
     * @param  y   a sample parameter for a method
     * @return     the sum of x and y 
     */
    public void fillBoard(List<Tile> tilesPermutation)
    {
        for(int i=0;i<16;i++)
        {
            for(int j=0;j<16;j++)
            {
                this.board[i][j] = tilesPermutation.get(16*i+j);
            }
        }
        computeHealthParameters(tilesPermutation);
    }
    
    public void computeHealthParameters(List<Tile> tilesPermutation)
    {
        //Computing health and checking whether boundary was properly formed
        int boundary = board[0][0].north;
        for(int i=0;i<16;i++)
        {
            for(int j=0;j<16;j++)
            {
                if(i==0)
                {
                    if(j<15)
                    {
                        if(board[i][j].east == board[i][j+1].west)
                        {
                            this.health++;
                        }
                        if(board[i][j].north != boundary)
                        {
                            this.properBoundaries = false;
                        }
                    }  
                }
                else
                {
                    if(j<15)
                    {
                        if(board[i][j].east == board[i][j+1].west)
                        {
                            this.health++;
                        }
                    }
                    if(board[i][j].north == board[i-1][j].south)
                    {
                        this.health++;
                    }
                    if(j==0 && board[i][j].west != boundary)
                    {
                        this.properBoundaries = false;
                    }
                    if(j==15 && board[i][j].east != boundary)
                    {
                        this.properBoundaries = false;
                    }
                    if(i==15 && board[i][j].south != boundary)
                    {
                        this.properBoundaries = false;
                    }
                }
            }
        }
        
    }
    
    
}
