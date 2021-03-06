

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

 CREATE TABLE owners (
   owner_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
   owner_name VARCHAR(255) NOT NULL,
   owner_adr VARCHAR(999),
   p_id INTEGER NOT NULL
  );

INSERT INTO sites
	(site_id, s_limit)
    Values
    ("cdon way", 15),
    ("nailsea way", 15);

INSERT INTO cams
	(cam_m, site_cam_id, s_id)
  VALUES
  (0,1,1),
  (250,2,1),
  (500,3,1),
  (750,4,1),
  (0,1,2),
  (250,2,2),
  (500,3,2),
  (750,4,2);

INSERT INTO plates
	(plate)
  Values
("FT56 GHY"),
("SU84 XFR"),
("IC89 DUX"),
("FB37 OMD");

  INSERT INTO plates
  (plate, p_foreign) Values ("ER69 GIN", 'TRUE');

INSERT INTO data
	(p_id, uuid, s_id, time, cam_id, speed)
VALUES
	(1, 'badda476-bcd2-44bd-8398-31d9f5c1b73d', 1, 1449783321, 1, NULL),
	(1, '2ffd7afb-4cc2-4eba-8454-4ec526da9b6f', 1, 1449756345, 2, 1),
	(1, '27b18d82-b240-44af-a795-ba052218bf87', 1, 1449785645, 3, -4),
    (1, '9329a1fc-510b-4944-afeb-b0e52a6638bb', 1, 1449773351, 4, -64),

    (2, 'd06fbb96-af53-464e-9242-feb72ad35e09', 1, 1449783378, 1, NULL),
	(2, '45fb79e3-4635-4b05-baac-d926cfa605bd', 1, 1449756367, 2, -3),
	(2, 'b1988021-10d6-43bd-8669-0db6587e1cdc', 1, 1449785653, 3, 3),
    (2, 'a436c181-db8d-44aa-b6d9-4326a45a78eb', 1, 1449773382, 4, -9),

  (5, '13a10378-5f54-4361-973f-1c1ed43d526c', 1, 1448557729, 1, NULL),
	(5, 'e4df2d42-bfc6-4175-9078-7e2d6e0eac71', 1, 1448557732, 2, 68.3333333),
	(5, 'ca7f6046-5182-4313-b734-bb5beabefda2', 1, 1448557734, 3, 110.0),
  (5, 'b71efb0c-d78b-43a9-b418-8c0d241bf1ed', 1, 1448557741, 4, 20.7142857);

  INSERT INTO owners
  	(owner_name, owner_adr, p_id)
    VALUES

    ("Allan Carr","1 Woodburn Way, Alva, Clackmannanshire FK12 5LB, UK",1),
    ("Santiago Bass","27-29 St Mary's Pl, Townend, Kirkcudbright, Dumfries and Galloway DG6 4BA, UK",2),
    ("Cathy Little","9 Kenilworth Dr, Willsbridge, Bristol, South Gloucestershire BS30 6UP, UK",3),
    ("Zachary Holmes","5 Granville Rd, Ilfracombe, Devon EX34 8AS, UK",4),
    ("Darla Johnson","2 Shirley Rd, Ripley, Derbyshire DE5 3HB, UK",5);
