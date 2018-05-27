/*
Navicat MySQL Data Transfer

Source Server         : root
Source Server Version : 50721
Source Host           : localhost:3306
Source Database       : work_fund

Target Server Type    : MYSQL
Target Server Version : 50721
File Encoding         : 65001

Date: 2018-05-21 08:07:48
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for fund_basic_info
-- ----------------------------
DROP TABLE IF EXISTS `fund_basic_info`;
CREATE TABLE `fund_basic_info` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `fund_status` varchar(255) DEFAULT NULL,
  `fund_stage` varchar(255) DEFAULT NULL,
  `vintage_year` varchar(255) DEFAULT NULL,
  `management_firm` varchar(255) DEFAULT NULL,
  `fund_size` varchar(255) DEFAULT NULL,
  `fund_size_target` varchar(255) DEFAULT NULL,
  `fund_investors_type` varchar(255) DEFAULT NULL,
  `detail_loc` varchar(255) DEFAULT NULL,
  `city` varchar(255) DEFAULT NULL,
  `state` varchar(255) DEFAULT NULL,
  `country` varchar(255) DEFAULT NULL,
  `phone` varchar(255) DEFAULT NULL,
  `fax` varchar(255) DEFAULT NULL,
  `website` varchar(255) DEFAULT NULL,
  `file_info` varchar(2000) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4419 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for fund_direct_investments
-- ----------------------------
DROP TABLE IF EXISTS `fund_direct_investments`;
CREATE TABLE `fund_direct_investments` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `fund_id` bigint(20) DEFAULT NULL,
  `fund_name` varchar(255) DEFAULT NULL,
  `company_name` varchar(255) DEFAULT NULL,
  `industry` varchar(255) DEFAULT NULL,
  `still_in_portfolio` varchar(255) DEFAULT NULL,
  `company_status` varchar(255) DEFAULT NULL,
  `last_investment_date` varchar(255) DEFAULT NULL,
  `location` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=148270 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for fund_executives
-- ----------------------------
DROP TABLE IF EXISTS `fund_executives`;
CREATE TABLE `fund_executives` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `fund_id` bigint(20) DEFAULT NULL,
  `fund_name` varchar(255) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `title` varchar(255) DEFAULT NULL,
  `phone` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=73673 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for fund_investment_profile_industry_breakdown
-- ----------------------------
DROP TABLE IF EXISTS `fund_investment_profile_industry_breakdown`;
CREATE TABLE `fund_investment_profile_industry_breakdown` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `fund_id` bigint(20) DEFAULT NULL,
  `fund_name` varchar(255) DEFAULT NULL,
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
) ENGINE=InnoDB AUTO_INCREMENT=28520 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for fund_investment_profile_nation_breakdown
-- ----------------------------
DROP TABLE IF EXISTS `fund_investment_profile_nation_breakdown`;
CREATE TABLE `fund_investment_profile_nation_breakdown` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `fund_id` bigint(20) DEFAULT NULL,
  `fund_name` varchar(255) DEFAULT NULL,
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
) ENGINE=InnoDB AUTO_INCREMENT=11437 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for fund_investment_profile_stage_breakdown
-- ----------------------------
DROP TABLE IF EXISTS `fund_investment_profile_stage_breakdown`;
CREATE TABLE `fund_investment_profile_stage_breakdown` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `fund_id` bigint(20) DEFAULT NULL,
  `fund_name` varchar(255) DEFAULT NULL,
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
) ENGINE=InnoDB AUTO_INCREMENT=25005 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for fund_investment_profile_state_breakdown
-- ----------------------------
DROP TABLE IF EXISTS `fund_investment_profile_state_breakdown`;
CREATE TABLE `fund_investment_profile_state_breakdown` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `fund_id` bigint(20) DEFAULT NULL,
  `fund_name` varchar(255) DEFAULT NULL,
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
) ENGINE=InnoDB AUTO_INCREMENT=42093 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for fund_investment_profile_status_breakdown
-- ----------------------------
DROP TABLE IF EXISTS `fund_investment_profile_status_breakdown`;
CREATE TABLE `fund_investment_profile_status_breakdown` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `fund_id` bigint(20) DEFAULT NULL,
  `fund_name` varchar(255) DEFAULT NULL,
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
) ENGINE=InnoDB AUTO_INCREMENT=18980 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for fund_investment_profile_year_breakdown
-- ----------------------------
DROP TABLE IF EXISTS `fund_investment_profile_year_breakdown`;
CREATE TABLE `fund_investment_profile_year_breakdown` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `fund_id` bigint(20) DEFAULT NULL,
  `fund_name` varchar(255) DEFAULT NULL,
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
) ENGINE=InnoDB AUTO_INCREMENT=41112 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for fund_known_lp_investors
-- ----------------------------
DROP TABLE IF EXISTS `fund_known_lp_investors`;
CREATE TABLE `fund_known_lp_investors` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `fund_id` bigint(20) DEFAULT NULL,
  `fund_name` varchar(255) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1671 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for fund_top_co_investors
-- ----------------------------
DROP TABLE IF EXISTS `fund_top_co_investors`;
CREATE TABLE `fund_top_co_investors` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `fund_id` bigint(20) DEFAULT NULL,
  `fund_name` varchar(255) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `num_of_companies` varchar(255) DEFAULT NULL,
  `num_of_rounds` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19943 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for other_funds_managed_by_firm
-- ----------------------------
DROP TABLE IF EXISTS `other_funds_managed_by_firm`;
CREATE TABLE `other_funds_managed_by_firm` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `fund_id` bigint(20) DEFAULT NULL,
  `fund_name` varchar(255) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `size` varchar(255) DEFAULT NULL,
  `fund_stage` varchar(255) DEFAULT NULL,
  `vintage` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=43810 DEFAULT CHARSET=utf8;
