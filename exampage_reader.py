from lxml import etree

file_url = input('本地网页文档:')

fp = open(file_url, 'rb')
page_text = fp.read().decode('utf-8')
fp.close()

tree = etree.HTML(page_text)

imfor1 = tree.xpath('//div[@class="CyBottom"]//div[@class="fl"]/text()')
imfor2 = tree.xpath('//div[@class="CyBottom"]//div[@class="fl"]/p/text()')

with open('text.txt', 'w', encoding='utf-8') as fp:
    for text in imfor1+imfor2:
        fp.write(text + '\n')