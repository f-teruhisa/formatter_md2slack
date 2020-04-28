"""Use to delete format markdown checkbox."""

def format_textfile(txtfile):
    """
    Read txtfile and send function for format
    """
    text = txtfile.read()
    translate_checkbox_to_bullet(text)

def translate_checkbox_to_bullet(text):
    """
    Delete checkbox of markdown into bullet(-)
    """
    replaced_text = text.replace('[ ]', '').replace('[x]', '')
    output_txt_file(replaced_text)

def output_txt_file(text):
    """
    Output formatted text to console and src/formatted_text.txt
    """
    with open('src/formatted_text.txt', mode='w') as format_text:
        format_text.write(text)
        print('Complete. Please check src/formatted_text.txt')
        print('-----------------------------------------------')
        print(text)
        print('-----------------------------------------------')

print('Start to convert...')
f = open('src/text.txt')
format_textfile(f)
f.close()
