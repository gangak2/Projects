
/**
 * Write a description of class GeneticAlgorithms here.
 * 
 * @author (Gangaprasad Koturwar) 
 * @version (a version number or a date)
 */

import java.util.*;
import java.util.Random;

public class GeneticAlgorithms
{
    // instance variables - replace the example below with your own
    public Generation next = new Generation();
    public List<Integer> memberseeds = new ArrayList<Integer>();
    public List<Integer> tileseeds = new ArrayList<Integer>();

    /**
     * Constructor for objects of class GeneticAlgorithms
     */
    public GeneticAlgorithms()
    {
        for(int i=0;i<1000;i++)
        {
            memberseeds.add(i);
        }
        
        for(int i=0;i<256;i++)
        {
            tileseeds.add(i);
        }
    }

    /**
     * An example of a method - replace this comment with your own
     * 
     * @param  y   a sample parameter for a method
     * @return     the sum of x and y 
     */
    public Generation generateNextgeneration(Generation current)
    {
        Member[] eliteMembers = current.sortHealthwise();
        elitism(eliteMembers);
        mutation(current);
        crossover(current);
        return next;
    }
    
    public void elitism(Member[] current)
    {
        //Copy first 100 elite members as it is to next generation
        for(int i=0; i<100; i++)
        {
            next.members[i] = new Member();
            next.members[i] = current[i];
        }
    }
    
    public void mutation(Generation current)
    {
        //Generate the next 600 members through mutation
        java.util.Collections.shuffle(memberseeds);
        for(int i=0;i<600;i++)
        {
            java.util.Collections.shuffle(tileseeds);
            for(int k=0;k<50;k++)
            {
                int x = tileseeds.get(k)/16;
                int y = tileseeds.get(k)%16;
                int selmem = memberseeds.get(i);
                int tilePosStrength = mutationTilePositionStrength(current, selmem, x, y);
                for(int j=0;j<4;j++)
                {
                    System.out.println("TEST : " + selmem + " " + x + " " + y);
                    current.members[selmem].board[x][y].rotateClockwise();
                    if(mutationTilePositionStrength(current, selmem, x, y) >= tilePosStrength)
                    {
                        break;
                    }
                }
            }
            next.members[i+100] = new Member();
            next.members[i+100] = current.members[i];
        }
    }
    
    public int mutationTilePositionStrength(Generation current, int seed, int x, int y)
    {
        int strength = 0;
        if(x+1 < 16 && current.members[memberseeds.get(seed)].board[x][y].east == current.members[memberseeds.get(seed)].board[x+1][y].west)
        {
            strength++;
        }
            
        if(y+1 < 16 && current.members[memberseeds.get(seed)].board[x][y].south == current.members[memberseeds.get(seed)].board[x][y+1].north)
        {
            strength++;
        }
        
        if(x > 0 && current.members[memberseeds.get(seed)].board[x][y].west == current.members[memberseeds.get(seed)].board[x-1][y].east)
        {
            strength++;
        }
        
        if(y > 0 && current.members[memberseeds.get(seed)].board[x][y].north == current.members[memberseeds.get(seed)].board[x][y-1].south)
        {
            strength++;
        }
        
        return strength;
    }
    
    public void crossover(Generation current)
    {
        //Create the next 300 members using crossover
        java.util.Collections.shuffle(memberseeds);
        for(int k=0;k<300;k++)
        {
            int mem1 = memberseeds.get(k);
            int mem2 = memberseeds.get(999-k);
            boolean found = false;
            // Get a chromosome from member 1 to perform crossover with member 2
            Chromosome chr1 = selectChromosomeForCrossover(current.members[mem1]);
            for(int i=0;i<15-chr1.width;i++)
            {
                for(int j=0;j<15-chr1.height;j++)
                {
                    Chromosome chr2 = getChromosome(chr1,current.members[mem2]);
                    int strength = crossoverChromosomePositionStrength(chr2,current.members[mem2]);
                    placeChromosome(current.members[mem2],chr1,i,j);
                    if(crossoverChromosomePositionStrength(chr2,current.members[mem2]) > strength)
                    {
                        found = true;
                        break;
                    }
                    else
                    {
                        placeChromosome(current.members[mem2],chr2,i,j);
                    }
                }
                if(found)
                {
                    break;
                }
            }
            next.members[k+700] = new Member();
            next.members[k+700] = current.members[mem2];
        }
    }
    
    public void placeChromosome(Member mem, Chromosome chr, int x, int y)
    {
        for(int i=0;i<chr.height;i++)
        {
            for(int j=0;j<chr.width;j++)
            {
                mem.board[i+y][j+x]=chr.dna[i][j];
            }
        }
    }
    
    public Chromosome getChromosome(Chromosome chr, Member mem)
    {
        Chromosome retchr = chr;
        for(int i=chr.posX;i<chr.posX+chr.height;i++)
        {
            for(int j=chr.posY;j<chr.posY+chr.width;j++)
            {
                retchr.dna[i-chr.posX][j-chr.posY] = mem.board[i][j];
            }
        }
        
        return retchr;
    }
    
    public Chromosome selectChromosomeForCrossover(Member mem)
    {
        Random rand = new Random();
        int height = rand.nextInt(7) + 1;
        int width = rand.nextInt(7) + 1;
        int posX = rand.nextInt(15 - height);
        int posY = rand.nextInt(15 - width);
        
        Chromosome chr = new Chromosome(mem,height,width,posX,posY);
        
        return chr;
    }
    
    public int crossoverChromosomePositionStrength(Chromosome chr, Member mem)
    {
        int strength = 0;
        if(chr.posY-1 >= 0)
        {
            for(int i=chr.posX;i<chr.posX+chr.height;i++)
            {
                if(mem.board[i][chr.posY].north == mem.board[i][chr.posY-1].south)
                {
                    strength++;
                }
            }
        }
        
        if(chr.posY+chr.width+1 < 16)
        {
            for(int i=chr.posX;i<chr.posX+chr.height;i++)
            {
                if(mem.board[i][chr.posY+chr.width].south == mem.board[i][chr.posY+chr.width+1].north)
                {
                    strength++;
                }
            }
        }
        
        if(chr.posX-1 >= 0)
        {
            for(int j=chr.posY;j<chr.posY+chr.width;j++)
            {
                if(mem.board[chr.posX][j].west == mem.board[chr.posX-1][j].east)
                {
                    strength++;
                }
            }
        }
        
        if(chr.posX+chr.height+1 < 16)
        {
            for(int j=chr.posY;j<chr.posY+chr.width;j++)
            {
                if(mem.board[chr.posX+chr.height][j].east == mem.board[chr.posX+chr.height+1][j].west)
                {
                    strength++;
                }
            }
        }
      
        return strength;
    }
}
