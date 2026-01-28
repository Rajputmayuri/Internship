//Write a program to calculate the sum of the numbers occuring in the multiplication table of n.

package com.company;

import java.util.Scanner;

public class sum_of_no_occuring_in_table {
    static void main() {
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter a number =");
        int n=sc.nextInt();
        int result=0;
        for(int i=1;i<=10;i++) {
            result = result + (n * i);
        }
        System.out.println("Sum of numbers in the multiplication table of "+ n + " = "+result);

    }
}
