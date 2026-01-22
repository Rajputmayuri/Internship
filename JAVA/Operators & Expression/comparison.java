package com.company;
import java.util.Scanner;
public class comparison {
    static void main() {
        //Use Comparison operator to find out whether a given number is greater than the user entered number or not.
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter number =");
        int number=sc.nextInt();
        int a=9;
        System.out.println(number>a);
    }
}
