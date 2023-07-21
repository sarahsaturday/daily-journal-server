CREATE TABLE Entries (
    id INTEGER PRIMARY KEY,
    concept TEXT,
    entry TEXT,
    mood_id INTEGER,
    date DATE,
    FOREIGN KEY(mood_id) REFERENCES Moods(id)
);

CREATE TABLE Moods (
    id INTEGER PRIMARY KEY,
    label TEXT
);

CREATE TABLE Tags (
    id INTEGER PRIMARY KEY,
    tag_name TEXT
);

CREATE TABLE Entry_tags (
    id INTEGER PRIMARY KEY,
    tag_id INTEGER,
    entry_id INTEGER,
    FOREIGN KEY(tag_id) REFERENCES Tags(id),
    FOREIGN KEY(entry_id) REFERENCES Entries(id)
);

INSERT INTO Moods (id, label) VALUES
(1, 'Happy'),
(2, 'Sad'),
(3, 'Angry'),
(4, 'Ok');

INSERT INTO Entries (id, concept, entry, mood_id, date) VALUES
(1, 'Javascript', 'I learned about loops today. They can be a lot of fun.\nI learned about loops today. They can be a lot of fun.\nI learned about loops today. They can be a lot of fun.', 1, '2021-09-15 10:10:47'),
(2, 'Python', 'Python is named after the Monty Python comedy group from the UK. Im sad because I thought it was named after the snake', 4, '2021-09-15 10:11:33'),
(3, 'Python', 'Why did it take so long for python to have a switch statement? It is much cleaner than if/elif blocks', 3, '2021-09-15 10:13:11'),
(4, 'Javascript', 'Dealing with Date is terrible. Why do you have to add an entire package just to format a date. It makes no sense.', 3, '2021-09-15 10:14:05');

INSERT INTO Tags (id, tag_name) VALUES
(1, 'Python'),
(2, 'JavaScript'),
(3, 'Programming'),
(4, 'Learning');

INSERT INTO Entry_tags (id, tag_id, entry_id) VALUES
(1, 1, 1),  -- Tag: Python, Entry: 1
(2, 2, 1),  -- Tag: JavaScript, Entry: 1
(3, 3, 1),  -- Tag: Programming, Entry: 1
(4, 1, 2),  -- Tag: Python, Entry: 2
(5, 4, 2),  -- Tag: Learning, Entry: 2
(6, 2, 3),  -- Tag: JavaScript, Entry: 3
(7, 3, 4);  -- Tag: Programming, Entry: 4