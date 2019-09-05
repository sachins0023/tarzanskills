# tarzanskills
day 2 work includes readme and file day-2.py
Give output in the form of
1
1 2
1 2 3
1 2 3 4
1 2 3
1 2
1

To store your credentials for git push, use
    git config credential.helper store
    git push https://github.com/owner/repo.git

Creating a new repo 'tarzanskills'
Including readme.md where today's work has to be highlighted
A new file day-2.py is created

Master and Branch
In a team project, each individual works on their own branch and once the code is in working condition, the individual has to do a pull request to the manager who manages the master branch.
In this way, the code in the master branch is always executable without errors or unwanted results. If another branch wants to add their code, then the manager adds it to the master branch
provided it doesn't cause any discrepancy. If any problems are encountered, the manager could manage the editing or deletion of the branch.

After every work completion, the individual does a git pull to check whether their code is same as what the master has. If the master has some changes that the individual doesn't have, then
it is updated in the individual's file through git pull. If the master has an updated file for which the individual also made changes, then the individual has to incorporate the earlier
committed code in master into his update and make sure both the updates work.

Git commands
git branch - to see the branches
git branch <name> - to create a new branch
git checkout <name> - to switch branch
git checkout -b <name> - to create a branch and switch into it

To identify  which branch are you currently on, in PyCharm, check  bottom right where it shows Git: <CurrentBranch>

In case of arithmetic operations, if one of the number is a decimal, then the answer will always be a decimal except in the case of complex numbers.
In python, j is used to denote square root of -1. In terms of complex numbers, it never gives you zero as decimal numbers with j.

Some examples of arithmetic operations:
2j+3j=5j
1-2.0=-1.0
2j*3j=-6+0j
1/4j=-0.25j
1j/4j=0.25 +0j
1%2.0=1.0
1%2j=error
1j%4j=error

In from decimal import Decimal,
operations should be enclosed without quotes while numbers have to be put in quotes to attain exact values. Due to how floating numbers are defined sum of 1.1+2.2 gives a result of
3.3000000003 or something and is mathematically incorrect. Hence Decimal can be used to attain exact mathematically accurate values for similar discrepancies.error

from fractions import Fraction
helps you work with fractions and their arithmetic and logical uses.

Always in the case of solving arithmetic involving decimals try to use from decimal import Decimal and include the numbers in quotes inside Decimal()
