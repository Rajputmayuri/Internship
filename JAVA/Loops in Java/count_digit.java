//count number of digit in a number

package com.company;

import java.util.Scanner;

public class count_digit {
    static void main() {
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter a number =");
        int n=sc.nextInt();
        int count=0;
        do{
            count++;
            n/=10;
        }while(n!=0);
        System.out.println("Number of digits ="+count);
    }
}
