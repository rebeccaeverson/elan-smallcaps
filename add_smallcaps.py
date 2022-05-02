'''
STEPS:
    - Script input: text file, tier name, file with grammatical elements
    - Read text file
    - Read grammatical elements file into a list
    - Find tier
    - Get text from that tier
    - Find grammatical elements by looping through grammatical elements file values
    - Replace text in that tier with grammatical elements in \textsc
    
Challenges:
    - Sometimes the tier goes onto the next line
    - Some glossing tiers have words separated with tabs, others don't - how to maintain spacing in output?
    - Different element separators: -, :
'''

import sys
import re


def replace_regex(text, element_regex):
    return re.sub(element_regex, r'\1\\textsc{\2}', text)

if __name__ == "__main__":
    if len(sys.argv) < 4:
        sys.exit(f"Usage: {sys.argv[0]} file tier elements_file")

    tier_name = sys.argv[2]
    gram_elements_file = sys.argv[3]
    gram_elements = []

    with open(gram_elements_file, 'r') as f:
        for line in f:
            gram_elements.append(line.strip())
    element_regex = '|'.join(re.escape(element) for element in gram_elements)
    # Add separators here
    element_regex = f'([-:])({element_regex})'
    
    with open(sys.argv[1], "r", encoding='utf-8') as f:
        # TODO: Make this its own function
        found_end = True
        new_text = []
        for line in f:
            if found_end:
                key_value = line.strip().split('\t')
                key = key_value[0].strip()
                if key == tier_name:
                    found_end = False
                    for value in key_value[1:]:
                        new_text.append(replace_regex(value, element_regex))
            else:
                if line.startswith('\t'):
                    new_text.append(replace_regex(line.strip(), element_regex))
                else:
                    print(' '.join(new_text))
                    found_end = True
                    new_text = []