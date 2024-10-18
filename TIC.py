import streamlit as st

# Initialize the game state
if "board" not in st.session_state:
    st.session_state.board = [' ' for _ in range(9)]
    st.session_state.current_player = "X"
    st.session_state.game_over = False
    st.session_state.winner = None

# Function to check the winner
def check_winner(board):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
        [0, 4, 8], [2, 4, 6]              # Diagonal
    ]
    
    for combination in winning_combinations:
        if board[combination[0]] == board[combination[1]] == board[combination[2]] and board[combination[0]] != ' ':
            return board[combination[0]]
    return None

# Function to check if the board is full (tie)
def check_tie(board):
    return all(spot != ' ' for spot in board)

# Reset the game
def reset_game():
    st.session_state.board = [' ' for _ in range(9)]
    st.session_state.current_player = "X"
    st.session_state.game_over = False
    st.session_state.winner = None

# Display the board
def display_board():
    board = st.session_state.board
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button(board[0], key="btn1"):
            make_move(0)
        if st.button(board[3], key="btn4"):
            make_move(3)
        if st.button(board[6], key="btn7"):
            make_move(6)
    
    with col2:
        if st.button(board[1], key="btn2"):
            make_move(1)
        if st.button(board[4], key="btn5"):
            make_move(4)
        if st.button(board[7], key="btn8"):
            make_move(7)
    
    with col3:
        if st.button(board[2], key="btn3"):
            make_move(2)
        if st.button(board[5], key="btn6"):
            make_move(5)
        if st.button(board[8], key="btn9"):
            make_move(8)

# Make a move
def make_move(index):
    if st.session_state.board[index] == ' ' and not st.session_state.game_over:
        st.session_state.board[index] = st.session_state.current_player
        winner = check_winner(st.session_state.board)
        
        if winner:
            st.session_state.winner = winner
            st.session_state.game_over = True
        elif check_tie(st.session_state.board):
            st.session_state.game_over = True
        else:
            st.session_state.current_player = "O" if st.session_state.current_player == "X" else "X"

# App title
st.title("Tic-Tac-Toe Game")

# Display current player
if not st.session_state.game_over:
    st.write(f"Current player: {st.session_state.current_player}")

# Display the board
display_board()

# Display the result after the game is over
if st.session_state.game_over:
    if st.session_state.winner:
        st.success(f"Player {st.session_state.winner} wins!")
    else:
        st.info("It's a tie!")

# Add a reset button
if st.button("Reset Game"):
    reset_game()

