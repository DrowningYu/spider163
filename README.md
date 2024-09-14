# spider163

视频展示效果 https://www.bilibili.com/video/BV1uJtPe9E1Q/

AE脚本-爬取网易云歌词，输出成AE合成中的文字图层


需要安装python3
以及

pip install requests

pip install beautifulsoup4

pip install lxml


脚本可以支持输入网易云的单曲链接，歌单链接和专辑链接。(歌单和专辑仅支持前10首的加载)
整个脚本非常脆弱
点了应用之后不要再乱点其他东西，不然AE很容易崩溃。
歌单和专辑里面的单曲不要太多，5首就可以了，不然加载的非常非常非常慢，还容易崩溃。

个别单曲不能加载，懒得找原因了。有bug也不想修了

注：其实这是我23年的爬虫结课作业 原本的功能是只能把单曲的歌词爬下来 但是我怕分量不够 所以就加了很多臃肿的功能，最后就变成了这样
