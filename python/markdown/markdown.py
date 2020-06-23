import re

HEADER = re.compile(r'^(#{1,6}) (.*)')
STRONG = re.compile(r'(.*)__(.*)__(.*)')
EM = re.compile(r'(.*)_(.*)_(.*)')
LI_SUB = re.compile(r'^\* (.*)', flags=re.MULTILINE)
UL_WRAP = re.compile(r'(<li>.*</li>)', flags=re.DOTALL)
PLAIN_TEXT = re.compile(r'^(?!(\*|\#|<ul|<li|<h))(.*)')


def parse(markdown):
    res = ''
    matches = HEADER.search(markdown)
    if matches:
        tier = str(len(matches.group(1)))
        markdown = HEADER.sub(f'<h{tier}>' + r'\2' + f'</h{tier}>', markdown)
    markdown = STRONG.sub(r"\1<strong>\2</strong>\3", markdown)
    markdown = EM.sub(r"\1<em>\2</em>\3", markdown)
    markdown = LI_SUB.sub(r'<li>\1</li>', markdown)
    markdown = UL_WRAP.sub(r'<ul>\1</ul>', markdown)
    for line in markdown.splitlines():
        res += PLAIN_TEXT.sub(r'<p>\2</p>', line)
    return res
