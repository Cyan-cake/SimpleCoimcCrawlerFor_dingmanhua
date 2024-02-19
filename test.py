import ebooklib
from ebooklib import epub

# 创建一个新的EPUB书籍
book = epub.EpubBook()

# 设置书籍的标识符、标题和语言
book.set_identifier('id123456')
book.set_title('Sample Book')
book.set_language('en')

# 添加封面图片
cover_image = 'pictures/动画新视觉图/image_8.jpg'  # 更改为你的封面图片路径
book.set_cover(file_name='cover.jpg', content=open(cover_image, 'rb').read())

# 添加一个包含图片的页面
content = epub.EpubHtml(title='Image Page', file_name='image_page.xhtml', lang='en')
content.content = '<html><body><h1>Image Page</h1><p><img src="image.jpg"></p></body></html>'

# 添加图片文件
image = 'pictures/动画新视觉图/image_8.jpg'  # 更改为你的图片路径
epub_image = epub.EpubItem(file_name='image.jpg', media_type='image/jpeg', content=open(image, 'rb').read())

# 将页面和图片添加到书籍中
book.add_item(content)
book.add_item(epub_image)

# 定义书籍结构
book.toc = (epub.Link('image_page.xhtml', 'Image Page', 'imagepage'),)
book.add_item(epub.EpubNcx())
book.add_item(epub.EpubNav())

# 设置书籍的封面和目录页为首页
book.spine = ['nav', content]

# 创建EPUB文件
epub.write_epub('sample_book.epub', book, {})
