//Write a java program that compare two numbers using relational operators (<,>,<=,>=,==,!=) and prints the result of each comparison.

package com.company;
import java.util.Scanner;

public class relational_operators {
    static void main() {
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter 1st number =");
        int a = sc.nextInt();
        System.out.print("Enter 2nd number =");
        int b = sc.nextInt();
        System.out.println(a > b);
        System.out.println(a < b);
        System.out.println(a >= b);
        System.out.println(a <= b);
        System.out.println(a == b);
        System.out.println(a != b);
    }
}
