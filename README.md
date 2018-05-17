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

## Development

### Quick Start
Create `config.json` file in project root and copy the contents from `config_example.py`.

*Note:* Don't delete/modify `config_example.py` - it is used for tests.

Go to project root and run:
`python run.py`

### Development Installation
Create a new virtualenv, go to project root and run:
`python install setup.py`

Now you can run the game from anywhere with:
`ttt`

Or import it with:
`import tictactoe`

### Testing
Make sure pytest is installed:
`pip install pytest`

Navigate to project root and run:
`pytest -v`

For test coverage install pytest-cov:
`pip install pytest-cov`

Run the tests with:
`pytest -v --cov=tictactoe`

## Deployment
Clone project on target machine, go to project root and run:
`python setup.py install`

After installation, you should see the `site-packages` folder, where the game was installed on your system.

For example: `C:\Users\m\AppData\Local\Programs\Python\Python36-32\Lib\site-packages\tictactoe-1.0.0-py3.6.egg`

Create `config.json` file in this directory, copying the config from `config_example.json` and modifying as you wish.

Start the game fro anywhere in your system with: `ttt`.
