//Write a java program to check whether a given number is even or odd.

package com.company;

import java.util.Scanner;

public class even_odd {
    static void main() {
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter a number =");
        int number =sc.nextInt();
        if (number%2==0) {
            System.out.println("Even number ");
        }
        else {
            System.out.println("Odd number ");
        }
    }
}
