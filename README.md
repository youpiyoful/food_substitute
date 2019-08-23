# food_substitute

## App description :
This program offers you 2 functionalities : 
1. Which food do you want to replace ?
2. Record substitute food

The user selects 1. The program asks the user the following questions and the user selects the answers:

Select the category. [Several proposals associated with a number. The user enters the corresponding digit and presses enter]
Select the food. [Several proposals associated with a number. The user enters the digit corresponding to the chosen food and presses enter]
The program offers a substitute, its description, a store or buy it (if any) and a link to the Open Food Facts page about that food.
The user then has the possibility to save the result in the database.

## Features : 
* Food search in the Open Food Facts database.
* The user interacts with the program in the terminal
* If the user enters a character that is not a digit, the program repeat the question
* The search are done on a MySQL basis.

## Behavior driven development :

### start_use_program:

1. **Given** a user want use the programm
2. **When** he selects one of the proposals made by the program 
3. **Then** the program proposes to take the next step 
---

### found_food_substitute :

#### triggering_questions:
1. **Given** a user want found a substitute food
2. **When** he selects the choice number 1 corresponding to "found a substitute food"
3. **Then** the program offers a choice of food categories
---

#### select_category_of_food :
1. **Given** a user want select a category of food to substitute
2. **When** he select the number corresponding to one of them
3. **Then** the program offers a choice of substitute foods
---

#### select_a_food :
1. **Given** a user want select a food to substitute
2. **When** he select the number corresponding to the chosen food
3. **Then** The program offers a substitute, its description, a store or buy it (if any) and
a link to the Open Food Facts page about that food.
---

### record_food_substitute_found :

1. **Given** a user has found a substitute food
2. **And** he wants to save it
2. **When** he selects "save food substitute found"
3. **Then** the program save the article in a specific place
---

### found_recorded_subsitute_food :

1. **Given** a user wants to find substituted registered foods
2. **When** he selects the choice number 2 (found registered susbstitute foods)
3. **Then** the program shows him **all** the substituted foods saved
---