import streamlit as st
import random
import time

# Page configuration
st.set_page_config(
    page_title="Rock Paper Scissors",
    page_icon="✂️",
    layout="centered"
)

# Custom CSS for animations and styling
st.markdown("""
<style>
    .main {
        background-color: #f0f8ff;
    }
    
    .game-title {
        text-align: center;
        color: #1E90FF;
        font-size: 3em;
        margin-bottom: 20px;
        animation: pulse 2s infinite;
    }
    
    .result-win {
        color: #2E8B57;
        font-size: 2em;
        text-align: center;
        animation: celebrate 1s ease-in-out;
    }
    
    .result-lose {
        color: #CD5C5C;
        font-size: 2em;
        text-align: center;
    }
    
    .result-tie {
        color: #DAA520;
        font-size: 2em;
        text-align: center;
    }
    
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    
    @keyframes celebrate {
        0% { transform: scale(1); }
        50% { transform: scale(1.2); }
        100% { transform: scale(1); }
    }
    
    .button-container {
        display: flex;
        justify-content: center;
        gap: 20px;
        margin: 20px 0;
    }
    
    .choice-display {
        display: flex;
        justify-content: space-around;
        margin: 30px 0;
        font-size: 1.5em;
    }
    
    .score-display {
        background-color: #F0F8FF;
        padding: 10px 20px;
        border-radius: 10px;
        margin: 10px 0;
        text-align: center;
    }
    
    .instructions {
        background-color: #E6E6FA;
        padding: 15px;
        border-radius: 10px;
        margin-top: 20px;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'user_score' not in st.session_state:
    st.session_state.user_score = 0
if 'computer_score' not in st.session_state:
    st.session_state.computer_score = 0
if 'ties' not in st.session_state:
    st.session_state.ties = 0
if 'result' not in st.session_state:
    st.session_state.result = None
if 'user_choice' not in st.session_state:
    st.session_state.user_choice = None
if 'computer_choice' not in st.session_state:
    st.session_state.computer_choice = None
if 'game_count' not in st.session_state:
    st.session_state.game_count = 0

# Title
st.markdown('<h1 class="game-title">Rock 🪨 Paper 📄 Scissors ✂️ By ZeeJay 🙅‍♂️</h1>', unsafe_allow_html=True)

# Functions
def get_emoji(choice):
    if choice == 'r':
        return "🪨"
    elif choice == 'p':
        return "📄"
    else:
        return "✂️"

def get_full_name(choice):
    if choice == 'r':
        return "Rock"
    elif choice == 'p':
        return "Paper"
    else:
        return "Scissors"

def is_win(player, opponent):
    # Return true if player wins
    # r > s, s > p, p > r 
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

def play(user_choice):
    computer_choice = random.choice(['r', 'p', 's'])
    
    st.session_state.user_choice = user_choice
    st.session_state.computer_choice = computer_choice
    st.session_state.game_count += 1
    
    if user_choice == computer_choice:
        st.session_state.result = 'tie'
        st.session_state.ties += 1
        return 'tie'
    
    if is_win(user_choice, computer_choice):
        st.session_state.result = 'win'
        st.session_state.user_score += 1
        return 'win'
    
    st.session_state.result = 'lose'
    st.session_state.computer_score += 1
    return 'lose'

def reset_game():
    st.session_state.user_score = 0
    st.session_state.computer_score = 0
    st.session_state.ties = 0
    st.session_state.result = None
    st.session_state.user_choice = None
    st.session_state.computer_choice = None
    st.session_state.game_count = 0

# Game information
st.markdown("""
<div class="instructions">
    <h3>How to Play:</h3>
    <p>1. Choose either Rock, Paper, or Scissors by clicking one of the buttons below.</p>
    <p>2. The computer will randomly select its choice.</p>
    <p>3. Winner is determined by these rules:</p>
    <ul>
        <li>Rock crushes Scissors</li>
        <li>Scissors cuts Paper</li>
        <li>Paper covers Rock</li>
    </ul>
    <p>First to win 5 rounds is the grand champion!</p>
</div>
""", unsafe_allow_html=True)

# Score display
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(f'<div class="score-display">You: {st.session_state.user_score}</div>', unsafe_allow_html=True)
with col2:
    st.markdown(f'<div class="score-display">Ties: {st.session_state.ties}</div>', unsafe_allow_html=True)
with col3:
    st.markdown(f'<div class="score-display">Computer: {st.session_state.computer_score}</div>', unsafe_allow_html=True)

# Game choices
st.markdown('<div class="button-container">', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("🪨 Rock", key="rock", use_container_width=True):
        play('r')
with col2:
    if st.button("📄 Paper", key="paper", use_container_width=True):
        play('p')
with col3:
    if st.button("✂️ Scissors", key="scissors", use_container_width=True):
        play('s')
st.markdown('</div>', unsafe_allow_html=True)

# Display choices and results
if st.session_state.user_choice and st.session_state.computer_choice:
    st.markdown(f"""
    <div class="choice-display">
        <div>You chose: {get_emoji(st.session_state.user_choice)} {get_full_name(st.session_state.user_choice)}</div>
        <div>Computer chose: {get_emoji(st.session_state.computer_choice)} {get_full_name(st.session_state.computer_choice)}</div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.session_state.result == 'win':
        st.markdown('<div class="result-win">🎉 You Won! 🎉</div>', unsafe_allow_html=True)
    elif st.session_state.result == 'lose':
        st.markdown('<div class="result-lose">You Lost! 😢</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="result-tie">It\'s a Tie! 🤝</div>', unsafe_allow_html=True)

# Champion celebration
if st.session_state.user_score >= 5:
    st.balloons()
    st.markdown("""
    <div style="text-align:center; animation: celebrate 1s infinite; margin: 20px 0;">
        <h2 style="color: gold;">🏆 GRAND CHAMPION! 🏆</h2>
        <p style="font-size: 1.5em;">You defeated the computer!</p>
    </div>
    """, unsafe_allow_html=True)
elif st.session_state.computer_score >= 5:
    st.markdown("""
    <div style="text-align:center; margin: 20px 0;">
        <h2 style="color: #CD5C5C;">Computer Wins the Match</h2>
        <p style="font-size: 1.2em;">Better luck next time!</p>
    </div>
    """, unsafe_allow_html=True)

# Game stats
if st.session_state.game_count > 0:
    st.markdown("""
    <div style="margin-top: 30px; background-color: #f8f9fa; padding: 15px; border-radius: 10px;">
        <h3 style="text-align: center;">Game Statistics</h3>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        win_rate = (st.session_state.user_score / st.session_state.game_count) * 100
        st.metric("Win Rate", f"{win_rate:.1f}%")
    with col2:
        tie_rate = (st.session_state.ties / st.session_state.game_count) * 100
        st.metric("Tie Rate", f"{tie_rate:.1f}%")
    
    st.markdown("</div>", unsafe_allow_html=True)

# Reset button
if st.button("Reset Game"):
    reset_game()