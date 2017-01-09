package com.google.challenges; 

public class Answer {   
    public static int answer(int[] inp) {
    int noC = 0;
    int[] noD = new int[inp.length];

    for( int i = 1; i < inp.length-1; ++i)
    {
        for( int j = 0; j < i; ++j)
        {
            if( inp[i] % inp[j] == 0)
                ++noD[i];
        }
    }

    for( int i = 2; i < inp.length; i++)
    {
        for( int j = 1; j < i; ++j)
        {
            if( inp[i] % inp[j] == 0)
                noC += noD[j];
        }
    }

    return noC;
}
}
