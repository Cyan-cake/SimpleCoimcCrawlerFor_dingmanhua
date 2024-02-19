from pathlib import Path
from ebooklib import epub

book = epub.EpubBook()
book.set_identifier('ByCyanCakeOnly')
book.set_title('葬送的芙莉莲')
book.set_language('en')

cover_image = 'pictures/动画新视觉图/image_8.jpg'
book.set_cover(file_name='cover.jpg', content=open(cover_image, 'rb').read())

parent_folder = Path('pictures')

entries = list(parent_folder.iterdir())
sorted_entries = sorted(entries, key=lambda x: x.stat().st_ctime, reverse=False)

for entry in sorted_entries:
    if entry.is_dir():
        print(entry.name)

        body = ""

        imageList = Path(entry).glob('*.jpg')
        sorted_imageList = sorted(imageList,  key=lambda x: x.stat().st_mtime, reverse=False)

        for index, image in enumerate(sorted_imageList):
            body += f"<img src=\"{entry.name}image{index}.jpg\" alt=\"Sample Image\">"
            epub_image = epub.EpubItem(file_name=f'{entry.name}image{index}.jpg', media_type='image/jpg', content=open(image, 'rb').read())
            book.add_item(epub_image)

        chapter = epub.EpubHtml(title=entry.name, file_name=f'{entry.name}.xhtml', lang='zh')
        chapter.content = f'<html><body>{body}</body></html>'

        book.toc.append(chapter)
        book.add_item(chapter)

book.add_item(epub.EpubNcx())
book.add_item(epub.EpubNav())

book.spine = ['nav'] + book.toc
epub.write_epub('葬送的芙莉莲.epub', book, {})