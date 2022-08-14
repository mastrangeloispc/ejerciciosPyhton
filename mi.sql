CREATE DATABASE pelu_can;
use pelu_can;

CREATE TABLE Dueno (
DNI varchar(10) NOT NULL UNIQUE,
Nombre varchar(30) NOT NULL,
Apellido varchar(60) NOT NULL,
Telefono varchar(20) NOT NULL,
Direccion varchar(100) NOT NULL,
PRIMARY KEY (DNI)
);

CREATE TABLE Perro (
ID_Perro int NOT NULL UNIQUE,
Nombre varchar(50) NOT NULL,
Fecha_nac date NOT NULL,
Sexo varchar(10),
DNI_Dueno varchar(10) NOT NULL,
PRIMARY KEY (ID_Perro),
constraint fk_DNI_Dueno
foreign key (DNI_Dueno) references Dueno(DNI)
);

CREATE TABLE Historial (
ID_Historial int NOT NULL UNIQUE auto_increment,
Fecha date NOT NULL,
Perro int NOT NULL,
Descripcion varchar(255),
Monto float NOT NULL,
PRIMARY KEY (ID_Historial),
constraint fk_Perro
foreign key (Perro) references Perro (ID_Perro)
);

INSERT INTO Dueno(DNI, Nombre, Apellido, Telefono, Direccion) VALUES
("12345678", 'Edinson', 'Cavani', '12345', 'Barrio Pituco 123'),
("91011121", 'Luis', 'Suarez', '678910', 'Clasemedio 345'),
("14151617", 'Diego', 'Forlan', '111213', 'Piojo resucitado 321'),
("18192021", 'Georgian', 'De Arrascaeta', '14151617', 'Genocida con nombre de calle 32'),
("22232425", 'Darwin', 'Nunez', '18192021', 'Vecinos chusmas 654');

INSERT INTO Perro(ID_Perro, Nombre, Fecha_nac, Sexo, DNI_dueno) VALUES
(1, 'Lassie atado', '1976-08-30', 'Macho', "12345678"),
(2, 'Cara de Papa', '2008-05-04', 'Hembra', "22232425"),
(3, 'Preguntale', '2015-02-02', 'No binario', "91011121"),
(4, 'Snoopy', '1977-05-17', 'Macho', "18192021"),
(5, 'Santillan', '1940-11-12', 'Macho', "14151617");

INSERT INTO Historial(ID_Historial, Fecha, Perro, Descripcion, Monto) VALUES
(1, '2021-02-18', 5, 'Cuticulas', 1750.00),
(2, '2022-05-20', 1, 'Piercing en cuarta mama', 15200.30),
(3, '2021-07-15', 3, 'Tatuaje tribal', 9500.00 ),
(4, '2020-11-03', 2, 'Alisado de pelo (de caniche)', 1000.00),
(5, '2022-08-08', 4, 'Normalizacion de base de datos 3NF', 150.50);


# 8 -insertar un nuevo registro en la tabla Historial de un perro cuyo ID Perro es igual a 10.
insert into Historial values (10, "2022-08-14",25,"Corte de uñas",2000);
