DROP TABLE IF EXISTS `testtable`;
CREATE TABLE `testtable` (
    `id` INT(4) UNSIGNED NOT NULL,
    `text` VARCHAR(8192) NOT NULL,
    `created_at` TIMESTAMP NOT NULL,
    `status` ENUM('a', 'b', 'c', 'd') NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
