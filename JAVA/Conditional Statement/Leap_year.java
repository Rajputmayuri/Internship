/*Write a java program to check whether the year enter by the user is leap year or not.*/

package com.company;
import java.util.Scanner;

public class Leap_year {
    static void main() {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a year = ");
        int year = sc.nextInt();
        if (year % 400 == 0 || (year % 4 == 0 && year % 100!=0)) {
            System.out.println("Leap Year ");
        } else {
            System.out.println("Not Leap Year ");
        }

    }
}
