import sqlite3
verbindung = sqlite3.connect("kanzlei.db")
zeiger = verbindung.cursor()

zeiger.executescript("""
    DROP TABLE IF EXISTS `fall`;
    CREATE TABLE `fall` (
      `fallnr` INTEGER PRIMARY KEY AUTOINCREMENT,
      `datum` date NOT NULL,
      `zeit` time NOT NULL, 
      `gericht` char(50),
      `sachverhalt` char(300),
      `rechtsgebiet` char(50),
      `tatort` char(100)
    ); 

    insert into `fall` (`fallnr`,`datum`,`zeit`,`gericht`,`sachverhalt`,`rechtsgebiet`,`tatort`) values (1,'2023-02-24','11:11:11',`Klaus-Kleber Gericht`,`Klient hat öffentlich uriniert`,`StgB`,`Weißes Haus`);
    insert into `fall` (`fallnr`,`datum`,`zeit`,`gericht`,`sachverhalt`,`rechtsgebiet`,`tatort`) values (2,'2001-09-11','11:11:11',`Essens-Gericht`,`Entwendung eines Käsebrötchens`,`StgB`,`Zwei Türme`);
    insert into `fall` (`fallnr`,`datum`,`zeit`,`gericht`,`sachverhalt`,`rechtsgebiet`,`tatort`) values (3,'2006-06-06','11:11:11',`Bundesverfassungsgericht`,`änderung des Grundgesetzes`,`BGB`,`Gibt keinen-Verfassungsklage`);
    insert into `fall` (`fallnr`,`datum`,`zeit`,`gericht`,`sachverhalt`,`rechtsgebiet`,`tatort`) values (4,'2024-12-24','11:11:11',`
    DROP TABLE IF EXISTS `personen`;

    CREATE TABLE `personen` (
      `personr` INTEGER PRIMARY KEY AUTOINCREMENT,
      `name` char(20),
      `vorname` char(20),
      'anschrift' char(40), int(6),
      'kontaktinfo' int(20),
      'geburtsdatum' date default NULL
    );

    insert into `personen` (`personr`,`name`,`vorname`,'anschrift','kontaktinfo','geburtsdatum') values (1,'Baecker','Philip','Knesebeckstrasse 83','49 02684 98 72 81','1999-03-30');
    insert into `personen` (`personr`,`name`,`vorname`,'anschrift','kontaktinfo','geburtsdatum') values (2,'Wagner','Marko','Fontenay 26','49 09241 35 12 26','1969-04-25');
    insert into `personen` (`personr`,`name`,`vorname`,'anschrift','kontaktinfo','geburtsdatum') values (3,'Dudruff','Iwan G.','Charlottenstrasse 58','49 0351 12 68 86','2001-10-17');
    insert into `personen` (`personr`,`name`,`vorname`,'anschrift','kontaktinfo','geburtsdatum') values (4,'Machslochoff','Ivanka','Schoenebergerstrasse 81','49 03761 36 90 57','1937-09-17');
    insert into `personen` (`personr`,`name`,`vorname`,'anschrift','kontaktinfo','geburtsdatum') values (5,'Lehrer','Philipp','Mollstrasse 26','49 06145 14 17 41','2004-01-04');
    insert into `personen` (`personr`,`name`,`vorname`,'anschrift','kontaktinfo','geburtsdatum') values (6,'Schwab','Stephanie','Heinrich Heine Platz 13','49 03583 81 60 22','1978-07-07');
    insert into `personen` (`personr`,`name`,`vorname`,'anschrift','kontaktinfo','geburtsdatum') values (7,'Goldschmitt','Lisa','Boxhagener Str. 84','49 040 12 51 46','1973-02-02');
    insert into `personen` (`personr`,`name`,`vorname`,'anschrift','kontaktinfo','geburtsdatum') values (8,'Fenstermacher','Mandy','Holstenwall 14','49 034633 81 57','1999-05-17');
    insert into `personen` (`personr`,`name`,`vorname`,'anschrift','kontaktinfo','geburtsdatum') values (18,'Schwartz','Marko','Karl-Liebknecht-Strasse 24','49 04271 33 13 84','1967-11-08');
    insert into `personen` (`personr`,`name`,`vorname`,'anschrift','kontaktinfo','geburtsdatum') values (19,'Gottlieb','Anja','Reeperbahn 34','49 037606 60 98','1978-05-19');
    insert into `personen` (`personr`,`name`,`vorname`,'anschrift','kontaktinfo','geburtsdatum') values (22,'Kunze','Nadine','Friedrichstrasse 26','49 0211 61 63 49','1959-10-16');
    insert into `personen` (`personr`,`name`,`vorname`,'anschrift','kontaktinfo','geburtsdatum') values (23,'Eiffel','Sabrina','Lietzenburger Strasse 8','49 0226146 29 39','1994-06-21');
    insert into `personen` (`personr`,`name`,`vorname`,'anschrift','kontaktinfo','geburtsdatum') values (24,'Mauer','Andrea','Invalidenstraße 19','49 06337 85 81 49','1940-02-27');
    insert into `personen` (`personr`,`name`,`vorname`,'anschrift','kontaktinfo','geburtsdatum') values (25,'Nacht','Anna','Luckenwalder Straße 37','49 04975 53 77 73','1937-07-17');
    insert into `personen` (`personr`,`name`,`vorname`,'anschrift','kontaktinfo','geburtsdatum') values (27,'Traugott','Jonas','Bleibtreustrasse 12','49 05254 83 91 49');
    insert into `personen` (`personr`,`name`,`vorname`,'anschrift','kontaktinfo','geburtsdatum') values (28,'Ackermann','Kerstin','Rheinstraße 73','49 089 13 20 06','1984-03-31');
    insert into `personen` (`personr`,`name`,`vorname`,'anschrift','kontaktinfo','geburtsdatum') values (29,'Frankfurter','Paul','Ansbacher Straße 5','49 06543 21 62 89','1993-02-21');
    insert into `personen` (`personr`,`name`,`vorname`,'anschrift','kontaktinfo','geburtsdatum') values (30,'Egger','Matthias','Kurfürstendamm 73','49 0383 92 72 50','1992-10-18');
    insert into `personen` (`personr`,`name`,`vorname`,'anschrift','kontaktinfo','geburtsdatum') values (31,'Kuhn','Philipp','Billwerder Neuer Deich 10','49 09941 87 16 67','2001-10-03');
    insert into `personen` (`personr`,`name`,`vorname`,'anschrift','kontaktinfo','geburtsdatum') values (32,'Schmid','Thorsten','Bleibtreustraße 92','49 07832 16 43 27','1968-06-06');
    insert into `personen` (`personr`,`name`,`vorname`,'anschrift','kontaktinfo','geburtsdatum') values (33,'Schweizer','Anna','Eschenweg 38','49 03641 38 08 25','1957-08-08');
    insert into `personen` (`personr`,`name`,`vorname`,'anschrift','kontaktinfo','geburtsdatum') values (34,'Fisher','Kerstin','Anhalter Straße 87','49b 06362 95 85 11','1946-04-12');
    


    DROP TABLE IF EXISTS `dokumente`;

    CREATE TABLE `dokumente` (
      `dokumentnr` INTEGER PRIMARY KEY AUTOINCREMENT,
      `fall` char(2000) NOT NULL,
      `personnr` int(6) NOT NULL,
      `kategorie` char(60)
    );

    insert into `dokumente` (`dokumentnr`,`fall`,`personr`,`kategorie`) values (1,"a","xy","xy");
    insert into `dokumente` (`dokumentnr`,`fall`,`personr`,`kategorie`) values (2,"b","xy","xy");
    insert into `dokumente` (`dokumentnr`,`fall`,`personr`,`kategorie`) values (3,"c","xy","xy");
    insert into `dokumente` (`dokumentnr`,`fall`,`personr`,`kategorie`) values (4,"d","xy","xy");
  
verbindung.commit()
verbindung.close()
