# print_in_box('To boldly go where no one has gone before.')

# further exploration
#lets say i have 90 char
# need to bread into 3 lines
def print_in_box(txt):
    if len(txt) <= 40:
        print (f'+-{"-"*(len(txt))}-+\n'
            f'| {" "*(len(txt))} |\n'
            f'| {txt} |\n'
            f'| {" "*(len(txt))} |\n'
            f'+-{"-"*(len(txt))}-+\n'
            )
    
    else:
        print (
            f'+-{"-"*40}-+\n'
            f'| {" "*40} |'
            )
        
        line_start = 0
        line_end = 40
        while len(txt) > line_start:
            new_line = txt[line_start:line_end]
            print(f'| {new_line}{" "*(40-len(new_line))} |')
            line_start += 40
            line_end += 40
        
        print (
            f'| {" "*40} |\n'
            f'+-{"-"*40}-+\n'
            )

txt = 'For a challenging but fun exercise, try word wrapping messages that are too long to fit, so that they appear on multiple lines but are still contained within the box. This isnt an easy problem, but its doable with basic Python'

print_in_box(txt)

    

