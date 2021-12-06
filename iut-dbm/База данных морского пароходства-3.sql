CREATE TABLE `cargo_types` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255) UNIQUE NOT NULL
);

CREATE TABLE `ports` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255) UNIQUE NOT NULL
);

CREATE TABLE `crews` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255) UNIQUE NOT NULL
);

CREATE TABLE `positions` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255) UNIQUE NOT NULL
);

CREATE TABLE `ships` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255) UNIQUE NOT NULL,
  `capacity` float NOT NULL,
  `cargo_type_id` int NOT NULL,
  `port_id` int,
  `crew_id` int
);

CREATE TABLE `employees` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `lastname` varchar(255) NOT NULL,
  `firstname` varchar(255) NOT NULL,
  `middlename` varchar(255),
  `birthday` timestamp NOT NULL,
  `hiring_date` date NOT NULL,
  `dismissal_date` date,
  `salary` float,
  `position_id` int,
  `crew_id` int
);

CREATE TABLE `ship_movement_log` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `ship_id` int NOT NULL,
  `datetime` timestamp NOT NULL DEFAULT (now()),
  `latitude` float NOT NULL,
  `longitude` float NOT NULL
);

CREATE TABLE `major_repairs` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `ship_id` int NOT NULL,
  `datetime` timestamp NOT NULL DEFAULT (now())
);

CREATE TABLE `cargos` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `cargo_type_id` int NOT NULL
);

CREATE TABLE `cities` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255) NOT NULL
);

CREATE TABLE `banks` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `name` int NOT NULL,
  `city_id` int NOT NULL,
  `inn` char(12) NOT NULL,
  `payment_account` char(20) NOT NULL
);

CREATE TABLE `charterers` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `address` varchar(255),
  `phone` int,
  `fax` int,
  `email` varchar(255),
  `bank_id` int NOT NULL
);

CREATE TABLE `route` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `ship_id` int NOT NULL,
  `cargo_id` int,
  `charterer_id` int NOT NULL,
  `planned_start_date` date NOT NULL,
  `planned_end_date` date NOT NULL,
  `actual_start_date` date,
  `actual_end_date` date
);

CREATE TABLE `route_points` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `route_id` int NOT NULL,
  `port_id` int NOT NULL
);

ALTER TABLE `ships` ADD FOREIGN KEY (`cargo_type_id`) REFERENCES `cargo_types` (`id`);

ALTER TABLE `ships` ADD FOREIGN KEY (`port_id`) REFERENCES `ports` (`id`);

ALTER TABLE `ships` ADD FOREIGN KEY (`crew_id`) REFERENCES `crews` (`id`);

ALTER TABLE `employees` ADD FOREIGN KEY (`position_id`) REFERENCES `positions` (`id`);

ALTER TABLE `employees` ADD FOREIGN KEY (`crew_id`) REFERENCES `crews` (`id`);

ALTER TABLE `ship_movement_log` ADD FOREIGN KEY (`ship_id`) REFERENCES `ships` (`id`);

ALTER TABLE `major_repairs` ADD FOREIGN KEY (`ship_id`) REFERENCES `ships` (`id`);

ALTER TABLE `cargos` ADD FOREIGN KEY (`cargo_type_id`) REFERENCES `cargo_types` (`id`);

ALTER TABLE `banks` ADD FOREIGN KEY (`city_id`) REFERENCES `cities` (`id`);

ALTER TABLE `charterers` ADD FOREIGN KEY (`bank_id`) REFERENCES `banks` (`id`);

ALTER TABLE `route` ADD FOREIGN KEY (`ship_id`) REFERENCES `ships` (`id`);

ALTER TABLE `route` ADD FOREIGN KEY (`cargo_id`) REFERENCES `cargos` (`id`);

ALTER TABLE `route` ADD FOREIGN KEY (`charterer_id`) REFERENCES `charterers` (`id`);

ALTER TABLE `route_points` ADD FOREIGN KEY (`route_id`) REFERENCES `route` (`id`);

ALTER TABLE `route_points` ADD FOREIGN KEY (`port_id`) REFERENCES `ports` (`id`);
