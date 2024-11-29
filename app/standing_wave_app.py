import sys
import numpy as np
import streamlit as st

sys.path.insert(0, '..')
import standing_wave as chl

@st.cache_data
def calculate_image(size, a, b, m, n, cutoff, stable_point_value, source_location: chl.VibrationSourceLocation) -> np.ndarray:
    I = chl.wave_intensity_array(size, a, b, m, n, source_location)

    I[abs(I) <= cutoff] = stable_point_value  # make stable points stand out by setting them to a huge value
    I = (I / I.max() * 255).astype(np.uint8)  # normalize
    return 255-I

def run():
    st.set_page_config(page_title='Standing wave pattern simulation')
    sb = st.sidebar

    sb.title('Options')
    a_col, b_col = sb.columns(2)
    size = a_col.number_input('Resolution', value=1200, min_value=12, max_value=2400)
    source_location = b_col.selectbox('Source Y coordinate', ['Bottom', 'Mid'])
    if source_location == 'Bottom':
        source_location = chl.VibrationSourceLocation.CORNER
    else:
        source_location = chl.VibrationSourceLocation.MID
    cutoff = float(a_col.text_input('Cutoff (default: π/42)', value=round(np.pi/42, 6)))
    stable_value = b_col.number_input('Value for stable points', value=255, min_value=0)
    a = a_col.number_input('a', value=1.0)
    b = b_col.number_input('b', value=1.0)
    m = a_col.number_input('m', value=8, min_value=1, max_value=1000)
    n = b_col.number_input('n', value=8, min_value=1, max_value=1000)

    image = calculate_image(size, a, b, m, n, cutoff, stable_value, source_location)
    st.image(image, output_format='PNG', use_column_width=True)


if __name__ == '__main__':
    run()