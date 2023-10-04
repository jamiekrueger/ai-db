import os

from db import create_table, create_connection
from schema import *


def insert_to_customers(conn):
    
    sql = """
        INSERT INTO customers VALUES
        (customerId, name, birthdate, gender) values (1, 'Skyler Thulborn', '2/2/1960', 'Male'),
        (customerId, name, birthdate, gender) values (2, 'Drew Pleasants', '7/16/1998', 'Male'),
        (customerId, name, birthdate, gender) values (3, 'Emmerich Biasioli', '12/2/1964', 'Male'),
        (customerId, name, birthdate, gender) values (4, 'Marlon Fuggle', '1/16/1999', 'Male'),
        (customerId, name, birthdate, gender) values (5, 'Pietro Keaveny', '3/1/1988', 'Male'),
        (customerId, name, birthdate, gender) values (6, 'Addie Crissil', '4/20/2007', 'Female'),
        (customerId, name, birthdate, gender) values (7, 'Cairistiona Beamond', '2/5/1966', 'Female'),
        (customerId, name, birthdate, gender) values (8, 'Nola Margetts', '5/27/1979', 'Female'),
        (customerId, name, birthdate, gender) values (9, 'Joane Viney', '12/15/1992', 'Female'),
        (customerId, name, birthdate, gender) values (10, 'Brynna Hayer', '6/14/1958', 'Female'),
        (customerId, name, birthdate, gender) values (11, 'Pippa Dubose', '11/9/1985', 'Female'),
        (customerId, name, birthdate, gender) values (12, 'Bob Hughlock', '2/23/1993', 'Male'),
        (customerId, name, birthdate, gender) values (13, 'Montgomery Pickhaver', '12/15/1966', 'Male'),
        (customerId, name, birthdate, gender) values (14, 'Andrew Bigadike', '12/21/1964', 'Male'),
        (customerId, name, birthdate, gender) values (15, 'Reid Ternouth', '1/28/1968', 'Male'),
        (customerId, name, birthdate, gender) values (16, 'Ichabod Pillinger', '12/28/1957', 'Male'),
        (customerId, name, birthdate, gender) values (17, 'Gaspar Ryson', '1/3/2007', 'Male'),
        (customerId, name, birthdate, gender) values (18, 'Suzette Yellow', '6/8/1972', 'Female'),
        (customerId, name, birthdate, gender) values (19, 'Nollie Eard', '7/21/1976', 'Male'),
        (customerId, name, birthdate, gender) values (20, 'Christoforo Finlay', '9/22/1985', 'Male'),
        (customerId, name, birthdate, gender) values (21, 'Olympia Falks', '6/6/1989', 'Female'),
        (customerId, name, birthdate, gender) values (22, 'Mickey Blaisdale', '8/30/1980', 'Male'),
        (customerId, name, birthdate, gender) values (23, 'Fredericka Palethorpe', '10/26/1967', 'Female'),
        (customerId, name, birthdate, gender) values (24, 'Arabele Medland', '2/28/1994', 'Female'),
        (customerId, name, birthdate, gender) values (25, 'Miguelita Shireff', '4/29/1978', 'Female'),
        (customerId, name, birthdate, gender) values (26, 'Ellynn Shuter', '4/3/2010', 'Female'),
        (customerId, name, birthdate, gender) values (27, 'Andi Clementi', '9/7/1981', 'Female'),
        (customerId, name, birthdate, gender) values (28, 'Kristyn Frazer', '6/6/1975', 'Female'),
        (customerId, name, birthdate, gender) values (29, 'Nickolas Proschek', '7/21/2010', 'Male'),
        (customerId, name, birthdate, gender) values (30, 'Adelbert Pfaff', '12/17/1967', 'Male'),
        (customerId, name, birthdate, gender) values (31, 'Desmond Djurkovic', '7/3/1970', 'Male'),
        (customerId, name, birthdate, gender) values (32, 'Tina McKane', '7/29/1993', 'Female'),
        (customerId, name, birthdate, gender) values (33, 'Quinlan Di Pietro', '5/18/1963', 'Male'),
        (customerId, name, birthdate, gender) values (34, 'Kerrie Mallalieu', '7/2/1996', 'Female'),
        (customerId, name, birthdate, gender) values (35, 'Tabatha Passfield', '10/31/2003', 'Female'),
        (customerId, name, birthdate, gender) values (36, 'Ronalda Rame', '7/6/1996', 'Female'),
        (customerId, name, birthdate, gender) values (37, 'Teri Sturm', '10/4/1975', 'Female'),
        (customerId, name, birthdate, gender) values (38, 'Catrina Heaney', '11/5/1991', 'Female'),
        (customerId, name, birthdate, gender) values (39, 'Alyce Gidley', '8/8/2011', 'Female'),
        (customerId, name, birthdate, gender) values (40, 'Glenden McGinty', '10/19/2014', 'Male'),
        (customerId, name, birthdate, gender) values (41, 'Berti Arnaudon', '8/21/1996', 'Male'),
        (customerId, name, birthdate, gender) values (42, 'Agnella Siehard', '10/12/2015', 'Female'),
        (customerId, name, birthdate, gender) values (43, 'Fabian Cucuzza', '1/18/1997', 'Male'),
        (customerId, name, birthdate, gender) values (44, 'Edwin Borthe', '3/20/1962', 'Male'),
        (customerId, name, birthdate, gender) values (45, 'Lanny Mansuer', '10/20/1995', 'Female'),
        (customerId, name, birthdate, gender) values (46, 'Guillema Dilger', '1/11/2010', 'Female'),
        (customerId, name, birthdate, gender) values (47, 'Wynne Skein', '9/17/1987', 'Female'),
        (customerId, name, birthdate, gender) values (48, 'Antonio Scrane', '9/4/1958', 'Male'),
        (customerId, name, birthdate, gender) values (49, 'Trace Cribbins', '4/2/2001', 'Male'),
        (customerId, name, birthdate, gender) values (50, 'Savina Onthank', '8/20/1966', 'Female'),
        (customerId, name, birthdate, gender) values (51, 'Lauritz Cranham', '5/30/2002', 'Male'),
        (customerId, name, birthdate, gender) values (52, 'Farra Gislebert', '4/7/1964', 'Female'),
        (customerId, name, birthdate, gender) values (53, 'Shae MacGiffin', '5/3/1978', 'Female'),
        (customerId, name, birthdate, gender) values (54, 'Mireielle Seagrave', '6/2/2001', 'Female'),
        (customerId, name, birthdate, gender) values (55, 'Oren Sisland', '8/2/1986', 'Male'),
        (customerId, name, birthdate, gender) values (56, 'Arabela Duckitt', '3/28/1994', 'Female'),
        (customerId, name, birthdate, gender) values (57, 'Eloisa Hoolaghan', '4/6/1977', 'Female'),
        (customerId, name, birthdate, gender) values (58, 'Xena Semor', '4/8/1979', 'Female'),
        (customerId, name, birthdate, gender) values (59, 'Deb Attreed', '5/24/1969', 'Female'),
        (customerId, name, birthdate, gender) values (60, 'Gina Dumke', '1/28/1998', 'Female'),
        (customerId, name, birthdate, gender) values (61, 'Ddene Greaterex', '9/4/1978', 'Female'),
        (customerId, name, birthdate, gender) values (62, 'Phillipe Hastie', '7/20/1961', 'Male'),
        (customerId, name, birthdate, gender) values (63, 'Jinny Port', '8/29/2005', 'Female'),
        (customerId, name, birthdate, gender) values (64, 'Hildy Lau', '7/31/2003', 'Female'),
        (customerId, name, birthdate, gender) values (65, 'Michaelina Bucke', '10/6/1975', 'Female'),
        (customerId, name, birthdate, gender) values (66, 'Hillier Norheny', '5/30/1958', 'Male'),
        (customerId, name, birthdate, gender) values (67, 'Fred Zealander', '3/31/1964', 'Female'),
        (customerId, name, birthdate, gender) values (68, 'Ferd Lehrmann', '9/2/2014', 'Male'),
        (customerId, name, birthdate, gender) values (69, 'Alix Pedroli', '10/8/1989', 'Female'),
        (customerId, name, birthdate, gender) values (70, 'Tirrell Crippen', '6/29/1985', 'Male'),
        (customerId, name, birthdate, gender) values (71, 'Eile Boston', '4/24/1962', 'Male'),
        (customerId, name, birthdate, gender) values (72, 'Brinn Margrett', '12/5/1968', 'Female'),
        (customerId, name, birthdate, gender) values (73, 'Amalea Bodiam', '10/10/2011', 'Female'),
        (customerId, name, birthdate, gender) values (74, 'Norby Chedzoy', '5/22/2010', 'Male'),
        (customerId, name, birthdate, gender) values (75, 'Marillin Petyt', '12/3/2005', 'Female'),
        (customerId, name, birthdate, gender) values (76, 'Joice McGarel', '2/2/1987', 'Female'),
        (customerId, name, birthdate, gender) values (77, 'Clementius Winnard', '2/25/1970', 'Male'),
        (customerId, name, birthdate, gender) values (78, 'Leone Hellyer', '8/16/1999', 'Female'),
        (customerId, name, birthdate, gender) values (79, 'Lawton Bartzen', '5/7/1981', 'Male'),
        (customerId, name, birthdate, gender) values (80, 'Curry Grayshon', '4/18/1964', 'Male'),
        (customerId, name, birthdate, gender) values (81, 'Averil Pirelli', '11/6/1988', 'Female'),
        (customerId, name, birthdate, gender) values (82, 'Gavin Heaker', '5/4/1980', 'Male'),
        (customerId, name, birthdate, gender) values (83, 'Rem Husby', '7/18/1966', 'Male'),
        (customerId, name, birthdate, gender) values (84, 'Wendy Stuckow', '2/21/1981', 'Female'),
        (customerId, name, birthdate, gender) values (85, 'Clayborne Quartley', '3/5/2005', 'Male'),
        (customerId, name, birthdate, gender) values (86, 'Timmy Cradduck', '11/18/1962', 'Male'),
        (customerId, name, birthdate, gender) values (87, 'Wallas Reynold', '4/6/1960', 'Male'),
        (customerId, name, birthdate, gender) values (88, 'Sibyl Oleszcuk', '7/5/1992', 'Female'),
        (customerId, name, birthdate, gender) values (89, 'Alaine Betteriss', '11/26/1963', 'Female'),
        (customerId, name, birthdate, gender) values (90, 'Thatcher Renol', '7/1/1959', 'Male'),
        (customerId, name, birthdate, gender) values (91, 'Jocko Shegog', '11/23/1980', 'Male'),
        (customerId, name, birthdate, gender) values (92, 'Eydie Barthod', '2/26/1982', 'Female'),
        (customerId, name, birthdate, gender) values (93, 'Donny Onn', '6/18/1985', 'Female'),
        (customerId, name, birthdate, gender) values (94, 'Claudette Lyddy', '7/31/1974', 'Female'),
        (customerId, name, birthdate, gender) values (95, 'Celina O''Kelly', '2/18/1968', 'Female'),
        (customerId, name, birthdate, gender) values (96, 'Ruthe Drakeley', '4/9/1981', 'Female'),
        (customerId, name, birthdate, gender) values (97, 'Levi McGaughey', '2/10/2014', 'Male'),
        (customerId, name, birthdate, gender) values (98, 'Ashby Crawforth', '5/8/1980', 'Male'),
        (customerId, name, birthdate, gender) values (99, 'Zacharie O''Heagertie', '5/12/2014', 'Male'),
        (customerId, name, birthdate, gender) values (100, 'Adams Waterman', '3/31/1982', 'Male');
    """

    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.lastrowid

def insert_to_games(conn):

    sql = """
        INSERT INTO games 
        (gameId, name, category, description, publisher, playtime, numPlayers) values (1, 'Sonsing', 'Card Game', '', 'Quatz', 32, 7),
        (gameId, name, category, description, publisher, playtime, numPlayers) values (2, 'Alphazap', 'Party Game', '', 'Aimbu', 53, 4),
        (gameId, name, category, description, publisher, playtime, numPlayers) values (3, 'Fix San', 'Space Exploration', '', 'Skynoodle', 58, 5),
        (gameId, name, category, description, publisher, playtime, numPlayers) values (4, 'Stringtough', 'Novel-based', '', 'Rhybox', 54, 6),
        (gameId, name, category, description, publisher, playtime, numPlayers) values (5, 'Zontrax', 'Fantasy', '', 'Skynoodle', 112, 5),
        (gameId, name, category, description, publisher, playtime, numPlayers) values (6, 'Stim', 'Party Game', '', 'Mymm', 36, 9),
        (gameId, name, category, description, publisher, playtime, numPlayers) values (7, 'Otcom', 'Card Game', '', 'Mymm', 76, 4),
        (gameId, name, category, description, publisher, playtime, numPlayers) values (8, 'Wrapsafe', 'Science Fiction', '', 'Rhybox', 36, 11),
        (gameId, name, category, description, publisher, playtime, numPlayers) values (9, 'Span', 'Spies/Secret Agents', '', 'Aimbu', 67, 9),
        (gameId, name, category, description, publisher, playtime, numPlayers) values (10, 'Cookley', 'Educational', '', 'Aimbu', 103, 5),
        (gameId, name, category, description, publisher, playtime, numPlayers) values (11, 'Oodle Smack', 'Horror', '', 'Skynoodle', 36, 8),
        (gameId, name, category, description, publisher, playtime, numPlayers) values (12, 'Regrant', 'Abstract Strategy', '', 'Quatz', 66, 6),
        (gameId, name, category, description, publisher, playtime, numPlayers) values (13, 'Sonair', 'Science Fiction', '', 'Quatz', 83, 12),
        (gameId, name, category, description, publisher, playtime, numPlayers) values (14, 'Lotlux', 'Spies/Secret Agents', '', 'Skynoodle', 92, 7),
        (gameId, name, category, description, publisher, playtime, numPlayers) values (15, 'Fintone', 'Card Game', '', 'Rhybox', 83, 9),
        (gameId, name, category, description, publisher, playtime, numPlayers) values (16, 'Job', 'Horror', '', 'Gabcube', 81, 10),
        (gameId, name, category, description, publisher, playtime, numPlayers) values (17, 'Prodder', 'Fantasy', '', 'Gabcube', 14, 3),
        (gameId, name, category, description, publisher, playtime, numPlayers) values (18, 'Temp', 'Novel-based', '', 'Mymm', 73, 4),
        (gameId, name, category, description, publisher, playtime, numPlayers) values (19, 'Home Ing', 'Card Game', '', 'Gabcube', 10, 4),
        (gameId, name, category, description, publisher, playtime, numPlayers) values (20, 'Duobam', 'Party Game', '', 'Gabcube', 43, 12),
        (gameId, name, category, description, publisher, playtime, numPlayers) values (21, 'Aerified', 'Space Exploration', '', 'Gabcube', 116, 12),
        (gameId, name, category, description, publisher, playtime, numPlayers) values (22, 'Stronghold', 'Abstract Strategy', '', 'Rhybox', 119, 12),
        (gameId, name, category, description, publisher, playtime, numPlayers) values (23, 'Magic in Malofe', 'Fantasy', '', 'Yadel', 63, 9),
        (gameId, name, category, description, publisher, playtime, numPlayers) values (24, 'Grub n Go', 'Card Game', '', 'Yadel', 7, 4),
        (gameId, name, category, description, publisher, playtime, numPlayers) values (25, 'Vento-San-Zap', 'Card Game', '', 'Yadel', 18, 4);
    """
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.lastrowid

def insert_to_inventory(conn):

    sql = """
        INSERT INTO inventory VALUES
        (gameId, price, quantity) values (1, '$8.48', 8),
        (gameId, price, quantity) values (2, '$25.63', 98),
        (gameId, price, quantity) values (3, '$21.94', 94),
        (gameId, price, quantity) values (4, '$43.48', 63),
        (gameId, price, quantity) values (5, '$29.47', 88),
        (gameId, price, quantity) values (6, '$42.38', 26),
        (gameId, price, quantity) values (7, '$17.66', 11),
        (gameId, price, quantity) values (8, '$20.02', 45),
        (gameId, price, quantity) values (9, '$35.29', 96),
        (gameId, price, quantity) values (10, '$34.56', 67),
        (gameId, price, quantity) values (11, '$36.42', 52),
        (gameId, price, quantity) values (12, '$49.04', 42),
        (gameId, price, quantity) values (13, '$24.97', 7),
        (gameId, price, quantity) values (14, '$7.85', 38),
        (gameId, price, quantity) values (15, '$25.44', 15),
        (gameId, price, quantity) values (16, '$9.85', 41),
        (gameId, price, quantity) values (17, '$28.87', 0),
        (gameId, price, quantity) values (18, '$33.12', 30),
        (gameId, price, quantity) values (19, '$42.04', 76),
        (gameId, price, quantity) values (20, '$21.73', 78),
        (gameId, price, quantity) values (21, '$44.15', 68),
        (gameId, price, quantity) values (22, '$10.76', 84),
        (gameId, price, quantity) values (23, '$5.44', 97),
        (gameId, price, quantity) values (24, '$24.63', 49),
        (gameId, price, quantity) values (25, '$17.57', 48);
    """
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.lastrowid

def insert_to_orders(conn):
    sql = """
        INSERT INTO orders VALUES
        (orderId, customerId, gameId) values (1, 54, 16),
        (orderId, customerId, gameId) values (2, 67, 18),
        (orderId, customerId, gameId) values (3, 59, 18),
        (orderId, customerId, gameId) values (4, 74, 6),
        (orderId, customerId, gameId) values (5, 7, 5),
        (orderId, customerId, gameId) values (6, 99, 5),
        (orderId, customerId, gameId) values (7, 14, 19),
        (orderId, customerId, gameId) values (8, 9, 2),
        (orderId, customerId, gameId) values (9, 8, 9),
        (orderId, customerId, gameId) values (10, 59, 11),
        (orderId, customerId, gameId) values (11, 30, 8),
        (orderId, customerId, gameId) values (12, 95, 17),
        (orderId, customerId, gameId) values (13, 80, 16),
        (orderId, customerId, gameId) values (14, 38, 11),
        (orderId, customerId, gameId) values (15, 71, 15),
        (orderId, customerId, gameId) values (16, 85, 1),
        (orderId, customerId, gameId) values (17, 2, 10),
        (orderId, customerId, gameId) values (18, 64, 22),
        (orderId, customerId, gameId) values (19, 35, 11),
        (orderId, customerId, gameId) values (20, 29, 5),
        (orderId, customerId, gameId) values (21, 4, 13),
        (orderId, customerId, gameId) values (22, 52, 23),
        (orderId, customerId, gameId) values (23, 49, 13),
        (orderId, customerId, gameId) values (24, 40, 11),
        (orderId, customerId, gameId) values (25, 64, 23),
        (orderId, customerId, gameId) values (26, 27, 15),
        (orderId, customerId, gameId) values (27, 16, 3),
        (orderId, customerId, gameId) values (28, 36, 3),
        (orderId, customerId, gameId) values (29, 75, 11),
        (orderId, customerId, gameId) values (30, 99, 17),
        (orderId, customerId, gameId) values (31, 34, 9),
        (orderId, customerId, gameId) values (32, 93, 23),
        (orderId, customerId, gameId) values (33, 13, 3),
        (orderId, customerId, gameId) values (34, 78, 11),
        (orderId, customerId, gameId) values (35, 33, 17),
        (orderId, customerId, gameId) values (36, 52, 2),
        (orderId, customerId, gameId) values (37, 94, 6),
        (orderId, customerId, gameId) values (38, 20, 25),
        (orderId, customerId, gameId) values (39, 46, 13),
        (orderId, customerId, gameId) values (40, 98, 3),
        (orderId, customerId, gameId) values (41, 24, 9),
        (orderId, customerId, gameId) values (42, 45, 17),
        (orderId, customerId, gameId) values (43, 24, 21),
        (orderId, customerId, gameId) values (44, 47, 24),
        (orderId, customerId, gameId) values (45, 67, 3),
        (orderId, customerId, gameId) values (46, 42, 14),
        (orderId, customerId, gameId) values (47, 62, 15),
        (orderId, customerId, gameId) values (48, 99, 19),
        (orderId, customerId, gameId) values (49, 7, 21),
        (orderId, customerId, gameId) values (50, 80, 17)
        (orderId, customerId, gameId) values (51, 60, 8),
        (orderId, customerId, gameId) values (52, 94, 17),
        (orderId, customerId, gameId) values (53, 64, 22),
        (orderId, customerId, gameId) values (54, 81, 6),
        (orderId, customerId, gameId) values (55, 69, 20),
        (orderId, customerId, gameId) values (56, 67, 16),
        (orderId, customerId, gameId) values (57, 43, 20),
        (orderId, customerId, gameId) values (58, 33, 6),
        (orderId, customerId, gameId) values (59, 18, 6),
        (orderId, customerId, gameId) values (60, 64, 14),
        (orderId, customerId, gameId) values (61, 21, 25),
        (orderId, customerId, gameId) values (62, 72, 18),
        (orderId, customerId, gameId) values (63, 5, 9),
        (orderId, customerId, gameId) values (64, 14, 5),
        (orderId, customerId, gameId) values (65, 26, 11),
        (orderId, customerId, gameId) values (66, 68, 23),
        (orderId, customerId, gameId) values (67, 54, 4),
        (orderId, customerId, gameId) values (68, 6, 2),
        (orderId, customerId, gameId) values (69, 58, 5),
        (orderId, customerId, gameId) values (70, 87, 23),
        (orderId, customerId, gameId) values (71, 55, 1),
        (orderId, customerId, gameId) values (72, 38, 20),
        (orderId, customerId, gameId) values (73, 99, 1),
        (orderId, customerId, gameId) values (74, 52, 23),
        (orderId, customerId, gameId) values (75, 49, 20),
        (orderId, customerId, gameId) values (76, 96, 17),
        (orderId, customerId, gameId) values (77, 100, 20),
        (orderId, customerId, gameId) values (78, 41, 13),
        (orderId, customerId, gameId) values (79, 43, 6),
        (orderId, customerId, gameId) values (80, 55, 5),
        (orderId, customerId, gameId) values (81, 3, 1),
        (orderId, customerId, gameId) values (82, 11, 4),
        (orderId, customerId, gameId) values (83, 63, 23),
        (orderId, customerId, gameId) values (84, 60, 3),
        (orderId, customerId, gameId) values (85, 6, 4),
        (orderId, customerId, gameId) values (86, 70, 14),
        (orderId, customerId, gameId) values (87, 77, 25),
        (orderId, customerId, gameId) values (88, 87, 19),
        (orderId, customerId, gameId) values (89, 25, 2),
        (orderId, customerId, gameId) values (90, 95, 25),
        (orderId, customerId, gameId) values (91, 46, 22),
        (orderId, customerId, gameId) values (92, 26, 21),
        (orderId, customerId, gameId) values (93, 52, 11),
        (orderId, customerId, gameId) values (94, 86, 9),
        (orderId, customerId, gameId) values (95, 1, 20),
        (orderId, customerId, gameId) values (96, 28, 6),
        (orderId, customerId, gameId) values (97, 79, 20),
        (orderId, customerId, gameId) values (98, 59, 4),
        (orderId, customerId, gameId) values (99, 77, 1),
        (orderId, customerId, gameId) values (100, 62, 23),
        (orderId, customerId, gameId) values (101, 53, 24),
        (orderId, customerId, gameId) values (102, 97, 2),
        (orderId, customerId, gameId) values (103, 26, 18),
        (orderId, customerId, gameId) values (104, 35, 8),
        (orderId, customerId, gameId) values (105, 6, 15),
        (orderId, customerId, gameId) values (106, 51, 9),
        (orderId, customerId, gameId) values (107, 21, 21),
        (orderId, customerId, gameId) values (108, 20, 24),
        (orderId, customerId, gameId) values (109, 69, 23),
        (orderId, customerId, gameId) values (110, 59, 23),
        (orderId, customerId, gameId) values (111, 21, 21),
        (orderId, customerId, gameId) values (112, 92, 11),
        (orderId, customerId, gameId) values (113, 16, 4),
        (orderId, customerId, gameId) values (114, 57, 18),
        (orderId, customerId, gameId) values (115, 75, 12),
        (orderId, customerId, gameId) values (116, 26, 16),
        (orderId, customerId, gameId) values (117, 55, 20),
        (orderId, customerId, gameId) values (118, 94, 2),
        (orderId, customerId, gameId) values (119, 9, 19),
        (orderId, customerId, gameId) values (120, 6, 16);
    """
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.lastrowid

def insert_to_reviews(conn):

    sql = """
        INSERT INTO reviews VALUES
        (reviewId, customerId, gameId, comment, rating) values (1, 54, 16, 'We had a lot of fun playing this at first, but the pieces are too easy to break so it is unplayable now. The game was great other than the brittle pieces.', 1.7),
        (reviewId, customerId, gameId, comment, rating) values (2, 67, 18, 'This is a fun game! After playing with family and friends I would definitely recommend it. There are several variants as well as customizable rules for hours of entertainment.', 4.2),
        (reviewId, customerId, gameId, comment, rating) values (3, 59, 18, 'It was a gift for my nephew visiting on labor day weekend. I had the package unopened for him. When he opened the item, all the wooden tokens were missing. No longer able to return. Disappointed with the purchase.', 1.2),
        (reviewId, customerId, gameId, comment, rating) values (4, 74, 6, '', 4.0),
        (reviewId, customerId, gameId, comment, rating) values (5, 7, 5, '', 3.5),
        (reviewId, customerId, gameId, comment, rating) values (6, 99, 5, 'Thiiiiis gaaaaaame issssssss toooooooo looooooooooong.', 1.9),
        (reviewId, customerId, gameId, comment, rating) values (7, 14, 19, '', 3.9),
        (reviewId, customerId, gameId, comment, rating) values (8, 9, 2, '', 2.0),
        (reviewId, customerId, gameId, comment, rating) values (9, 8, 9, 'What a waste of my money. Cute, but a waste. DO NOT BUY', 1.6),
        (reviewId, customerId, gameId, comment, rating) values (10, 59, 11, '', 3.1),
        (reviewId, customerId, gameId, comment, rating) values (11, 30, 8, 'It was a pretty cool game, but it seemed to take a lot longer than we planned, so if you play this be prepared to spend several hours more than it says on the box.', 1.8),
        (reviewId, customerId, gameId, comment, rating) values (12, 95, 17, '', 3.5),
        (reviewId, customerId, gameId, comment, rating) values (13, 80, 16, 'The game came with a bunch of pieces broken in the box, but we decided to still give it a try. Fun, but terrible pieces.', 1.6),
        (reviewId, customerId, gameId, comment, rating) values (14, 38, 11, '', 4.4),
        (reviewId, customerId, gameId, comment, rating) values (15, 71, 15, 'I ordered this with a few different games. Trying to relive my youth through memories of playing those games we all played. Theres nothing classic about this game. Why would you ruin a great game with this version? If I was an executive of Rhybox I would fire everyone who approved this.', 1.0),
        (reviewId, customerId, gameId, comment, rating) values (16, 85, 1, '', 4.1),
        (reviewId, customerId, gameId, comment, rating) values (17, 2, 10, '', 4.2),
        (reviewId, customerId, gameId, comment, rating) values (18, 64, 22, 'WAHT A WILD RIDE! We went on quite the rollercoaster playing this! I would say give it a try!', 2.9),
        (reviewId, customerId, gameId, comment, rating) values (19, 35, 11, '', 2.7),
        (reviewId, customerId, gameId, comment, rating) values (20, 29, 5, '', 1.9),
        (reviewId, customerId, gameId, comment, rating) values (21, 4, 13, '', 4.6),
        (reviewId, customerId, gameId, comment, rating) values (22, 52, 23, '', 3.2),
        (reviewId, customerId, gameId, comment, rating) values (23, 49, 13, '', 2.0),
        (reviewId, customerId, gameId, comment, rating) values (24, 40, 11, '', 2.4),
        (reviewId, customerId, gameId, comment, rating) values (25, 64, 23, '', 2.0),
        (reviewId, customerId, gameId, comment, rating) values (26, 27, 15, '', 1.5),
        (reviewId, customerId, gameId, comment, rating) values (27, 16, 3, '', 4.2),
        (reviewId, customerId, gameId, comment, rating) values (28, 36, 3, '', 3.3),
        (reviewId, customerId, gameId, comment, rating) values (29, 75, 11, '', 3.5),
        (reviewId, customerId, gameId, comment, rating) values (30, 99, 17, '', 3.9),
        (reviewId, customerId, gameId, comment, rating) values (31, 34, 9, 'I heard bad things about this game, but after playing it it is definitely one of my new favorites. The in depth and strategy to this game are well worth the price.', 4.7),
        (reviewId, customerId, gameId, comment, rating) values (32, 93, 23, '', 2.9),
        (reviewId, customerId, gameId, comment, rating) values (33, 13, 3, '', 1.7),
        (reviewId, customerId, gameId, comment, rating) values (34, 78, 11, '', 4.0),
        (reviewId, customerId, gameId, comment, rating) values (35, 33, 17, '', 2.5),
        (reviewId, customerId, gameId, comment, rating) values (36, 52, 2, '', 4.0),
        (reviewId, customerId, gameId, comment, rating) values (37, 94, 6, '', 2.6),
        (reviewId, customerId, gameId, comment, rating) values (38, 20, 25, '', 2.9),
        (reviewId, customerId, gameId, comment, rating) values (39, 46, 13, '', 2.6),
        (reviewId, customerId, gameId, comment, rating) values (40, 98, 3, '', 3.0),
        (reviewId, customerId, gameId, comment, rating) values (41, 24, 9, 'This is an absolute RIPOFF!!! DO NOT BUY!', 1.1),
        (reviewId, customerId, gameId, comment, rating) values (42, 45, 17, '', 2.4),
        (reviewId, customerId, gameId, comment, rating) values (43, 24, 21, '', 4.4),
        (reviewId, customerId, gameId, comment, rating) values (44, 47, 24, '', 2.1),
        (reviewId, customerId, gameId, comment, rating) values (45, 67, 3, '', 4.5),
        (reviewId, customerId, gameId, comment, rating) values (46, 42, 14, 'THIS IS THE BEST GAM I HAVE EVR PLAED!!! YOU SHULD PLAY IT TOO!!!', 5.0),
        (reviewId, customerId, gameId, comment, rating) values (47, 62, 15, '', 4.9),
        (reviewId, customerId, gameId, comment, rating) values (48, 99, 19, '', 4.0),
        (reviewId, customerId, gameId, comment, rating) values (49, 7, 21, '', 3.6),
        (reviewId, customerId, gameId, comment, rating) values (50, 80, 17, '', 3.2);
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


