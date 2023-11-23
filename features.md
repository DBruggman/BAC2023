# Identified features

## LoanNr_ChkDgt
Toss.
Unique identifier. 

## Name
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
Encoding: Maybe one-hot for decision trees and default rate for deel learning and regression?


## ApprovalDate, ApprovalYear
Toss by now.
Feature engineer for interest rate.
Feature engineer for comparative value.
Feature engineer for loans signed in the X period before.
Feature engineer for seasonality.

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
Maybe feature engineer into one-hot labels for small, medium and big business?



