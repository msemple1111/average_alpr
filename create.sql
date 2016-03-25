

CREATE TABLE plates (
  p_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  plate VARCHAR(15) NOT NULL,
  p_foreign BOOLEAN NOT NULL DEFAULT FALSE
);

CREATE TABLE data (
   d_index INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
   p_id INTEGER NOT NULL,
   uuid Char(36) NOT NULL,
   s_id INT NOT NULL,
   time BIGINT NOT NULL,
   cam_id INT NOT NULL,
   speed float(4,2)
 );

CREATE TABLE cams (
cam_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
site_cam_id INTEGER NOT NULL,
cam_m float(6,2) NOT NULL,
s_id INTEGER NOT NULL
);


CREATE TABLE sites (
  s_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  site_id VARCHAR(255) NOT NULL,
  s_limit float(5,2) NOT NULL
 );

INSERT INTO sites
	(site_id, s_limit)
    Values
    ("cdon way", 15);

INSERT INTO cams
	(cam_m, site_cam_id, s_id)
  VALUES
  (0,1,1),
  (250,2,1),
  (500,3,1),
  (750,4,1);

INSERT INTO plates
	(plate) Values ("FT56 GHY");
INSERT INTO plates
	(plate) Values ("SU84 XFR");
INSERT INTO plates
	(plate) Values ("IC89 DUX");
INSERT INTO plates
	(plate) Values ("FB37 OMD");

INSERT INTO data
	(p_id, uuid, s_id, time, cam_id, speed)
VALUES
	(1, 'badda476-bcd2-44bd-8398-31d9f5c1b73d', 1, 1449783321, 1, NULL),
	(2, '2ffd7afb-4cc2-4eba-8454-4ec526da9b6f', 1, 1449756345, 3, 1),
	(3, '27b18d82-b240-44af-a795-ba052218bf87', 1, 1449785645, 1, -4),
    (4, '9329a1fc-510b-4944-afeb-b0e52a6638bb', 1, 1449773351, 1, -64),

    (1, 'd06fbb96-af53-464e-9242-feb72ad35e09', 1, 1449783378, 2, NULL),
	(2, '45fb79e3-4635-4b05-baac-d926cfa605bd', 1, 1449756367, 4, 3),
	(3, 'b1988021-10d6-43bd-8669-0db6587e1cdc', 1, 1449785653, 2, 3),
    (4, 'a436c181-db8d-44aa-b6d9-4326a45a78eb', 1, 1449773382, 2, 9);
