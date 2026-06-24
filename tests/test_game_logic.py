import importlib
import os
import sys

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

import streamlit as st
from logic_utils import check_guess


def test_attempts_initializes_to_zero():
    """Regression test for the fixed attempt counter initialization."""
    if "app" in sys.modules:
        del sys.modules["app"]
    st.session_state.clear()

    import app as game_app
    importlib.reload(game_app)

    assert "attempts" in st.session_state
    assert st.session_state.attempts == 0


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"


def test_too_high_hint_string():
    """Test that 'Too High' outcome has the correct 'Go LOWER!' hint."""
    outcome, message = check_guess(60, 35)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"


def test_too_low_hint_string():
    """Test that 'Too Low' outcome has the correct 'Go HIGHER!' hint."""
    outcome, message = check_guess(20, 50)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"


def test_hint_strings_with_string_secret():
    """Test that hints are correct when secret is passed as a string."""
    # This tests the fix for the bug where secret could be converted to string
    outcome, message = check_guess(60, "35")
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"
    
    outcome, message = check_guess(20, "50")
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"
