package ense_350_lab5;

import java.util.Scanner;

public class MultipleSegmentTrapezoidal {

	public static float funcY(float x)
	{
		//function f(x) = 2 - 5x + 10x^2 + 1/2x^3
		return 2 - 5 * x + 10 * x * x+ 1/2 * x * x * x;
	}
	
	// Function to evaluate the value of integral 
    public static float multipleSegmentTrapezoidal(float a, float b, float n) 
    { 
        // Grid spacing 
        float h = (b - a) / n; 
      
        // Computing sum of first and last terms 
        // in above formula 
        float s = funcY(a) + funcY(b); 
      
        // Adding middle terms in above formula 
        for (int i = 1; i < n; i++) 
            s += 2 * funcY( a + i * h); 
      
        // h/2 indicates (b-a)/2n. Multiplying h/2 
        // with s. 
        return (h / 2) * s; 
    } 
      
    public static void main(String[] args) 
    { 
    	
    	Scanner input = new Scanner(System.in);

    	System.out.println("Enter the number for segment 1: ");
    	float segment1 = input.nextFloat();
    	
    	System.out.println("Enter the number for segment 2: ");
    	float segment2 = input.nextFloat();
    	
    	// Number of grids. Higher value with higher accuracy 
    	System.out.println("Enter the number for n: ");
    	int n = input.nextInt();
    	
    	input.close();

      
        System.out.println("Value of integral is "+ 
                           Math.round(multipleSegmentTrapezoidal(segment1, segment2, n)  
                           * 10000.0) / 10000.0); 
    } 
}
