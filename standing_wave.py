from enum import Enum
import numpy as np
from numpy import pi, sin

class VibrationSourceLocation(Enum):
    CORNER = 0
    MID = 1


def wave_intensity(x: float, y: float, a: float, b: float, m: int, n: int) -> float:
    """ Calculates and returns the intensity for a single point with coordinates (x,y). """
    forward = a * sin(pi * n * x) * sin(pi * m * y)
    backward = b * sin(pi * m * x) * sin(pi * n * y)
    return forward+backward


def wave_intensity_for_row(x, Y, a, b, m, n) -> np.ndarray:
    """ Same as wave_intensity, just Y is a vector """
    forward = a * sin(pi * n * x) * sin(pi * m * Y)
    backward = b * sin(pi * m * x) * sin(pi * n * Y)
    return forward+backward


def wave_intensity_for_arr(X: np.ndarray, Y: np.ndarray, a: float, b: float, m: int, n: int) -> np.ndarray:
    """ Calculates and returns the intensity for all points (x,y) in X and Y."""
    X_, Y_ = np.meshgrid(X, Y)
    forward = a * sin(pi * n * X_) * sin(pi * m * Y_)
    backward = b * sin(pi * m * X_) * sin(pi * n * Y_)
    return forward+backward


def wave_intensity_array(point_count: int, a: float, b: float, m: int, n: int, source_location: VibrationSourceLocation) -> np.ndarray:
    """
    Returns wave intensity array of size (point_count, point_count).
    a, b, m, n are multipliers in the trigonometric expressions.
    Restricting m and n to integers produces "nicer" results.
    """
    if source_location == VibrationSourceLocation.CORNER:
        y_coords = np.linspace(start=0, stop=1, num=point_count)
    else:
        y_coords = np.mod(np.linspace(start=0.5, stop=1.5, num=point_count), 1)
    return wave_intensity_for_arr(X=np.linspace(start=0, stop=1, num=point_count), Y=y_coords, a=a, b=b, m=m, n=n)


if __name__ == '__main__':
    L = 600
    a = 1 # recommended: floats in [-2, 2]
    b = 1 # recommended: floats in [-2, 2]
    m = 39  # recommended: integers
    n = 71  # recommended: integers
    # print(wave_intensity(12, 14, a, b, m, n))
    I = wave_intensity_array(L, a, b, m, n, source_location=VibrationSourceLocation.CORNER)
    print(I)


