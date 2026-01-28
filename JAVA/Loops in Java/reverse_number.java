package com.company;

import org.w3c.dom.ls.LSOutput;

import java.util.Scanner;

public class reverse_number {
    static void main() {
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter a number =");
        int n=sc.nextInt();
        //The loop extracts the last digit using % 10, appends it to the reversed number by multiplying rev by 10, and removes the last digit of the original number by dividing it by 10.
        int rev=0;
        while(n>0){
            int digit=n%10;
            rev=rev*10+digit;
            n/=10;
        }
        System.out.println("Revered number =" +rev);
    }

}
