import os

def format_textfile(txtfile):
    text = txtfile.read()
    translate_checkbox_to_bullet(text)

def translate_checkbox_to_bullet(text):
    replaced_text = text.replace('[ ]', '').replace('[x]', '')
    output_txt_file(replaced_text)

def output_txt_file(text):
    with open('src/formatted_text.txt', mode='w') as t:
        t.write(text)
        print('Complete. Please check src/formatted_text.txt')
        print('-----------------------------------------------')
        print(text)
        print('-----------------------------------------------')

print('Start to convert...')
f = open('src/text.txt')
format_textfile(f)
f.close()
