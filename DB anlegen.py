import sqlite3
verbindung = sqlite3.connect("bibliothek.db")
zeiger = verbindung.cursor()

zeiger.executescript("""
    DROP TABLE IF EXISTS `ausleihen`;
sssss
    CREATE TABLE `ausleihen` (
      `ausleihnr` INTEGER PRIMARY KEY AUTOINCREMENT,
      `buchnr` int(6) NOT NULL,
      `lesernr` int(6) NOT NULL,
      `ausleihedatum` date NOT NULL,
      `rueckgabedatum` date default NULL     
    ); 

    insert into `ausleihen` (`ausleihnr`,`buchnr`,`lesernr`,`ausleihedatum`,`rueckgabedatum`) values (1,1,2,'2023-02-24','2023-03-24');
    insert into `ausleihen` (`ausleihnr`,`buchnr`,`lesernr`,`ausleihedatum`,`rueckgabedatum`) values (2,3,1,'2023-01-12','2023-02-24');
    insert into `ausleihen` (`ausleihnr`,`buchnr`,`lesernr`,`ausleihedatum`,`rueckgabedatum`) values (3,2,5,'2023-02-01','2023-03-01');

    DROP TABLE IF EXISTS `autoren`;

    CREATE TABLE `autoren` (
      `autorennr` INTEGER PRIMARY KEY AUTOINCREMENT,
      `name` char(20),
      `vorname` char(20)
    );

    insert into `autoren` (`autorennr`,`name`,`vorname`) values (1,'Tollkühn','Dschey Ar');
    insert into `autoren` (`autorennr`,`name`,`vorname`) values (2,'Rowling','Joanne Kos');
    insert into `autoren` (`autorennr`,`name`,`vorname`) values (3,'Haddon','Mark');
    insert into `autoren` (`autorennr`,`name`,`vorname`) values (4,'Roberts','John Maddox');
    insert into `autoren` (`autorennr`,`name`,`vorname`) values (5,'von Münchhausen','Marco');
    insert into `autoren` (`autorennr`,`name`,`vorname`) values (6,'Montrucchio','Alessandra');
    insert into `autoren` (`autorennr`,`name`,`vorname`) values (7,'Boyle','Tom Coreghar');
    insert into `autoren` (`autorennr`,`name`,`vorname`) values (8,'Vargas','Fred');
    insert into `autoren` (`autorennr`,`name`,`vorname`) values (18,'Moore','Michael');
    insert into `autoren` (`autorennr`,`name`,`vorname`) values (19,'Knopf','Jim');
    insert into `autoren` (`autorennr`,`name`,`vorname`) values (22,'Kästner','Erich');
    insert into `autoren` (`autorennr`,`name`,`vorname`) values (23,'Feist','Raymond');
    insert into `autoren` (`autorennr`,`name`,`vorname`) values (24,'Kafka','Franz');
    insert into `autoren` (`autorennr`,`name`,`vorname`) values (25,'Flemming','Ian');
    insert into `autoren` (`autorennr`,`name`,`vorname`) values (27,'Harris','Thomas');
    insert into `autoren` (`autorennr`,`name`,`vorname`) values (28,'Pratchett','Terry');
    insert into `autoren` (`autorennr`,`name`,`vorname`) values (29,'Tucholsky','Kurt');
    insert into `autoren` (`autorennr`,`name`,`vorname`) values (30,'Jordan','Robert');
    insert into `autoren` (`autorennr`,`name`,`vorname`) values (31,'Kuhn','Wilfried');
    insert into `autoren` (`autorennr`,`name`,`vorname`) values (32,'Christi','Agatha');
    insert into `autoren` (`autorennr`,`name`,`vorname`) values (33,'Williams','T.');


    DROP TABLE IF EXISTS `buecher`;

    CREATE TABLE `buecher` (
      `buchnr` INTEGER PRIMARY KEY AUTOINCREMENT,
      `titel` char(60) NOT NULL,
      `autorennr` int(6) NOT NULL,
      `kategorie` char(5) default NULL
    );

    insert into `buecher` (`buchnr`,`titel`,`autorennr`,`kategorie`) values (1,'Der Herr der Augenringe',1,'humor');
    insert into `buecher` (`buchnr`,`titel`,`autorennr`,`kategorie`) values (2,'Harry Potter und der Orden des Phönix',2,'fan');
    insert into `buecher` (`buchnr`,`titel`,`autorennr`,`kategorie`) values (3,'Supergute Tage oder Die sonderbare Welt des Christopher Boon',3,'humor');
    insert into `buecher` (`buchnr`,`titel`,`autorennr`,`kategorie`) values (4,'SPQR Ein Krimi aus dem alten Rom',4,'krimi');
    insert into `buecher` (`buchnr`,`titel`,`autorennr`,`kategorie`) values (5,'So zähmen Sie Ihren inneren Schweinehund',5,'humor');
    insert into `buecher` (`buchnr`,`titel`,`autorennr`,`kategorie`) values (6,'Harry Potter und der Stein der Weisen',2,'fan');
    insert into `buecher` (`buchnr`,`titel`,`autorennr`,`kategorie`) values (7,'Harry Potter und der Stein der Weisen',2,'fan');
    insert into `buecher` (`buchnr`,`titel`,`autorennr`,`kategorie`) values (8,'Harry Potter und der Stein der Weisen',2,'fan');
    insert into `buecher` (`buchnr`,`titel`,`autorennr`,`kategorie`) values (9,'Fisch sucht Fahrrad',6,'liebe');
    insert into `buecher` (`buchnr`,`titel`,`autorennr`,`kategorie`) values (10,'Grün ist die Hoffnung',7,'humor');
    insert into `buecher` (`buchnr`,`titel`,`autorennr`,`kategorie`) values (11,'Der untröstliche Witwer von Montparnasse',8,'krimi');
    insert into `buecher` (`buchnr`,`titel`,`autorennr`,`kategorie`) values (12,'Das doppelte Lottchen',22,'kind');
    insert into `buecher` (`buchnr`,`titel`,`autorennr`,`kategorie`) values (19,'Das Schweigen der Lämmer',9,'krimi');
    insert into `buecher` (`buchnr`,`titel`,`autorennr`,`kategorie`) values (22,'Tiger,Panther&Co',29,'humor');
    insert into `buecher` (`buchnr`,`titel`,`autorennr`,`kategorie`) values (23,'Das Rad Der Zeit',30,'fan');
    insert into `buecher` (`buchnr`,`titel`,`autorennr`,`kategorie`) values (24,'Handbuch der experimentellen Physik',31,'humor');
    insert into `buecher` (`buchnr`,`titel`,`autorennr`,`kategorie`) values (25,'Helle Barden',28,'humor');
    insert into `buecher` (`buchnr`,`titel`,`autorennr`,`kategorie`) values (27,'Mord im Orient Express',32,'krimi');
    insert into `buecher` (`buchnr`,`titel`,`autorennr`,`kategorie`) values (28,'Otherland River of blue fire',33,'fan');

    DROP TABLE IF EXISTS `leser`;

    CREATE TABLE `leser` (
      `lesernr` INTEGER PRIMARY KEY AUTOINCREMENT,
      `name` char(20) default NULL,
      `vorname` char(20) default NULL,
      `gebdatum` date default NULL,
      `geschlecht` char(1) NOT NULL,
      `strasse` char(30) default NULL,
      `plz` int(5) default NULL,
      `ort` char(20) default NULL
    );

    insert into `leser` (`lesernr`,`name`,`vorname`,`gebdatum`,`geschlecht`,`strasse`,`plz`,`ort`) values (1,'Mustermann','Max','1965-04-01','m','Musterstr. 1',11111,'Musterdorf');
    insert into `leser` (`lesernr`,`name`,`vorname`,`gebdatum`,`geschlecht`,`strasse`,`plz`,`ort`) values (2,'Taler','Tim','1973-06-03','m','Kannengasse 6',15242,'Nudelsbach');
    insert into `leser` (`lesernr`,`name`,`vorname`,`gebdatum`,`geschlecht`,`strasse`,`plz`,`ort`) values (3,'Socke','Erna','1972-03-03','w','Strumpfgasse 7',13329,'Seidenstadt');
    insert into `leser` (`lesernr`,`name`,`vorname`,`gebdatum`,`geschlecht`,`strasse`,`plz`,`ort`) values (4,'Esel','Wilhelm','1928-01-17','m','Kaiserdamm 242',10986,'Residenzstadt');
    insert into `leser` (`lesernr`,`name`,`vorname`,`gebdatum`,`geschlecht`,`strasse`,`plz`,`ort`) values (5,'Pause','Lila','1992-12-24','w','Alpenweg 3',1232,'Bergstadt');
    insert into `leser` (`lesernr`,`name`,`vorname`,`gebdatum`,`geschlecht`,`strasse`,`plz`,`ort`) values (6,'Lupus','Georg','1963-04-18','m','Lammstrasse 36',64738,'Liebenburg');
    insert into `leser` (`lesernr`,`name`,`vorname`,`gebdatum`,`geschlecht`,`strasse`,`plz`,`ort`) values (7,'Radieschen','Ruth','1948-11-23','w','Trampelpfad 7',23443,'Gartenstadt');
    insert into `leser` (`lesernr`,`name`,`vorname`,`gebdatum`,`geschlecht`,`strasse`,`plz`,`ort`) values (8,'Tell','Wilhelm','1951-07-05','m','Apfelweg 23',62632,'Bogendorf');
    insert into `leser` (`lesernr`,`name`,`vorname`,`gebdatum`,`geschlecht`,`strasse`,`plz`,`ort`) values (9,'Ritter','Rudolph','1981-01-08','m','Kokosstraße 43',87172,'Burg');
    insert into `leser` (`lesernr`,`name`,`vorname`,`gebdatum`,`geschlecht`,`strasse`,`plz`,`ort`) values (10,'Hemd','Rosa','1991-04-05','w','Lotusweg 8',23443,'Gartenstadt');
    insert into `leser` (`lesernr`,`name`,`vorname`,`gebdatum`,`geschlecht`,`strasse`,`plz`,`ort`) values (11,'Müller','Tinchen','1988-07-07','w','Cautiusstr. 15',14444,'Berlin');
    insert into `leser` (`lesernr`,`name`,`vorname`,`gebdatum`,`geschlecht`,`strasse`,`plz`,`ort`) values (12,'Miller','Swetlana','1984-05-01','w','Tegler Weg',16598,'Berlin');
    insert into `leser` (`lesernr`,`name`,`vorname`,`gebdatum`,`geschlecht`,`strasse`,`plz`,`ort`) values (13,'Brosnan','Pierce','1957-04-30','m','Peterstr.5',12159,'Berlin');
    """)
verbindung.commit()
verbindung.close()
