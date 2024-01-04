-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: horizon_restaurants
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `allergens`
--

DROP TABLE IF EXISTS `allergens`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `allergens` (
  `allergen_id` int NOT NULL,
  `allergen_name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`allergen_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `allergens`
--

LOCK TABLES `allergens` WRITE;
/*!40000 ALTER TABLE `allergens` DISABLE KEYS */;
INSERT INTO `allergens` VALUES (1,'Gluten'),(2,'Lupin'),(3,'Celery'),(4,'Crustaceans'),(5,'Milk'),(6,'Sulpher Dioxide'),(7,'Sesame'),(8,'Molluscs'),(9,'Mustard'),(10,'Nuts'),(11,'Eggs'),(12,'Fish'),(13,'Soybeans'),(14,'Peanuts'),(15,'None');
/*!40000 ALTER TABLE `allergens` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `branch_cities`
--

DROP TABLE IF EXISTS `branch_cities`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `branch_cities` (
  `city_id` int NOT NULL,
  `city_name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`city_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `branch_cities`
--

LOCK TABLES `branch_cities` WRITE;
/*!40000 ALTER TABLE `branch_cities` DISABLE KEYS */;
INSERT INTO `branch_cities` VALUES (1,'Birmingham'),(2,'Bristol'),(3,'Cardiff'),(4,'Glasgow'),(5,'Manchester'),(6,'Nottingham'),(7,'London');
/*!40000 ALTER TABLE `branch_cities` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `branch_locations`
--

DROP TABLE IF EXISTS `branch_locations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `branch_locations` (
  `branch_id` int NOT NULL AUTO_INCREMENT,
  `branch_postcode` varchar(45) NOT NULL,
  `city_id` int NOT NULL,
  PRIMARY KEY (`branch_id`),
  KEY `city_id_idx` (`city_id`),
  CONSTRAINT `city_id` FOREIGN KEY (`city_id`) REFERENCES `branch_cities` (`city_id`)
) ENGINE=InnoDB AUTO_INCREMENT=55 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `branch_locations`
--

LOCK TABLES `branch_locations` WRITE;
/*!40000 ALTER TABLE `branch_locations` DISABLE KEYS */;
INSERT INTO `branch_locations` VALUES (1,'B1 1AA',1),(2,'B2 8HH',1),(3,'BS1 2BB',2),(4,'BS3 9II',2),(5,'CF1 3CC',3),(6,'CF3 0JJ',3),(7,'G1 4DD',4),(8,'G2 5EE',4),(9,'M1 5EE',5),(10,'M2 6FF',5),(11,'NG1 6FF',6),(12,'NG2 7GG',6),(13,'W1 7GG',7),(14,'W2 8HH',7);
/*!40000 ALTER TABLE `branch_locations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `customer_id` int NOT NULL,
  `first_name` varchar(45) DEFAULT NULL,
  `last_name` varchar(45) DEFAULT NULL,
  `phone_number` char(10) DEFAULT NULL,
  `allergen_id` int NOT NULL,
  PRIMARY KEY (`customer_id`),
  KEY `customer_allergens_idx` (`allergen_id`),
  CONSTRAINT `allergens_id` FOREIGN KEY (`allergen_id`) REFERENCES `allergens` (`allergen_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (1,'Binayam','Gurung','2147483647',15),(2,'Bob','Gurung','7407385753',2);
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `menu_allergens`
--

DROP TABLE IF EXISTS `menu_allergens`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `menu_allergens` (
  `menu_allergen_id` int NOT NULL AUTO_INCREMENT,
  `menu_item_id` int DEFAULT NULL,
  `allergen_id` int DEFAULT NULL,
  PRIMARY KEY (`menu_allergen_id`),
  KEY `menu_item_id_idx` (`menu_item_id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `menu_allergens`
--

LOCK TABLES `menu_allergens` WRITE;
/*!40000 ALTER TABLE `menu_allergens` DISABLE KEYS */;
INSERT INTO `menu_allergens` VALUES (1,1,5),(2,2,15),(3,3,15),(4,4,15),(5,5,15),(6,6,15),(7,7,15),(8,8,15),(9,9,5),(10,9,11),(11,9,1),(12,10,15),(13,11,15),(14,12,15),(15,13,15),(16,14,15),(17,16,5),(18,17,5),(19,18,5),(20,19,5),(21,20,5),(22,21,15),(23,22,15),(24,23,15),(25,24,15),(26,25,15),(27,20,15),(28,16,2),(29,17,2),(30,18,2),(31,19,2),(32,20,2),(33,19,6);
/*!40000 ALTER TABLE `menu_allergens` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `menu_items`
--

DROP TABLE IF EXISTS `menu_items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `menu_items` (
  `menu_item_id` int NOT NULL,
  `photo_url` varchar(4000) DEFAULT NULL,
  `item_name` varchar(45) DEFAULT NULL,
  `description` varchar(256) DEFAULT NULL,
  `price` float DEFAULT NULL,
  `category` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`menu_item_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `menu_items`
--

LOCK TABLES `menu_items` WRITE;
/*!40000 ALTER TABLE `menu_items` DISABLE KEYS */;
INSERT INTO `menu_items` VALUES (1,NULL,'Chicken Tenders','Six delicious, crispy chicken tenders.',13.5,'Main'),(2,NULL,'Chicken Wrap','Chicken wrap with a variety of vegetables.',11,'Main'),(3,NULL,'Chicken Burger','Very good chicken burger.',15.5,'Main'),(4,NULL,'Chicken Popcorn','Very nice bite-sized chicken popcorn.',6,'Main'),(5,NULL,'Chicken Shwarma','Amazing chicken shwarma.',17.55,'Main'),(6,NULL,'Salad Bowl','Very healthy salad bowl with a touch of vinegar.',5,'Side'),(7,NULL,'Fries','Freshly made fries.',4.65,'Side'),(8,NULL,'Sweet Potato Fries','Similar to regular fries but made with fresh sweet potatoes.',7,'Side'),(9,NULL,'Halloumi Sticks','Seven very nice halloumi sticks.',6.75,'Side'),(10,NULL,'Rice','Very fresh and fluffy rice.',5.5,'Side'),(11,NULL,'Coca Cola','Classic bottle of Coca Cola.',2,'Drink'),(12,NULL,'Sprite','Can of refreshing Sprite.',2,'Drink'),(13,NULL,'Orange Juice','Fresh orange juice from the fridge.',3.5,'Drink'),(15,NULL,'Pomegranate Juice','Homemade pomegranate juice.',5,'Drink'),(16,NULL,'Vanilla Icecream','A scoop of delicious vanilla ice cream.',6.5,'Dessert'),(17,NULL,'Chocolate Icecream','A scoop of rich chocolate ice cream.',6.5,'Dessert'),(18,NULL,'Strawberry Icecream','A scoop of refreshing strawberry ice cream.',6.5,'Dessert'),(19,NULL,'Tiramisu','Very nice tiramisu made with coffee from coffee beans.',9,'Dessert'),(20,NULL,'Cheesecake','Homemade cheesecake.',7,'Dessert'),(21,NULL,'Butternut Squash Soup','Nice and comforting butternut squash soup.',13,'Soup'),(22,NULL,'Creamy Wild Rice Soup','Good creamy soup with wild rice.',13,'Soup'),(23,NULL,'Potato Leek Soup','Amazing potato leek soup.',13,'Soup'),(24,NULL,'Broccoli Cheddar Soup','Magnificent broccoli cheddar soup.',13,'Soup'),(25,NULL,'White Bean Soup','Marvellous soup made with white beans.',13,'Soup');
/*!40000 ALTER TABLE `menu_items` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders` (
  `order_id` int NOT NULL,
  `order_date` date DEFAULT NULL,
  `reservation_id` int DEFAULT NULL,
  `order_time` time DEFAULT NULL,
  PRIMARY KEY (`order_id`),
  KEY `reservation_id_idx` (`reservation_id`),
  CONSTRAINT `reservation_id` FOREIGN KEY (`reservation_id`) REFERENCES `reservations` (`reservation_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payments`
--

DROP TABLE IF EXISTS `payments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `payments` (
  `payment_id` int NOT NULL AUTO_INCREMENT,
  `customer_id` int NOT NULL,
  `order_id` int NOT NULL,
  `total_price` int DEFAULT NULL,
  PRIMARY KEY (`payment_id`),
  KEY `customer_id_idx` (`customer_id`),
  KEY `order_id_idx` (`order_id`),
  CONSTRAINT `customer_id` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`customer_id`),
  CONSTRAINT `order_id` FOREIGN KEY (`order_id`) REFERENCES `orders` (`order_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payments`
--

LOCK TABLES `payments` WRITE;
/*!40000 ALTER TABLE `payments` DISABLE KEYS */;
/*!40000 ALTER TABLE `payments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reservations`
--

DROP TABLE IF EXISTS `reservations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reservations` (
  `reservation_id` int NOT NULL,
  `date` date DEFAULT NULL,
  `time` time DEFAULT NULL,
  `table_number` int DEFAULT NULL,
  `branch_id` int DEFAULT NULL,
  PRIMARY KEY (`reservation_id`),
  KEY `branch_id_idx` (`branch_id`),
  CONSTRAINT `branch_id` FOREIGN KEY (`branch_id`) REFERENCES `reservations` (`reservation_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reservations`
--

LOCK TABLES `reservations` WRITE;
/*!40000 ALTER TABLE `reservations` DISABLE KEYS */;
INSERT INTO `reservations` VALUES (1,'2023-05-28','10:30:12',42,1);
/*!40000 ALTER TABLE `reservations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `staff`
--

DROP TABLE IF EXISTS `staff`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `staff` (
  `staff_idx` int NOT NULL,
  `first_name` varchar(45) NOT NULL,
  `last_name` varchar(45) NOT NULL,
  `staff_id_number` int NOT NULL AUTO_INCREMENT,
  `staff_id_password` varchar(256) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `email` varchar(45) DEFAULT NULL,
  `branch_role` int NOT NULL,
  `branch_id` int DEFAULT NULL,
  PRIMARY KEY (`staff_idx`),
  UNIQUE KEY `account_number_UNIQUE` (`staff_id_number`),
  UNIQUE KEY `account_password_UNIQUE` (`staff_id_password`),
  KEY `branch_id_idx` (`branch_id`)
) ENGINE=InnoDB AUTO_INCREMENT=123461 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `staff`
--

LOCK TABLES `staff` WRITE;
/*!40000 ALTER TABLE `staff` DISABLE KEYS */;
INSERT INTO `staff` VALUES (1,'Binayam','Gurung',123456,'chickeneater','1234567',NULL,1,4),(2,'Reece','Turner',123459,'coder','1234568',NULL,5,2),(3,'Milo','Carroll',123460,'noclue','1234153',NULL,1,5),(4,'staff','user',1,'grenade','999999',NULL,1,3),(5,'chef','user',2,'asdasd','123123123',NULL,2,8);
/*!40000 ALTER TABLE `staff` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-01-04 19:46:55
