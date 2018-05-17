# Tic-Tac-Toe: Remastered
Tic-Tac-Toe game written in Python 3.

## Features
- configurable grid size (3-10),
- configurable number of players,
- configurable player characters,
- a bit stupid AI.

## Requirements
- Python 3
- pytest (for testing)

## Quick start
Create `config.json` file in project root and copy the contents from `example_config.py`.

Note: Don't delete nor modify `example_config.py` - it is used for tests.

Go to project root and run:
`python run.py`

## Development Installation
Go to project root and run:
`pip install . -e`
Now you can import the game from anywhere with:
`import tictactoe`
You can also run it from command line with:
`ttt`

## Testing
Make sure pytest is installed:
`pip install -U pytest`
Navigate to project root and run:
`pytest -v`
