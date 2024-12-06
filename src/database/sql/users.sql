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
    number int not null,
	age int not null,
	rut int not null,
	password VARCHAR(200),
	rol INTEGER REFERENCES roles(id) not null
);

/* Tabla medicos */
CREATE TABLE info_medico(
	id INTEGER REFERENCES users(id),
	especialidad varchar(255),
	foto varchar(255),
	descripcion varchar(400)
);

/* Tabla de las citas medicas */
create table citas_medicas(
	id_paciente INTEGER REFERENCES users(id) not null,
	fecha DATE,
	id_doctor INTEGER REFERENCES users(id) not null
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

/* ver info medicos */
SELECT u.name, im.especialidad, im.foto, im.descripcion FROM users u JOIN info_medico im ON u.id = im.id

truncate table users;