import os

from db import create_table, create_connection
from schema import *


def insert_to_customers(conn):
    sql = """
        INSERT INTO customers VALUES
        (1, 'Skyler Thulborn', '2/2/1960', 'Male'),
        (2, 'Drew Pleasants', '7/16/1998', 'Male'),
        (3, 'Emmerich Biasioli', '12/2/1964', 'Male'),
        (4, 'Marlon Fuggle', '1/16/1999', 'Male'),
        (5, 'Pietro Keaveny', '3/1/1988', 'Male'),
        (6, 'Addie Crissil', '4/20/2007', 'Female'),
        (7, 'Cairistiona Beamond', '2/5/1966', 'Female'),
        (8, 'Nola Margetts', '5/27/1979', 'Female'),
        (9, 'Joane Viney', '12/15/1992', 'Female'),
        (10, 'Brynna Hayer', '6/14/1958', 'Female'),
        (11, 'Pippa Dubose', '11/9/1985', 'Female'),
        (12, 'Bob Hughlock', '2/23/1993', 'Male'),
        (13, 'Montgomery Pickhaver', '12/15/1966', 'Male'),
        (14, 'Andrew Bigadike', '12/21/1964', 'Male'),
        (15, 'Reid Ternouth', '1/28/1968', 'Male'),
        (16, 'Ichabod Pillinger', '12/28/1957', 'Male'),
        (17, 'Gaspar Ryson', '1/3/2007', 'Male'),
        (18, 'Suzette Yellow', '6/8/1972', 'Female'),
        (19, 'Nollie Eard', '7/21/1976', 'Male'),
        (20, 'Christoforo Finlay', '9/22/1985', 'Male'),
        (21, 'Olympia Falks', '6/6/1989', 'Female'),
        (22, 'Mickey Blaisdale', '8/30/1980', 'Male'),
        (23, 'Fredericka Palethorpe', '10/26/1967', 'Female'),
        (24, 'Arabele Medland', '2/28/1994', 'Female'),
        (25, 'Miguelita Shireff', '4/29/1978', 'Female'),
        (26, 'Ellynn Shuter', '4/3/2010', 'Female'),
        (27, 'Andi Clementi', '9/7/1981', 'Female'),
        (28, 'Kristyn Frazer', '6/6/1975', 'Female'),
        (29, 'Nickolas Proschek', '7/21/2010', 'Male'),
        (30, 'Adelbert Pfaff', '12/17/1967', 'Male'),
        (31, 'Desmond Djurkovic', '7/3/1970', 'Male'),
        (32, 'Tina McKane', '7/29/1993', 'Female'),
        (33, 'Quinlan Di Pietro', '5/18/1963', 'Male'),
        (34, 'Kerrie Mallalieu', '7/2/1996', 'Female'),
        (35, 'Tabatha Passfield', '10/31/2003', 'Female'),
        (36, 'Ronalda Rame', '7/6/1996', 'Female'),
        (37, 'Teri Sturm', '10/4/1975', 'Female'),
        (38, 'Catrina Heaney', '11/5/1991', 'Female'),
        (39, 'Alyce Gidley', '8/8/2011', 'Female'),
        (40, 'Glenden McGinty', '10/19/2014', 'Male'),
        (41, 'Berti Arnaudon', '8/21/1996', 'Male'),
        (42, 'Agnella Siehard', '10/12/2015', 'Female'),
        (43, 'Fabian Cucuzza', '1/18/1997', 'Male'),
        (44, 'Edwin Borthe', '3/20/1962', 'Male'),
        (45, 'Lanny Mansuer', '10/20/1995', 'Female'),
        (46, 'Guillema Dilger', '1/11/2010', 'Female'),
        (47, 'Wynne Skein', '9/17/1987', 'Female'),
        (48, 'Antonio Scrane', '9/4/1958', 'Male'),
        (49, 'Trace Cribbins', '4/2/2001', 'Male'),
        (50, 'Savina Onthank', '8/20/1966', 'Female'),
        (51, 'Lauritz Cranham', '5/30/2002', 'Male'),
        (52, 'Farra Gislebert', '4/7/1964', 'Female'),
        (53, 'Shae MacGiffin', '5/3/1978', 'Female'),
        (54, 'Mireielle Seagrave', '6/2/2001', 'Female'),
        (55, 'Oren Sisland', '8/2/1986', 'Male'),
        (56, 'Arabela Duckitt', '3/28/1994', 'Female'),
        (57, 'Eloisa Hoolaghan', '4/6/1977', 'Female'),
        (58, 'Xena Semor', '4/8/1979', 'Female'),
        (59, 'Deb Attreed', '5/24/1969', 'Female'),
        (60, 'Gina Dumke', '1/28/1998', 'Female'),
        (61, 'Ddene Greaterex', '9/4/1978', 'Female'),
        (62, 'Phillipe Hastie', '7/20/1961', 'Male'),
        (63, 'Jinny Port', '8/29/2005', 'Female'),
        (64, 'Hildy Lau', '7/31/2003', 'Female'),
        (65, 'Michaelina Bucke', '10/6/1975', 'Female'),
        (66, 'Hillier Norheny', '5/30/1958', 'Male'),
        (67, 'Fred Zealander', '3/31/1964', 'Female'),
        (68, 'Ferd Lehrmann', '9/2/2014', 'Male'),
        (69, 'Alix Pedroli', '10/8/1989', 'Female'),
        (70, 'Tirrell Crippen', '6/29/1985', 'Male'),
        (71, 'Eile Boston', '4/24/1962', 'Male'),
        (72, 'Brinn Margrett', '12/5/1968', 'Female'),
        (73, 'Amalea Bodiam', '10/10/2011', 'Female'),
        (74, 'Norby Chedzoy', '5/22/2010', 'Male'),
        (75, 'Marillin Petyt', '12/3/2005', 'Female'),
        (76, 'Joice McGarel', '2/2/1987', 'Female'),
        (77, 'Clementius Winnard', '2/25/1970', 'Male'),
        (78, 'Leone Hellyer', '8/16/1999', 'Female'),
        (79, 'Lawton Bartzen', '5/7/1981', 'Male'),
        (80, 'Curry Grayshon', '4/18/1964', 'Male'),
        (81, 'Averil Pirelli', '11/6/1988', 'Female'),
        (82, 'Gavin Heaker', '5/4/1980', 'Male'),
        (83, 'Rem Husby', '7/18/1966', 'Male'),
        (84, 'Wendy Stuckow', '2/21/1981', 'Female'),
        (85, 'Clayborne Quartley', '3/5/2005', 'Male'),
        (86, 'Timmy Cradduck', '11/18/1962', 'Male'),
        (87, 'Wallas Reynold', '4/6/1960', 'Male'),
        (88, 'Sibyl Oleszcuk', '7/5/1992', 'Female'),
        (89, 'Alaine Betteriss', '11/26/1963', 'Female'),
        (90, 'Thatcher Renol', '7/1/1959', 'Male'),
        (91, 'Jocko Shegog', '11/23/1980', 'Male'),
        (92, 'Eydie Barthod', '2/26/1982', 'Female'),
        (93, 'Donny Onn', '6/18/1985', 'Female'),
        (94, 'Claudette Lyddy', '7/31/1974', 'Female'),
        (95, 'Celina O''Kelly', '2/18/1968', 'Female'),
        (96, 'Ruthe Drakeley', '4/9/1981', 'Female'),
        (97, 'Levi McGaughey', '2/10/2014', 'Male'),
        (98, 'Ashby Crawforth', '5/8/1980', 'Male'),
        (99, 'Zacharie O''Heagertie', '5/12/2014', 'Male'),
        (100, 'Adams Waterman', '3/31/1982', 'Male');
    """

    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.lastrowid


def insert_to_games(conn):
    sql = """
        INSERT INTO games VALUES
        (1, 'Sonsing', 'Card Game', '', 'Quatz', 32, 7),
        (2, 'Alphazap', 'Party Game', '', 'Aimbu', 53, 4),
        (3, 'Fix San', 'Space Exploration', '', 'Skynoodle', 58, 5),
        (4, 'Stringtough', 'Novel-based', '', 'Rhybox', 54, 6),
        (5, 'Zontrax', 'Fantasy', '', 'Skynoodle', 112, 5),
        (6, 'Stim', 'Party Game', '', 'Mymm', 36, 9),
        (7, 'Otcom', 'Card Game', '', 'Mymm', 76, 4),
        (8, 'Wrapsafe', 'Science Fiction', '', 'Rhybox', 36, 11),
        (9, 'Span', 'Spies/Secret Agents', '', 'Aimbu', 67, 9),
        (10, 'Cookley', 'Educational', '', 'Aimbu', 103, 5),
        (11, 'Oodle Smack', 'Horror', '', 'Skynoodle', 36, 8),
        (12, 'Regrant', 'Abstract Strategy', '', 'Quatz', 66, 6),
        (13, 'Sonair', 'Science Fiction', '', 'Quatz', 83, 12),
        (14, 'Lotlux', 'Spies/Secret Agents', '', 'Skynoodle', 92, 7),
        (15, 'Fintone', 'Card Game', '', 'Rhybox', 83, 9),
        (16, 'Job', 'Horror', '', 'Gabcube', 81, 10),
        (17, 'Prodder', 'Fantasy', '', 'Gabcube', 14, 3),
        (18, 'Temp', 'Novel-based', '', 'Mymm', 73, 4),
        (19, 'Home Ing', 'Card Game', '', 'Gabcube', 10, 4),
        (20, 'Duobam', 'Party Game', '', 'Gabcube', 43, 12),
        (21, 'Aerified', 'Space Exploration', '', 'Gabcube', 116, 12),
        (22, 'Stronghold', 'Abstract Strategy', '', 'Rhybox', 119, 12),
        (23, 'Magic in Malofe', 'Fantasy', '', 'Yadel', 63, 9),
        (24, 'Grub n Go', 'Card Game', '', 'Yadel', 7, 4),
        (25, 'Vento-San-Zap', 'Card Game', '', 'Yadel', 18, 4);
    """
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.lastrowid


def insert_to_inventory(conn):
    sql = """
        INSERT INTO inventory VALUES
        (1, '$8.48', 8),
        (2, '$25.63', 98),
        (3, '$21.94', 94),
        (4, '$43.48', 63),
        (5, '$29.47', 88),
        (6, '$42.38', 26),
        (7, '$17.66', 11),
        (8, '$20.02', 45),
        (9, '$35.29', 96),
        (10, '$34.56', 67),
        (11, '$36.42', 52),
        (12, '$49.04', 42),
        (13, '$24.97', 7),
        (14, '$7.85', 38),
        (15, '$25.44', 15),
        (16, '$9.85', 41),
        (17, '$28.87', 0),
        (18, '$33.12', 30),
        (19, '$42.04', 76),
        (20, '$21.73', 78),
        (21, '$44.15', 68),
        (22, '$10.76', 84),
        (23, '$5.44', 97),
        (24, '$24.63', 49),
        (25, '$17.57', 48);
    """
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.lastrowid


def insert_to_orders(conn):
    sql = """
        INSERT INTO orders VALUES
        (1, 54, 16),
        (2, 67, 18),
        (3, 59, 18),
        (4, 74, 6),
        (5, 7, 5),
        (6, 99, 5),
        (7, 14, 19),
        (8, 9, 2),
        (9, 8, 9),
        (10, 59, 11),
        (11, 30, 8),
        (12, 95, 17),
        (13, 80, 16),
        (14, 38, 11),
        (15, 71, 15),
        (16, 85, 1),
        (17, 2, 10),
        (18, 64, 22),
        (19, 35, 11),
        (20, 29, 5),
        (21, 4, 13),
        (22, 52, 23),
        (23, 49, 13),
        (24, 40, 11),
        (25, 64, 23),
        (26, 27, 15),
        (27, 16, 3),
        (28, 36, 3),
        (29, 75, 11),
        (30, 99, 17),
        (31, 34, 9),
        (32, 93, 23),
        (33, 13, 3),
        (34, 78, 11),
        (35, 33, 17),
        (36, 52, 2),
        (37, 94, 6),
        (38, 20, 25),
        (39, 46, 13),
        (40, 98, 3),
        (41, 24, 9),
        (42, 45, 17),
        (43, 24, 21),
        (44, 47, 24),
        (45, 67, 3),
        (46, 42, 14),
        (47, 62, 15),
        (48, 99, 19),
        (49, 7, 21),
        (50, 80, 17),
        (51, 60, 8),
        (52, 94, 17),
        (53, 64, 22),
        (54, 81, 6),
        (55, 69, 20),
        (56, 67, 16),
        (57, 43, 20),
        (58, 33, 6),
        (59, 18, 6),
        (60, 64, 14),
        (61, 21, 25),
        (62, 72, 18),
        (63, 5, 9),
        (64, 14, 5),
        (65, 26, 11),
        (66, 68, 23),
        (67, 54, 4),
        (68, 6, 2),
        (69, 58, 5),
        (70, 87, 23),
        (71, 55, 1),
        (72, 38, 20),
        (73, 99, 1),
        (74, 52, 23),
        (75, 49, 20),
        (76, 96, 17),
        (77, 100, 20),
        (78, 41, 13),
        (79, 43, 6),
        (80, 55, 5),
        (81, 3, 1),
        (82, 11, 4),
        (83, 63, 23),
        (84, 60, 3),
        (85, 6, 4),
        (86, 70, 14),
        (87, 77, 25),
        (88, 87, 19),
        (89, 25, 2),
        (90, 95, 25),
        (91, 46, 22),
        (92, 26, 21),
        (93, 52, 11),
        (94, 86, 9),
        (95, 1, 20),
        (96, 28, 6),
        (97, 79, 20),
        (98, 59, 4),
        (99, 77, 1),
        (100, 62, 23),
        (101, 53, 24),
        (102, 97, 2),
        (103, 26, 18),
        (104, 35, 8),
        (105, 6, 15),
        (106, 51, 9),
        (107, 21, 21),
        (108, 20, 24),
        (109, 69, 23),
        (110, 59, 23),
        (111, 21, 21),
        (112, 92, 11),
        (113, 16, 4),
        (114, 57, 18),
        (115, 75, 12),
        (116, 26, 16),
        (117, 55, 20),
        (118, 94, 2),
        (119, 9, 19),
        (120, 6, 16);
    """
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.lastrowid


def insert_to_reviews(conn):
    sql = """
        INSERT INTO reviews VALUES
        (1, 54, 16, 'We had a lot of fun playing this at first, but the pieces are too easy to break so it is unplayable now. The game was great other than the brittle pieces.', 1.7),
        (2, 67, 18, 'This is a fun game! After playing with family and friends I would definitely recommend it. There are several variants as well as customizable rules for hours of entertainment.', 4.2),
        (3, 59, 18, 'It was a gift for my nephew visiting on labor day weekend. I had the package unopened for him. When he opened the item, all the wooden tokens were missing. No longer able to return. Disappointed with the purchase.', 1.2),
        (4, 74, 6, '', 4.0),
        (5, 7, 5, '', 3.5),
        (6, 99, 5, 'Thiiiiis gaaaaaame issssssss toooooooo looooooooooong.', 1.9),
        (7, 14, 19, '', 3.9),
        (8, 9, 2, '', 2.0),
        (9, 8, 9, 'What a waste of my money. Cute, but a waste. DO NOT BUY', 1.6),
        (10, 59, 11, '', 3.1),
        (11, 30, 8, 'It was a pretty cool game, but it seemed to take a lot longer than we planned, so if you play this be prepared to spend several hours more than it says on the box.', 1.8),
        (12, 95, 17, '', 3.5),
        (13, 80, 16, 'The game came with a bunch of pieces broken in the box, but we decided to still give it a try. Fun, but terrible pieces.', 1.6),
        (14, 38, 11, '', 4.4),
        (15, 71, 15, 'I ordered this with a few different games. Trying to relive my youth through memories of playing those games we all played. Theres nothing classic about this game. Why would you ruin a great game with this version? If I was an executive of Rhybox I would fire everyone who approved this.', 1.0),
        (16, 85, 1, '', 4.1),
        (17, 2, 10, '', 4.2),
        (18, 64, 22, 'WAHT A WILD RIDE! We went on quite the rollercoaster playing this! I would say give it a try!', 2.9),
        (19, 35, 11, '', 2.7),
        (20, 29, 5, '', 1.9),
        (21, 4, 13, '', 4.6),
        (22, 52, 23, '', 3.2),
        (23, 49, 13, '', 2.0),
        (24, 40, 11, '', 2.4),
        (25, 64, 23, '', 2.0),
        (26, 27, 15, '', 1.5),
        (27, 16, 3, '', 4.2),
        (28, 36, 3, '', 3.3),
        (29, 75, 11, '', 3.5),
        (30, 99, 17, '', 3.9),
        (31, 34, 9, 'I heard bad things about this game, but after playing it it is definitely one of my new favorites. The in depth and strategy to this game are well worth the price.', 4.7),
        (32, 93, 23, '', 2.9),
        (33, 13, 3, '', 1.7),
        (34, 78, 11, '', 4.0),
        (35, 33, 17, '', 2.5),
        (36, 52, 2, '', 4.0),
        (37, 94, 6, '', 2.6),
        (38, 20, 25, '', 2.9),
        (39, 46, 13, '', 2.6),
        (40, 98, 3, '', 3.0),
        (41, 24, 9, 'This is an absolute RIPOFF!!! DO NOT BUY!', 1.1),
        (42, 45, 17, '', 2.4),
        (43, 24, 21, '', 4.4),
        (44, 47, 24, '', 2.1),
        (45, 67, 3, '', 4.5),
        (46, 42, 14, 'THIS IS THE BEST GAM I HAVE EVR PLAED!!! YOU SHULD PLAY IT TOO!!!', 5.0),
        (47, 62, 15, '', 4.9),
        (48, 99, 19, '', 4.0),
        (49, 7, 21, '', 3.6),
        (50, 80, 17, '', 3.2);
    """
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.lastrowid


def main():
    database = "./pythonsqlite.db"

    # create a database connection
    conn = create_connection(database)
    create_table(conn, sql_create_customers_table)
    insert_to_customers(conn)
    create_table(conn, sql_create_games_table)
    insert_to_games(conn)
    create_table(conn, sql_create_inventory_table)
    insert_to_inventory(conn)
    create_table(conn, sql_create_orders_table)
    insert_to_orders(conn)
    create_table(conn, sql_create_reviews_table)
    insert_to_reviews(conn)

    print("Database build successful!")


if __name__ == "__main__":
    main()
