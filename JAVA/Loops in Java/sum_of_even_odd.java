//Write a program to find the sum of even and odd numbers separately from 1 to n.
package com.company;

import java.util.Scanner;

public class sum_of_even_odd {
    static void main() {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter n = ");
        int n = sc.nextInt();

        int even_sum = 0;
        int odd_sum = 0;

        for (int i = 1; i <= n; i++) {
            if (i % 2 == 0) {
                even_sum += i;
            } else {
                odd_sum += i;
            }
        }

        System.out.println("Even number sum = " + even_sum);
        System.out.println("Odd number sum = " + odd_sum);
    }
}