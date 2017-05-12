# Yachess: Yet Another Chess (AI)

Yachess is a simple chess game with AI inspired by this Medium article: [A step-by-step guide to building a simple chess AI](https://medium.freecodecamp.com/simple-chess-ai-step-by-step-1d55a9266977).

<img src="img/screenshot.png" width="346" height="382" />

This project is entirely for fun and learning the basics of AI such as minimax, alpha-beta pruning, etc.

### How to
To play, simply do the following from project root, assuming python3 and pip3 is already installed:
1. `git clone https://github.com/devinalvaro/yachess`
2. `cd yachess`
3. `make` (install python-chess from pip3)
4. `python3 src/game.py`

However, a simple executable file to run Yachess is to be expected in the near future.

### Todos

 - smarter AI:
   - move-ordering
   - faster move-generation
   - end-game evaluation
 - GUI:
   - log message &#10003;
   - promotion
   - moves highlight &#10003;
   - win condition
 - executable program

### License

MIT
