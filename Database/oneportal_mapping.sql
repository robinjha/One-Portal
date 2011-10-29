CREATE DATABASE  IF NOT EXISTS `oneportal` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `oneportal`;
-- MySQL dump 10.13  Distrib 5.1.40, for Win32 (ia32)
--
-- Host: localhost    Database: oneportal
-- ------------------------------------------------------
-- Server version	5.1.51-community

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `mapping`
--

DROP TABLE IF EXISTS `mapping`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mapping` (
  `map_id` int(10) NOT NULL AUTO_INCREMENT,
  `role_id` int(10) NOT NULL,
  `user_id` int(10) NOT NULL,
  `keywords` longtext,
  `names` longtext,
  `emails` longtext,
  PRIMARY KEY (`map_id`),
  KEY `FK__roles` (`role_id`),
  KEY `FK_Mapping_user` (`user_id`),
  CONSTRAINT `FK_Mapping_user` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`),
  CONSTRAINT `FK__roles` FOREIGN KEY (`role_id`) REFERENCES `roles` (`role_id`)
) ENGINE=InnoDB AUTO_INCREMENT=50 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mapping`
--

LOCK TABLES `mapping` WRITE;
/*!40000 ALTER TABLE `mapping` DISABLE KEYS */;
INSERT INTO `mapping` VALUES (5,4,1,'student;teacher','David;Ritu','rpradhan@brandeis.edu'),(6,1,2,'CEO;student;faulty','Colon;Tim','tim@brandeis.edu'),(7,5,2,'admin','David;Cotter','test@edu.com'),(8,6,2,'student;admin\r\n','David;Cotter\r\n','test@edu.com\r\n'),(11,9,3,'creative;director;urgent','creative','deepali@gmail.com'),(12,10,3,'meeting;urgent','ritu','ritu@edu.com'),(14,12,1,'urgent;meeting','deepali;ritu','deepali@edu.com'),(19,12,2,'','','deepali'),(20,2,1,NULL,NULL,NULL),(21,3,1,NULL,NULL,NULL),(22,2,2,NULL,NULL,NULL),(23,3,2,NULL,NULL,NULL),(24,2,3,NULL,NULL,NULL),(25,3,3,NULL,NULL,NULL),(26,2,4,NULL,NULL,NULL),(27,3,4,NULL,NULL,NULL),(28,2,5,NULL,NULL,NULL),(29,3,5,NULL,NULL,NULL),(30,2,6,NULL,NULL,NULL),(31,3,6,NULL,NULL,NULL),(32,2,7,NULL,NULL,NULL),(33,3,7,NULL,NULL,NULL),(34,2,8,NULL,NULL,NULL),(35,3,8,NULL,NULL,NULL),(36,2,9,NULL,NULL,NULL),(37,3,9,NULL,NULL,NULL),(38,13,9,'urgent;student','Thanya;Thas;Cat','deepali@edu.com;ritu@edu.com'),(40,2,10,NULL,NULL,NULL),(41,3,10,NULL,NULL,NULL),(42,2,11,NULL,NULL,NULL),(43,3,11,NULL,NULL,NULL),(44,15,11,'urgent;meeting','Yogesh;Ritu','deepali@edu.com'),(45,2,12,NULL,NULL,NULL),(46,3,12,NULL,NULL,NULL),(47,2,13,NULL,NULL,NULL),(48,3,13,NULL,NULL,NULL),(49,16,13,'urgent;student','Robin;Tariff;ritu','deepali@gmail.com');
/*!40000 ALTER TABLE `mapping` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2010-12-06 22:33:40
