import sass

# How to use:
# Set scss_filepath and output_filepath at the bottom of this file
# python build.py

def convert_scss_to_css(scss_filepath, output_filepath):
    print("Compiling scss...")
    assert scss_filepath.endswith('.scss')
    assert output_filepath.endswith('.css')
    # create normal .css file
    css_data = sass.compile(filename=scss_filepath, output_style='expanded')
    write_string_file(output_filepath, css_data)
    # create compressed .min.css
    min_output_filepath = output_filepath[:-4] + ".min.css"
    css_data_min = sass.compile(
        filename=scss_filepath, output_style='compressed')
    write_string_file(min_output_filepath, css_data_min)
    print("Done ["+output_filepath + "] and [" +
          min_output_filepath + "] created.")


def write_string_file(output_path, string_data):
    with open(output_path, "wb") as output_file:
        output_file.write(string_data.encode("utf-8"))


if __name__ == '__main__':
    convert_scss_to_css('src/styles.scss', 'dist/styles.css')
