# User Stories
## Feature 1: State Comparisons

* User story: As a user, I want to see two (or more?) states' statistics side by side so that they can be compared
* Acceptance Criteria: If I input North Dakota and South Dakota as my states to compare, then the two states' data appear side by side.
* Acceptance Test is in the test_tableMaker.py file in the class TestTableOutputUserStories in function test_two_state_display

## Feature 2: Data Display for entire USA

* User story: As a user I want to see price data for the entire US so that I am more informed.
* Acceptance Criteria: The user will be able to enter a command (python3 code.py -price "US") and the average energy prices for the US will be displayed. 
* Acceptance Test is in the test_tableMaker.py file in the class TestTableOutputUserStories in function test_us_display

## Feature 3: Individual State Displays

* User story: As a user I want to see data for a specific state so that I am more informed about energy consumption for each state.
* Acceptance Criteria: The user will be able to enter a command (python3 code.py "Minnesota"), then all available energy data for Minnesota will be displayed. 
* Acceptance Test is in the test_tableMaker.py file in the class TestTableOutputUserStories in function test_single_state_display
