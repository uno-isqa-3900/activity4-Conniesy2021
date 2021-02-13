# Activity 4 - Python Exercise - Lists, Tuples and Dictionaries

## Objectives
* Demonstrate a your knowledge of how to create, modify and use python lists. 
* Demonstrate a your knowledge of how to create and use python tuples. 

Create 2 Python program files meeting the requirements listed below. Both files should include the following at the top:
Simple comments including the following at the top of the Python file:
* Your name
* The course name and date
* A short description of the code in the file (i.e. purpose of the program)

## Directions for program 4a
1. Create a python program file called activity4a.py to complete the following requirements:
2. Create a List Duplicate Remover or Deduplication program which eliminate any duplicates in a list and creates a new list with no duplicates.  Use the following list:
```Python
names = ['mary','mary','bill','sam','maria','kahn','bill','barry','george','hank','belinda','maria','karthik']
```
3. Sort each list.
4. Create a new list from the original with duplicates removed. Use a Python function that receives the original list as a parameter and returns a list with the duplicates removed.
5. Print both lists to the screen which should look similar to the following output:

![activity4 lists-results](https://github.com/uno-isqa-3900/activity4/blob/main/images/activity5-lists-results.png)

Note: The program should involve creating a depulicate_remover or deduplication function where above list is sent to the function. The function should return the deduplicated list to be sorted and printed.

## Directions for program 4b
Create a python program file called activity4b.py to complete the following requirements:
1. Similar to the test_scores.py file provided with this assignment on Canvas, your program should ask for a series of test scores from 0 to 100 points. You will continue to add these scores to a Python list until a -1 (negative 1) is entered.
2. After -1 is input, print out all the scores in a list format
3. Print the sum of all the scores, the average score based on the number of scores input, and the letter grade of the average score. Use the scale provided in canvas to assign a letter grade: 
4. Executing the program in the command window should look and act like the program below. Notice the “out of bounds error” was handled with an appropriate message and the user was asked to reenter the score.
5. REQUIRED: The use of exception handing is required in order to recover from user inputs that are not numeric data. When invalid values are input, display an appropriate error message and continue to prompt the user to reenter the score until it is valid. Only values between 0 and 100 (inclusive) should be accepted as valid. -1 should end the user input loop. See canvas PDF for sample screenshot.

## Submitting your assignment
1. When you are happy with your working code push the code to GitHub and be sure your GitHub repository is updated.
2. Create a markdown file/document and make one or more  screenshots of the code working in the command line  (run several different grades through the program and add it to the markdown file/document labeled 3900_Activity4.

## Rubric
See the Rubric posted with this assignment on Canvas for grading details.
