//Write a program to find factorial of a given number using for loop & while loop.
package com.company;
import java.util.Scanner;

/*
public class factorial {
    static void main() {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number =");
        int n = sc.nextInt();

        int fact = 1;
        for (int i = 1; i <= n; i++) {
            fact = fact * i;
        }
        System.out.println("Factorial of " + n + " = " + fact);
    }
}
*/

public class factorial{
    static void main() {
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter a number =");
        int n=sc.nextInt();
        int i=1;
        int fact=1;
        while(i<=n){
            fact=fact*i;
            i++;
        }
        System.out.println("Factorial is ="+fact);
    }
}
