# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  In the sidebar, it says the number of attempts allowed is 8, but in the header the number of attempts is 7. 
  I toggled the Show Hint button, and it showed the hint while guessing. 
  Clicking the Developer Debug Info, I see the attempts, the secret number, difficulty, history, etc. 
  When submitting the first attempt, the # of attempts didnt change. It should start at 0 at the start of the game, not 1. 

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  1. I opened the Developer Debug Info tab and it mentioned that the secret number is 35. When submitting my guess of 60, it said to "Guess Higher" when it should be to "Guess Lower".

  2. The difficulties seem to be incorrect. Easy has a range from 1 to 20, but the secret number is 47.   


**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|guess of 60 | A hint to guess with a lower number | A hint to guess with a higher number | "Go HIGHER!" |
| submit guess | # of attempts to decrease at first submit and go from 6 to 5| # of attempts stayed the same at first submission, and then went from 6 to 4 | Attmepts at 7 -> Attempts at 4 |
| submit "New Game" | New Game to have started with attempts back to 7 and new secret # | New Game was not able to be started. The state remained the same | None |
|None |Guess a number between 1 and 100. Attempts left: 8 | Guess a number between 1 and 100. Attempts left: 7   | Disrepancy between # of attempts in sidebar and main body across difficulties.
| Sumbitting correct number | Developer Debug' Score is -5 is You won! | Developer Debug' Score should be 55| The secret was 47. Final score: 55

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? 
    I used the Copilot tool for this project. 
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
    Background: I wanted to know what the reason was for the number of attempts bug. So I asked AI something like this "I found one glitch where I submit the first guess attmept, and it doesn't decrease from 7 to 6, it just stays at 7. Afterwards, as i continue making guess attempts it jumps from 6 to 4 attempts. Please explain the underlying logic causing it."

    AI Suggestion: AI suggested that the reason for the attempt count glitch was becase as the game starts, st.session_state.attempts = 1, instead it should be 0. "So the game begins as if 1 attempt has already been used. For Normal difficulty, that means the UI starts at 8 - 1 = 7 attempts left before you even submit a guess."

    Verification: I verified this fix by strating a new game and looking at develope debug tools' attempts section to make the number of attempts is correct when starting the game and increasing/decreasing as I continue to make guesses.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

    Background: A part of the UI that I was unsure of if it was a bug, was the score. In the developer's tools it just negative socres when submitting attempts that was not matching the secret number. I tried to clairfy with AI since I am unfamiliar with playing the game: `Can you get a negative socre in number guessing game?`


    AI Suggestion: The suggestion or answer from AI for this question was:
    `Yes — you can get a negative score
    In app.py, update_score() starts from st.session_state.score = 0 and then:
    "Too Low" always does current_score - 5
    "Too High" on odd attempts also does current_score - 5
    There is no lower bound/floor on score, so a first wrong guess that is too low will drop the score to -5`

    Verification:
    I am still unsure of what the anwers of this is, since it only answered in the context of the code/application itself rather than general knowledge. If I'd implement the change for the supposed bug fix, the game would be incorrect and would not return the right score.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
    I decided whethere the (too low/too high) bug was fixed by playing the game again. While know the actual secret number, I double checked the hint was correct as I was making guess attempts.
- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
  Using pytest, I ran some tests for the check_guess function to test that bug was fixed and logic was correct. What it showed about the code was that the secret_number could possibly be an number or a string and those two cases need to be considered to be able to return the correct hint. 
- Did AI help you design or understand any tests? How?
    AI did help me to design the test in `test_game_logic.py`. I added to the prompt what tests to add for the bug fix implemented: `Generate a `pytest` case in `test/test_game_logic.py` that targets the bug fix for the too low/too high hint string in check_guess.` One thing I would have liked to do differently, was to figure out what cases to test for myself and it to the prompt. 

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  Streamlit reruns help to run a set of instructions immediately. Session state is one way to share certain variables in those instructions between each rerun and for each session.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  One habit that I would like to reuse in future labs and project is prompting strategy. Throughout the labs, Ive noticed we spent most of the time gathering requirement and thinking and planning the system architecture before prompting AI. This is a great approach compared to just jumping into AI prompting "Fix this". 
- What is one thing you would do differently next time you work with AI on a coding task?
  One thing I would do differently next time I work with AI on a coding task, is actually spend some time thinking what is I am requesting and drafting detailed prompts before submitting it to AI. This will helpme strengthen my problem-solving and critical thinking ability. 
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  This project chnaged the way I think about AI generated code as before I believed with using AI you can ufortunately loose critical thinking ability as it's doing the work for you. But now I think it has really help me to spend more time planning before touching code and/or using AI. 