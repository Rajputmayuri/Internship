//Write a program using while loop to find the factorial of a number.
package com.company;

import java.util.Scanner;

public class factorial_using_while_loop {
    static void main() {
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter a number =");
        int num=sc.nextInt();

        int i=1;
        int fact=1;
        while (i<=num){
            fact=fact*i;
            i++;
        }
        System.out.println("Factorial of " +num+ " is =" +fact);
    }
}
