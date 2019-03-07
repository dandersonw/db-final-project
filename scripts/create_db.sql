create table authors (
       id integer primary key auto_increment,
       author_name varchar(128) not null
);

create table series (
       id integer primary key auto_increment,
       series_name varchar(128) not null
);

create table series_author (
       series_id integer not null,
       author_id integer not null,
       primary key (author_id, series_id),
       foreign key (author_id) references authors (id) on delete restrict,
       foreign key (series_id) references series (id) on delete restrict
);

create table reading_status (
       id integer primary key auto_increment,
       status_name varchar(64)
);
insert into reading_status values (NULL, NULL);
insert into reading_status values (NULL, 'Want to Read');
insert into reading_status values (NULL, 'Reading');
insert into reading_status values (NULL, 'Read');

create table books (
       id integer primary key auto_increment,
       title varchar(128) not null,
       status integer default 1 references reading_status (id)
);

create table book_series (
       book_id integer not null,
       series_id integer not null,
       ordinal_position integer not null,
       primary key (series_id, book_id),
       foreign key (series_id) references series (id) on delete cascade,
       foreign key (book_id) references books (id) on delete cascade       
);

create table book_author (
       book_id integer not null,
       author_id integer not null,
       author_index integer not null, 
       check (0<=author_index),
       primary key (author_id, book_id),
       foreign key (author_id) references authors (id) on delete cascade,
       foreign key (book_id) references books (id) on delete cascade
);

create table readinglists (
       id integer primary key auto_increment,
       readinglist_name varchar(128) not null
);

create table readinglist_book (
       readinglist_id integer not null,
       book_id integer not null,
       primary key (readinglist_id, book_id),
       foreign key (readinglist_id) references readinglists (id) on delete cascade,
       foreign key (book_id) references books (id) on delete cascade
);

create table reviews (
       book_id integer not null,
       review_text text not null,
       rating decimal(2, 1) not null,
       check (0<=rating<=5),
       primary key (book_id),
       foreign key (book_id) references books (id) on delete cascade
);

create procedure check_rating (in rating decimal(2, 1))
begin
        if rating < 0 or rating > 5 then
           signal sqlstate '45000'
           set MESSAGE_TEXT = 'check constraint on reviews.rating failed';
        end if;
end;

create trigger reviews_before_insert before insert on reviews
for each row call check_rating(NEW.rating);


