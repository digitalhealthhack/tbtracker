-- MySQL dump 10.13  Distrib 5.7.12, for osx10.11 (x86_64)
--
-- Host: localhost    Database: tbtracker
-- ------------------------------------------------------
-- Server version	5.7.12

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
-- Table structure for table `who_data_dictionary`
--

DROP TABLE IF EXISTS `who_data_dictionary`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `who_data_dictionary` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `variable_name` varchar(255) DEFAULT NULL,
  `dataset` varchar(255) DEFAULT NULL,
  `code_list` varchar(255) DEFAULT NULL,
  `definition` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=328 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `who_tb_burden_countries_20160507`
--

DROP TABLE IF EXISTS `who_tb_burden_countries_20160507`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `who_tb_burden_countries_20160507` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `country` varchar(255) DEFAULT NULL,
  `iso2` varchar(255) DEFAULT NULL,
  `iso3` varchar(255) DEFAULT NULL,
  `iso_numeric` varchar(255) DEFAULT NULL,
  `who_region` varchar(255) DEFAULT NULL,
  `year` int(11) DEFAULT NULL,
  `e_pop_num` int(11) DEFAULT NULL,
  `e_prev_100k` int(11) DEFAULT NULL,
  `e_prev_100k_lo` int(11) DEFAULT NULL,
  `e_prev_100k_hi` int(11) DEFAULT NULL,
  `e_prev_num` int(11) DEFAULT NULL,
  `e_prev_num_lo` int(11) DEFAULT NULL,
  `e_prev_num_hi` int(11) DEFAULT NULL,
  `e_inc_100k` int(11) DEFAULT NULL,
  `e_inc_100k_lo` int(11) DEFAULT NULL,
  `e_inc_100k_hi` int(11) DEFAULT NULL,
  `e_inc_num` int(11) DEFAULT NULL,
  `e_inc_num_lo` int(11) DEFAULT NULL,
  `e_inc_num_hi` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5338 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `world_bank_metadata_countries`
--

DROP TABLE IF EXISTS `world_bank_metadata_countries`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `world_bank_metadata_countries` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `country_code` varchar(255) DEFAULT NULL,
  `region` varchar(255) DEFAULT NULL,
  `income_group` varchar(255) DEFAULT NULL,
  `notes` text,
  `tablename` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=248 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `world_bank_tb_data`
--

DROP TABLE IF EXISTS `world_bank_tb_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `world_bank_tb_data` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `country_code` varchar(255) DEFAULT NULL,
  `year` int(11) DEFAULT NULL,
  `tb_count` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6201 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-05-14 15:33:27
