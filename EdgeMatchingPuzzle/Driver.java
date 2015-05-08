
/**
 * Write a description of class Driver here.
 * 
 * @author (Gangaprasad Koturwar) 
 * @version (a version number or a date)
 */
public class Driver
{
    // instance variables - replace the example below with your own
    
    /**
     * An example of a method - replace this comment with your own
     * 
     * @param  y   a sample parameter for a method
     * @return     the sum of x and y 
     */
    public static void main(String[] args) {
		Evolution ev = new Evolution();
		Member best = ev.simulateEvolution(10);
		System.out.println("best fit in the first generation is with health " + best.health);
	}
}
