"""
A package for various console and file update messages and performance reporting.
"""

header_width = 60

def report_msg(category, item="", measure=""):
    """ Prints a formatted and indented message with three columns. """
    msg = "".join(["\t", f"{category.upper():<10} {':::'} {item:>30}: {measure}"])
    # logger.info(msg)
    print(msg)

def report_performance(category, item="", measure=""):
    """ Prints a formatted and indented message to the performance log. """
    msg = "".join(["\t", f"{category.upper():<10} {':::'} {item:>30}: {measure}"])
    performance_logger.info(msg)
    print(msg)

def format_header(header, char, width=header_width, lead_char=""):
    # Calculate the padding length on each side
    padding_length = (width - len(header)) // 2
    # Create the padded header
    formatted_header = f"{lead_char}{char * padding_length} {header} {char * padding_length}"
    # Adjust if the total length is odd
    if len(formatted_header) < width:
        formatted_header += char
    return formatted_header

def h1(header):
    """ Prints a level 1 header for output messages."""
    h1_str= format_header(header, "#")
    # logger.info(h1_str)
    return print("\n", h1_str)

def h2(header):
    """ Prints a level 2 header for output messages."""
    h2_str = format_header(header, "-")
    # logger.info(h2_str)
    return print(h2_str)
