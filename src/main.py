from textnode import TextNode


def main():
    text = "gel gamzelim"
    text_type = "italic"
    url = "www.bombabomba.com"
    textnode = TextNode(text, text_type, url)
    print(textnode)


main()

