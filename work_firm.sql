/*
Navicat MySQL Data Transfer

Source Server         : root
Source Server Version : 50721
Source Host           : localhost:3306
Source Database       : work_firm

Target Server Type    : MYSQL
Target Server Version : 50721
File Encoding         : 65001

Date: 2018-05-21 08:07:37
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for firm_basic_info
-- ----------------------------
DROP TABLE IF EXISTS `firm_basic_info`;
CREATE TABLE `firm_basic_info` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
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
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=639 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for firm_direct_investments
-- ----------------------------
DROP TABLE IF EXISTS `firm_direct_investments`;
CREATE TABLE `firm_direct_investments` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `firm_id` bigint(20) DEFAULT NULL,
  `firm_name` varchar(255) DEFAULT NULL,
  `company_name` varchar(255) DEFAULT NULL,
  `industry` varchar(255) DEFAULT NULL,
  `still_in_portfolio` varchar(255) DEFAULT NULL,
  `company_status` varchar(255) DEFAULT NULL,
  `last_investment_date` varchar(255) DEFAULT NULL,
  `location` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=81823 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for firm_executives
-- ----------------------------
DROP TABLE IF EXISTS `firm_executives`;
CREATE TABLE `firm_executives` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `firm_id` bigint(20) DEFAULT NULL,
  `firm_name` varchar(255) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `title` varchar(255) DEFAULT NULL,
  `phone` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9494 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for firm_funds_managed_by_firm
-- ----------------------------
DROP TABLE IF EXISTS `firm_funds_managed_by_firm`;
CREATE TABLE `firm_funds_managed_by_firm` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `firm_id` bigint(20) DEFAULT NULL,
  `firm_name` varchar(255) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `size` varchar(255) DEFAULT NULL,
  `fund_stage` varchar(255) DEFAULT NULL,
  `vintage` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5736 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for firm_investment_profile_industry_breakdown
-- ----------------------------
DROP TABLE IF EXISTS `firm_investment_profile_industry_breakdown`;
CREATE TABLE `firm_investment_profile_industry_breakdown` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
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
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5929 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for firm_investment_profile_nation_breakdown
-- ----------------------------
DROP TABLE IF EXISTS `firm_investment_profile_nation_breakdown`;
CREATE TABLE `firm_investment_profile_nation_breakdown` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
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
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3331 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for firm_investment_profile_stage_breakdown
-- ----------------------------
DROP TABLE IF EXISTS `firm_investment_profile_stage_breakdown`;
CREATE TABLE `firm_investment_profile_stage_breakdown` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
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
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5480 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for firm_investment_profile_state_breakdown
-- ----------------------------
DROP TABLE IF EXISTS `firm_investment_profile_state_breakdown`;
CREATE TABLE `firm_investment_profile_state_breakdown` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
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
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10644 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for firm_investment_profile_status_breakdown
-- ----------------------------
DROP TABLE IF EXISTS `firm_investment_profile_status_breakdown`;
CREATE TABLE `firm_investment_profile_status_breakdown` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
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
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3711 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for firm_investment_profile_year_breakdown
-- ----------------------------
DROP TABLE IF EXISTS `firm_investment_profile_year_breakdown`;
CREATE TABLE `firm_investment_profile_year_breakdown` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
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
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11787 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for firm_other_offices
-- ----------------------------
DROP TABLE IF EXISTS `firm_other_offices`;
CREATE TABLE `firm_other_offices` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `firm_id` bigint(20) DEFAULT NULL,
  `firm_name` varchar(255) DEFAULT NULL,
  `detail_loc` varchar(255) DEFAULT NULL,
  `city` varchar(255) DEFAULT NULL,
  `state` varchar(255) DEFAULT NULL,
  `country` varchar(255) DEFAULT NULL,
  `phone` varchar(255) DEFAULT NULL,
  `fax` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=933 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for firm_related_news
-- ----------------------------
DROP TABLE IF EXISTS `firm_related_news`;
CREATE TABLE `firm_related_news` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `firm_id` bigint(20) DEFAULT NULL,
  `firm_name` varchar(255) DEFAULT NULL,
  `headline` varchar(255) DEFAULT NULL,
  `date` varchar(255) DEFAULT NULL,
  `publication` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for firm_top_co_investors
-- ----------------------------
DROP TABLE IF EXISTS `firm_top_co_investors`;
CREATE TABLE `firm_top_co_investors` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `firm_id` bigint(20) DEFAULT NULL,
  `firm_name` varchar(255) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `num_of_companies` varchar(255) DEFAULT NULL,
  `num_of_rounds` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3010 DEFAULT CHARSET=utf8;
