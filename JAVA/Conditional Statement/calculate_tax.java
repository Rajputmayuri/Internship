/*Calculate income tax paid by an employee to the government as per the stats mentioned below.
Income stat         Tax
2.5L-5.0L           5%
5.0L-10.0L          20%
Above 10.0L         30%

Note that there is no tax below 2.5L. Take input amount as an input from the user.*/
package com.company;
import java.util.Scanner;



public class calculate_tax {
    static void main() {


        Scanner sc=new Scanner(System.in);
        System.out.print("Enter your annual income  =");
        double amount=sc.nextDouble();
        double tax=0;
        if (amount<=250000)

    {
        tax = 0;
    }
        else if (amount <=500000)

    {
        tax = (amount - 250000) * 0.05;
    }
        else if (amount<=1000000)

    {
        tax = (250000 * 0.05) + (amount - 500000) * 0.20;
    }
        else

    {
        tax = (250000 * 0.05) + (500000 * 0.20) + (amount - 1000000) * 0.30;
    }

        System.out.println("Income Tax to be paid : Rs."+tax);

    }

}
