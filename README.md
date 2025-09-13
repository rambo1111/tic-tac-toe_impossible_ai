# 🎮 Tic-Tac-Toe + an Unbeatable AI 🧠

Welcome to a classic game of Tic-Tac-Toe with a twist: the AI opponent is literally impossible to beat. Built with the Minimax algorithm, this AI has every possible move pre-calculated, ensuring it plays a perfect game every time.

Can you outsmart a perfect machine? The best you can hope for is a draw! 🤝

---

### ✨ **[Play the game right here!](https://rambo1111.github.io/tic-tac-toe_impossible_ai/)** ✨

---

## 🤖 How the AI Thinks

This isn't your average game AI. It doesn't "think" in real-time. Instead, its perfection is achieved through a clever pre-computation process:

1.  **Game State Mapping:** Using the `Tic-Tac-Toe_State_Generator.py` script, every single possible board layout in Tic-Tac-Toe was generated.
2.  **Minimax Perfection:** For each of these 5,478 states, the Minimax algorithm was used to determine the mathematically optimal move.
3.  **The AI's "Brain":** All of these states and their corresponding best moves were then hardcoded into a giant JavaScript object inside `index.html`.
4.  **Flawless Execution:** When it's the AI's turn, it simply finds the current board configuration in its pre-computed "brain" and executes the perfect move instantly. No thinking, no delay, no mistakes. ⚡

## 🚀 Features

-   **Unbeatable Opponent:** A true challenge for any Tic-Tac-Toe enthusiast.
-   **Zero-Latency AI:** The AI's moves are instantaneous.
-   **Client-Side Only:** Runs entirely in your browser. No server or backend needed.
-   **Minimalist Design:** A clean and simple interface that lets you focus on the game.
-   **Great Learning Tool:** A fantastic demonstration of game theory and the Minimax algorithm.

## 🛠️ Technologies Used

-   **HTML5**
-   **CSS3**
-   **JavaScript**
-   **Python** (for the one-time AI move generation)

## 📂 Repository Files

-   `index.html`: The complete game, including all the UI, logic, and the AI's pre-computed moves.
-   `Tic-Tac-Toe_State_Generator.py`: The script used to create the AI's "brain." You don't need to run this to play.
-   `tictactoe_states.ttts`: This is the AI's brain.
