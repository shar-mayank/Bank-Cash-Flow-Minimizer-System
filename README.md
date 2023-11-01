# Bank-Cash-Flow-Minimizer-System

This project aims to minimize the number of financial transactions among multiple banks that use different payment methods. To achieve this, we introduce a "World Bank" that supports all payment methods. When banks need to transfer money and don't share a common payment method, they go through the World Bank as an intermediary.
Let's take an example. say we have the following banks: Bank_of_America (World bank)
State Bank India
Axis Bank
Kotak Mahindra Bank Punjab_National_Bank
 
Following are the payments to be done:
<img width="670" alt="image" src="https://github.com/Shar-Mayank/Bank-Cash-Flow-Minimizer-System/assets/108417648/245e9a70-7756-47f0-851b-8b16c6ff3eb8">

But there's a catch!! Each Bank only supports a set of modes of payments and can make or receive payments only via those. Only World Bank supports all modes of payments. In our current example we have only three payment modes :
Google_Pay PhonePe Paytm
Following is the list of Banks and their supported payment modes:
Bank_of_America State Bank Of India Axis_bank
Kotak Punjab_National_Bank
How It Works:
- Paytm, Google_pay, PhonePe - Paytm, Google_pay
- Paytm
- Paytm, PhonePe - Google_pay
 To minimize transactions, we follow these steps:
1. Calculate the "net amount" for each bank using this formula: Net Amount = (Sum of all money to be received) - (Sum of all money to be paid).

2. Find the bank with the largest debt (the most negative net amount). This bank (let's call it Bank X) needs to pay the most.

3. Find a bank with the largest credit (the most positive net amount) and shares a payment method (let's say M1) with Bank X (let's call it Bank Y).

4. Calculate the amount to transfer, which is the minimum of the absolute values of X's debt and Y's credit. Let's call it "Z."

5. Bank X pays Z to Bank Y.

6. Three cases may arise:
• If the absolute value of X's debt is less than Y's credit (|X| < Y),
Bank X is fully settled and removed from the list.
• If the absolute value of X's debt is greater than Y's credit (|X| >
Y), Bank Y is fully settled and removed from the list.
• If the absolute value of X's debt equals Y's credit (|X| = Y), both
banks are fully settled and removed from the list

7. Repeat this process for the remaining banks.
