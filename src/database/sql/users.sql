/* Lo primero que deben ejecutar es esto */
CREATE TABLE roles(
	id int PRIMARY KEY,
	rol varchar(20)
);

/* Lo segundo que deben ejecutar es esto */
CREATE TABLE users(
	id SERIAL PRIMARY KEY,
	name VARCHAR(100) not null,
	mail VARCHAR(100) not null,
	age int not null,
	rut int not null,
	password VARCHAR(200) not null,
	rol INTEGER REFERENCES roles(id)
);

/* COMANDO QUE PUEDEN SERVIR */

/* Eliminar la tabla users*/
DROP TABLE users;

/* Metodo para insertar manualmente valores, la CRUD ya tiene su metodo propio */
INSERT INTO roles (id, rol) VALUES (1, 'admin'), (2, 'especialista'), (3, 'paciente');

SELECT * FROM users;

INSERT INTO users (name, mail, age, rut, password,rol) VALUES ('javier campos','javier@gmail.com', 19, 216500113, 'hola1234', 1);

/*Ver el nombre junto al rol*/
SELECT users.name as users, roles.rol as roles from users join roles on users.rol = roles.id;

truncate table users;