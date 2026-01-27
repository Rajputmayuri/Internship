//Write a java program to determine whether a triangle is valid based on the sum of its angles.

package com.company;

import java.util.Scanner;

public class valid_triangle {
    static void main() {
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter first angle =");
        int a=sc.nextInt();
        System.out.print("Enter second angle =");
        int b=sc.nextInt();
        System.out.print("Enter third angle =");
        int c=sc.nextInt();
        if (a+b+c==180) {
            System.out.println("Triangle is Valid");
        }
        else {
            System.out.println("Triangle is not Valid");
        }
    }


}
