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

    insert into `fall` (`fallnr`,`datum`,`zeit`,`gericht`,`sachverhalt`,`rechtsgebiet`,`tatort`) values (1,'2023-02-24','11:11:11',`Klaus-Kleber Gericht`,`Klient hat öffentlich uriniert`,`Rechtsgebiet`,`Weißes Haus`);
    insert into `fall` (`fallnr`,`datum`,`zeit`,`gericht`,`sachverhalt`,`rechtsgebiet`,`tatort`) values (2,'2001-09-11','11:11:11',`Essens-Gericht`,`Entwendung eines Käsebrötchens`,`Diebstahl`,`Zwei Türme`);

    DROP TABLE IF EXISTS `personen`;

    CREATE TABLE `personen` (
      `personr` INTEGER PRIMARY KEY AUTOINCREMENT,
      `name` char(20),
      `vorname` char(20),
      'anschrift' char(40), int(6),
      'kontaktinfo' int(20),
      'geburtsdatum' date default NULL
    );

    insert into `personen` (`personr`,`name`,`vorname`,'anschrift','kontaktinfo','geburtsdatum') values (1,'Baecker','Philip,'Knesebeckstrasse 83','49 02684 98 72 81','1999-03-30');
    insert into `personen` (`personr`,`name`,`vorname`,'anschrift','kontaktinfo','geburtsdatum') values (2,'Wagner','Marko','Fontenay 26','49 09241 35 12 26','1969-04-25');
    insert into `personen` (`personr`,`name`,`vorname`,'anschrift','kontaktinfo','geburtsdatum') values (3,'Loewe','Sophia','Charlottenstrasse 58','49 0351 12 68 86','2001-10-17');
    insert into `personen` (`personr`,`name`,`vorname`,'anschrift','kontaktinfo','geburtsdatum') values (4,'Gaertner','Angelika','Schoenebergerstrasse 81','49 03761 36 90 57','1937-09-17');
    insert into `personen` (`personr`,`name`,`vorname`,'anschrift','kontaktinfo','geburtsdatum') values (5,'Lehrer','Philipp','Mollstrasse 26','49 06145 14 17 41','2004-01-04');
    insert into `personen` (`personr`,`name`,`vorname`,'anschrift','kontaktinfo','geburtsdatum') values (6,'Schwab','Stephanie','Heinrich Heine Platz 13','49 03583 81 60 22','1978-07-07');
    insert into `personen` (`personr`,`name`,`vorname`,'anschrift','kontaktinfo','geburtsdatum') values (7,'Goldschmitt','Lisa','Boxhagener Str. 84','49 040 12 51 46','1973-02-02');
    insert into `personen` (`personr`,`name`,`vorname`,'anschrift','kontaktinfo','geburtsdatum') values (8,'Fenstermacher','Mandy','Holstenwall 14','49 034633 81 57','1999-05-17');
    insert into `personen` (`personr`,`name`,`vorname`,'anschrift','kontaktinfo','geburtsdatum') values (18,'Schwartz','Marko','Karl-Liebknecht-Strasse 24','49 04271 33 13 84','1967-11-08');
    insert into `personen` (`personr`,`name`,`vorname`,'anschrift','kontaktinfo','geburtsdatum') values (19,'Gottlieb','Anja','Reeperbahn 34','49 037606 60 98','1978-05-19');
    insert into `personen` (`personr`,`name`,`vorname`,'anschrift','kontaktinfo','geburtsdatum') values (22,'Kunze','Nadine','Friedrichstrasse 26','49 0211 61 63 49','1959-10-16');
    insert into `personen` (`personr`,`name`,`vorname`,'anschrift','kontaktinfo','geburtsdatum') values (23,'Eiffel','Sabrina','Lietzenburger Strasse 8','49 0226146 29 39','1994-06-21');
    insert into `personen` (`personr`,`name`,`vorname`,'anschrift','kontaktinfo','geburtsdatum') values (24,'Kafka','Franz');
    insert into `personen` (`personr`,`name`,`vorname`,'anschrift','kontaktinfo','geburtsdatum') values (25,'Flemming','Ian');
    insert into `personen` (`personr`,`name`,`vorname`,'anschrift','kontaktinfo','geburtsdatum') values (27,'Harris','Thomas');
    insert into `personen` (`personr`,`name`,`vorname`,'anschrift','kontaktinfo','geburtsdatum') values (28,'Pratchett','Terry');
    insert into `personen` (`personr`,`name`,`vorname`,'anschrift','kontaktinfo','geburtsdatum') values (29,'Tucholsky','Kurt');
    insert into `personen` (`personr`,`name`,`vorname`,'anschrift','kontaktinfo','geburtsdatum') values (30,'Jordan','Robert');
    insert into `personen` (`personr`,`name`,`vorname`,'anschrift','kontaktinfo','geburtsdatum') values (31,'Kuhn','Wilfried');
    insert into `personen` (`personr`,`name`,`vorname`,'anschrift','kontaktinfo','geburtsdatum') values (32,'Christi','Agatha');
    insert into `personen` (`personr`,`name`,`vorname`,'anschrift','kontaktinfo','geburtsdatum') values (33,'Williams','T.');


    DROP TABLE IF EXISTS `dokumente`;

    CREATE TABLE `dokumente` (
      `dokumentnr` INTEGER PRIMARY KEY AUTOINCREMENT,
      `fall` char(60) NOT NULL,
      `personr` int(6) NOT NULL,
      `kategorie` char(2000)
    );

    insert into `dokumente` (`dokumentnr`,`fall`,`personr`,`kategorie`) values (1,'Der Herr der Augenringe',1,'humor');
    insert into `dokumente` (`dokumentnr`,`fall`,`personr`,`kategorie`) values (2,'Harry Potter und der Orden des Phönix',2,'fan');
    insert into `dokumente` (`dokumentnr`,`fall`,`personr`,`kategorie`) values (3,'Supergute Tage oder Die sonderbare Welt des Christopher Boon',3,'humor');
    insert into `dokumente` (`dokumentnr`,`fall`,`personr`,`kategorie`) values (4,'SPQR Ein Krimi aus dem alten Rom',4,'krimi');
    insert into `dokumente` (`dokumentnr`,`fall`,`personr`,`kategorie`) values (5,'So zähmen Sie Ihren inneren Schweinehund',5,'humor');
    insert into `dokumente` (`dokumentnr`,`fall`,`personr`,`kategorie`) values (6,'Harry Potter und der Stein der Weisen',2,'fan');
    insert into `dokumente` (`dokumentnr`,`fall`,`personr`,`kategorie`) values (7,'Harry Potter und der Stein der Weisen',2,'fan');
    insert into `dokumente` (`dokumentnr`,`fall`,`personr`,`kategorie`) values (8,'Harry Potter und der Stein der Weisen',2,'fan');
    insert into `dokumente` (`dokumentnr`,`fall`,`personr`,`kategorie`) values (9,'Fisch sucht Fahrrad',6,'liebe');
    insert into `dokumente` (`dokumentnr`,`fall`,`personr`,`kategorie`) values (10,'Grün ist die Hoffnung',7,'humor');
    insert into `dokumente` (`dokumentnr`,`fall`,`personr`,`kategorie`) values (11,'Der untröstliche Witwer von Montparnasse',8,'krimi');
    insert into `dokumente` (`dokumentnr`,`fall`,`personr`,`kategorie`) values (12,'Das doppelte Lottchen',22,'kind');
    insert into `dokumente` (`dokumentnr`,`fall`,`personr`,`kategorie`) values (19,'Das Schweigen der Lämmer',9,'krimi');
    insert into `dokumente` (`dokumentnr`,`fall`,`personr`,`kategorie`) values (22,'Tiger,Panther&Co',29,'humor');
    insert into `dokumente` (`dokumentnr`,`fall`,`personr`,`kategorie`) values (23,'Das Rad Der Zeit',30,'fan');
    insert into `dokumente` (`dokumentnr`,`fall`,`personr`,`kategorie`) values (24,'Handbuch der experimentellen Physik',31,'humor');
    insert into `dokumente` (`dokumentnr`,`fall`,`personr`,`kategorie`) values (25,'Helle Barden',28,'humor');
    insert into `dokumente` (`dokumentnr`,`fall`,`personr`,`kategorie`) values (27,'Mord im Orient Express',32,'krimi');
    insert into `dokumente` (`dokumentnr`,`fall`,`personr`,`kategorie`) values (28,'Otherland River of blue fire',33,'fan');

  
verbindung.commit()
verbindung.close()
