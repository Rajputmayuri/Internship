package com.company;
import java.util.Scanner;

public class ch1_ps5 {
    static void main() {
        //Write a java program to detect whether a number entered by the user is integer or not.
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter number =");
        System.out.println(sc.hasNextInt());
    }
}
