
/**
 * Class Evolution
 * current_generation : Evolution is defined by the current surviving generation
 * 
 * methods:
 * simulateEvolution() : 
 * 
 * @author (Gangaprasad Koturwar) 
 * @version (a version number or a date)
 */
import java.util.*;
import java.io.*;

public class Evolution
{
    // instance variables - replace the example below with your own
    public Generation current_generation = new Generation();
    public GeneticAlgorithms algo = new GeneticAlgorithms();
    
    /**
     * Constructor for objects of class Evolution
     */
    public Evolution()
    {
        //Read the tiles from the text file
        List<Tile> genes = new ArrayList<Tile>(256);
        
        Scanner scanner = null;
        try
        {
            scanner = new Scanner(new File("Tiles.txt"));
            for(int i=0;i<256;i++)
            {
                Tile tmp = new Tile();
                tmp.north = scanner.nextInt();
                tmp.east = scanner.nextInt();
                tmp.south = scanner.nextInt();
                tmp.west = scanner.nextInt();
                genes.add(tmp);
            }
        }
        catch(IOException ioe)
        {
            System.err.println("An IOException was caught!");
            ioe.printStackTrace();
        }
        
        current_generation.populateFirstGeneration(genes);
    }

    /**
     * An example of a method - replace this comment with your own
     * 
     * @param  y   a sample parameter for a method
     * @return     the sum of x and y 
     */
    public Member simulateEvolution(int gens)
    {
        //Examine if the best member is indeed a solution, if yes terminate else simulate evolutions
        Member[] eliteMembers = current_generation.sortHealthwise();
        if (eliteMembers[0].health == 480 && eliteMembers[0].properBoundaries || gens == 0)
        {
            return eliteMembers[0];
        }
        else
        {
            current_generation = algo.generateNextgeneration(current_generation);
            return simulateEvolution(gens--);
        }
    }
}
