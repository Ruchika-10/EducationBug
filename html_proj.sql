-- phpMyAdmin SQL Dump
-- version 4.7.9
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Jul 29, 2018 at 06:06 PM
-- Server version: 5.7.21
-- PHP Version: 5.6.35

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `html_proj`
--

-- --------------------------------------------------------

--
-- Table structure for table `colleges`
--

DROP TABLE IF EXISTS `colleges`;
CREATE TABLE IF NOT EXISTS `colleges` (
  `image` varchar(100) NOT NULL,
  `name` varchar(200) NOT NULL,
  `state` varchar(100) NOT NULL,
  `rank` int(2) NOT NULL,
  `link` varchar(200) NOT NULL,
  `type` varchar(50) NOT NULL,
  `sno` int(3) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`sno`)
) ENGINE=MyISAM AUTO_INCREMENT=84 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `colleges`
--

INSERT INTO `colleges` (`image`, `name`, `state`, `rank`, `link`, `type`, `sno`) VALUES
('iitmadras.png', 'IIT Madras(or Chennai)', 'Tamil-Nadu', 1, 'iitmadras', 'iit', 2),
('iitbombay.png', 'IIT Bombay', 'Maharashtra', 2, 'iitbombay', 'iit', 3),
('iitkharagpur.png', 'IIT Kharagpur', 'West-Bengal', 3, 'iitkharagpur', 'iit', 4),
('nittiruchirappalli.jpg', 'NIT, Tiruchirappalli', 'Tamil-Nadu', 1, 'nittiruchirappalli', 'nit', 5),
('nitsurat.png', 'Sardar Vallabhai NIT,Surat', 'Gujarat', 2, 'nitsurat', 'nit', 6),
('nitnagpur.jpg', 'Visvesvaraya NIT,Nagpur', 'Maharashtra', 3, 'nitnagpur', 'nit', 7),
('bitspilani.png', 'BITS Pilani', 'Rajasthan', 1, 'bitspilani', 'top10engg', 8),
('delhitechnological.jpg', 'Delhi Technological University', '-', 2, 'delhitechnological', 'top10engg', 9),
('bitsmesra.jpg', 'BITS Mesra', 'Jharkhand', 3, 'bitsmesra', 'top10engg', 10),
('iimahmedabad.png', 'IIM Ahmedabad', 'Gujarat', 1, 'iimahmedabad', 'iim', 11),
('iimbangalore.png', 'IIM Bangalore', 'Karnataka', 2, 'iimbangalore', 'iim', 12),
('iimcalcutta.jpg', 'IIM Calcutta', 'West-Bengal', 3, 'iimcalcutta', 'iim', 13),
('fms.jpg', 'Faculty of Management Studies,Delhi', '-', 2, 'fmsd', 'top10mba', 15),
('spjimr.jpg', 'SP Jain Institute of Management & Research,Mumbai', 'Maharashtra', 3, 'spjimrm', 'top10mba', 16),
('nlsiub.png', 'National Law School of India University,Bangalore', 'Karnataka', 1, 'nlsiub', 'top10law', 17),
('wbnujsk.jpeg', 'The West-Bengal National University of Juridicial Sciences', 'West-Bengal', 2, 'wbnujsk', 'top10law', 18),
('slsp.png', 'Symbiosis Law School,Pune', 'Maharashtra', 3, 'slsp', 'top10law', 19),
('aiimsnd.jpeg', 'AIIMS,New Delhi', '-', 1, 'aiimsnd', 'top10medgovt', 20),
('kgmul.jpeg', 'King George Medical University,Lucknow', 'Uttar-Pradesh', 2, 'kgmul', 'top10medgovt', 21),
('ucmsd.png', 'University College of Medical Sciences,Delhi', '-', 3, 'ucmsd', 'top10medgovt', 22),
('cmcv.png', 'Christian Medical College,Vellore', 'Tamil-Nadu', 1, 'cmcv', 'top10medpvt', 23),
('kmkm1.jpeg', 'Kasturba Medical College,Manipal', 'Karnataka', 2, 'kmkm', 'top10medpvt', 24),
('sjmcb.jpeg', 'St Johns Medical College,Bangalore', 'Karnataka', 3, 'sjmcb', 'top10medpvt', 25),
('iitdelhi.png', 'IIT Delhi', '-', 4, 'http://www.iitd.ac.in/', 'iit', 26),
('iitkanpur.png', 'IIT Kanpur', 'Uttar-Pradesh', 5, 'http://www.iitk.ac.in/', 'iit', 27),
('iitguwahati.png', 'IIT Guwahati', 'Assam', 6, 'http://www.iitg.ac.in/', 'iit', 28),
('iitroorkee.jpeg', 'IIT Roorkee', 'Uttarakhand', 7, 'https://www.iitr.ac.in/', 'iit', 29),
('iitvaranasi.jpeg', 'IIT(BHU) Varanasi', 'Uttar-Pradesh', 8, 'https://www.iitbhu.ac.in/', 'iit', 30),
('iitindore.png', 'IIT Indore', 'Madhya-Pradesh', 9, 'http://www.iiti.ac.in/', 'iit', 31),
('iithyderabad.png', 'IIT Hyderabad', 'Andhra-Pradesh', 10, 'https://www.iith.ac.in/', 'iit', 32),
('xlrij.jpg', 'Xavier Labour Relations Institute,Jamshedpur', 'Jharkhand', 1, 'xlrij', 'top10mba', 34),
('mdig.png', 'Management Development Institute, Gurgaon', 'Haryana', 4, 'https://www.mdi.ac.in/', 'top10mba', 35),
('iiftnd.jfif', 'Indian Institute of Foreign Trade,New Delhi', '-', 5, 'http://tedu.iift.ac.in/iift/index.php', 'top10mba', 36),
('imind.png', 'International Management Institute,New Delhi', '-', 6, 'http://www.imi.edu/', 'top10mba', 37),
('nmimsm.png', 'Narsee Monjee Institute of Management Studies,Mumbai', 'Maharashtra', 7, 'http://www.nmims.edu/', 'top10mba', 38),
('nitiem.jfif', 'National Institute of Industrial Engineering,Mumbai', 'Maharashtra', 8, 'https://www.nitie.edu/', 'top10mba', 39),
('jbimsm.jfif', 'Jamnalal Bajaj Institute of Management Studie, Mumbai', 'Maharashtra', 9, 'http://jbims.edu/', 'top10mba', 40),
('isbh.jfif', 'Indian School of Business, Hyderabad', 'Andhra-Pradesh', 10, 'http://www.isb.edu/pgp/campuses/hyderabad', 'top10mba', 41),
('iimindore.png', 'IIM Indore', 'Madhya-Pradesh', 4, 'https://www.iimidr.ac.in/', 'iim', 42),
('iimlucknow.png', 'IIM Lucknow', 'Uttar-Pradesh', 5, 'http://www.iiml.ac.in/', 'iim', 43),
('iimranchi.jfif', 'IIM Ranchi', 'Jharkhand', 6, 'https://www.iimranchi.ac.in/', 'iim', 44),
('iimkashipur.png', 'IIM Kashipur', 'Uttarakhand', 7, 'http://www.iimkashipur.ac.in/', 'iim', 45),
('iimrohtak.jfif', 'IIM Rohtak', 'Haryana', 8, 'http://www.iimrohtak.ac.in/', 'iim', 46),
('iimkozhikode.png', 'IIM Kozhikode', 'Kerala', 9, 'http://www.iimk.ac.in/', 'iim', 47),
('iimraipur.png', 'IIM Raipur', 'Chhattisgarh', 10, 'http://www.iimraipur.ac.in/', 'iim', 48),
('iiith.jfif', 'IIT Hyderabad', 'Andhra-Pradesh', 4, 'https://www.iiit.ac.in/', 'top10engg', 49),
('nsit.jfif', 'Netaji Subhas Institute of Technology,New-Delhi', '-', 5, 'http://www.nsit.ac.in/', 'top10engg', 50),
('au.png', 'Anna University,Chennai', 'Tamil-Nadu', 6, 'https://www.annauniv.edu/', 'top10engg', 51),
('ju.png', 'Jadavpur University,Kolkata', 'West-Bengal', 7, 'http://www.jaduniv.edu.in/', 'top10engg', 52),
('pec.png', 'Punjab Engineering College,Chandigarh', 'Punjab-Haryana', 8, 'http://www.pec.ac.in/', 'top10engg', 53),
('iiita.jfif', 'IIIT Allahabad', 'Uttar-Pradesh', 9, 'https://www.iiita.ac.in/', 'top10engg', 54),
('cep.jfif', 'Colleges of Engineering,Pune', 'Maharashtra', 10, 'http://www.coep.org.in/', 'top10engg', 55),
('nitrourkela.png', 'NIT Rourkela', 'Odisha', 4, 'http://www.nitrkl.ac.in/', 'nit', 56),
('nitsurathkal.png', 'NIT Surathkal', 'Karnataka', 5, 'http://www.nitk.ac.in/', 'nit', 57),
('nitwarangal.jfif', 'NIT Warangal', 'Telangana', 6, 'https://www.nitw.ac.in/', 'nit', 58),
('mnnit.png', 'Motilal Nehru NIT,Allahabad', 'Uttar-Pradesh', 7, 'http://www.mnnit.ac.in/', 'nit', 59),
('nitcalicut.jfif', 'NIT Calicut', 'Kerala', 8, 'http://www.nitc.ac.in/', 'nit', 60),
('nitsilchar.jfif', 'NIT Silchar', 'Assam', 9, 'http://www.nits.ac.in/', 'nit', 61),
('nitdurgapur.jfif', 'NIT Durgapur', 'West-Bengal', 10, 'http://www.nitdgp.ac.in/', 'nit', 62),
('ils.jfif', 'ILS Law College,Pune', 'Maharashtra', 4, 'https://ilslaw.edu/', 'top10law', 63),
('flbhuv.jfif', 'Faculty of law,Banaras Hindu University Varanasi', 'Uttar-Pradesh', 5, 'http://www.bhu.ac.in/law/', 'top10law', 64),
('alsn.jfif', 'Amity Law School,Delhi', '-', 6, 'http://www.amity.edu/als/', 'top10law', 65),
('amuv.jfif', 'Aligarh Muslim University Varanasi', 'Uttar-Pradesh', 7, 'https://www.amu.ac.in/dshowfacultydata2.jsp?did=16&eid=1603', 'top10law', 66),
('bvnlp.jfif', 'Bharati Vidyapeeth New Law College,Pune', 'Maharashtra', 8, 'http://bvpnlcpune.org/', 'top10law', 67),
('fljmid.png', 'Faculty of Law Jamia Millia Islamia ,Delhi', '-', 9, 'https://www.jmi.ac.in/law', 'top10law', 68),
('slcub.jfif', 'School of Law Christ University Bangalore', 'Karnataka', 10, 'https://christuniversity.in/academics/school-of-law', 'top10law', 69),
('jipmerp.jfif', 'Jawaharlal Institute of postgraduate Medical Education and Research,Puducherry', 'Tamil-Nadu', 4, 'http://www.jipmer.puducherry.gov.in/', 'top10medgovt', 70),
('imsbhdv.png', 'Institute of Medical Sciences,Banaras Hindu University,Varanasi', 'Uttar-Pradesh', 5, 'http://www.bhu.ac.in/ims/', 'top10medgovt', 71),
('mamcnd.jfif', 'Maulana Azad Medical College,New-Delhi', '-', 6, 'http://www.mamc.ac.in/', 'top10medgovt', 72),
('afmcp.jfif', 'Armed forces Medical College,Pune', 'Maharashtra', 7, 'http://www.afmc.nic.in/', 'top10medgovt', 73),
('lhmcwnd.jfif', 'Lady Hardinge Medical College for Women,New-Delhi', '-', 8, 'http://lhmc-hosp.gov.in/', 'top10medgovt', 74),
('gmchc.jfif', 'Government Medical College and Hospital,Chandigarh', 'Punjab-Haryana', 9, 'https://gmch.gov.in/', 'top10medgovt', 75),
('sgsmcakemmcm.gif', 'Seth Gordhandas Sunderdas Medical College and King Edward Memorial Medical College,Mumbai', 'Maharashtra', 10, 'http://www.kem.edu/', 'top10medgovt', 76),
('cmcl.jfif', 'Christian Medical College Ludhiana', 'Punjab', 4, 'http://cmcludhiana.in/medical_college/contactus.php', 'top10medpvt', 77),
('srmcric.png', 'Shri Ramachandra Medical College and Research Institute Chennai', 'Tamil-Nadu', 5, 'https://www.sriramachandra.edu.in/', 'top10medpvt', 78),
('jnmcb.jfif', 'Jawaharlal Nehru Medical College,Belgaum', 'Karnataka', 6, 'https://www.jnmc.edu/', 'top10medpvt', 79),
('kmcm.jfif', 'Kasturba Medical College,Mangalore', 'Karnataka', 7, 'https://manipal.edu/kmc-mangalore.html', 'top10medpvt', 80),
('srmmchrcc.jfif', 'SRM Medical College,Hospital and Research Centre,Chennai', 'Tamil-Nadu', 8, 'http://www.srmuniv.ac.in/medical-college/hospital-and-research-centre', 'top10medpvt', 81),
('jssmchm.jfif', 'JSS Medical College and Hospital Mysore', 'Karnataka', 9, 'https://www.jssuni.edu.in/JSSWeb/WebShowFromDB.aspx?MID=0&CID=4&PID=10002', 'top10medpvt', 82),
('msrmcb.jfif', 'MS Ramaiah Medical College Bangalore', 'Andhra-Pradesh', 10, 'http://www.msrmc.ac.in/', 'top10medpvt', 83);

-- --------------------------------------------------------

--
-- Table structure for table `contactus`
--

DROP TABLE IF EXISTS `contactus`;
CREATE TABLE IF NOT EXISTS `contactus` (
  `name` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `message` varchar(500) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `contactus`
--

INSERT INTO `contactus` (`name`, `email`, `message`) VALUES
('Harshita', 'harshita9419@gmail.com', 'hello there. please suggest me some exams i can give after my 12th edical.'),
('Anuragh Singh', 'anuraghsingh32.com', 'please suggest me some medical colleges in punjab,india'),
('Muskan', 'muskan123@gmail.com', 'please suggest me stream for 12th as i want to be a CA.'),
('Sanam', 'sanamjeet@gmail.com', 'can you tell me  about buisness courses i can do in punjab.'),
('Kanu', 'kanupriya001@gmail.com', 'i am presently doing BDS in chandigarh what are opportunities i can seek after this.\r\n');

-- --------------------------------------------------------

--
-- Table structure for table `rating`
--

DROP TABLE IF EXISTS `rating`;
CREATE TABLE IF NOT EXISTS `rating` (
  `rate` varchar(5) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `signup`
--

DROP TABLE IF EXISTS `signup`;
CREATE TABLE IF NOT EXISTS `signup` (
  `full_name` varchar(100) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `username` varchar(20) DEFAULT NULL,
  `password` varchar(20) DEFAULT NULL,
  `mobile` bigint(11) DEFAULT NULL,
  `gender` char(2) DEFAULT NULL,
  `type` varchar(10) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `signup`
--

INSERT INTO `signup` (`full_name`, `dob`, `email`, `username`, `password`, `mobile`, `gender`, `type`) VALUES
('Ruchika Syal', '1999-01-10', 'ruchika8872@gmail.com', 'Ruchika', '1234', 8146248870, 'F', 'Admin'),
('Harsita', '2003-05-08', 'harshita9419@gmail.com', 'Harshita', '123', 9419015870, 'F', 'User'),
('Rubina Makkar', '1999-01-02', 'rubinamkr@gmail.com', 'Rubina', '1234', 7347397030, 'F', 'Admin'),
('Anurag Singh', '1992-12-07', 'anuragrattan@gmail.com', 'Anurag', '123', 7347562314, 'M', 'User'),
('Sanamjeet Singh', '1994-02-11', 'jeetsanam@gmail.com', 'Sanam', '123', 9624581972, 'M', 'User'),
('Simranjeet Kaur', '1998-08-24', 'jeetsimran@gmail.com', 'Simran', '123', 9463849114, 'F', 'User'),
('Manisha Bhaskar', '1998-03-27', 'manishabhaskar@gmail.com', 'Manisha', '123', 9463849114, 'F', 'User'),
('Navraj Syal', '1997-03-01', 'navrajsyal97@gmail.com', 'Navraj', '123', 9996765795, 'M', 'User'),
('Aryan Rattan', '2001-10-26', 'aryanrattan26@gmail.com', 'Aryan', '123', 9646015720, 'M', 'User');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
