import json
from googletrans import Translator

source_dir = './Tests/'
target_dir = './Tests/'
source_file = 'spells-test.json'
target_file = 'spells-pt-br-test.json'
language = 'pt_br'
letters_limit = 1029
icon = "magic-swirl"
icon_back = "magic-swirl"
color = "#4a6898"
books = ['PHB', 'XGE', 'TCE', 'FTD', 'AAG']

def translate_cards(rpg_cards, books):   
    rpg_cards_ptbr = []
    for jindex in range(len(rpg_cards)):
        lines = rpg_cards[jindex]['contents']
        title = rpg_cards[jindex]['title']
        tags = rpg_cards[jindex]['tags']
        
        ### Find the amount of lines to split card
        amount_lines = 0
        for i in  range(len(lines)):
            amount_lines = amount_lines + len(lines[i])

        ### Translate content
        for index in  range(len(lines)):
            if lines[index].find("|") > -1:
                text = lines[index].split("|", maxsplit=1)

                translator = Translator()
                translation = translator.translate(text[1], dest=language)
                pt_br = text[0] + "| "+ translation.text
                

                rpg_cards[jindex]['contents'][index] = pt_br
                
        ### Adding book's name in footer
        book = list(set(books).intersection(tags))[0]
        rpg_cards[jindex]['contents'].append("fill")
        rpg_cards[jindex]['contents'].append("text | " + book)
        
        ### Translate title
        translation = translator.translate(title, dest=language)
        rpg_cards[jindex]['title'] = translation.text
        
        
        ### Setup style
        rpg_cards[jindex]['color'] = color
        rpg_cards[jindex]['icon'] = icon
        rpg_cards[jindex]['icon_back'] = icon_back
        rpg_cards_ptbr.append(rpg_cards[jindex])
        
        ## INFORMATION
        print(rpg_cards[jindex])
        # print(rpg_cards[jindex]['title'])
        # print(amount_lines)
        ## INFORMATION
        
    return rpg_cards_ptbr



with open(source_dir+source_file) as f:
   rpg_cards = json.load(f)

rpg_cards_ptbr = translate_cards(rpg_cards, books)

# with open(target_dir+target_file, 'w') as f:
#     f.write(json.dumps(rpg_cards_ptbr))
