-- create a table for artists, albums, and songs
CREATE TABLE artist (
    id INTEGER PRIMARY KEY,
    name TEXT
);
CREATE TABLE album (
    id INTEGER PRIMARY KEY,
    title TEXT,
    artist TEXT
);
CREATE TABLE songs (
    id INTEGER PRIMARY KEY,
    track_id INTEGER,
    title TEXT,
    album TEXT,
    run_time TEXT
);

-- populate artist table with artists
INSERT INTO artist (name) VALUES ("Miles Davis");
INSERT INTO artist (name) VALUES ("Fleetwood Mac");
INSERT INTO artist (name) VALUES ("Stevie Wonder");

-- populate album table with albums, 1 per artist
INSERT INTO album (title, artist) VALUES ("Kind of Blue", "Miles Davis");
INSERT INTO album (title, artist) VALUES ("Rumours", "Fleetwood Mac");
INSERT INTO album (title, artist) VALUES ("Talking Book", "Stevie Wonder");

-- populate song table with songs from each album
-- Kind of Blue
INSERT INTO songs (track_id, title, album, run_time) VALUES (1, "So What", "Kind of Blue", "9:22");
INSERT INTO songs (track_id, title, album, run_time) VALUES (2, "Freddie Freeloader", "Kind of Blue", "9:46");
INSERT INTO songs (track_id, title, album, run_time) VALUES (3, "Blue in Green", "Kind of Blue", "5:27");
INSERT INTO songs (track_id, title, album, run_time) VALUES (4, "All Blues", "Kind of Blue", "11:33");
INSERT INTO songs (track_id, title, album, run_time) VALUES (5, "Flamenco Sketches", "Kind of Blue", "9:26");

-- Rumours
INSERT INTO songs (track_id, title, album, run_time) VALUES (1, "Second Hand News", "Rumours", "2:43");
INSERT INTO songs (track_id, title, album, run_time) VALUES (2, "Dreams", "Rumours", "4:14");
INSERT INTO songs (track_id, title, album, run_time) VALUES (3, "Never Going Back", "Rumours", "2:02");
INSERT INTO songs (track_id, title, album, run_time) VALUES (4, "Don't Stop", "Rumours", "3:11");
INSERT INTO songs (track_id, title, album, run_time) VALUES (5, "Go Your Own Way", "Rumours", "3:38");
INSERT INTO songs (track_id, title, album, run_time) VALUES (6, "Song Bird", "Rumours", "3:20");
INSERT INTO songs (track_id, title, album, run_time) VALUES (7, "The Chain", "Rumours", "4:28");
INSERT INTO songs (track_id, title, album, run_time) VALUES (8, "You Make Loving Fun", "Rumours", "3:31");
INSERT INTO songs (track_id, title, album, run_time) VALUES (9, "I Don't Want to Know", "Rumours", "3:11");
INSERT INTO songs (track_id, title, album, run_time) VALUES (10, "Oh Daddy", "Rumours", "3:54");
INSERT INTO songs (track_id, title, album, run_time) VALUES (11, "Gold Dust Woman", "Rumours", "4:51");

-- Talking Book
INSERT INTO songs (track_id, title, album, run_time) VALUES (1, "You Are the Sunshine of My Life", "Talking Book", "2:58");
INSERT INTO songs (track_id, title, album, run_time) VALUES (2, "Maybe My Baby", "Talking Book", "6:45");
INSERT INTO songs (track_id, title, album, run_time) VALUES (3, "You and I (We Can Conquer the World)", "Talking Book", "4:39");
INSERT INTO songs (track_id, title, album, run_time) VALUES (4, "Tuesday Heartbreak", "Talking Book", "3:09");
INSERT INTO songs (track_id, title, album, run_time) VALUES (5, "You've Got It Bad Girl", "Talking Book", "4:55");
INSERT INTO songs (track_id, title, album, run_time) VALUES (6, "Superstition", "Talking Book", "4:26");
INSERT INTO songs (track_id, title, album, run_time) VALUES (7, "Big Brother", "Talking Book", "3:35");
INSERT INTO songs (track_id, title, album, run_time) VALUES (8, "Blame It on the Sun", "Talking Book", "3:28");
INSERT INTO songs (track_id, title, album, run_time) VALUES (9, "Lookin' for Another Pure Love", "Talking Book", "4:45");
INSERT INTO songs (track_id, title, album, run_time) VALUES (10, "I Believe (When I Fall in Love It Will Be Forever)", "Talking Book", "4:48");

-- display table with track listing for each album including album and artist names
SELECT artist, album, songs.track_id, songs.title, songs.run_time
FROM songs
INNER JOIN album ON songs.album = album.title;
