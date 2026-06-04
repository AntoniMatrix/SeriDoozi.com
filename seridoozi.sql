-- phpMyAdmin SQL Dump
-- version 5.2.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jun 04, 2026 at 09:09 AM
-- Server version: 10.6.18-MariaDB-cll-lve
-- PHP Version: 8.4.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `seridoozi`
--

-- --------------------------------------------------------

--
-- Table structure for table `accounts_user`
--

CREATE TABLE `accounts_user` (
  `id` bigint(20) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `phone` varchar(20) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `accounts_user`
--

INSERT INTO `accounts_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`, `phone`) VALUES
(1, 'pbkdf2_sha256$1000000$f2J1sw0cY0sKjADJOascd5$HmxeyuQUR+Y305fNbo0xjyXx9mZFsA3zRcVaSEcepj0=', '2026-05-24 07:16:31.783466', 1, 'Hirad_Yadegari', 'هیراد', 'یادگاری', 'hirad.ya23@gmail.com', 1, 1, '2026-05-02 16:24:35.000000', '09101742390'),
(3, 'pbkdf2_sha256$1000000$hXhTddt4UAgq5mZB45SKMS$iXWukQkHg0DJV9ydaH5zFlfC4kVL+lMa8snJimX65vA=', '2026-06-02 23:46:47.173647', 0, 'Antoni_Matrix', '', '', 'hiradgogoli1382@gmail.com', 0, 1, '2026-05-02 18:47:35.102337', '09912805945'),
(4, 'pbkdf2_sha256$1000000$8IaImdxPVwF8zhPkZiGy0k$5588vP3USI9eQZQdwQIaZevjDSiRtM/p2wGELRqihZg=', '2026-06-02 23:44:27.000000', 1, 'Akbar_Yadegari', '', '', 'akbaryadegari47@gmail.com', 1, 1, '2026-05-03 11:07:33.000000', '09124028834'),
(5, 'pbkdf2_sha256$1000000$xUixMbazpPANX2f7bZwHCN$2CgFymXuR7Niwkl+TkTXreTrEWlmFOxX/ssEKK/vlSs=', '2026-05-20 19:08:28.000000', 0, 'behnoush', 'بهنوش', 'روزبهانی', 'behnooshroozbahani2000@gmail.com', 1, 1, '2026-05-20 19:08:27.000000', '09909078324');

-- --------------------------------------------------------

--
-- Table structure for table `accounts_user_groups`
--

CREATE TABLE `accounts_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `accounts_user_groups`
--

INSERT INTO `accounts_user_groups` (`id`, `user_id`, `group_id`) VALUES
(2, 5, 1);

-- --------------------------------------------------------

--
-- Table structure for table `accounts_user_user_permissions`
--

CREATE TABLE `accounts_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `auth_group`
--

INSERT INTO `auth_group` (`id`, `name`) VALUES
(1, 'SEO');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `auth_group_permissions`
--

INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES
(1, 1, 72),
(2, 1, 69),
(3, 1, 70),
(4, 1, 71),
(5, 1, 25),
(6, 1, 26),
(7, 1, 27),
(8, 1, 28);

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add contact message', 6, 'add_contactmessage'),
(22, 'Can change contact message', 6, 'change_contactmessage'),
(23, 'Can delete contact message', 6, 'delete_contactmessage'),
(24, 'Can view contact message', 6, 'view_contactmessage'),
(25, 'Can add Site Page', 7, 'add_sitepage'),
(26, 'Can change Site Page', 7, 'change_sitepage'),
(27, 'Can delete Site Page', 7, 'delete_sitepage'),
(28, 'Can view Site Page', 7, 'view_sitepage'),
(29, 'Can add tutorial', 8, 'add_tutorial'),
(30, 'Can change tutorial', 8, 'change_tutorial'),
(31, 'Can delete tutorial', 8, 'delete_tutorial'),
(32, 'Can view tutorial', 8, 'view_tutorial'),
(33, 'Can add user', 9, 'add_user'),
(34, 'Can change user', 9, 'change_user'),
(35, 'Can delete user', 9, 'delete_user'),
(36, 'Can view user', 9, 'view_user'),
(37, 'Can add Order', 10, 'add_order'),
(38, 'Can change Order', 10, 'change_order'),
(39, 'Can delete Order', 10, 'delete_order'),
(40, 'Can view Order', 10, 'view_order'),
(41, 'Can add Order Item', 11, 'add_orderitem'),
(42, 'Can change Order Item', 11, 'change_orderitem'),
(43, 'Can delete Order Item', 11, 'delete_orderitem'),
(44, 'Can view Order Item', 11, 'view_orderitem'),
(45, 'Can add Order File', 12, 'add_orderfile'),
(46, 'Can change Order File', 12, 'change_orderfile'),
(47, 'Can delete Order File', 12, 'delete_orderfile'),
(48, 'Can view Order File', 12, 'view_orderfile'),
(49, 'Can add Order Message', 13, 'add_ordermessage'),
(50, 'Can change Order Message', 13, 'change_ordermessage'),
(51, 'Can delete Order Message', 13, 'delete_ordermessage'),
(52, 'Can view Order Message', 13, 'view_ordermessage'),
(53, 'Can add Payment', 14, 'add_payment'),
(54, 'Can change Payment', 14, 'change_payment'),
(55, 'Can delete Payment', 14, 'delete_payment'),
(56, 'Can view Payment', 14, 'view_payment'),
(57, 'Can add VIP Size', 15, 'add_orderitemvipsize'),
(58, 'Can change VIP Size', 15, 'change_orderitemvipsize'),
(59, 'Can delete VIP Size', 15, 'delete_orderitemvipsize'),
(60, 'Can view VIP Size', 15, 'view_orderitemvipsize'),
(61, 'Can add Invoice', 16, 'add_invoice'),
(62, 'Can change Invoice', 16, 'change_invoice'),
(63, 'Can delete Invoice', 16, 'delete_invoice'),
(64, 'Can view Invoice', 16, 'view_invoice'),
(65, 'Can add Invoice Item', 17, 'add_invoiceitem'),
(66, 'Can change Invoice Item', 17, 'change_invoiceitem'),
(67, 'Can delete Invoice Item', 17, 'delete_invoiceitem'),
(68, 'Can view Invoice Item', 17, 'view_invoiceitem'),
(69, 'Can add post', 18, 'add_post'),
(70, 'Can change post', 18, 'change_post'),
(71, 'Can delete post', 18, 'delete_post'),
(72, 'Can view post', 18, 'view_post');

-- --------------------------------------------------------

--
-- Table structure for table `blog_post`
--

CREATE TABLE `blog_post` (
  `id` bigint(20) NOT NULL,
  `title` varchar(255) NOT NULL,
  `slug` varchar(50) NOT NULL,
  `excerpt` longtext NOT NULL,
  `thumbnail` varchar(100) DEFAULT NULL,
  `meta_title` varchar(255) NOT NULL,
  `meta_description` longtext NOT NULL,
  `canonical_url` varchar(200) NOT NULL,
  `content` longtext NOT NULL,
  `status` varchar(10) NOT NULL,
  `published_at` datetime(6) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `core_contactmessage`
--

CREATE TABLE `core_contactmessage` (
  `id` bigint(20) NOT NULL,
  `name` varchar(80) NOT NULL,
  `email` varchar(254) NOT NULL,
  `subject` varchar(120) NOT NULL,
  `message` longtext NOT NULL,
  `ip_address` char(39) DEFAULT NULL,
  `user_agent` varchar(240) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `is_read` tinyint(1) NOT NULL,
  `number` varchar(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `core_sitepage`
--

CREATE TABLE `core_sitepage` (
  `id` bigint(20) NOT NULL,
  `key` varchar(30) NOT NULL,
  `title` varchar(120) NOT NULL,
  `meta_title` varchar(70) NOT NULL,
  `meta_description` varchar(160) NOT NULL,
  `canonical_path` varchar(200) NOT NULL,
  `hero_title` varchar(120) NOT NULL,
  `hero_subtitle` varchar(240) NOT NULL,
  `body` longtext NOT NULL,
  `highlights_json` longtext DEFAULT NULL CHECK (json_valid(`highlights_json`)),
  `is_published` tinyint(1) NOT NULL,
  `updated_at` datetime(6) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `core_sitepage`
--

INSERT INTO `core_sitepage` (`id`, `key`, `title`, `meta_title`, `meta_description`, `canonical_path`, `hero_title`, `hero_subtitle`, `body`, `highlights_json`, `is_published`, `updated_at`) VALUES
(1, 'about', 'درباره ما', 'درباره کارگاه سری‌دوزی | ثبت سفارش تولید', 'درباره کارگاه سری‌دوزی، ظرفیت تولید، کنترل کیفیت و روند ثبت سفارش و تحویل.', '', 'کارگاه سری‌دوزی لباس زنانه', 'تولید منظم، کنترل کیفیت، تحویل دقیق', 'کارگاه سری‌دوزی ما از سال ۱۳۶۸ در زمینه تولید عمده پوشاک زنانه و سری‌دوزی تخصصی فعالیت می‌کند.\r\n\r\nماموریت ما ارائه دوخت باکیفیت، تحویل دقیق و تجربه‌ای مطمئن برای مشتریانی است که به استاندارد حرفه‌ای تولید لباس اهمیت می‌دهند.\r\n\r\nما خدمات زیر را ارائه می‌دهیم:\r\n\r\n• تولید عمده پوشاک زنانه\r\n\r\n• سری‌دوزی برای مزون‌ها، فروشگاه‌ها و برندها\r\n\r\n• دوخت لباس فرم مدارس و سازمان‌ها\r\n\r\n• آموزش تخصصی خیاطی برای ورود به بازار کار\r\n\r\nهدف ما ایجاد این احساس در مخاطب است که:\r\n\r\nبرای سپردن سفارش دوخت، اینجا بهترین انتخاب است.', '[{\"desc\": \"\\u0628\\u0631\\u0631\\u0633\\u06cc \\u0645\\u0631\\u062d\\u0644\\u0647\\u200c\\u0627\\u06cc \\u0642\\u0628\\u0644 \\u0627\\u0632 \\u062a\\u062d\\u0648\\u06cc\\u0644\", \"title\": \"\\u06a9\\u0646\\u062a\\u0631\\u0644 \\u06a9\\u06cc\\u0641\\u06cc\\u062a\"}, {\"desc\": \"\\u067e\\u0630\\u06cc\\u0631\\u0634 \\u0633\\u0641\\u0627\\u0631\\u0634\\u200c\\u0647\\u0627\\u06cc \\u062a\\u06cc\\u0631\\u0627\\u0698\", \"title\": \"\\u0638\\u0631\\u0641\\u06cc\\u062a \\u062a\\u0648\\u0644\\u06cc\\u062f\"}, {\"desc\": \"\\u062a\\u062d\\u0648\\u06cc\\u0644 \\u0637\\u0628\\u0642 \\u0628\\u0631\\u0646\\u0627\\u0645\\u0647\", \"title\": \"\\u0632\\u0645\\u0627\\u0646\\u200c\\u0628\\u0646\\u062f\\u06cc\"}, {\"title\": \"\\u067e\\u0631\\u062f\\u0627\\u062e\\u062a \\u0622\\u0633\\u0627\\u0646\", \"desc\": \"\\u0627\\u0645\\u06a9\\u0627\\u0646 \\u067e\\u0631\\u062f\\u0627\\u062e\\u062a \\u0645\\u0631\\u062d\\u0644\\u0647\\u200c\\u0627\\u06cc \\u0628\\u0631\\u0627\\u06cc \\u0631\\u0627\\u062d\\u062a\\u06cc \\u0628\\u06cc\\u0634\\u062a\\u0631 \\u0645\\u0634\\u062a\\u0631\\u06cc\"}, {\"title\": \"\\u067e\\u06cc\\u0634\\u200c\\u0641\\u0627\\u06a9\\u062a\\u0648\\u0631 \\u0634\\u0641\\u0627\\u0641\", \"desc\": \"\\u0627\\u0631\\u0633\\u0627\\u0644 \\u067e\\u06cc\\u0634\\u200c\\u0641\\u0627\\u06a9\\u062a\\u0648\\u0631 \\u062f\\u0642\\u06cc\\u0642 \\u0642\\u0628\\u0644 \\u0627\\u0632 \\u0634\\u0631\\u0648\\u0639 \\u06a9\\u0627\\u0631\"}, {\"title\": \"\\u0646\\u0645\\u0648\\u0646\\u0647\\u200c\\u062f\\u0648\\u0632\\u06cc \\u0627\\u0648\\u0644\\u06cc\\u0647\", \"desc\": \"\\u062a\\u062d\\u0648\\u06cc\\u0644 \\u0633\\u0631\\u06cc\\u0639 \\u0627\\u0648\\u0644\\u06cc\\u0646 \\u0646\\u0645\\u0648\\u0646\\u0647 \\u062c\\u0647\\u062a \\u062a\\u0623\\u06cc\\u06cc\\u062f \\u0646\\u0647\\u0627\\u06cc\\u06cc\"}, {\"title\": \"\\u062a\\u0636\\u0645\\u06cc\\u0646 \\u0635\\u062f\\u0627\\u0642\\u062a\", \"desc\": \"\\u062a\\u0639\\u0647\\u062f \\u06a9\\u0627\\u0645\\u0644 \\u0628\\u0647 \\u0634\\u0641\\u0627\\u0641\\u06cc\\u062a \\u062f\\u0631 \\u0647\\u0645\\u0647 \\u0645\\u0631\\u0627\\u062d\\u0644 \\u06a9\\u0627\\u0631\"}, {\"title\": \"\\u062a\\u062e\\u0635\\u0635 \\u062d\\u0631\\u0641\\u0647\\u200c\\u0627\\u06cc\", \"desc\": \"\\u062a\\u062c\\u0631\\u0628\\u0647 \\u0686\\u0646\\u062f \\u062f\\u0647\\u0647 \\u0641\\u0639\\u0627\\u0644\\u06cc\\u062a \\u062a\\u062e\\u0635\\u0635\\u06cc \\u062f\\u0631 \\u0633\\u0631\\u06cc\\u200c\\u062f\\u0648\\u0632\\u06cc\"}, {\"title\": \"\\u06a9\\u06cc\\u0641\\u06cc\\u062a \\u067e\\u0627\\u06cc\\u062f\\u0627\\u0631\", \"desc\": \"\\u0627\\u0633\\u062a\\u0641\\u0627\\u062f\\u0647 \\u0627\\u0632 \\u0628\\u0647\\u062a\\u0631\\u06cc\\u0646 \\u0631\\u0648\\u0634\\u200c\\u0647\\u0627\\u06cc \\u062f\\u0648\\u062e\\u062a \\u0628\\u0631\\u0627\\u06cc \\u0645\\u0627\\u0646\\u062f\\u06af\\u0627\\u0631\\u06cc \\u0645\\u062d\\u0635\\u0648\\u0644\"}]', 1, '2026-05-04 15:34:37.473335'),
(2, 'contact', 'تماس با ما', 'تماس با ما | ثبت سفارش سری‌دوزی', 'برای ارتباط با کارگاه، سوالات و همکاری از فرم تماس استفاده کنید.', '', 'تماس با ما', 'پاسخ‌گویی سریع به درخواست‌ها', 'برای ثبت سفارش از صفحه ثبت سفارش استفاده کنید.\nبرای سوالات، فرم تماس را ارسال کنید.', '[]', 1, '2026-02-27 12:45:39.000000'),
(3, 'FAQ', 'سوالات متداول', 'سوالات متداول', 'برای ارتباط با کارگاه، سوالات و همکاری از فرم تماس استفاده کنید.', '', 'سوالات متداول', '', 'سوالات متداول', '[{\"question\": \"\\u062d\\u062f\\u0627\\u0642\\u0644 \\u062a\\u0639\\u062f\\u0627\\u062f \\u0633\\u0641\\u0627\\u0631\\u0634 \\u0628\\u0631\\u0627\\u06cc \\u0633\\u0631\\u06cc\\u200c\\u062f\\u0648\\u0632\\u06cc \\u0686\\u0642\\u062f\\u0631 \\u0627\\u0633\\u062a\\u061f\", \"answer\": \"\\u062d\\u062f\\u0627\\u0642\\u0644 \\u062a\\u06cc\\u0631\\u0627\\u0698 \\u0628\\u0633\\u062a\\u0647 \\u0628\\u0647 \\u0646\\u0648\\u0639 \\u0644\\u0628\\u0627\\u0633 \\u0645\\u062a\\u0641\\u0627\\u0648\\u062a \\u0627\\u0633\\u062a\\u060c \\u0627\\u0645\\u0627 \\u0645\\u0639\\u0645\\u0648\\u0644\\u0627\\u064b \\u0633\\u0641\\u0627\\u0631\\u0634\\u200c\\u0647\\u0627 \\u0627\\u0632 \\u06f1\\u06f0 \\u062a\\u0627 \\u06f3\\u06f0 \\u0639\\u062f\\u062f \\u0622\\u063a\\u0627\\u0632 \\u0645\\u06cc\\u200c\\u0634\\u0648\\u062f.\"}, {\"question\": \"\\u0622\\u06cc\\u0627 \\u0642\\u0628\\u0644 \\u0627\\u0632 \\u062a\\u0648\\u0644\\u06cc\\u062f \\u0627\\u0646\\u0628\\u0648\\u0647 \\u0646\\u0645\\u0648\\u0646\\u0647 \\u0627\\u0648\\u0644\\u06cc\\u0647 \\u0627\\u0631\\u0627\\u0626\\u0647 \\u0645\\u06cc\\u200c\\u0634\\u0648\\u062f\\u061f\", \"answer\": \"\\u0628\\u0644\\u0647\\u060c \\u067e\\u06cc\\u0634 \\u0627\\u0632 \\u0634\\u0631\\u0648\\u0639 \\u0633\\u0631\\u06cc\\u200c\\u062f\\u0648\\u0632\\u06cc\\u060c \\u06cc\\u06a9 \\u0646\\u0645\\u0648\\u0646\\u0647 \\u0627\\u0648\\u0644\\u06cc\\u0647 \\u062c\\u0647\\u062a \\u062a\\u0623\\u06cc\\u06cc\\u062f \\u0646\\u0647\\u0627\\u06cc\\u06cc \\u0622\\u0645\\u0627\\u062f\\u0647 \\u0648 \\u0627\\u0631\\u0627\\u0626\\u0647 \\u0645\\u06cc\\u200c\\u0634\\u0648\\u062f.\"}, {\"question\": \"\\u0645\\u062f\\u062a \\u0632\\u0645\\u0627\\u0646 \\u062a\\u062d\\u0648\\u06cc\\u0644 \\u0633\\u0641\\u0627\\u0631\\u0634 \\u0686\\u0642\\u062f\\u0631 \\u0627\\u0633\\u062a\\u061f\", \"answer\": \"\\u0632\\u0645\\u0627\\u0646 \\u062a\\u062d\\u0648\\u06cc\\u0644 \\u0628\\u0647 \\u0645\\u062f\\u0644 \\u0648 \\u062a\\u06cc\\u0631\\u0627\\u0698 \\u0628\\u0633\\u062a\\u06af\\u06cc \\u062f\\u0627\\u0631\\u062f\\u060c \\u0627\\u0645\\u0627 \\u0628\\u0631\\u0646\\u0627\\u0645\\u0647 \\u0632\\u0645\\u0627\\u0646\\u200c\\u0628\\u0646\\u062f\\u06cc \\u062f\\u0642\\u06cc\\u0642 \\u067e\\u06cc\\u0634 \\u0627\\u0632 \\u0634\\u0631\\u0648\\u0639 \\u06a9\\u0627\\u0631 \\u0627\\u0639\\u0644\\u0627\\u0645 \\u0645\\u06cc\\u200c\\u0634\\u0648\\u062f.\"}, {\"question\": \"\\u0627\\u0645\\u06a9\\u0627\\u0646 \\u067e\\u0631\\u062f\\u0627\\u062e\\u062a \\u0645\\u0631\\u062d\\u0644\\u0647\\u200c\\u0627\\u06cc \\u0648\\u062c\\u0648\\u062f \\u062f\\u0627\\u0631\\u062f\\u061f\", \"answer\": \"\\u0628\\u0644\\u0647\\u060c \\u0628\\u0631\\u0627\\u06cc \\u0631\\u0641\\u0627\\u0647 \\u0645\\u0634\\u062a\\u0631\\u06cc\\u0627\\u0646 \\u0627\\u0645\\u06a9\\u0627\\u0646 \\u067e\\u0631\\u062f\\u0627\\u062e\\u062a \\u0645\\u0631\\u062d\\u0644\\u0647\\u200c\\u0627\\u06cc \\u0641\\u0631\\u0627\\u0647\\u0645 \\u0634\\u062f\\u0647 \\u0627\\u0633\\u062a.\"}, {\"question\": \"\\u0622\\u06cc\\u0627 \\u067e\\u06cc\\u0634\\u200c\\u0641\\u0627\\u06a9\\u062a\\u0648\\u0631 \\u0627\\u0631\\u0633\\u0627\\u0644 \\u0645\\u06cc\\u200c\\u06a9\\u0646\\u06cc\\u062f\\u061f\", \"answer\": \"\\u0628\\u0644\\u0647\\u060c \\u0642\\u0628\\u0644 \\u0627\\u0632 \\u0634\\u0631\\u0648\\u0639 \\u06a9\\u0627\\u0631 \\u067e\\u06cc\\u0634\\u200c\\u0641\\u0627\\u06a9\\u062a\\u0648\\u0631 \\u0634\\u0641\\u0627\\u0641 \\u0634\\u0627\\u0645\\u0644 \\u0647\\u0632\\u06cc\\u0646\\u0647\\u200c\\u0647\\u0627 \\u0648 \\u0632\\u0645\\u0627\\u0646 \\u062a\\u062d\\u0648\\u06cc\\u0644 \\u0627\\u0631\\u0627\\u0626\\u0647 \\u0645\\u06cc\\u200c\\u0634\\u0648\\u062f.\"}, {\"question\": \"\\u0622\\u06cc\\u0627 \\u0628\\u0631\\u0627\\u06cc \\u0645\\u062f\\u0627\\u0631\\u0633 \\u0648 \\u0633\\u0627\\u0632\\u0645\\u0627\\u0646\\u200c\\u0647\\u0627 \\u0647\\u0645 \\u0633\\u0641\\u0627\\u0631\\u0634 \\u0645\\u06cc\\u200c\\u067e\\u0630\\u06cc\\u0631\\u06cc\\u062f\\u061f\", \"answer\": \"\\u0628\\u0644\\u0647\\u060c \\u062f\\u0648\\u062e\\u062a \\u0644\\u0628\\u0627\\u0633 \\u0641\\u0631\\u0645 \\u0645\\u062f\\u0627\\u0631\\u0633\\u060c \\u0634\\u0631\\u06a9\\u062a\\u200c\\u0647\\u0627 \\u0648 \\u0627\\u062f\\u0627\\u0631\\u0647\\u200c\\u062c\\u0627\\u062a \\u0627\\u0646\\u062c\\u0627\\u0645 \\u0645\\u06cc\\u200c\\u0634\\u0648\\u062f.\"}, {\"question\": \"\\u0622\\u06cc\\u0627 \\u0627\\u0645\\u06a9\\u0627\\u0646 \\u062a\\u0647\\u06cc\\u0647 \\u067e\\u0627\\u0631\\u0686\\u0647 \\u062a\\u0648\\u0633\\u0637 \\u06a9\\u0627\\u0631\\u06af\\u0627\\u0647 \\u0648\\u062c\\u0648\\u062f \\u062f\\u0627\\u0631\\u062f\\u061f\", \"answer\": \"\\u0628\\u0644\\u0647\\u060c \\u062f\\u0631 \\u0635\\u0648\\u0631\\u062a \\u0646\\u06cc\\u0627\\u0632 \\u062a\\u0647\\u06cc\\u0647 \\u067e\\u0627\\u0631\\u0686\\u0647 \\u0627\\u0646\\u062c\\u0627\\u0645 \\u0645\\u06cc\\u200c\\u0634\\u0648\\u062f \\u06cc\\u0627 \\u0645\\u06cc\\u200c\\u062a\\u0648\\u0627\\u0646\\u06cc\\u062f \\u067e\\u0627\\u0631\\u0686\\u0647 \\u0631\\u0627 \\u062e\\u0648\\u062f\\u062a\\u0627\\u0646 \\u062a\\u0623\\u0645\\u06cc\\u0646 \\u06a9\\u0646\\u06cc\\u062f.\"}, {\"question\": \"\\u0622\\u06cc\\u0627 \\u062f\\u0648\\u0631\\u0647 \\u0622\\u0645\\u0648\\u0632\\u0634 \\u062e\\u06cc\\u0627\\u0637\\u06cc \\u0628\\u0631\\u06af\\u0632\\u0627\\u0631 \\u0645\\u06cc\\u200c\\u06a9\\u0646\\u06cc\\u062f\\u061f\", \"answer\": \"\\u0628\\u0644\\u0647\\u060c \\u062f\\u0648\\u0631\\u0647\\u200c\\u0647\\u0627\\u06cc \\u062a\\u062e\\u0635\\u0635\\u06cc \\u062e\\u06cc\\u0627\\u0637\\u06cc \\u0648 \\u0633\\u0631\\u06cc\\u200c\\u062f\\u0648\\u0632\\u06cc \\u0628\\u0631\\u0627\\u06cc \\u0648\\u0631\\u0648\\u062f \\u062d\\u0631\\u0641\\u0647\\u200c\\u0627\\u06cc \\u0628\\u0647 \\u0628\\u0627\\u0632\\u0627\\u0631 \\u06a9\\u0627\\u0631 \\u0628\\u0631\\u06af\\u0632\\u0627\\u0631 \\u0645\\u06cc\\u200c\\u0634\\u0648\\u062f.\"}]', 1, '2026-06-01 11:20:37.209742');

-- --------------------------------------------------------

--
-- Table structure for table `core_tutorial`
--

CREATE TABLE `core_tutorial` (
  `id` bigint(20) NOT NULL,
  `title` varchar(200) NOT NULL,
  `slug` varchar(50) NOT NULL,
  `thumbnail` varchar(100) NOT NULL,
  `video` varchar(500) NOT NULL,
  `description` longtext NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2026-05-05 10:11:49.381017', '5', '245 × شومیز یقه مردانه', 2, '[{\"changed\": {\"fields\": [\"Fabric type\"]}}]', 11, 1),
(2, '2026-05-05 10:13:35.411502', '1', 'Hirad_Yadegari', 2, '[{\"changed\": {\"fields\": [\"First name\", \"Last name\", \"User permissions\", \"Phone\"]}}]', 9, 1),
(3, '2026-05-05 10:14:11.631847', '1', 'Hirad_Yadegari', 2, '[{\"changed\": {\"fields\": [\"User permissions\"]}}]', 9, 1),
(4, '2026-05-20 12:23:08.790311', '1', 'SEO', 1, '[{\"added\": {}}]', 3, 1),
(5, '2026-05-20 12:23:24.874732', '4', 'Akbar_Yadegari', 2, '[{\"changed\": {\"fields\": [\"Staff status\"]}}]', 9, 1),
(6, '2026-05-20 12:26:31.799255', '4', 'Akbar_Yadegari', 2, '[{\"changed\": {\"fields\": [\"Staff status\"]}}]', 9, 1),
(7, '2026-05-20 12:32:12.848252', '4', 'Akbar_Yadegari', 2, '[{\"changed\": {\"fields\": [\"Groups\"]}}]', 9, 1),
(8, '2026-05-20 12:33:16.941849', '4', 'Akbar_Yadegari', 2, '[{\"changed\": {\"fields\": [\"Groups\"]}}]', 9, 1),
(9, '2026-05-20 14:09:55.805643', '16', 'Order #16 - کا', 3, '', 10, 1),
(10, '2026-05-20 14:15:23.186689', '17', 'Order #17 - کت یقه بلیزری آستین دوتیکه', 2, '[{\"changed\": {\"fields\": [\"Title\"]}}]', 10, 1),
(11, '2026-05-20 14:37:36.965483', '18', 'Order #18 - پافر', 2, '[{\"changed\": {\"fields\": [\"Status\"]}}]', 10, 1),
(12, '2026-05-20 19:11:00.997304', '5', 'behnoush', 2, '[{\"changed\": {\"fields\": [\"First name\", \"Last name\", \"Staff status\", \"Groups\"]}}]', 9, 1),
(13, '2026-05-20 19:12:08.148861', '1', 'SEO', 2, '[{\"changed\": {\"fields\": [\"Permissions\"]}}]', 3, 1),
(14, '2026-05-22 17:05:48.468865', '4', 'Akbar_Yadegari', 2, '[{\"changed\": {\"fields\": [\"Staff status\", \"Superuser status\"]}}]', 9, 1),
(15, '2026-05-23 22:44:44.176997', '21', 'Order #21 -  \"-prompt(8)-\" \'-prompt(8)-\' \";a=prompt,a()// \';a=prompt,a()// \'-eval(\"window[\'pro\'%2B\'mpt\'](8)\")-\' \"-eval(\"window[\'pro\'%2B\'mpt\'](8)\")-\" \"onclick=prompt(8)>\"@x.y \"onclick=prompt(8)><svg/on', 3, '', 10, 1),
(16, '2026-05-23 22:46:20.308764', '1', '\"-prompt(8)-\" \'-prompt(8)-\' \";a=prompt,a()// \';a=prompt,a()// \'-eval(\"window[\'p - \"-prompt(8)-\" \'-prompt(8)-\' \";', 3, '', 6, 1),
(17, '2026-06-02 23:45:27.644799', '4', 'Akbar_Yadegari', 2, '[{\"changed\": {\"fields\": [\"Staff status\", \"Superuser status\"]}}]', 9, 1),
(18, '2026-06-02 23:46:01.527667', '4', 'Akbar_Yadegari', 2, '[{\"changed\": {\"fields\": [\"Staff status\", \"Superuser status\"]}}]', 9, 1),
(19, '2026-06-02 23:46:25.371178', '7', 'Payment 5500 IRR - قابل پرداخت for Order #19', 3, '', 14, 1),
(20, '2026-06-02 23:46:25.371445', '6', 'Payment 11000 IRR - پرداخت شده for Order #4', 3, '', 14, 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(2, 'auth', 'permission'),
(3, 'auth', 'group'),
(4, 'contenttypes', 'contenttype'),
(5, 'sessions', 'session'),
(6, 'core', 'contactmessage'),
(7, 'core', 'sitepage'),
(8, 'core', 'tutorial'),
(9, 'accounts', 'user'),
(10, 'orders', 'order'),
(11, 'orders', 'orderitem'),
(12, 'orders', 'orderfile'),
(13, 'orders', 'ordermessage'),
(14, 'orders', 'payment'),
(15, 'orders', 'orderitemvipsize'),
(16, 'orders', 'invoice'),
(17, 'orders', 'invoiceitem'),
(18, 'blog', 'post');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2026-05-02 13:53:14.147453'),
(2, 'contenttypes', '0002_remove_content_type_name', '2026-05-02 13:53:14.184901'),
(3, 'auth', '0001_initial', '2026-05-02 13:53:14.312039'),
(4, 'auth', '0002_alter_permission_name_max_length', '2026-05-02 13:53:14.330861'),
(5, 'auth', '0003_alter_user_email_max_length', '2026-05-02 13:53:14.342113'),
(6, 'auth', '0004_alter_user_username_opts', '2026-05-02 13:53:14.353137'),
(7, 'auth', '0005_alter_user_last_login_null', '2026-05-02 13:53:14.363288'),
(8, 'auth', '0006_require_contenttypes_0002', '2026-05-02 13:53:14.366004'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2026-05-02 13:53:14.376407'),
(10, 'auth', '0008_alter_user_username_max_length', '2026-05-02 13:53:14.386509'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2026-05-02 13:53:14.396697'),
(12, 'auth', '0010_alter_group_name_max_length', '2026-05-02 13:53:14.416760'),
(13, 'auth', '0011_update_proxy_permissions', '2026-05-02 13:53:14.428513'),
(14, 'auth', '0012_alter_user_first_name_max_length', '2026-05-02 13:53:14.441167'),
(15, 'accounts', '0001_initial', '2026-05-02 13:53:14.562815'),
(16, 'admin', '0001_initial', '2026-05-02 13:53:14.634558'),
(17, 'admin', '0002_logentry_remove_auto_add', '2026-05-02 13:53:14.650973'),
(18, 'admin', '0003_logentry_add_action_flag_choices', '2026-05-02 13:53:14.666788'),
(19, 'blog', '0001_initial', '2026-05-02 13:53:14.711085'),
(20, 'blog', '0002_post_remove_articleblock_article_delete_article_and_more', '2026-05-02 13:53:14.791622'),
(21, 'blog', '0003_alter_post_content', '2026-05-02 13:53:14.796871'),
(22, 'blog', '0004_alter_post_content_alter_post_status', '2026-05-02 13:53:14.804854'),
(23, 'core', '0001_initial', '2026-05-02 13:53:14.829489'),
(24, 'core', '0002_contactmessage_number', '2026-05-02 13:53:14.846816'),
(25, 'core', '0003_alter_tutorial_video', '2026-05-02 13:53:14.860633'),
(26, 'orders', '0001_initial', '2026-05-02 13:53:15.194778'),
(27, 'orders', '0002_alter_payment_options_payment_gateway_and_more', '2026-05-02 13:53:15.558345'),
(28, 'orders', '0003_alter_payment_options_and_more', '2026-05-02 13:53:15.924701'),
(29, 'orders', '0004_alter_payment_options_remove_payment_service_type', '2026-05-02 13:53:15.979275'),
(30, 'orders', '0005_alter_order_status_alter_payment_date_and_more', '2026-05-02 13:53:16.060984'),
(31, 'orders', '0006_alter_payment_gateway_alter_payment_transaction_id', '2026-05-02 13:53:16.127833'),
(32, 'orders', '0007_remove_order_customer_note_and_more', '2026-05-02 13:53:16.554712'),
(33, 'orders', '0008_alter_invoice_tax_rate', '2026-05-02 13:53:16.589535'),
(34, 'orders', '0009_alter_invoiceitem_quantity', '2026-05-02 13:53:16.612640'),
(35, 'orders', '0010_payment_authority', '2026-05-02 13:53:16.646820'),
(36, 'orders', '0011_alter_orderitem_size_mode', '2026-05-02 13:53:16.674679'),
(37, 'orders', '0012_remove_order_delivery_date', '2026-05-02 13:53:16.712992'),
(38, 'sessions', '0001_initial', '2026-05-02 13:53:16.734981');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('ddaag9yvm7hz3qwaksmgo97o6lk3zv70', '.eJxVjMsOwiAUBf-FtSFSyhVcuvcbyH2AVA0kpV0Z_12bdKHbMzPnpSKuS4lrT3OcRJ2VVYffjZAfqW5A7lhvTXOryzyR3hS9066vTdLzsrt_BwV7-dbMzgfrEQcHYGWgYFjAkcEsXhg9ACKN4IaTD2zZZspAksdwpNEAqvcH-FY4mA:1wKabr:eaGuJoWWB2uzkQM57VCh6K0apiZMLky5swVx1soRU1M', '2026-05-20 11:40:11.469202'),
('6vjouw8i3ni6k5fk6d2aq3ghup0t6kse', '.eJxVjMsOwiAUBf-FtSFSyhVcuvcbyH2AVA0kpV0Z_12bdKHbMzPnpSKuS4lrT3OcRJ2VVYffjZAfqW5A7lhvTXOryzyR3hS9066vTdLzsrt_BwV7-dbMzgfrEQcHYGWgYFjAkcEsXhg9ACKN4IaTD2zZZspAksdwpNEAqvcH-FY4mA:1wKDrd:m2CrlG9_DPQVEnnK2x34kJPSw6CtqNWS0YcQ19qiu5E', '2026-05-19 11:22:57.645970'),
('qf7zi70sya0re2m00kccgmvn4enzlkh3', '.eJxVjMsOwiAQRf-FtSG8BZfu-w1kYAapGkhKuzL-uzbpQrf3nHNfLMK21rgNWuKM7MIkO_1uCfKD2g7wDu3Wee5tXebEd4UfdPCpIz2vh_t3UGHUb50capfJZCN1oGKNV1pASdqQsJKyRlu8Bzyb4AiUEEG5pMlLEMZjAfb-AOfqN_s:1wMVKO:lC_sZJA_P2pbXgTq1XJpauiIX5nvaBdCGURB3O9MNDg', '2026-05-25 18:26:04.061886'),
('5jvytn4ffhov1buto3c16mrasor7ooyj', '.eJxVjMsOwiAQRf-FtSG8BZfu-w1kYAapGkhKuzL-uzbpQrf3nHNfLMK21rgNWuKM7MIkO_1uCfKD2g7wDu3Wee5tXebEd4UfdPCpIz2vh_t3UGHUb50capfJZCN1oGKNV1pASdqQsJKyRlu8Bzyb4AiUEEG5pMlLEMZjAfb-AOfqN_s:1wMZTf:jL3V_mL3BNqbhQpXfMfZMVZ_-vjAmWctiUfKk8DxG-4', '2026-05-25 22:51:55.864219'),
('pp7olbzsb0vpicnxwo4iyjbw2ymmyfgw', '.eJxVjEEOwiAQRe_C2pBhGCx16b5naKAzSNVAUtqV8e7apAvd_vfef6kxbGsetybLOLO6KFKn3y2G6SFlB3wP5Vb1VMu6zFHvij5o00NleV4P9-8gh5a_NYYICfsgGMm6TogMGCJnPPbSoUfrCBATICQ4E4sVG9kxAXsCC-r9AbObNl0:1wND1c:taCcuztjPbrwUGIfjeGwlKklFYFIv7-P7hUzeE_n2Zs', '2026-05-27 17:05:36.697549'),
('cmov84v50kzg1q1ocezpxxhqpwv04z1v', '.eJxVjEEOwiAQRe_C2pBhGCx16b5naKAzSNVAUtqV8e7apAvd_vfef6kxbGsetybLOLO6KFKn3y2G6SFlB3wP5Vb1VMu6zFHvij5o00NleV4P9-8gh5a_NYYICfsgGMm6TogMGCJnPPbSoUfrCBATICQ4E4sVG9kxAXsCC-r9AbObNl0:1wMhpe:k-WEwW1oftx0Wl_7kmMQg0DHf7PiL2HO5v66fXdYiS0', '2026-05-26 07:47:10.405470'),
('gxigtvkjx1hbczfgkgho54t0yunjb83l', '.eJxVjMsOwiAQRf-FtSG8BZfu-w1kYAapGkhKuzL-uzbpQrf3nHNfLMK21rgNWuKM7MIkO_1uCfKD2g7wDu3Wee5tXebEd4UfdPCpIz2vh_t3UGHUb50capfJZCN1oGKNV1pASdqQsJKyRlu8Bzyb4AiUEEG5pMlLEMZjAfb-AOfqN_s:1wQTQa:lozLw1zrEEFLVazDe5PvsmnFfFRKKUBgc7ChYuENW84', '2026-06-05 17:12:52.481535'),
('e6ow6ankrxwetwgxbc64jgo29apvi1bm', '.eJxVjEEOwiAQRe_C2pBhGCx16b5naKAzSNVAUtqV8e7apAvd_vfef6kxbGsetybLOLO6KFKn3y2G6SFlB3wP5Vb1VMu6zFHvij5o00NleV4P9-8gh5a_NYYICfsgGMm6TogMGCJnPPbSoUfrCBATICQ4E4sVG9kxAXsCC-r9AbObNl0:1wPhfS:E1yxPnZjDW0MmCfTQ8ZAUHwFmge7C6hJFBb5e5oPKvM', '2026-06-03 14:13:02.948590'),
('xyix6waziqilre1dvjy5l9adjq1capqh', '.eJxVjMsOwiAQRf-FtSG8BZfu-w1kYAapGkhKuzL-uzbpQrf3nHNfLMK21rgNWuKM7MIkO_1uCfKD2g7wDu3Wee5tXebEd4UfdPCpIz2vh_t3UGHUb50capfJZCN1oGKNV1pASdqQsJKyRlu8Bzyb4AiUEEG5pMlLEMZjAfb-AOfqN_s:1wR34Z:JxNqqonsULdNa_59zH0RdiBAzPstRhQyX6l434oeC6c', '2026-06-07 07:16:31.788238'),
('f9vnguifbghw5em4ifigg0fjdkmvjl7e', '.eJxVjDsOwjAQBe_iGln-fyjpOYO19m5wANlSnFSIu0OkFNC-mXkvlmBba9oGLWlGdmaWnX63DOVBbQd4h3brvPS2LnPmu8IPOvi1Iz0vh_t3UGHUb-08OqGtiTpITVr5jHZCBVlRNrZQFtETkJIhiAgkphBNKdERRhOsBPb-ANm5N-U:1wPmHM:M5_O348ctbDZ5KjS4YEpgWe2jwl8RmRxluVIdma1FfY', '2026-06-03 19:08:28.455178'),
('zmilai7bu19lrmt9zt394k3rfwstoqpx', '.eJxVjMsOwiAUBf-FtSFSyhVcuvcbyH2AVA0kpV0Z_12bdKHbMzPnpSKuS4lrT3OcRJ2VVYffjZAfqW5A7lhvTXOryzyR3hS9066vTdLzsrt_BwV7-dbMzgfrEQcHYGWgYFjAkcEsXhg9ACKN4IaTD2zZZspAksdwpNEAqvcH-FY4mA:1wUYop:5Q08yNVS6yP2D2brtQLeScWa7rBUge-AvV2Ft5kC3Fw', '2026-06-16 23:46:47.175945');

-- --------------------------------------------------------

--
-- Table structure for table `orders_invoice`
--

CREATE TABLE `orders_invoice` (
  `id` bigint(20) NOT NULL,
  `invoice_type` varchar(20) NOT NULL,
  `tax_rate` decimal(5,0) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `order_id` bigint(20) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `orders_invoice`
--

INSERT INTO `orders_invoice` (`id`, `invoice_type`, `tax_rate`, `created_at`, `updated_at`, `order_id`) VALUES
(4, 'MATERIAL', 10, '2026-06-02 23:44:04.262245', '2026-06-02 23:44:04.262310', 19),
(3, 'MATERIAL', 10, '2026-05-05 11:07:04.207909', '2026-05-05 11:07:04.207949', 4);

-- --------------------------------------------------------

--
-- Table structure for table `orders_invoiceitem`
--

CREATE TABLE `orders_invoiceitem` (
  `id` bigint(20) NOT NULL,
  `title` varchar(255) NOT NULL,
  `description` longtext NOT NULL,
  `quantity` decimal(10,0) NOT NULL,
  `unit` varchar(50) NOT NULL,
  `unit_price_currency` varchar(3) NOT NULL,
  `unit_price_amount` decimal(12,0) NOT NULL,
  `invoice_id` bigint(20) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `orders_invoiceitem`
--

INSERT INTO `orders_invoiceitem` (`id`, `title`, `description`, `quantity`, `unit`, `unit_price_currency`, `unit_price_amount`, `invoice_id`) VALUES
(6, 'پارچه', '', 1, 'عدد', 'IRR', 5000, 4),
(5, 'کت', '', 1, 'عدد', 'IRR', 10000, 3);

-- --------------------------------------------------------

--
-- Table structure for table `orders_order`
--

CREATE TABLE `orders_order` (
  `id` bigint(20) NOT NULL,
  `title` varchar(255) NOT NULL,
  `status` varchar(12) NOT NULL,
  `fabric_by_workshop` tinyint(1) NOT NULL,
  `materials_by_workshop` tinyint(1) NOT NULL,
  `deadline` date DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `assigned_to_id` bigint(20) DEFAULT NULL,
  `customer_id` bigint(20) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `orders_order`
--

INSERT INTO `orders_order` (`id`, `title`, `status`, `fabric_by_workshop`, `materials_by_workshop`, `deadline`, `created_at`, `updated_at`, `assigned_to_id`, `customer_id`) VALUES
(2, 'شلوار و سارافون جین', 'DELIVERED', 1, 1, '2025-05-30', '2025-05-22 11:10:18.150881', '2025-05-22 11:10:18.150938', NULL, 4),
(3, 'شومیز یقه مردانه', 'DELIVERED', 1, 1, '2025-07-08', '2025-06-28 11:15:47.686268', '2025-06-28 11:15:47.686330', NULL, 4),
(4, 'شومیز یقه مردانه آستین کیمونو', 'DELIVERED', 1, 1, '2025-08-06', '2025-07-27 11:24:35.593989', '2025-07-27 11:24:35.594034', NULL, 4),
(12, 'کت یقه هفت', 'DELIVERED', 1, 1, '2025-08-19', '2025-08-11 13:43:57.681416', '2025-08-11 13:43:57.681454', NULL, 4),
(13, 'پیراهن پشت بنددار', 'DELIVERED', 1, 1, '2025-09-08', '2025-09-01 13:46:56.810033', '2025-09-01 13:46:56.810095', NULL, 4),
(14, 'کت یقه آرشال شالی', 'DELIVERED', 0, 1, '2025-10-02', '2025-09-16 13:50:06.363937', '2025-09-16 13:50:06.363997', NULL, 4),
(15, 'ژیله یقه هفت جیب فیلتو', 'DELIVERED', 1, 1, '2025-10-18', '2025-10-07 13:56:29.439642', '2025-10-07 13:56:29.439707', NULL, 4),
(18, 'پافر', 'DELIVERED', 1, 1, '2025-11-13', '2025-11-01 14:17:33.959861', '2025-11-01 14:37:36.960234', NULL, 4),
(17, 'کت یقه بلیزری آستین دوتیکه', 'DELIVERED', 1, 1, '2025-10-27', '2025-10-18 14:00:05.109962', '2025-10-18 14:15:23.181517', NULL, 4),
(19, 'بارانی آستر دار بلند', 'QUOTED', 1, 1, '2025-11-26', '2025-11-11 14:22:19.125856', '2025-11-11 14:22:19.125921', NULL, 4);

-- --------------------------------------------------------

--
-- Table structure for table `orders_orderfile`
--

CREATE TABLE `orders_orderfile` (
  `id` bigint(20) NOT NULL,
  `file` varchar(100) NOT NULL,
  `description` longtext NOT NULL,
  `uploaded_at` datetime(6) NOT NULL,
  `order_id` bigint(20) NOT NULL,
  `order_item_id` bigint(20) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `orders_orderitem`
--

CREATE TABLE `orders_orderitem` (
  `id` bigint(20) NOT NULL,
  `title` varchar(200) NOT NULL,
  `quantity` int(10) UNSIGNED NOT NULL CHECK (`quantity` >= 0),
  `description` longtext NOT NULL,
  `fabric_type` varchar(100) NOT NULL,
  `size_mode` varchar(10) NOT NULL,
  `size_from` varchar(50) NOT NULL,
  `size_to` varchar(50) NOT NULL,
  `order_id` bigint(20) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `orders_orderitem`
--

INSERT INTO `orders_orderitem` (`id`, `title`, `quantity`, `description`, `fabric_type`, `size_mode`, `size_from`, `size_to`, `order_id`) VALUES
(1, 'کت', 50, '', 'کتان', 'NORMAL', '34', '46', 1),
(2, 'شلوار', 25, '', '', 'VIP', '', '', 1),
(3, 'شلوار', 289, 'جهت سفارش مدارس', 'جین', 'NORMAL', '20', '40', 2),
(4, 'سارافون', 289, 'جهت سفارش مدارس', 'جین', 'NORMAL', '20', '40', 2),
(5, 'شومیز یقه مردانه', 245, 'جهت سفارش مدارس', 'تترون نخی', 'NORMAL', '20', '38', 3),
(6, 'شومیز یقه مردانه آستین کیمونو', 114, '', 'لنین', 'VIP', '', '', 4),
(18, 'پیراهن پشت بنددار', 105, '', 'لنین', 'NORMAL', 'L', '', 13),
(17, 'کت یقه هفت', 120, '', 'کرپ', 'NORMAL', 'XL', '', 12),
(19, 'کت یقه آرشال شالی', 110, '', 'لنین', 'NORMAL', 'XXL', '', 14),
(20, 'ژیله', 150, '', 'کرپ', 'NORMAL', 'XXXL', '', 15),
(23, 'پافر', 162, '', 'فوتر', 'NORMAL', 'M', 'S', 18),
(24, 'بارانی', 162, '', 'نینو', 'NORMAL', 'XS', 'XXS', 19),
(22, 'کت یقه بلیزری آستین دوتیکه', 120, '', 'کرپ', 'NORMAL', 'XXL', '', 17);

-- --------------------------------------------------------

--
-- Table structure for table `orders_orderitemvipsize`
--

CREATE TABLE `orders_orderitemvipsize` (
  `id` bigint(20) NOT NULL,
  `size` varchar(20) NOT NULL,
  `quantity` varchar(50) NOT NULL,
  `order_item_id` bigint(20) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `orders_orderitemvipsize`
--

INSERT INTO `orders_orderitemvipsize` (`id`, `size`, `quantity`, `order_item_id`) VALUES
(1, '۳۴', '10', 2),
(2, '۳۶', '15', 2),
(3, 'XXL', '114', 6);

-- --------------------------------------------------------

--
-- Table structure for table `orders_ordermessage`
--

CREATE TABLE `orders_ordermessage` (
  `id` bigint(20) NOT NULL,
  `body` longtext NOT NULL,
  `is_internal` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `order_id` bigint(20) NOT NULL,
  `sender_id` bigint(20) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `orders_ordermessage`
--

INSERT INTO `orders_ordermessage` (`id`, `body`, `is_internal`, `created_at`, `order_id`, `sender_id`) VALUES
(4, 'a', 0, '2026-05-05 13:58:10.381924', 4, 1),
(3, 'سلام', 0, '2026-05-05 12:07:24.416634', 4, 1),
(5, 'a', 0, '2026-05-05 14:07:19.504881', 4, 1),
(6, 's', 0, '2026-05-05 14:15:57.021481', 4, 1),
(7, 'سلام', 0, '2026-05-08 10:34:46.750256', 4, 3),
(8, 'سلام', 0, '2026-05-08 10:34:46.754832', 4, 3);

-- --------------------------------------------------------

--
-- Table structure for table `orders_payment`
--

CREATE TABLE `orders_payment` (
  `id` bigint(20) NOT NULL,
  `amount_currency` varchar(3) NOT NULL,
  `amount_amount` decimal(12,0) NOT NULL,
  `date` date DEFAULT NULL,
  `description` longtext NOT NULL,
  `order_id` bigint(20) NOT NULL,
  `gateway` varchar(50) DEFAULT NULL,
  `paid_at` datetime(6) DEFAULT NULL,
  `stage` varchar(20) NOT NULL,
  `status` varchar(20) NOT NULL,
  `transaction_id` varchar(255) DEFAULT NULL,
  `invoice_id` bigint(20) DEFAULT NULL,
  `stage_order` int(11) NOT NULL,
  `authority` varchar(64) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `accounts_user`
--
ALTER TABLE `accounts_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `accounts_user_groups`
--
ALTER TABLE `accounts_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `accounts_user_groups_user_id_group_id_59c0b32f_uniq` (`user_id`,`group_id`),
  ADD KEY `accounts_user_groups_user_id_52b62117` (`user_id`),
  ADD KEY `accounts_user_groups_group_id_bd11a704` (`group_id`);

--
-- Indexes for table `accounts_user_user_permissions`
--
ALTER TABLE `accounts_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `accounts_user_user_permi_user_id_permission_id_2ab516c2_uniq` (`user_id`,`permission_id`),
  ADD KEY `accounts_user_user_permissions_user_id_e4f0a161` (`user_id`),
  ADD KEY `accounts_user_user_permissions_permission_id_113bb443` (`permission_id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  ADD KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  ADD KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`);

--
-- Indexes for table `blog_post`
--
ALTER TABLE `blog_post`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `slug` (`slug`);

--
-- Indexes for table `core_contactmessage`
--
ALTER TABLE `core_contactmessage`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `core_sitepage`
--
ALTER TABLE `core_sitepage`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `key` (`key`);

--
-- Indexes for table `core_tutorial`
--
ALTER TABLE `core_tutorial`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `slug` (`slug`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `orders_invoice`
--
ALTER TABLE `orders_invoice`
  ADD PRIMARY KEY (`id`),
  ADD KEY `orders_invoice_order_id_bc372e79` (`order_id`);

--
-- Indexes for table `orders_invoiceitem`
--
ALTER TABLE `orders_invoiceitem`
  ADD PRIMARY KEY (`id`),
  ADD KEY `orders_invoiceitem_invoice_id_4d34717d` (`invoice_id`);

--
-- Indexes for table `orders_order`
--
ALTER TABLE `orders_order`
  ADD PRIMARY KEY (`id`),
  ADD KEY `orders_order_assigned_to_id_e4866e32` (`assigned_to_id`),
  ADD KEY `orders_order_customer_id_0b76f6a4` (`customer_id`);

--
-- Indexes for table `orders_orderfile`
--
ALTER TABLE `orders_orderfile`
  ADD PRIMARY KEY (`id`),
  ADD KEY `orders_orderfile_order_id_591c0f30` (`order_id`),
  ADD KEY `orders_orderfile_order_item_id_1534351e` (`order_item_id`);

--
-- Indexes for table `orders_orderitem`
--
ALTER TABLE `orders_orderitem`
  ADD PRIMARY KEY (`id`),
  ADD KEY `orders_orderitem_order_id_fe61a34d` (`order_id`);

--
-- Indexes for table `orders_orderitemvipsize`
--
ALTER TABLE `orders_orderitemvipsize`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `orders_orderitemvipsize_order_item_id_size_58efed29_uniq` (`order_item_id`,`size`),
  ADD KEY `orders_orderitemvipsize_order_item_id_7ec44635` (`order_item_id`);

--
-- Indexes for table `orders_ordermessage`
--
ALTER TABLE `orders_ordermessage`
  ADD PRIMARY KEY (`id`),
  ADD KEY `orders_ordermessage_order_id_f48b0135` (`order_id`),
  ADD KEY `orders_ordermessage_sender_id_b8cfb343` (`sender_id`);

--
-- Indexes for table `orders_payment`
--
ALTER TABLE `orders_payment`
  ADD PRIMARY KEY (`id`),
  ADD KEY `orders_payment_order_id_bdccf250` (`order_id`),
  ADD KEY `orders_payment_invoice_id_157ae570` (`invoice_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `accounts_user`
--
ALTER TABLE `accounts_user`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `accounts_user_groups`
--
ALTER TABLE `accounts_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `accounts_user_user_permissions`
--
ALTER TABLE `accounts_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=73;

--
-- AUTO_INCREMENT for table `blog_post`
--
ALTER TABLE `blog_post`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `core_contactmessage`
--
ALTER TABLE `core_contactmessage`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `core_sitepage`
--
ALTER TABLE `core_sitepage`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `core_tutorial`
--
ALTER TABLE `core_tutorial`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=39;

--
-- AUTO_INCREMENT for table `orders_invoice`
--
ALTER TABLE `orders_invoice`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `orders_invoiceitem`
--
ALTER TABLE `orders_invoiceitem`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `orders_order`
--
ALTER TABLE `orders_order`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `orders_orderfile`
--
ALTER TABLE `orders_orderfile`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `orders_orderitem`
--
ALTER TABLE `orders_orderitem`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT for table `orders_orderitemvipsize`
--
ALTER TABLE `orders_orderitemvipsize`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `orders_ordermessage`
--
ALTER TABLE `orders_ordermessage`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `orders_payment`
--
ALTER TABLE `orders_payment`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
