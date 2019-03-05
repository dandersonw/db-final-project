create table authors (
       id integer primary key autoincrement,
       author_name varchar(128) not null
);

create table series (
       id integer primary key autoincrement,
       series_name varchar(128) not null
);

create table series_author (
       author_id integer not null,
       series_id integer not null,
       primary key (author_id, series_id),
       foreign key (author_id) references authors (id) on delete restrict,
       foreign key (series_id) references series (id) on delete restrict
);

create table books (
       id integer primary key autoincrement,
       book_name varchar(128) not null
);

create table readinglists (
       id integer primary key autoincrement,
       readinglist_name varchar(128) not null
);

create table readinglist_book (
       readinglist_id integer not null,
       book_id integer not null,
       primary key (readinglist_id, book_id),
       foreign key (readinglist_id) references readinglists (id) on delete cascade,
       foreign key (book_id) references books (id) on delete cascade,
);

create table review (
       id integer primary key autoincrement,
       book_id integer not null,
       review_text text not null,
       rating float check (0<=rating<=5) not null,
       foreign key (book_id) references books (id) on delete cascade
);

