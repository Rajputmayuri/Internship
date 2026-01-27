//Write a java program to check whether a number is positive, negative, or zero.
package com.company;

import java.util.Scanner;

public class pos_neg {
    static void main() {
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter a number =");
        int number=sc.nextInt();
        if (number ==0) {
            System.out.println("Number is Zero ");
        }
        else if (number >0) {
            System.out.println("Positive number ");
        }
        else {
            System.out.println("Negative number ");
        }

    }
}
