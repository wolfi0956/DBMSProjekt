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
    insert into `personen` (`personr`,`name`,`vorname`,'anschrift','kontaktinfo','geburtsdatum') values (2,'Rowling','Joanne Kos');
    insert into `personen` (`personr`,`name`,`vorname`,'anschrift','kontaktinfo','geburtsdatum') values (3,'Haddon','Mark');
    insert into `personen` (`personr`,`name`,`vorname`,'anschrift','kontaktinfo','geburtsdatum') values (4,'Roberts','John Maddox');
    insert into `personen` (`personr`,`name`,`vorname`,'anschrift','kontaktinfo','geburtsdatum') values (5,'von Münchhausen','Marco');
    insert into `personen` (`personr`,`name`,`vorname`,'anschrift','kontaktinfo','geburtsdatum') values (6,'Montrucchio','Alessandra');
    insert into `personen` (`personr`,`name`,`vorname`,'anschrift','kontaktinfo','geburtsdatum') values (7,'Boyle','Tom Coreghar');
    insert into `personen` (`personr`,`name`,`vorname`,'anschrift','kontaktinfo','geburtsdatum') values (8,'Vargas','Fred');
    insert into `personen` (`personr`,`name`,`vorname`,'anschrift','kontaktinfo','geburtsdatum') values (18,'Moore','Michael');
    insert into `personen` (`personr`,`name`,`vorname`,'anschrift','kontaktinfo','geburtsdatum') values (19,'Knopf','Jim');
    insert into `personen` (`personr`,`name`,`vorname`,'anschrift','kontaktinfo','geburtsdatum') values (22,'Kästner','Erich');
    insert into `personen` (`personr`,`name`,`vorname`,'anschrift','kontaktinfo','geburtsdatum') values (23,'Feist','Raymond');
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
