# collatz-visualizer

A simple visualizer of the Collatz Conjecture (The 3x+1 problem)

## Defining the Collatz Conjecture

The Collatz Conjecture states that:

- If the number is even, divide it by 2
- If the number is odd, multiply it by 3 and add one
- Repeat

For "almost all" positive integers, it will converge to 1. Just ONE integer that doesn't converge, a counterexample, will result in the Collatz Conjecture falling apart. But no one has been able to either prove or disprove it

This visualizer hopes to serve as a simple visualizer for how volatile numbers will "move" following this conjecture

## Installation

```bash
> git clone git@github.com:L23de/collatz-visualizer.git
> cd collatz-visualizer
> pip install pipenv
> pipenv install
```

This clones the repo to your local machine, as well as sets up a virtual environment and installs the appropriate dependencies required

To run the visualizer, simply run the following command:

```bash
streamlit run app.py
```

[Streamlit](https://streamlit.io/), the engine behind the webapp will launch it on port 8501 by default on localhost. You should get output in the terminal to get to http://localhost:8501

Inspired by [Vertasium's](https://www.youtube.com/watch?v=094y1Z2wpJg) video on the subject