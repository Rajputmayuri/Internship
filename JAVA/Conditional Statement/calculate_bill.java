/*Write a java program to calculate electricity bill based on given units and slab rates.
conditions :
-For first 100 units -->Rs.5 per unit
-For next 100 units(101-200) -->Rs. 7 per unit
-Above 200 units --> Rs. 10 per unit
 */

package com.company;

import java.util.Scanner;

public class calculate_bill {
    static void main() {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter number of units consumed =");
        int units = sc.nextInt();

        double bill = 0;

        if (units <= 100) {
            bill = units * 5;
        }
        else if (units <= 200) {
            bill = (100 * 5) + (units - 100) * 7;
        }
        else {
            bill = (100 * 5) + (100 * 7) + (units - 200) * 10;
        }
        System.out.println("Total Electricity Bill = Rs. " + bill);
    }
}

