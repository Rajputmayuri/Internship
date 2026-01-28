//Sum of digits of a number
package com.company;

import java.util.Scanner;

public class sum_of_digits_of_number {
    static void main() {
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter a number =");
        int n=sc.nextInt();
        //The loop extracts each digit of the number using modulus (% 10), adds it to sum, and removes the digit by dividing the number by 10. This continues until the number becomes zero.
        int sum=0;
        while(n>0){
            sum+=n%10;
            n/=10;
        }
        System.out.println("Sum of digits ="+sum);
    }
}
