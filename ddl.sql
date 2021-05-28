CREATE DATABASE messageApp;

CREATE TABLE user (
    user_id int(20) NOT NULL AUTO_INCREMENT,
    username varchar(45) NOT NULL,
    password varchar(45) NOT NULL,
    PRIMARY KEY (user_id)
);

CREATE TABLE message (
    message_id int(20) NOT NULL AUTO_INCREMENT,
    user_id int(20) NOT NULL,
    creation_date datetime NOT NULL,
    message text,
    PRIMARY KEY (message_id),
    FOREIGN KEY (user_id) REFERENCES user(user_id)
);
