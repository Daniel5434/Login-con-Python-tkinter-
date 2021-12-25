create database AplicacionR;
use AplicacionR;

create table usuarios(
id int not null auto_increment,
nombre varchar(50),
contraseña varchar (50),
PRIMARY KEY(id)
);

select * from usuarios;