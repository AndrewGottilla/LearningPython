### 2020-09-14
### Author: Andrew Gottilla
### Lesson 45: Default values

def test_score(name, score="--"):
    """Displays a message about a student's test score."""
    print(name.title() + " has a test score of " + str(score) + " out of 100.")

test_score("Ryuji", 100)
test_score("andrew")