DROP TABLE IF EXISTS Customer;
CREATE TABLE Customer (
    ID_Customer INTEGER PRIMARY KEY AUTOINCREMENT,
    Social_Number VARCHAR(12) NOT NULL,
    Name VARCHAR(30) NOT NULL,
    Address VARCHAR(30) NOT NULL
);


DROP TABLE IF EXISTS Product;
CREATE TABLE Product (
    ID_Product INT NOT NULL PRIMARY KEY,
    Manufacturer VARCHAR(10) NOT NULL,
    Model VARCHAR(20) NOT NULL,
    Memory INT NOT NULL,
    Release_Year INT NOT NULL,
    Price INT NOT NULL
);

DROP TABLE IF EXISTS ShippingMethod;
CREATE TABLE ShippingMethod (
    ID_SM INT NOT NULL PRIMARY KEY,
    Shipper VARCHAR(15) NOT NULL,
    Type VARCHAR(6)
);

DROP TABLE IF EXISTS ShoppingCart;
CREATE TABLE ShoppingCart (
    ID_SC INT NOT NULL PRIMARY KEY,
    ID_Customer INT NOT NULL,
    Total_Price INT NOT NULL,
    FOREIGN KEY (ID_Customer) REFERENCES Customer (ID_Customer)
);

DROP TABLE IF EXISTS Orders;
CREATE TABLE Orders (
    ID_Order INT NOT NULL PRIMARY KEY,
    ID_SC INT NOT NULL,
    Shipping INT NOT NULL,
    Date VARCHAR(11) NOT NULL,
    FOREIGN KEY (ID_SC) REFERENCES ShoppingCart (ID_SC),
    FOREIGN KEY (Shipping) REFERENCES ShippingMethod (ID_SM)
);

DROP TABLE IF EXISTS ProductsInShoppingCart;
CREATE TABLE ProductsInShoppingCart (
    ShoppingCart INT NOT NULL,
    Product INT NOT NULL,
    FOREIGN KEY (ShoppingCart) REFERENCES ShoppingCart (ID_SC),
    FOREIGN KEY (Product) REFERENCES Product (ID_Product)
);



--Customer ID has no special pattern
INSERT INTO Customer (Social_Number, Name, Address)
VALUES
    ("398-10-XXXX", "Alphius Oliver", "Keskiortentie 8"),
    ("586-52-XXXX", "Shane Lug", "Mämminiementie 53"),
    ("264-45-XXXX", "Lina Mina", "Korkeakoulunkatu 66"),
    ("158-96-XXXX", "Cornélio Pietro", "Gesterbyntie 54"),
    ("464-96-XXXX", "Prochorus Trudie", "Piilostentie 97"),
    ("253-56-XXXX", "Dagmar Vesna", "Snellmaninkatu 83"),
    ("124-31-XXXX", "Tsetseg Krishna", "Ysitie 53"),
    ("038-53-XXXX", "Ameyalli Cléopâtre", "Otakaari 24"),
    ("415-72-XXXX", "Bérenger Theia", "Siikarannantie 86"),
    ("256-37-XXXX", "Secundinus Nebil", "Kiannonkatu 16"),
    ("189-15-XXXX", "Sequoyah Nina", "Ysitie 58"),
    ("463-26-XXXX", "Siva Bohuslav", "Kaarrostie 8"),
    ("533-50-XXXX", "Ptolemy Malachy", "Oijärventie 48"),
    ("562-61-XXXX", "Gorgi Lyubov", "Kartanomäenkatu 67"),
    ("703-90-XXXX", "Lempi Blagoslav", "Rautatienkatu 76"),
    ("394-84-XXXX", "Katelin Dragoș", "Kluuvikatu 72"),
    ("765-99-XXXX", "Bertrand Eva", "Kanslerinrinne 60"),
    ("311-33-XXXX", "Yiorgos Alethea", "Linnankatu 17"),
    ("400-98-XXXX", "Arsène Waman", "Sulkuvartijankatu 82"),
    ("232-48-XXXX", "Donata Guðlaug", "Tawastintie 41");



--ID_Product for tablets has pattern "11XX"
--ID_Product for phones has pattern "22XX"
INSERT INTO Product (ID_Product, Manufacturer, Model, Memory, Release_Year, Price)
VALUES
    (1101, "Apple", "iPad Air", "64", 2020, 600),
    (1102, "Apple", "iPad Air (1)", "32", 2020, 500),
    (1103, "Apple", "iPad Pro", "128", 2021, 800),
    (1104, "Apple", "iPad Pro (1)", "64", 2021, 650),
    (1105, "Apple", "iPad Mini", "64", 2021, 400),
    (1106, "Apple", "iPad Mini (1)", "32", 2021, 350),
    (1107, "Samsung", "Galaxy Tab S5E", "128", 2020, 250),
    (1108, "Samsung", "Galaxy Tab S5E (1)", "64", 2020, 225),
    (1109, "Microsoft", "Surface Pro 8", "128", 2019, 900),
    (1110, "Samsung", "Galaxy Tab S7 Plus", "64", 2019, 200),
    (1111, "Xiaomi", "Pad 5", "32", 2020, 150),
    (1112, "Samsung", "Galaxy Tab S6", "32", 2018, 100),
    (2201, "Apple", "iPhone 13 Pro", "128", 2021, 1100),
    (2202, "Apple", "iPhone 13", "64", 2021, 1000),
    (2203, "Apple", "iPhone 12 Pro", "128", 2019, 900),
    (2204, "Apple", "iPhone 12", "64", 2019, 850),
    (2205, "Apple", "iPhone 11 Pro", "128", 2018, 850),
    (2206, "Apple", "iPhone 11", "64", 2018, 800),
    (2207, "Asus", "ROG Phone 5s", "128", 2020, 1200),
    (2208, "Xiaomi", "Mix 4", "32", 2020, 400),
    (2209, "Xiaomi", "11T Pro", "128", 2021, 600),
    (2210, "Google", "Pixel 6", "64", 2020, 900),
    (2211, "Sony", "Xperia 5 III", "128", 2019, 450),
    (2212, "Motorola", "Edge 20 Pro", "32", 2018, 300),
    (2213, "Xiaomi", "11 Lite 5G NE", "16", 2021, 250),
    (2214, "Honor", "50", "64", 2020, 300),
    (2215, "Huawei", "Nova 9", "32", 2019, 200),
    (2216, "realme", "GT Neo 2", "64", 2020, 400);



--ID_SM has pattern "33XX"
INSERT INTO ShippingMethod (ID_SM, Shipper, Type)
VALUES
    (3301, "Posti", "Ground"),
    (3302, "Matkahuolto", "Ground"),
    (3303, "UPS", "Ship"),
    (3304, "DHL", "Plane"),
    (3305, "DB Schencker", "Ground");



--ID_SC has pattern "44XX"
INSERT INTO ShoppingCart (ID_SC, ID_Customer, Total_Price)
VALUES
    (4401, 1, 1100),
    (4402, 2, 600),
    (4403, 3, 850),
    (4404, 4, 2200),
    (4405, 5, 900),
    (4406, 6, 600),
    (4407, 7, 500),
    (4408, 8, 1100),
    (4409, 9, 1100),
    (4410, 10, 1200),
    (4411, 11, 1100),
    (4412, 12, 900),
    (4413, 13, 250),
    (4414, 14, 350),
    (4415, 15, 450);



--ID_Order has pattern "55XX"
INSERT INTO Orders (ID_Order, ID_SC, Shipping, Date)
VALUES
    (5501, 4401, 3301, "07/01/2019"),
    (5502, 4403, 3301, "16/03/2019"),
    (5503, 4402, 3301, "07/04/2019"),
    (5504, 4407, 3302, "18/07/2019"),
    (5505, 4408, 3301, "10/01/2020"),
    (5506, 4405, 3301, "05/09/2020"),
    (5507, 4411, 3304, "29/07/2021"),
    (5508, 4409, 3303, "08/12/2021"),
    (5509, 4410, 3301, "10/03/2022"),
    (5510, 4412, 3305, "16/10/2022");

INSERT INTO ProductsInShoppingCart (Shoppingcart, Product)
VALUES
    (4401, 2201),
    (4402, 1101),
    (4403, 1105),
    (4403, 2211),
    (4404, 2201),
    (4404, 2201),
    (4405, 1109),
    (4406, 2209),
    (4407, 1102),
    (4408, 2201),
    (4409, 2201),
    (4410, 1101),
    (4410, 1101),
    (4411, 1102),
    (4411, 1101),
    (4412, 2210),
    (4413, 2213),
    (4414, 1106),
    (4415, 1110),
    (4415, 1107);
