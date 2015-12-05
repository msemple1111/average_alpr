CREATE TABLE plates (
  p_index INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  plate VARCHAR(15) NOT NULL,
  p_foreign BOOLEAN NOT NULL DEFAULT FALSE
);

CREATE TABLE data (
   d_index INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
   p_index INTEGER NOT NULL,
   r_id INTEGER,
   time_1 BIGINT NOT NULL,
   time_2 BIGINT,
   speed float(5,2)
 );

CREATE TABLE roads (
  r_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  r_name VARCHAR(255) NOT NULL,
  s_limit float(5,2) NOT NULL,
  r_dist float(8,2) NOT NULL
 );

INSERT INTO roads (r_name, s_limit, r_dist) VALUES ("A Road",15,100);