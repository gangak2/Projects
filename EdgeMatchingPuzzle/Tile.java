
/**
 * Write a description of class Tile here.
 * 
 * @author (Gangaprasad Koturwar) 
 * @version (a version number or a date)
 */
public class Tile
{
    // instance variables - replace the example below with your own
    public int north,east,west,south;

    /**
     * Constructor for objects of class Tile
     */
    public Tile()
    {
        
    }
    
    public Tile(int n, int e, int s, int w)
    {
        this.north = n;
        this.east = e;
        this.west = w;
        this.south = s;
    }

    /**
     * An example of a method - replace this comment with your own
     * 
     * @param  y   a sample parameter for a method
     * @return     the sum of x and y 
     */
    public void rotateClockwise()
    {
        int tmp = this.north;
        this.north = this.west;
        this.west = this.south;
        this.south = this.east;
        this.east = tmp;
    }
    
    public void rotateAntiClockwise()
    {
        int tmp = this.north;
        this.north = this.east;
        this.east = this.south;
        this.south = this.west;
        this.west = tmp;
    }
}
