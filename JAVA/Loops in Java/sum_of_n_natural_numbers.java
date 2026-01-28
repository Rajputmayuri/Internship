//Sum of first n natural numbers
package com.company;

import java.util.Scanner;

public class sum_of_n_natural_numbers {
    static void main() {
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter value for n= ");
        int n=sc.nextInt();

        int sum=0;
        for (int i=1;i<=n;i++){
            sum+=i;
        }
        System.out.println("Sum ="+sum);
    }
}
