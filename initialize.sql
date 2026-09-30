DROP TABLE IF EXISTS posts;
DROP TABLE IF EXISTS users;


CREATE TABLE users (
   user_id INT PRIMARY KEY,
   name VARCHAR(50),
   email VARCHAR(100),
   password VARCHAR(50)
);


CREATE TABLE posts (
   post_id INT PRIMARY KEY,
   user_id INT,
   title VARCHAR(100),
   text TEXT,
   created_at DATE,
   FOREIGN KEY (user_id) REFERENCES users(user_id)
);


INSERT INTO users (user_id, name, email, password) VALUES
(1, 'John Doe', 'johndoe@example.com', 'password123'),
(2, 'Bob Smith', 'bobsmith@example.com', 'password456'),
(3, 'Hannah Montana', 'hannahmontana@example.com', 'password789'),
(4, 'Jill Johnson', 'jilljohnson@example.com', 'password101'),
(5, 'Jack White', 'jackwhite@example.com', 'password111'),
(6, 'Emily Johnson', 'emilyjohnson@example.com', 'password122'),
(7, 'David Lee', 'davidlee@example.com', 'password133'),
(8, 'Sarah Brown', 'sarahbrown@example.com', 'password144'),
(9, 'Michael Green', 'michaelgreen@example.com', 'password155'),
(10, 'Olivia Davis', 'oliviadavis@example.com', 'password166');


INSERT INTO posts (post_id, user_id, title, text, created_at) VALUES
(1, 1, 'This is my first post', 'This is the text of my first post', '2026-01-01'),
(2, 2, 'This is my second post', 'This is the text of my second post', '2026-01-02'),
(3, 3, 'This is my third post', 'This is the text of my third post', '2026-01-03'),
(4, 4, 'This is my fourth post', 'This is the text of my fourth post', '2026-01-04'),
(5, 5, 'This is my fifth post', 'This is the text of my fifth post', '2026-01-05'),
(6, 6, 'This is my sixth post', 'This is the text of my sixth post', '2026-01-06'),
(7, 7, 'This is my seventh post', 'This is the text of my seventh post', '2026-01-07'),
(8, 8, 'This is my eighth post', 'This is the text of my eighth post', '2026-01-08'),
(9, 9, 'This is my ninth post', 'This is the text of my ninth post', '2026-01-09'),
(10, 10, 'This is my tenth post', 'This is the text of my tenth post', '2026-01-10');
