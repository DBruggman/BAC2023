# Identified features

### LoanNr_ChkDgt
Toss.
Unique identifier. 

### Name
Toss by now.
Name of the company. Maybe engineer into the # of loans per company. 

## City, state, ZIP
Toss by now.
Choose one of them to obtain desired specificity.
Maybe feature engineer using Count encoding as a proxy for city population?

## Bank
**Keep it.**
Encoding: Maybe one-hot for decision trees and default rate for deep learning and regression?
Outliers: One-hot solves it. For the default rate add a bank 'NullBank' and calculate it's default rate.

## Bank State
Toss.

## NAICS
**Keep it.**
Encoding: Maybe one-hot for decision trees and default rate for deep learning and regression?


## ApprovalDate, ApprovalYear
Toss by now.
Feature engineer for interest rate.
Feature engineer for comparative value.
Feature engineer for loans signed in the X period before.
Feature engineer for seasonality.
Feature engineer for historical default ratio.

## Term
**Keep it.**
Term in months.

## NewExist
**Keep it.**
Binary encoding.
Outliers: Fill with the mode (Existing)

## NoEmp
**Keep it.**
Maybe directly use as number.
Bins: Think about doing logarithmic size?
    Encode: 
Maybe feature engineer into one-hot labels for small, medium and big business? Try different bins to see best results.

## CreateJobs, RetainJobs
Toss by now.
We don't understand yet how these work.

## FranchiseCode
**Keep it.**
Feature engineer for isFranchise binary encoding.
Maybe identify biggest franchises too.

78760: Subway
68020: Quiznos
50564: Mail Boxes Etc
21780: Dairy Queen
25650: Dunkin
79140: Super 8

## UrbanRural
**Keep it.**
Choose what to do with undefined! Keep it as a possible value?
Encoding: One-hot for urban rural.

## RevLineCr
**Keep it.**
Toss the really wierd ones. 
Understand 0 as N. Maybe Y and T.
Find out if the statiscal distributions are the same to see if we can combine them.
Binary Encoding.

## LowDoc
**Keep it.**
Toss the really wierd ones.
Maybe understand 0 as N.
Binary Encoding.

## ChgOffDate
Toss.
It only depends on if the loan was paid.

## DisbursementDate, DisbursementGross
Toss.
They are only units from the future.

## BalanceGross
Toss.
Useless.

## ChgOffPrinGr
Toss.
From the future.

## GRAppv
**Keep it.**
How much is it approved. 

## SBA_Appv
**Keep it.**







