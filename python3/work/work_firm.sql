/*
Navicat MySQL Data Transfer

Source Server         : root
Source Server Version : 50721
Source Host           : localhost:3306
Source Database       : work_firm

Target Server Type    : MYSQL
Target Server Version : 50721
File Encoding         : 65001

Date: 2018-06-27 01:20:09
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for direct_investments
-- ----------------------------
DROP TABLE IF EXISTS `direct_investments`;
CREATE TABLE `direct_investments` (
  `direct_investments_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `firm_id` bigint(20) DEFAULT NULL,
  `firm_name` varchar(255) DEFAULT NULL,
  `company_name` varchar(255) DEFAULT NULL,
  `industry` varchar(255) DEFAULT NULL,
  `still_in_portfolio` varchar(255) DEFAULT NULL,
  `company_status` varchar(255) DEFAULT NULL,
  `last_investment_date` varchar(255) DEFAULT NULL,
  `location` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`direct_investments_id`)
) ENGINE=InnoDB AUTO_INCREMENT=478700 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for executives
-- ----------------------------
DROP TABLE IF EXISTS `executives`;
CREATE TABLE `executives` (
  `executives_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `firm_id` bigint(20) DEFAULT NULL,
  `firm_name` varchar(255) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `title` varchar(255) DEFAULT NULL,
  `phone` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`executives_id`)
) ENGINE=InnoDB AUTO_INCREMENT=80447 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for firm_info
-- ----------------------------
DROP TABLE IF EXISTS `firm_info`;
CREATE TABLE `firm_info` (
  `firm_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `firm_status` varchar(255) DEFAULT NULL,
  `firm_type` varchar(255) DEFAULT NULL,
  `funded` varchar(255) DEFAULT NULL,
  `cap_under_mgmt` varchar(255) DEFAULT NULL,
  `affiliations` varchar(255) DEFAULT NULL,
  `detail_loc` varchar(255) DEFAULT NULL,
  `city` varchar(255) DEFAULT NULL,
  `state` varchar(255) DEFAULT NULL,
  `country` varchar(255) DEFAULT NULL,
  `phone` varchar(255) DEFAULT NULL,
  `fax` varchar(255) DEFAULT NULL,
  `website` varchar(255) DEFAULT NULL,
  `file_info` varchar(2000) DEFAULT NULL,
  PRIMARY KEY (`firm_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7765 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for funds_managed
-- ----------------------------
DROP TABLE IF EXISTS `funds_managed`;
CREATE TABLE `funds_managed` (
  `funds_managed_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `firm_id` bigint(20) DEFAULT NULL,
  `firm_name` varchar(255) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `size` varchar(255) DEFAULT NULL,
  `fund_stage` varchar(255) DEFAULT NULL,
  `vintage` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`funds_managed_id`)
) ENGINE=InnoDB AUTO_INCREMENT=43153 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for industry_breakdown
-- ----------------------------
DROP TABLE IF EXISTS `industry_breakdown`;
CREATE TABLE `industry_breakdown` (
  `industry_breakdown_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `firm_id` bigint(20) DEFAULT NULL,
  `firm_name` varchar(255) DEFAULT NULL,
  `num_of_company_total` varchar(255) DEFAULT NULL,
  `sum_inv_total` varchar(255) DEFAULT NULL,
  `avg_per_company_total` varchar(255) DEFAULT NULL,
  `percent_of_inv_total` varchar(255) DEFAULT NULL,
  `industry_name` varchar(255) DEFAULT NULL,
  `num_of_company` varchar(255) DEFAULT NULL,
  `sum_inv` varchar(255) DEFAULT NULL,
  `avg_per_company` varchar(255) DEFAULT NULL,
  `percent_of_inv` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`industry_breakdown_id`)
) ENGINE=InnoDB AUTO_INCREMENT=57163 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for nation_breakdown
-- ----------------------------
DROP TABLE IF EXISTS `nation_breakdown`;
CREATE TABLE `nation_breakdown` (
  `nation_breakdown_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `firm_id` bigint(20) DEFAULT NULL,
  `firm_name` varchar(255) DEFAULT NULL,
  `num_of_company_total` varchar(255) DEFAULT NULL,
  `sum_inv_total` varchar(255) DEFAULT NULL,
  `avg_per_company_total` varchar(255) DEFAULT NULL,
  `percent_of_inv_total` varchar(255) DEFAULT NULL,
  `nation_name` varchar(255) DEFAULT NULL,
  `num_of_company` varchar(255) DEFAULT NULL,
  `sum_inv` varchar(255) DEFAULT NULL,
  `avg_per_company` varchar(255) DEFAULT NULL,
  `percent_of_inv` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`nation_breakdown_id`)
) ENGINE=InnoDB AUTO_INCREMENT=28462 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for other_offices
-- ----------------------------
DROP TABLE IF EXISTS `other_offices`;
CREATE TABLE `other_offices` (
  `other_offices_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `firm_id` bigint(20) DEFAULT NULL,
  `firm_name` varchar(255) DEFAULT NULL,
  `detail_loc` varchar(255) DEFAULT NULL,
  `city` varchar(255) DEFAULT NULL,
  `state` varchar(255) DEFAULT NULL,
  `country` varchar(255) DEFAULT NULL,
  `phone` varchar(255) DEFAULT NULL,
  `fax` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`other_offices_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7096 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for related_news
-- ----------------------------
DROP TABLE IF EXISTS `related_news`;
CREATE TABLE `related_news` (
  `related_news_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `firm_id` bigint(20) DEFAULT NULL,
  `firm_name` varchar(255) DEFAULT NULL,
  `headline` varchar(255) DEFAULT NULL,
  `date` varchar(255) DEFAULT NULL,
  `publication` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`related_news_id`)
) ENGINE=InnoDB AUTO_INCREMENT=545 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for stage_breakdown
-- ----------------------------
DROP TABLE IF EXISTS `stage_breakdown`;
CREATE TABLE `stage_breakdown` (
  `stage_breakdown_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `firm_id` bigint(20) DEFAULT NULL,
  `firm_name` varchar(255) DEFAULT NULL,
  `num_of_company_total` varchar(255) DEFAULT NULL,
  `sum_inv_total` varchar(255) DEFAULT NULL,
  `avg_per_company_total` varchar(255) DEFAULT NULL,
  `percent_of_inv_total` varchar(255) DEFAULT NULL,
  `stage_name` varchar(255) DEFAULT NULL,
  `num_of_company` varchar(255) DEFAULT NULL,
  `sum_inv` varchar(255) DEFAULT NULL,
  `avg_per_company` varchar(255) DEFAULT NULL,
  `percent_of_inv` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`stage_breakdown_id`)
) ENGINE=InnoDB AUTO_INCREMENT=50571 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for state_breakdown
-- ----------------------------
DROP TABLE IF EXISTS `state_breakdown`;
CREATE TABLE `state_breakdown` (
  `state_breakdown_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `firm_id` bigint(20) DEFAULT NULL,
  `firm_name` varchar(255) DEFAULT NULL,
  `num_of_company_total` varchar(255) DEFAULT NULL,
  `sum_inv_total` varchar(255) DEFAULT NULL,
  `avg_per_company_total` varchar(255) DEFAULT NULL,
  `percent_of_inv_total` varchar(255) DEFAULT NULL,
  `state_name` varchar(255) DEFAULT NULL,
  `num_of_company` varchar(255) DEFAULT NULL,
  `sum_inv` varchar(255) DEFAULT NULL,
  `avg_per_company` varchar(255) DEFAULT NULL,
  `percent_of_inv` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`state_breakdown_id`)
) ENGINE=InnoDB AUTO_INCREMENT=86307 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for status_breakdown
-- ----------------------------
DROP TABLE IF EXISTS `status_breakdown`;
CREATE TABLE `status_breakdown` (
  `status_breakdown_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `firm_id` bigint(20) DEFAULT NULL,
  `firm_name` varchar(255) DEFAULT NULL,
  `num_of_company_total` varchar(255) DEFAULT NULL,
  `sum_inv_total` varchar(255) DEFAULT NULL,
  `avg_per_company_total` varchar(255) DEFAULT NULL,
  `percent_of_inv_total` varchar(255) DEFAULT NULL,
  `status_name` varchar(255) DEFAULT NULL,
  `num_of_company` varchar(255) DEFAULT NULL,
  `sum_inv` varchar(255) DEFAULT NULL,
  `avg_per_company` varchar(255) DEFAULT NULL,
  `percent_of_inv` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`status_breakdown_id`)
) ENGINE=InnoDB AUTO_INCREMENT=34824 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for top_coinvestors
-- ----------------------------
DROP TABLE IF EXISTS `top_coinvestors`;
CREATE TABLE `top_coinvestors` (
  `top_coinvestors_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `firm_id` bigint(20) DEFAULT NULL,
  `firm_name` varchar(255) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `num_of_companies` varchar(255) DEFAULT NULL,
  `num_of_rounds` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`top_coinvestors_id`)
) ENGINE=InnoDB AUTO_INCREMENT=35220 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for year_breakdown
-- ----------------------------
DROP TABLE IF EXISTS `year_breakdown`;
CREATE TABLE `year_breakdown` (
  `year_breakdown_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `firm_id` bigint(20) DEFAULT NULL,
  `firm_name` varchar(255) DEFAULT NULL,
  `num_of_company_total` varchar(255) DEFAULT NULL,
  `sum_inv_total` varchar(255) DEFAULT NULL,
  `avg_per_company_total` varchar(255) DEFAULT NULL,
  `percent_of_inv_total` varchar(255) DEFAULT NULL,
  `year_name` varchar(255) DEFAULT NULL,
  `num_of_company` varchar(255) DEFAULT NULL,
  `sum_inv` varchar(255) DEFAULT NULL,
  `avg_per_company` varchar(255) DEFAULT NULL,
  `percent_of_inv` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`year_breakdown_id`)
) ENGINE=InnoDB AUTO_INCREMENT=99954 DEFAULT CHARSET=utf8;
