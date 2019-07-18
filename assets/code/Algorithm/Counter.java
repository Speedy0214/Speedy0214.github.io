public class Counter
{
    private final String name;
    private int count;
    private String n1;
    
    // constructor
    public Counter(String id)
    { 
        
        name = id;
    
    }

    public void increment()
    { 
        System.out.println(n1);
        count++; 
    }

    public int tally()
    {return count; }

    public String toString()
    { return count + "" + name; }

    public static void main(String[] args)
    {
        Counter start = new Counter("start");
        Counter finish = new Counter("finish");

        start.increment();
        start.increment();
        finish.increment();

        System.out.println(start + "; " + finish);
        System.out.println(start.tally() + finish.tally());

    }

}
