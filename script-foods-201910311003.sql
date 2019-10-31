DROP TABLE IF EXISTS `a_substitute`;
DROP TABLE IF EXISTS `category`;
DROP TABLE IF EXISTS `food`;

CREATE TABLE `a_substitute` (
  `id_food food` int(10) NOT NULL,
  `id_food substitute` int(10) NOT NULL,
  PRIMARY KEY (`id_food food`,`id_food substitute`),
  KEY `id_food substitute` (`id_food substitute`),
  CONSTRAINT `a_substitute_ibfk_1` FOREIGN KEY (`id_food food`) REFERENCES `food` (`id_food`),
  CONSTRAINT `a_substitute_ibfk_2` FOREIGN KEY (`id_food substitute`) REFERENCES `food` (`id_food`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE `category` (
  `id_category` int(10) NOT NULL AUTO_INCREMENT,
  `name` text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `url_category` text NOT NULL,
  PRIMARY KEY (`id_category`)
) ENGINE=InnoDB AUTO_INCREMENT=147 DEFAULT CHARSET=utf8;


CREATE TABLE `food` (
  `id_food` int(10) NOT NULL AUTO_INCREMENT,
  `product_name` varchar(300) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `generic_name` text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `stores_tags` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `url` varchar(300) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `nutrition_grades` int(11) NOT NULL,
  `id_category` int(10) NOT NULL,
  PRIMARY KEY (`id_food`),
  UNIQUE KEY `product_name` (`product_name`,`nutrition_grades`,`url`,`id_category`),
  KEY `id_category` (`id_category`),
  CONSTRAINT `food_ibfk_1` FOREIGN KEY (`id_category`) REFERENCES `category` (`id_category`)
) ENGINE=InnoDB AUTO_INCREMENT=17321 DEFAULT CHARSET=utf8;

