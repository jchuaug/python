/*
Navicat MySQL Data Transfer

Source Server         : root
Source Server Version : 50721
Source Host           : localhost:3306
Source Database       : work_company

Target Server Type    : MYSQL
Target Server Version : 50721
File Encoding         : 65001

Date: 2018-06-27 01:19:57
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for assets
-- ----------------------------
DROP TABLE IF EXISTS `assets`;
CREATE TABLE `assets` (
  `assets_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `company_id` bigint(20) DEFAULT NULL,
  `company_name` varchar(255) DEFAULT NULL,
  `date` varchar(255) DEFAULT NULL,
  `cash_and_liquid_assets` varchar(255) DEFAULT NULL,
  `inventory` varchar(255) DEFAULT NULL,
  `current_assets` varchar(255) DEFAULT NULL,
  `tangible_fixed_assets` varchar(255) DEFAULT NULL,
  `non_current_assets` varchar(255) DEFAULT NULL,
  `total_assets` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`assets_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12566 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for company_info
-- ----------------------------
DROP TABLE IF EXISTS `company_info`;
CREATE TABLE `company_info` (
  `company_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `address_code` varchar(255) DEFAULT NULL,
  `address_country` varchar(255) DEFAULT NULL,
  `address_state` varchar(255) DEFAULT NULL,
  `address_city` varchar(255) DEFAULT NULL,
  `address_detail` varchar(255) DEFAULT NULL,
  `phone` varchar(255) DEFAULT NULL,
  `fax` varchar(255) DEFAULT NULL,
  `website` varchar(255) DEFAULT NULL,
  `ve_industry_code` varchar(255) DEFAULT NULL,
  `sic_code` varchar(255) DEFAULT NULL,
  `naic` varchar(255) DEFAULT NULL,
  `found_date` varchar(255) DEFAULT NULL,
  `found_year` varchar(255) DEFAULT NULL,
  `found_month` varchar(255) DEFAULT NULL,
  `found_day` varchar(255) DEFAULT NULL,
  `company_status` varchar(255) DEFAULT NULL,
  `pe_backed_status` varchar(255) DEFAULT NULL,
  `current_operating_stage` varchar(255) DEFAULT NULL,
  `excel_id` varchar(255) DEFAULT NULL,
  `file_info` varchar(2000) DEFAULT NULL,
  `bussiness_description` varchar(10000) DEFAULT NULL,
  `num_of_employees` varchar(255) DEFAULT NULL,
  `last_avaliable_sales_figure` varchar(255) DEFAULT NULL,
  `legal_counsel` varchar(255) DEFAULT NULL,
  `post_ipo_information` varchar(255) DEFAULT NULL,
  `ticker` varchar(255) DEFAULT NULL,
  `exchange` varchar(255) DEFAULT NULL,
  `ipo_date` varchar(255) DEFAULT NULL,
  `accountant` varchar(255) DEFAULT NULL,
  `amount_mil` varchar(255) DEFAULT NULL,
  `proceeds` varchar(255) DEFAULT NULL,
  `book_managers` varchar(255) DEFAULT NULL,
  `alias` varchar(255) DEFAULT NULL,
  `total_funding_to_date` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`company_id`)
) ENGINE=InnoDB AUTO_INCREMENT=38463 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for current_investors
-- ----------------------------
DROP TABLE IF EXISTS `current_investors`;
CREATE TABLE `current_investors` (
  `current_investors_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `company_id` bigint(20) DEFAULT NULL,
  `company_name` varchar(255) DEFAULT NULL,
  `firm` varchar(255) DEFAULT NULL,
  `fund` varchar(255) DEFAULT NULL,
  `fund_stage` varchar(255) DEFAULT NULL,
  `participation_round_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`current_investors_id`),
  KEY `firm_id_3` (`company_id`)
) ENGINE=InnoDB AUTO_INCREMENT=18975 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for directors
-- ----------------------------
DROP TABLE IF EXISTS `directors`;
CREATE TABLE `directors` (
  `directors_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `company_id` bigint(20) DEFAULT NULL,
  `company_name` varchar(255) DEFAULT NULL,
  `director_name` varchar(255) DEFAULT NULL,
  `director_title` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`directors_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7096 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for historical_investors
-- ----------------------------
DROP TABLE IF EXISTS `historical_investors`;
CREATE TABLE `historical_investors` (
  `historical_investors_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `company_id` bigint(20) DEFAULT NULL,
  `company_name` varchar(255) DEFAULT NULL,
  `firm` varchar(255) DEFAULT NULL,
  `fund` varchar(255) DEFAULT NULL,
  `fund_stage` varchar(255) DEFAULT NULL,
  `still_in_portfolio` varchar(255) DEFAULT NULL,
  `participation_history_id` bigint(11) DEFAULT NULL,
  PRIMARY KEY (`historical_investors_id`),
  KEY `firm_id_4` (`company_id`)
) ENGINE=InnoDB AUTO_INCREMENT=105348 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for income
-- ----------------------------
DROP TABLE IF EXISTS `income`;
CREATE TABLE `income` (
  `income_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `company_id` bigint(20) DEFAULT NULL,
  `company_name` varchar(255) DEFAULT NULL,
  `date` varchar(255) DEFAULT NULL,
  `net_sale_or_revenues` varchar(255) DEFAULT NULL,
  `gross_profit` varchar(255) DEFAULT NULL,
  `total_operating_costs` varchar(255) DEFAULT NULL,
  `total_expenses` varchar(255) DEFAULT NULL,
  `profit_before_tax` varchar(255) DEFAULT NULL,
  `profit_after_tax` varchar(255) DEFAULT NULL,
  `net_income` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`income_id`)
) ENGINE=InnoDB AUTO_INCREMENT=29446 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for investment_rounds
-- ----------------------------
DROP TABLE IF EXISTS `investment_rounds`;
CREATE TABLE `investment_rounds` (
  `investment_rounds_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `company_id` bigint(11) DEFAULT NULL,
  `company_name` varchar(255) DEFAULT NULL,
  `date` varchar(255) DEFAULT NULL,
  `num_of_inv` int(11) DEFAULT NULL,
  `stage` varchar(255) DEFAULT NULL,
  `deal_value` varchar(255) DEFAULT NULL,
  `equity_amount` varchar(255) DEFAULT NULL,
  `pe_debt_amt` varchar(255) DEFAULT NULL,
  `company_valuation` varchar(255) DEFAULT NULL,
  `investment_location` varchar(255) DEFAULT NULL,
  `firm` varchar(255) DEFAULT NULL,
  `fund` varchar(255) DEFAULT NULL,
  `fund_security_type` varchar(255) DEFAULT NULL,
  `p_equity_amount` varchar(255) DEFAULT NULL,
  `debt` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`investment_rounds_id`),
  KEY `firm_id` (`company_id`)
) ENGINE=InnoDB AUTO_INCREMENT=240909 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for liabilities
-- ----------------------------
DROP TABLE IF EXISTS `liabilities`;
CREATE TABLE `liabilities` (
  `liabilities_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `company_id` bigint(20) DEFAULT NULL,
  `company_name` varchar(255) DEFAULT NULL,
  `date` varchar(255) DEFAULT NULL,
  `current_liabilities` varchar(255) DEFAULT NULL,
  `total_debts` varchar(255) DEFAULT NULL,
  `long_term_liabilities` varchar(255) DEFAULT NULL,
  `total_liabilities` varchar(255) DEFAULT NULL,
  `total_shareholders_equity` varchar(255) DEFAULT NULL,
  `total_liabilities_and_shareholders_equity` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`liabilities_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12566 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for mergers_acquisitions
-- ----------------------------
DROP TABLE IF EXISTS `mergers_acquisitions`;
CREATE TABLE `mergers_acquisitions` (
  `mergers_acquisitions_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `company_id` bigint(20) DEFAULT NULL,
  `company_name` varchar(255) DEFAULT NULL,
  `date` varchar(255) DEFAULT NULL,
  `target_name` varchar(255) DEFAULT NULL,
  `acquiror_name` varchar(2000) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `deal_value` varchar(255) DEFAULT NULL,
  `ev_ebitda` varchar(255) DEFAULT NULL,
  `target_financial_advisor` varchar(255) DEFAULT NULL,
  `brief_desciption` varchar(2000) DEFAULT NULL,
  PRIMARY KEY (`mergers_acquisitions_id`)
) ENGINE=InnoDB AUTO_INCREMENT=69937 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for officers
-- ----------------------------
DROP TABLE IF EXISTS `officers`;
CREATE TABLE `officers` (
  `officers_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `company_id` bigint(20) DEFAULT NULL,
  `company_name` varchar(255) DEFAULT NULL,
  `officer_name` varchar(255) DEFAULT NULL,
  `officer_title` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`officers_id`),
  KEY `firm_id_7` (`company_id`)
) ENGINE=InnoDB AUTO_INCREMENT=39397 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for participation_history
-- ----------------------------
DROP TABLE IF EXISTS `participation_history`;
CREATE TABLE `participation_history` (
  `participation_history_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `company_id` bigint(20) DEFAULT NULL,
  `company_name` varchar(255) DEFAULT NULL,
  `firm` varchar(255) DEFAULT NULL,
  `fund` varchar(255) DEFAULT NULL,
  `round1` int(255) unsigned zerofill DEFAULT NULL,
  `round2` int(255) unsigned zerofill DEFAULT NULL,
  `round3` int(255) unsigned zerofill DEFAULT NULL,
  `round4` int(255) unsigned zerofill DEFAULT NULL,
  `round5` int(255) unsigned zerofill DEFAULT NULL,
  `round6` int(255) unsigned zerofill DEFAULT NULL,
  `round7` int(255) unsigned zerofill DEFAULT NULL,
  `round8` int(255) unsigned zerofill DEFAULT NULL,
  `round9` int(255) unsigned zerofill DEFAULT NULL,
  `round10` int(255) unsigned zerofill DEFAULT NULL,
  `round11` int(255) unsigned zerofill DEFAULT NULL,
  `round12` int(255) unsigned zerofill DEFAULT NULL,
  `round13` int(255) unsigned zerofill DEFAULT NULL,
  `round14` int(255) unsigned zerofill DEFAULT NULL,
  `round15` int(255) unsigned zerofill DEFAULT NULL,
  `round16` int(255) unsigned zerofill DEFAULT NULL,
  `round17` int(255) unsigned zerofill DEFAULT NULL,
  `round18` int(255) unsigned zerofill DEFAULT NULL,
  `round19` int(255) unsigned zerofill DEFAULT NULL,
  `round20` int(255) unsigned zerofill DEFAULT NULL,
  `round21` int(255) unsigned zerofill DEFAULT NULL,
  `round22` int(255) unsigned zerofill DEFAULT NULL,
  `round23` int(255) unsigned zerofill DEFAULT NULL,
  `round24` int(255) unsigned zerofill DEFAULT NULL,
  `round25` int(255) unsigned zerofill DEFAULT NULL,
  `round26` int(255) unsigned zerofill DEFAULT NULL,
  `round27` int(255) unsigned zerofill DEFAULT NULL,
  `round28` int(255) unsigned zerofill DEFAULT NULL,
  `round29` int(255) unsigned zerofill DEFAULT NULL,
  `round30` int(255) unsigned zerofill DEFAULT NULL,
  `round31` int(255) unsigned zerofill DEFAULT NULL,
  `round32` int(255) unsigned zerofill DEFAULT NULL,
  `round33` int(255) unsigned zerofill DEFAULT NULL,
  `round34` int(255) unsigned zerofill DEFAULT NULL,
  `round35` int(255) unsigned zerofill DEFAULT NULL,
  `round36` int(255) unsigned zerofill DEFAULT NULL,
  `round37` int(255) unsigned zerofill DEFAULT NULL,
  `round38` int(255) unsigned zerofill DEFAULT NULL,
  `round39` int(255) unsigned zerofill DEFAULT NULL,
  `round40` int(255) unsigned zerofill DEFAULT NULL,
  `round41` int(255) unsigned zerofill DEFAULT NULL,
  `round42` int(255) unsigned zerofill DEFAULT NULL,
  `round43` int(255) unsigned zerofill DEFAULT NULL,
  `round44` int(255) unsigned zerofill DEFAULT NULL,
  `round45` int(255) unsigned zerofill DEFAULT NULL,
  `round46` int(255) unsigned zerofill DEFAULT NULL,
  `round47` int(255) unsigned zerofill DEFAULT NULL,
  `round48` int(255) unsigned zerofill DEFAULT NULL,
  `round49` int(255) unsigned zerofill DEFAULT NULL,
  `round50` int(255) unsigned zerofill DEFAULT NULL,
  PRIMARY KEY (`participation_history_id`)
) ENGINE=InnoDB AUTO_INCREMENT=105547 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for participation_round
-- ----------------------------
DROP TABLE IF EXISTS `participation_round`;
CREATE TABLE `participation_round` (
  `participation_round_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `company_id` bigint(20) DEFAULT NULL,
  `company_name` varchar(255) DEFAULT NULL,
  `firm` varchar(255) DEFAULT NULL,
  `fund` varchar(255) DEFAULT NULL,
  `round1` int(255) unsigned zerofill DEFAULT NULL,
  `round2` int(255) unsigned zerofill DEFAULT NULL,
  `round3` int(255) unsigned zerofill DEFAULT NULL,
  `round4` int(255) unsigned zerofill DEFAULT NULL,
  `round5` int(255) unsigned zerofill DEFAULT NULL,
  `round6` int(255) unsigned zerofill DEFAULT NULL,
  `round7` int(255) unsigned zerofill DEFAULT NULL,
  `round8` int(255) unsigned zerofill DEFAULT NULL,
  `round9` int(255) unsigned zerofill DEFAULT NULL,
  `round10` int(255) unsigned zerofill DEFAULT NULL,
  `round11` int(255) unsigned zerofill DEFAULT NULL,
  `round12` int(255) unsigned zerofill DEFAULT NULL,
  `round13` int(255) unsigned zerofill DEFAULT NULL,
  `round14` int(255) unsigned zerofill DEFAULT NULL,
  `round15` int(255) unsigned zerofill DEFAULT NULL,
  `round16` int(255) unsigned zerofill DEFAULT NULL,
  `round17` int(255) unsigned zerofill DEFAULT NULL,
  `round18` int(255) unsigned zerofill DEFAULT NULL,
  `round19` int(255) unsigned zerofill DEFAULT NULL,
  `round20` int(255) unsigned zerofill DEFAULT NULL,
  `round21` int(255) unsigned zerofill DEFAULT NULL,
  `round22` int(255) unsigned zerofill DEFAULT NULL,
  `round23` int(255) unsigned zerofill DEFAULT NULL,
  `round24` int(255) unsigned zerofill DEFAULT NULL,
  `round25` int(255) unsigned zerofill DEFAULT NULL,
  `round26` int(255) unsigned zerofill DEFAULT NULL,
  `round27` int(255) unsigned zerofill DEFAULT NULL,
  `round28` int(255) unsigned zerofill DEFAULT NULL,
  `round29` int(255) unsigned zerofill DEFAULT NULL,
  `round30` int(255) unsigned zerofill DEFAULT NULL,
  `round31` int(255) unsigned zerofill DEFAULT NULL,
  `round32` int(255) unsigned zerofill DEFAULT NULL,
  `round33` int(255) unsigned zerofill DEFAULT NULL,
  `round34` int(255) unsigned zerofill DEFAULT NULL,
  `round35` int(255) unsigned zerofill DEFAULT NULL,
  `round36` int(255) unsigned zerofill DEFAULT NULL,
  `round37` int(255) unsigned zerofill DEFAULT NULL,
  `round38` int(255) unsigned zerofill DEFAULT NULL,
  `round39` int(255) unsigned zerofill DEFAULT NULL,
  `round40` int(255) unsigned zerofill DEFAULT NULL,
  `round41` int(255) unsigned zerofill DEFAULT NULL,
  `round42` int(255) unsigned zerofill DEFAULT NULL,
  `round43` int(255) unsigned zerofill DEFAULT NULL,
  `round44` int(255) unsigned zerofill DEFAULT NULL,
  `round45` int(255) unsigned zerofill DEFAULT NULL,
  `round46` int(255) unsigned zerofill DEFAULT NULL,
  `round47` int(255) unsigned zerofill DEFAULT NULL,
  `round48` int(255) unsigned zerofill DEFAULT NULL,
  `round49` int(255) unsigned zerofill DEFAULT NULL,
  `round50` int(255) unsigned zerofill DEFAULT NULL,
  PRIMARY KEY (`participation_round_id`)
) ENGINE=InnoDB AUTO_INCREMENT=19042 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for products
-- ----------------------------
DROP TABLE IF EXISTS `products`;
CREATE TABLE `products` (
  `products_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `company_id` bigint(20) DEFAULT NULL,
  `company_name` varchar(255) DEFAULT NULL,
  `product_name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`products_id`),
  KEY `firm_id_6` (`company_id`)
) ENGINE=InnoDB AUTO_INCREMENT=38548 DEFAULT CHARSET=utf8;
