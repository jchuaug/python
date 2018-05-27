/*
Navicat MySQL Data Transfer

Source Server         : root
Source Server Version : 50721
Source Host           : localhost:3306
Source Database       : work_company

Target Server Type    : MYSQL
Target Server Version : 50721
File Encoding         : 65001

Date: 2018-05-21 08:07:24
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for company_current_private_equity_investors
-- ----------------------------
DROP TABLE IF EXISTS `company_current_private_equity_investors`;
CREATE TABLE `company_current_private_equity_investors` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `company_id` bigint(20) DEFAULT NULL,
  `company_name` varchar(255) DEFAULT NULL,
  `firm` varchar(255) DEFAULT NULL,
  `fund` varchar(255) DEFAULT NULL,
  `fund_stage` varchar(255) DEFAULT NULL,
  `participation_round_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `firm_id_3` (`company_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7026 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for company_directors
-- ----------------------------
DROP TABLE IF EXISTS `company_directors`;
CREATE TABLE `company_directors` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `company_id` bigint(20) DEFAULT NULL,
  `company_name` varchar(255) DEFAULT NULL,
  `director_name` varchar(255) DEFAULT NULL,
  `director_title` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2758 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for company_historical_private_investors
-- ----------------------------
DROP TABLE IF EXISTS `company_historical_private_investors`;
CREATE TABLE `company_historical_private_investors` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `company_id` bigint(20) DEFAULT NULL,
  `company_name` varchar(255) DEFAULT NULL,
  `firm` varchar(255) DEFAULT NULL,
  `fund` varchar(255) DEFAULT NULL,
  `fund_stage` varchar(255) DEFAULT NULL,
  `still_in_portfolio` varchar(255) DEFAULT NULL,
  `participation_round_history_id` bigint(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `firm_id_4` (`company_id`)
) ENGINE=InnoDB AUTO_INCREMENT=40376 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for company_info
-- ----------------------------
DROP TABLE IF EXISTS `company_info`;
CREATE TABLE `company_info` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `excel_id` varchar(255) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `contact_info_phone` varchar(255) DEFAULT NULL,
  `contact_info_fax` varchar(255) DEFAULT NULL,
  `contact_info_website` varchar(255) DEFAULT NULL,
  `ve_industry_code` varchar(255) DEFAULT NULL,
  `sic_code` varchar(255) DEFAULT NULL,
  `naic` varchar(255) DEFAULT NULL,
  `bussiness_description` varchar(2000) DEFAULT NULL,
  `company_founded_date` varchar(255) DEFAULT NULL,
  `company_status` varchar(255) DEFAULT NULL,
  `pe_backed_status` varchar(255) DEFAULT NULL,
  `total_funding_to_date` varchar(255) DEFAULT NULL,
  `alias` varchar(255) DEFAULT NULL,
  `operating_stage` varchar(255) DEFAULT NULL,
  `num_of_employees` varchar(255) DEFAULT NULL,
  `last_avaliable_sales_figure` varchar(255) DEFAULT NULL,
  `current_operating_status` varchar(255) DEFAULT NULL,
  `legal_counsel` varchar(255) DEFAULT NULL,
  `post_ipo_information` varchar(255) DEFAULT NULL,
  `ticker` varchar(255) DEFAULT NULL,
  `exchange` varchar(255) DEFAULT NULL,
  `ipo_date` varchar(255) DEFAULT NULL,
  `accountant` varchar(255) DEFAULT NULL,
  `amount_mil` varchar(255) DEFAULT NULL,
  `proceeds` varchar(255) DEFAULT NULL,
  `book_managers` varchar(255) DEFAULT NULL,
  `file_info` varchar(2000) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17283 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for company_investment_rounds
-- ----------------------------
DROP TABLE IF EXISTS `company_investment_rounds`;
CREATE TABLE `company_investment_rounds` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
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
  PRIMARY KEY (`id`),
  KEY `firm_id` (`company_id`)
) ENGINE=InnoDB AUTO_INCREMENT=94640 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for company_key_financials_assets
-- ----------------------------
DROP TABLE IF EXISTS `company_key_financials_assets`;
CREATE TABLE `company_key_financials_assets` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `company_id` bigint(20) DEFAULT NULL,
  `company_name` varchar(255) DEFAULT NULL,
  `date` varchar(255) DEFAULT NULL,
  `cash_and_liquid_assets` varchar(255) DEFAULT NULL,
  `inventory` varchar(255) DEFAULT NULL,
  `current_assets` varchar(255) DEFAULT NULL,
  `tangible_fixed_assets` varchar(255) DEFAULT NULL,
  `non_current_assets` varchar(255) DEFAULT NULL,
  `total_assets` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4976 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for company_key_financials_income
-- ----------------------------
DROP TABLE IF EXISTS `company_key_financials_income`;
CREATE TABLE `company_key_financials_income` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
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
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11871 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for company_key_financials_liabilities
-- ----------------------------
DROP TABLE IF EXISTS `company_key_financials_liabilities`;
CREATE TABLE `company_key_financials_liabilities` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `company_id` bigint(20) DEFAULT NULL,
  `company_name` varchar(255) DEFAULT NULL,
  `date` varchar(255) DEFAULT NULL,
  `current_liabilities` varchar(255) DEFAULT NULL,
  `total_debts` varchar(255) DEFAULT NULL,
  `long_term_liabilities` varchar(255) DEFAULT NULL,
  `total_liabilities` varchar(255) DEFAULT NULL,
  `total_shareholders_equity` varchar(255) DEFAULT NULL,
  `total_liabilities_and_shareholders_equity` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4976 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for company_mergers_and_acquisitions
-- ----------------------------
DROP TABLE IF EXISTS `company_mergers_and_acquisitions`;
CREATE TABLE `company_mergers_and_acquisitions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
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
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28584 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for company_officers
-- ----------------------------
DROP TABLE IF EXISTS `company_officers`;
CREATE TABLE `company_officers` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `company_id` bigint(20) DEFAULT NULL,
  `company_name` varchar(255) DEFAULT NULL,
  `officer_name` varchar(255) DEFAULT NULL,
  `officer_title` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `firm_id_7` (`company_id`)
) ENGINE=InnoDB AUTO_INCREMENT=15307 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for company_products
-- ----------------------------
DROP TABLE IF EXISTS `company_products`;
CREATE TABLE `company_products` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `company_id` bigint(20) DEFAULT NULL,
  `company_name` varchar(255) DEFAULT NULL,
  `product_name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `firm_id_6` (`company_id`)
) ENGINE=InnoDB AUTO_INCREMENT=15036 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for participation_round
-- ----------------------------
DROP TABLE IF EXISTS `participation_round`;
CREATE TABLE `participation_round` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
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
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7093 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for participation_round_history
-- ----------------------------
DROP TABLE IF EXISTS `participation_round_history`;
CREATE TABLE `participation_round_history` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
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
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=40575 DEFAULT CHARSET=utf8;
