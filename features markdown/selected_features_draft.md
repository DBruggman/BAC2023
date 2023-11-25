# Selected features

Features that will take part in our models.

## Direct Inclusion

### Bank
Bank Name\
**Encoding:**\
One-Hot for tree-based models. An idea is to create a few columns like Bank A, Bank B, Bank C with the major banks.\
<mark>TODO: Identify most common banks.</mark> \
For regression models we could encode each bank with the percentage of default of its previous loans.\
**Cleaning:**\
1559 nulls.\
One-Hot should be able to fix nulls, as a null bank would just be 0 in each column.

### NAICS
North American Industry Classification System code\
**Encoding:**\
One-Hot for tree-based models. We can do a similar encoding as in the *Bank* feature. See [census](https://www.census.gov/naics/?58967?yearbck=2012) for identifying the industries. 
<mark>TODO: Identify most common industries.</mark> \
For regression-based models we could do the same as for *bank* and just substitute it for its default ratio.\

### Term
Loan term in months\
**Encoding:**\
For regression models it is inmediate, being a numeric feature.\
For tree-based models we may have to build bins. An idea would be to divide it into short, medium and long terms.
<mark>TODO: Design bins to divide the terms.</mark>

### NoEmp
Number of Business Employees
**Encoding:**\
For linear models it makes sense to use directly as a feature.\
For tree based models we might want to make bins for different business sizes.
<mark>TODO: Design bins to divide the business sizes.</mark>

### NewExist
1 = Existing Business, 2 = New Business\
**Encoding:**\
For both trees and regressions, the encoding is straightforward binary, 1 = existing, 0 = new.\
**Cleaning:**\
1034 values with 0.0.\
We can fill them with the mode (Existing) or toss the samples.
<mark>TODO: Decide what to do with the nulls.</mark>

### FranchiseCode
Franchise Code 00000 or 00001 = No Franchise\
**Encoding:**\
For both tree and regression models it would be good to feature engineer it into a division between *no-franchise, major-franchise and other-franchise*. We could have one bin for Subway, Quiznos, etc; one for other franchises and one for no franchise.\
Some values included are:\
78760: Subway
68020: Quiznos
50564: Mail Boxes Etc
21780: Dairy Queen
25650: Dunkin
79140: Super 8
<mark>TODO: Design bins to divide the franchises.</mark>

### UrbanRural
1= Urban, 2= Rural, 0 = Undefined\
**Encoding:**\
It has to be one-hot encoding for both trees and regression. 105343 are undefined, so it should be its own cathegory.

### RevLineCr
Revolving Line of Credit: Y = Yes\
**Encoding:**\
Makes sense to binary-encode it for both trees and regression. \
**Cleaning:**\
There is a significative amount of possible values which don't have a clear meaning (i.e. 0, T, 1, R, 2, C). There are also nulls.
<mark>TODO: Clean this data. </mark>

### LowDoc
LowDoc Loan Program: Y = Yes, N = No\
**Encoding:**\
Makes sense to binary-encode it for both trees and regression. \
**Cleaning:**\
There is a significative amount of possible values which don't have a clear meaning (i.e. 0, C, S, A, 1). There are also nulls.
<mark>TODO: Clean this data. </mark>

### GRAppv
Gross Amount of Loan Approved by Bank\
**Encoding:**\
Has to be translated into floats.

### SBA_Appv
SBA’s Guaranteed Amount of Approved Loan\
**Encoding:**\
Has to be translated into floats.