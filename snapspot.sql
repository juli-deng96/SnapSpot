-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema snapspot
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema snapspot
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `snapspot` DEFAULT CHARACTER SET utf8 ;
USE `snapspot` ;

-- -----------------------------------------------------
-- Table `snapspot`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `snapspot`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  `email` VARCHAR(250) NOT NULL,
  `password` VARCHAR(45) NOT NULL,
  `created_at` DATETIME NOT NULL DEFAULT NOW(),
  `updated_at` DATETIME NOT NULL DEFAULT NOW() ON UPDATE NOW(),
  PRIMARY KEY (`id`),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `snapspot`.`photo_spot`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `snapspot`.`photo_spot` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(45) NOT NULL,
  `location` VARCHAR(45) NOT NULL,
  `description` TEXT NOT NULL,
  `direct_sunlight` TINYINT NOT NULL,
  `bathroom_avail` TINYINT NOT NULL,
  `created_at` DATETIME NOT NULL DEFAULT NOW(),
  `updated_at` DATETIME NOT NULL DEFAULT NOW() ON UPDATE NOW(),
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`, `user_id`),
  INDEX `fk_photo_spot_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_photo_spot_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `snapspot`.`users` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
