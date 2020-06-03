#
# TABLE STRUCTURE FOR: scraped
#

DROP TABLE IF EXISTS `scraped`;

CREATE TABLE `scraped` (
  `links` varchar(255) NOT NULL,
  `name` varchar(100) NOT NULL,
  `type` varchar(100) NOT NULL,
  `price` int(10) NOT NULL,
  `address` varchar(255) NOT NULL,
  `built_up` varchar(9) NOT NULL,
  `land_area` varchar(10) NOT NULL,
  `bedrooms` int(11) NOT NULL,
  `bathrooms` int(11) NOT NULL,
  `monthly_installment` int(11) NOT NULL,
  `land_title` int(11) NOT NULL,
  `tenure` varchar(20) NOT NULL,
  `price_per_sqft` int(7) NOT NULL,
  `maintenance_fee` int(11) NOT NULL,
  `furnishing` varchar(20) NOT NULL,
  `state` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

