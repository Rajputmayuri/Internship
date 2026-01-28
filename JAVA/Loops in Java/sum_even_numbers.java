//Write a program to sum first n even numbers using while loop.

package com.company;

import java.util.Scanner;

public class sum_even_numbers {
    static void main() {
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter value for n =");
        int n=sc.nextInt();
        int i=1;
        int sum=0;
        while(i<=n){
            sum=sum+(2*i);
            i++;
        }
        System.out.println("Sum of "+n+"even number are ="+sum);
    }
}
