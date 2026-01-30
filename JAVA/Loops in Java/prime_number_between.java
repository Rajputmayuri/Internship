//Write a java program to print prime numbers from 1 to 100
package com.company;

public class prime_number_between {
    static void main() {
        for (int num = 2; num <= 100; num++) {
            int count = 0;

            for (int i = 1; i <= num; i++) {
                if (num % i == 0) {
                    count += 1;
                }
            }
            if (count == 2) {
                System.out.println(num + " ");
            }
        }
    }
}