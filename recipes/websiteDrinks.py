from drinks import driList
htmlList = []
def drinkOutput():
    for x in driList:
        print(x[1])
        # title, link, pic = x[0], x[1], x[2]
        # print(f'''<a href="{link}">{title}</a>
        # /n
        # <img src={pic}
        # ''')

drinkOutput()
