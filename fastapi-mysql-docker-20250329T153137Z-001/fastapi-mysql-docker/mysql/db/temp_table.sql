CREATE TABLE `product` (
  `id` int NOT NULL AUTO_INCREMENT,
  `IceCreamName` varchar(256) NOT NULL,
  `ToppingName` varchar(256) NOT NULL,
  `Size` varchar(256) NOT NULL,
  `Price` float,

  PRIMARY KEY (`id`)
);