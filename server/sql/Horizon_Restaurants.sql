-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: horizon_restaurants
-- ------------------------------------------------------
-- Server version	8.0.33

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
INSERT INTO `allergens` VALUES (1,'Gluten'),(2,'Lupin'),(3,'Celery'),(4,'Crustaceans'),(5,'Milk'),(6,'Sulpher Dioxide'),(7,'Sesame'),(8,'Molluscs'),(9,'Mustard'),(10,'Nuts'),(11,'Egg'),(12,'Fish'),(13,'Soybeans'),(14,'Peanuts'),(15,'None');
/*!40000 ALTER TABLE `allergens` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `branch_tables`
--

DROP TABLE IF EXISTS `branch_tables`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `branch_tables` (
  `table_id` int NOT NULL,
  `branch_id` int DEFAULT NULL,
  `table_capacity` int DEFAULT NULL,
  PRIMARY KEY (`table_id`),
  KEY `branch_id_idx` (`branch_id`),
  CONSTRAINT `branch_id` FOREIGN KEY (`branch_id`) REFERENCES `branches` (`branch_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `branch_tables`
--

LOCK TABLES `branch_tables` WRITE;
/*!40000 ALTER TABLE `branch_tables` DISABLE KEYS */;
/*!40000 ALTER TABLE `branch_tables` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `branches`
--

DROP TABLE IF EXISTS `branches`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `branches` (
  `branch_id` int NOT NULL AUTO_INCREMENT,
  `branch_postcode` varchar(45) NOT NULL,
  `city_id` int NOT NULL,
  PRIMARY KEY (`branch_id`),
  KEY `city_id_idx` (`city_id`),
  CONSTRAINT `city_id` FOREIGN KEY (`city_id`) REFERENCES `cities` (`city_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `branches`
--

LOCK TABLES `branches` WRITE;
/*!40000 ALTER TABLE `branches` DISABLE KEYS */;
/*!40000 ALTER TABLE `branches` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cities`
--

DROP TABLE IF EXISTS `cities`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cities` (
  `city_id` int NOT NULL,
  `city_name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`city_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cities`
--

LOCK TABLES `cities` WRITE;
/*!40000 ALTER TABLE `cities` DISABLE KEYS */;
INSERT INTO `cities` VALUES (1,'Birmingham'),(2,'Bristol'),(3,'Cardiff'),(4,'Glasgow'),(5,'Manchester'),(6,'Nottingham'),(7,'London');
/*!40000 ALTER TABLE `cities` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `customer_id` int NOT NULL,
  `customer_firstname` varchar(45) DEFAULT NULL,
  `customer_lastname` varchar(45) DEFAULT NULL,
  `customer_phone` char(10) DEFAULT NULL,
  `customer_allergens` int NOT NULL,
  PRIMARY KEY (`customer_id`),
  KEY `customer_allergens_idx` (`customer_allergens`),
  CONSTRAINT `customer_allergens` FOREIGN KEY (`customer_allergens`) REFERENCES `allergens` (`allergen_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (1,'Binayam Gurung',NULL,'2147483647',15),(2,'Bob Gurung',NULL,'7407385753',2);
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inventory`
--

DROP TABLE IF EXISTS `inventory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inventory` (
  `inventory_id` int NOT NULL,
  `stock_item_name` varchar(45) NOT NULL,
  `availability` int NOT NULL,
  `cost_per_item` float DEFAULT NULL,
  PRIMARY KEY (`inventory_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventory`
--

LOCK TABLES `inventory` WRITE;
/*!40000 ALTER TABLE `inventory` DISABLE KEYS */;
/*!40000 ALTER TABLE `inventory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `menu`
--

DROP TABLE IF EXISTS `menu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `menu` (
  `menu_item_id` int NOT NULL,
  `item_name` varchar(45) DEFAULT NULL,
  `price` float DEFAULT NULL,
  `description` varchar(45) DEFAULT NULL,
  `category` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`menu_item_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `menu`
--

LOCK TABLES `menu` WRITE;
/*!40000 ALTER TABLE `menu` DISABLE KEYS */;
INSERT INTO `menu` VALUES (1,'Chicken Tenders',13.5,'6 Delicious Tenders','Main'),(2,'Chicken Wrap',11,'Chicken Wrap with vegetables','Main'),(3,'Chicken Burger',15.5,'Very good chicken burger','Main'),(4,'Chicken Popcorn',6,'Very nice chicken popcorn','Main'),(5,'Chicken Shwarma',17.55,'Amazing Chicken Shwarma','Main'),(6,'Salad Bowl',5,'Very healthy salad bowl with some vinegar','Side'),(7,'Fries',4.65,'Fresh Fries','Side'),(8,'Sweet Potato Fries',7,'Same as fries but fresh sweet potato instead','Side'),(9,'Halloumi Sticks',6.75,'7 Very nice halloumi sticks','Side'),(10,'Rice',5.5,'Very fresh rice','Side'),(11,'Coca Cola',2,'Bottle of coca cola','Drink'),(12,'Sprite',2,'Can of Sprite','Drink'),(13,'Orange Juice',3.5,'Fresh Orange juice from fridge','Drink'),(15,'Pomegranate Juice',5,'Homemade pomegranate juice','Drink'),(16,'Vanilla Icecream',6.5,'Scoop of vanilla icecream','Dessert'),(17,'Chocolate Icecream',6.5,'Scoop of chocolate icecream','Dessert'),(18,'Strawberry Icecream',6.5,'Scoop of strawberry icecream','Dessert'),(19,'Tiramisu',9,'Very Nice Tiramisu made with coffee from coff','Dessert'),(20,'Cheesecake',7,'Homemade Cheesecake','Dessert'),(21,'Butternut Squash Soup',13,'Nice Soup','Soup'),(22,'Creamy Wild Rice Soup',13,'Good Soup','Soup'),(23,'Potato Leek Soup',13,'Amazing Soup','Soup'),(24,'Broccoli Cheddar Soup',13,'Magnificient Soup','Soup'),(25,'White Bean Soup',13,'Marvellous Soup','Soup');
/*!40000 ALTER TABLE `menu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders` (
  `order_id` int NOT NULL,
  `reservation_id` int DEFAULT NULL,
  `menu_item_id` int NOT NULL,
  PRIMARY KEY (`order_id`),
  KEY `item_id_idx` (`menu_item_id`),
  KEY `reservation_id_idx` (`reservation_id`),
  CONSTRAINT `menu_item_id` FOREIGN KEY (`menu_item_id`) REFERENCES `menu` (`menu_item_id`),
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
  `reservation_Id` int NOT NULL,
  `order_id` int NOT NULL,
  `total_price` int DEFAULT NULL,
  PRIMARY KEY (`payment_id`),
  KEY `customer_id_idx` (`customer_id`),
  KEY `reservation_id_idx` (`reservation_Id`),
  KEY `order_id_idx` (`order_id`),
  CONSTRAINT `customer_id` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`customer_id`),
  CONSTRAINT `order_id` FOREIGN KEY (`order_id`) REFERENCES `orders` (`order_id`),
  CONSTRAINT `reservaton_id` FOREIGN KEY (`reservation_Id`) REFERENCES `reservations` (`reservation_id`)
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
  `table_id` int DEFAULT NULL,
  `date` date DEFAULT NULL,
  `time` time DEFAULT NULL,
  `created_by_staff_idx` int DEFAULT NULL,
  PRIMARY KEY (`reservation_id`),
  KEY `table_id_idx` (`table_id`),
  KEY `created_by_staff_id_idx` (`created_by_staff_idx`),
  CONSTRAINT `created_by_staff_id` FOREIGN KEY (`created_by_staff_idx`) REFERENCES `staff` (`staff_idx`),
  CONSTRAINT `table_id` FOREIGN KEY (`table_id`) REFERENCES `branch_tables` (`table_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reservations`
--

LOCK TABLES `reservations` WRITE;
/*!40000 ALTER TABLE `reservations` DISABLE KEYS */;
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
  `staff_first_name` varchar(45) NOT NULL,
  `staff_last_name` varchar(45) NOT NULL,
  `staff_phone` int NOT NULL,
  `branch_role` int NOT NULL,
  `account_number` int NOT NULL AUTO_INCREMENT,
  `account_password` varchar(256) NOT NULL,
  PRIMARY KEY (`staff_idx`),
  UNIQUE KEY `account_number_UNIQUE` (`account_number`),
  UNIQUE KEY `account_password_UNIQUE` (`account_password`)
) ENGINE=InnoDB AUTO_INCREMENT=123461 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `staff`
--

LOCK TABLES `staff` WRITE;
/*!40000 ALTER TABLE `staff` DISABLE KEYS */;
INSERT INTO `staff` VALUES (1,'Binayam','Gurung',1234567,1,123456,'chickeneater'),(2,'Reece ','Turner',1234568,1,123459,'coder'),(3,'Bob','Chicken',1234153,1,123460,'noclue');
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

-- Dump completed on 2023-12-29 20:15:47
