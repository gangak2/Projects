
/**
 * Write a description of class Generation here.
 * 
 * @author (Gangaprasad Koturwar) 
 * @version (a version number or a date)
 */

import java.util.*;

public class Generation
{
    // instance variables - replace the example below with your own
    public Member[] members = new Member[1000];

    /**
     * Constructor for objects of class Generation
     */
    public Generation()
    {
        
    }

    /**
     * An example of a method - replace this comment with your own
     * 
     * @param  y   a sample parameter for a method
     * @return     the sum of x and y 
     */
    public void populateFirstGeneration(List<Tile> Tiles)
    {
        for(int i=0;i<1000;i++)
        {
            java.util.Collections.shuffle(Tiles);
            this.members[i] = new Member();
            this.members[i].fillBoard(Tiles);
        }
    }
    
    public Member[] sortHealthwise()
    {
        java.util.Arrays.sort(members, new Comparator<Member>()
                                                {
                                                    @Override
                                                    public int compare(Member m1, Member m2)
                                                    {
                                                        return m2.health-m1.health;
                                                    }
                                                }
                                                );
       return members;
    }
    
    public double averageHealthOfGeneration()
    {
        int hlth_sum=0;
        for(int i=0;i<1000;i++)
        {
            hlth_sum+=this.members[i].health;
        }
        return hlth_sum*1.0/1000;
    }
    
    
}
