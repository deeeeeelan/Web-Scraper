#
# TABLE STRUCTURE FOR: scraped
#

DROP TABLE IF EXISTS `scraped`;

CREATE TABLE `scrapex` (
  `links` varchar(255) NOT NULL,
  `name` varchar(100) NOT NULL,
  `type` varchar(40) NOT NULL,
  `price` int(10) NOT NULL,
  `address` varchar(150) NOT NULL,
  `built_up` varchar(13) NOT NULL,
  `land_area` varchar(13) NOT NULL,
  `bedrooms` varchar(2) NOT NULL,
  `bathrooms` varchar(2) NOT NULL,
  `monthly_installment` varchar(15) NOT NULL,
  `land_title` varchar(20) NOT NULL,
  `tenure` varchar(25) NOT NULL,
  `price_per_sqft` varchar(18) NOT NULL,
  `maintenance_fee` varchar(2) NOT NULL,
  `furnishing` varchar(25) NOT NULL,
  `state` varchar(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

