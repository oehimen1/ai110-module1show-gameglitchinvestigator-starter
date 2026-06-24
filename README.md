# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [X] Describe the game's purpose. 
      Number guessing game. Guess the correct secret number in the number of attempts given. 
- [X] Detail which bugs you found.
      Bugs I found:
      - Incorrect attempts number
      - Incorrent too low/too high tint
      - Clicking "new game" buttong doesn't fully refresh state of game. 
- [X] Explain what fixes you applied.
      - Corrected too low/too high bug
      - Changed number of starting attempts from 1 to 0. 

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User enters a guess of 10
2. Game returns "too low"
3. User enters a guess of 30
4. Game returns "too high"
5. Score updates after each guess
6. User enters a guess of 20 -> Too Low
7. User correclty answers a guess of 21
8. Games ends after correct guess

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->
![Game screenshot](/game_glitch_screenshot.png)
## 🧪 Test Results

python -m pytest tests/test_game_logic.py -v
```

tests/test_game_logic.py::test_attempts_initializes_to_zero PASSED                     [ 14%]
tests/test_game_logic.py::test_winning_guess PASSED                                    [ 28%]
tests/test_game_logic.py::test_guess_too_high PASSED                                   [ 42%]
tests/test_game_logic.py::test_guess_too_low PASSED                                    [ 57%]
tests/test_game_logic.py::test_too_high_hint_string PASSED                             [ 71%]
tests/test_game_logic.py::test_too_low_hint_string PASSED                              [ 85%]
tests/test_game_logic.py::test_hint_strings_with_string_secret PASSED                  [100%]

===================================== 7 passed in 1.57s =====================================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
