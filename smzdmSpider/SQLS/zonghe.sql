use SmzdmSpider;

DROP TABLE IF EXISTS `zong_he`;

SET @saved_cs_client = @@character_set_client;
SET CHARACTER_SET_CLIENT = utf8;

CREATE TABLE `zong_he` (
  `ID` INT(11) NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(30) NOT NULL DEFAULT '没有',
  `tag` VARCHAR(10) NOT NULL DEFAULT '没有',
  `image` VARCHAR(2083) NOT NULL DEFAULT '没有照片',
  `discounts` VARCHAR(100) NOT NULL DEFAULT '没有优惠',
  `description` TEXT(200) NOT NULL DEFAULT '没有描述',
  `goods` INT(10) NOT NULL DEFAULT 0,
  `bads` INT(10) NOT NULL DEFAULT 0,
  `stars` INT(10) NOT NULL DEFAULT 0,
  `comments` INT(10) NOT NULL DEFAULT 0,
  `time` VARCHAR(20) NOT NULL DEFAULT '没有时间信息',
  `provider` VARCHAR(20) NOT NULL DEFAULT '没有提供商信息',
  `purchase_link` VARCHAR(2083) NOT NULL DEFAULT '没有购买链接',
  PRIMARY KEY (`ID`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

SET CHARACTER_SET_CLIENT = @saved_cs_client;

# LOCK TABLES `zong_he` WRITE;
# INSERT INTO `zong_he` (title, tag, image, discounts, description, goods, bads, stars, comments, time, provider, purchase_link)
# VALUES (1, 'catfish', '8.50'),
#   (2, 'catfish', '8.50'),
#   (3, 'tuna', '8.00'),
#   (4, 'catfish', '5.00'),
#   (5, 'bass', '6.75'),
#   (6, 'haddock', '6.50'),
#   (7, 'salmon', '9.50'),
#   (8, 'trout', '6.00'),
#   (9, 'tuna', '7.50'),
#   (10, 'yellowfintuna', '12.00'),
#   (11, 'yellowfin tuna', '13.00'),
#   (12, 'tuna', '7.50');
# UNLOCK TABLES;