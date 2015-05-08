
/**
 * A set of adjecent tiles forming a rectangle that represents the chromosome counterpart, this will be used for cross over
 * 
 * @author (Gangaprasad Koturwar) 
 * @version (a version number or a date)
 */
public class Chromosome
{
    // instance variables - replace the example below with your own
    public int height;
    public int width;
    public int posX;
    public int posY;
    public Tile[][] dna;

    /**
     * Constructor for objects of class Chromosome
     */
    public Chromosome()
    {
        
    }
    
    public Chromosome(Member mem, int hgt, int wdt, int pX, int pY)
    {
        this(hgt,wdt,pX,pY);
        System.out.println("outside " + hgt + " " + wdt + " " + pX + " " + pY);
        for(int i=0;i<hgt;i++)
        {
            for(int j=0;j<wdt;j++)
            {
                System.out.println("inside " + i + " " + j + " " + pX + " " + pY);
                this.dna[i][j] = mem.board[i+pX][j+pY];
            }
        }
    }
    
    public Chromosome(int hgt, int wdt, int pX, int pY)
    {
        this.height = hgt;
        this.width = wdt;
        this.posX = pX;
        this.posY = pY;
        this.dna = new Tile[hgt][wdt];
    }

    /**
     * An example of a method - replace this comment with your own
     * 
     * @param  y   a sample parameter for a method
     * @return     the sum of x and y 
     */
    
    
    
}
