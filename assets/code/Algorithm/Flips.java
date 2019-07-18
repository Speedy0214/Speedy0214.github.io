public class Flips
{

    public static void main(String[] arg)
    {
    int T = Integer.parseInt(args[0]);
    Counter first = new Counter("first");
    Counter last = new Counter("last");
    for (int t = 0; t<T; t++)
        if (StdRandom.bernoulli(0.5))
            heads.increment();
        else tails.increment();
    StdOut.println(first);
    StdOut.println(last);
    }



}
