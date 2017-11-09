# SmzdmSpider
什么值得买  Python 爬虫项目

## 前提
* Firefox
* Geckodriver
* Selenium

## 配置环境
* 在settings.py里面配置mysql的用户名，密码，ip，（不要动数据库名）

# 建立数据库
cd SmzdmSpider/SQLS/
mysql -uroot -p < create_database.sql
mysql -uroot -p < zonghe.sql

# Run
cd SmzdmSpider
scapy crawl zong_he_pachong
