# Generative art using the sine function
*Inspired by standing waves/[Chladni](https://en.wikipedia.org/wiki/Chladni_plate) [plates](https://www.youtube.com/watch?v=tFAcYruShow)*

## Installation/usage

This tiny project uses poetry for its dependencies. To install them, run `poetry install` in the root directory of the project. 

Then, run `streamlit run standing_wave_app.py` from the app directory.


## Demo

[waves.webm](https://github.com/user-attachments/assets/ea600124-5550-42f1-874b-acfed3f4c61d)

## Technical details

The code calculates "wave" intensity for a 2D grid of points. Parameters a, b, m, n are parameters to the expression simulating the wave.
Points with absolute intensity below the cutoff parameter will be set to "Value for stable points", then intensity is normalized and inverted.

But if you take my advice, just play with the parameters, and watch what happens :)
