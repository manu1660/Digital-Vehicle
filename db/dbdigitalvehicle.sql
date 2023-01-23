-- phpMyAdmin SQL Dump
-- version 3.3.9
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: May 24, 2022 at 04:29 AM
-- Server version: 5.5.8
-- PHP Version: 5.3.5

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `dbdigitalvehicle`
--

-- --------------------------------------------------------

--
-- Table structure for table `tblcase`
--

CREATE TABLE IF NOT EXISTS `tblcase` (
  `caseId` int(11) NOT NULL AUTO_INCREMENT,
  `vid` int(11) NOT NULL,
  `casedetails` varchar(50) NOT NULL,
  `fine` varchar(50) NOT NULL,
  `pid` int(11) NOT NULL,
  `cdate` date NOT NULL,
  `status` varchar(50) NOT NULL,
  PRIMARY KEY (`caseId`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=6 ;

--
-- Dumping data for table `tblcase`
--

INSERT INTO `tblcase` (`caseId`, `vid`, `casedetails`, `fine`, `pid`, `cdate`, `status`) VALUES
(1, 1, 'Overspeed', '500', 1, '2021-05-19', 'paid'),
(2, 1, 'Overspeed', '500', 1, '2021-06-03', 'paid'),
(3, 1, 'Without helmet', '100', 1, '2021-06-03', 'paid'),
(4, 1, 'No mask', '500', 1, '2021-06-03', 'paid'),
(5, 3, 'No helmet', '500', 2, '2023-04-14', 'paid');

-- --------------------------------------------------------

--
-- Table structure for table `tblfeedback`
--

CREATE TABLE IF NOT EXISTS `tblfeedback` (
  `fId` int(11) NOT NULL AUTO_INCREMENT,
  `fDate` datetime NOT NULL,
  `vid` int(11) NOT NULL,
  `feedback` varchar(100) NOT NULL,
  PRIMARY KEY (`fId`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `tblfeedback`
--

INSERT INTO `tblfeedback` (`fId`, `fDate`, `vid`, `feedback`) VALUES
(1, '2021-07-01 14:17:18', 2, 'Good');

-- --------------------------------------------------------

--
-- Table structure for table `tblinsurancecompany`
--

CREATE TABLE IF NOT EXISTS `tblinsurancecompany` (
  `insId` int(11) NOT NULL AUTO_INCREMENT,
  `insName` varchar(50) NOT NULL,
  `insAddress` varchar(100) NOT NULL,
  `insEmail` varchar(50) NOT NULL,
  `insContact` varchar(50) NOT NULL,
  `insLicense` varchar(20) NOT NULL,
  PRIMARY KEY (`insId`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `tblinsurancecompany`
--

INSERT INTO `tblinsurancecompany` (`insId`, `insName`, `insAddress`, `insEmail`, `insContact`, `insLicense`) VALUES
(1, 'Bajaj', 'fvnh', 'bajaj@gmail.com', '8596471023', 'swf65w'),
(2, 'Safe kerala', 'jafs', 'safekerala@gmail.com', '7894152630', 'kjfvn5275');

-- --------------------------------------------------------

--
-- Table structure for table `tblinsurancedetails`
--

CREATE TABLE IF NOT EXISTS `tblinsurancedetails` (
  `iId` int(11) NOT NULL AUTO_INCREMENT,
  `vId` int(11) NOT NULL,
  `iDate` date DEFAULT NULL,
  `amt` int(11) NOT NULL,
  `insId` int(11) NOT NULL,
  `img` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`iId`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=13 ;

--
-- Dumping data for table `tblinsurancedetails`
--

INSERT INTO `tblinsurancedetails` (`iId`, `vId`, `iDate`, `amt`, `insId`, `img`) VALUES
(1, 1, '2022-05-03', 1000, 1, NULL),
(2, 1, '2021-06-03', 1000, 1, NULL),
(3, 1, '2021-06-03', 1000, 1, NULL),
(4, 1, '2021-06-03', 1000, 1, NULL),
(5, 1, '2021-06-03', 1000, 1, NULL),
(6, 1, '2021-06-03', 1000, 1, NULL),
(7, 1, '2021-06-03', 1000, 1, NULL),
(8, 3, '2023-04-14', 1000, 2, NULL),
(9, 3, '2023-04-14', 1000, 3, NULL),
(10, 1, '2022-06-02', 1000, 1, NULL),
(11, 1, '2022-06-02', 1000, 1, NULL),
(12, 2, '2022-05-17', 1000, 1, '/media/photo-enhance-02.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `tbllogin`
--

CREATE TABLE IF NOT EXISTS `tbllogin` (
  `uname` varchar(50) NOT NULL,
  `pwd` varchar(50) NOT NULL,
  `utype` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tbllogin`
--

INSERT INTO `tbllogin` (`uname`, `pwd`, `utype`, `status`) VALUES
('admin@gmail.com', 'admin', 'admin', '1'),
('aluvarto@gmail.com', 'aluvarto@123', 'rto', '1'),
('mspollution@gmail.com', 'msp@1234', 'pollution', '1'),
('bajaj@gmail.com', 'bajaj@123', 'insurance', '1'),
('ravi@gmail.com', 'ravi@1234', 'police', '1'),
('KL-41-L-5269', '7854961023', 'customer', '1'),
('prvrrto@gmail.com', 'prvr@123', 'rto', '1'),
('KL-41-P-8971', '9658471203', 'customer', '1'),
('pbvrrto@gmail.com', 'pbvr@123', 'rto', '1'),
('aneeshpol@gmail.com', 'aneesh@123', 'pollution', '1'),
('safekerala@gmail.com', 'safe@123', 'insurance', '1'),
('raghavan@gmail.com', 'raghavan@123', 'police', '1'),
('prathap@gmail.com', 'prathap@123', 'police', '0'),
('KL-38-F-4758', '7485961203', 'customer', '1'),
('KL-41-T-5869', '7410852963', 'customer', '1');

-- --------------------------------------------------------

--
-- Table structure for table `tblowner`
--

CREATE TABLE IF NOT EXISTS `tblowner` (
  `oId` int(11) NOT NULL AUTO_INCREMENT,
  `vId` int(11) NOT NULL,
  `ownerName` varchar(50) NOT NULL,
  `ownerAddress` varchar(100) NOT NULL,
  `ownerContact` varchar(50) NOT NULL,
  PRIMARY KEY (`oId`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `tblowner`
--

INSERT INTO `tblowner` (`oId`, `vId`, `ownerName`, `ownerAddress`, `ownerContact`) VALUES
(1, 4, 'Prakash K V', 'Aluva, Ernakulam', '7485961023'),
(2, 4, 'Yedhu K P', 'Edavanakkad', '7410852963');

-- --------------------------------------------------------

--
-- Table structure for table `tblpolice`
--

CREATE TABLE IF NOT EXISTS `tblpolice` (
  `pId` int(11) NOT NULL AUTO_INCREMENT,
  `pName` varchar(50) NOT NULL,
  `pStation` varchar(50) NOT NULL,
  `pEmail` varchar(50) NOT NULL,
  `pContact` varchar(50) NOT NULL,
  `pAadhar` varchar(12) NOT NULL,
  `pPhoto` varchar(100) NOT NULL,
  PRIMARY KEY (`pId`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `tblpolice`
--

INSERT INTO `tblpolice` (`pId`, `pName`, `pStation`, `pEmail`, `pContact`, `pAadhar`, `pPhoto`) VALUES
(1, 'Ravi', 'Aluva', 'ravi@gmail.com', '8965471023', '236514078955', ''),
(2, 'Raghavan', 'Aluva', 'raghavan@gmail.com', '9658230147', '859746120323', ''),
(3, 'Prathap', 'Edappally', 'prathap@gmail.com', '9658023147', '859647120323', '/media/te2.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `tblpollutioncenter`
--

CREATE TABLE IF NOT EXISTS `tblpollutioncenter` (
  `polId` int(11) NOT NULL AUTO_INCREMENT,
  `polName` varchar(50) NOT NULL,
  `polAddress` varchar(100) NOT NULL,
  `polContact` varchar(50) NOT NULL,
  `polEmail` varchar(50) NOT NULL,
  `polLicense` varchar(50) NOT NULL,
  PRIMARY KEY (`polId`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `tblpollutioncenter`
--

INSERT INTO `tblpollutioncenter` (`polId`, `polName`, `polAddress`, `polContact`, `polEmail`, `polLicense`) VALUES
(1, 'MS Pollution', 'Aluva', '7859461023', 'mspollution@gmail.com', 'k54'),
(3, 'Aneesh Pollution', 'Aluva', '8577496123', 'aneeshpol@gmail.com', 'kn5878');

-- --------------------------------------------------------

--
-- Table structure for table `tblpollutiondetails`
--

CREATE TABLE IF NOT EXISTS `tblpollutiondetails` (
  `poluId` int(11) NOT NULL AUTO_INCREMENT,
  `vId` int(11) NOT NULL,
  `polId` int(11) NOT NULL,
  `polDate` date NOT NULL,
  `amt` bigint(20) NOT NULL,
  `img` varchar(500) NOT NULL,
  PRIMARY KEY (`poluId`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `tblpollutiondetails`
--

INSERT INTO `tblpollutiondetails` (`poluId`, `vId`, `polId`, `polDate`, `amt`, `img`) VALUES
(1, 2, 3, '2022-05-17', 80, '/media/photo-enhance-02_w4xz5a4.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `tblrto`
--

CREATE TABLE IF NOT EXISTS `tblrto` (
  `rtoid` int(11) NOT NULL AUTO_INCREMENT,
  `rtoname` varchar(50) NOT NULL,
  `rtoregion` varchar(50) NOT NULL,
  `rtoemail` varchar(50) NOT NULL,
  `rtocontact` varchar(50) NOT NULL,
  `rtoLicense` varchar(50) NOT NULL,
  PRIMARY KEY (`rtoid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `tblrto`
--

INSERT INTO `tblrto` (`rtoid`, `rtoname`, `rtoregion`, `rtoemail`, `rtocontact`, `rtoLicense`) VALUES
(1, 'Aluva RTO', 'Aluva', 'aluvarto@gmail.com', '8596471023', 'df545'),
(2, 'Paravoor RTO', 'Paravoor', 'prvrrto@gmail.com', '8596471203', 'grf6545'),
(3, 'Perumbavoor RTO', 'Perumbavoor', 'pbvrrto@gmail.com', '9658741230', 'hb6398');

-- --------------------------------------------------------

--
-- Table structure for table `tblvehicle`
--

CREATE TABLE IF NOT EXISTS `tblvehicle` (
  `vid` int(11) NOT NULL AUTO_INCREMENT,
  `rtoId` int(11) NOT NULL,
  `vNumber` varchar(50) NOT NULL,
  `vChasis` varchar(50) NOT NULL,
  `manufacturer` varchar(50) NOT NULL,
  `rcowner` varchar(50) NOT NULL,
  `address` varchar(100) NOT NULL,
  `contact` varchar(50) NOT NULL,
  `insExp` date NOT NULL,
  `polExp` date NOT NULL,
  `insId` int(11) NOT NULL,
  PRIMARY KEY (`vid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `tblvehicle`
--

INSERT INTO `tblvehicle` (`vid`, `rtoId`, `vNumber`, `vChasis`, `manufacturer`, `rcowner`, `address`, `contact`, `insExp`, `polExp`, `insId`) VALUES
(1, 1, 'KL-41-L-5269', '7852', 'TVS', 'Manual P K', 'hndc', '7854961023', '2023-06-02', '2022-05-04', 1),
(2, 1, 'KL-41-P-8971', '8596', 'Hero', 'Madhu', 'Aluva', '9658471203', '2023-05-17', '2023-05-17', 1),
(3, 3, 'KL-38-F-4758', '488', 'hgvh', 'Sandhya', 'ghvuy', '7485961203', '2024-04-13', '2023-04-13', 2),
(4, 1, 'KL-41-T-5869', '5454', 'TVS', 'Yedhu K P', 'Edavanakkad', '7410852963', '2023-05-24', '2023-05-24', 1);
