insert into authors values
       (NULL, 'Haruki Murakami'),
       (NULL, 'Terry Pratchett'),
       (NULL, 'Neil Gaiman'),
       (NULL, 'J.R.R. Tolkien');

insert into series values
       (NULL, '1Q84'),
       (NULL, 'The Lord of the Rings');
insert into series_author values
       (1, 1),
       (2, 4);

insert into books values
       (NULL, '1Q84 Volume 1', 1),
       (NULL, '1Q84 Volume 2', 1),
       (NULL, '1Q84 Volume 3', 1),
       (NULL, '1Q84 Volume 4', 1),
       (NULL, 'Good Omens', 1),
       (NULL, 'The Fellowship of the Ring', 1),
       (NULL, 'The Two Towers', 1),
       (NULL, 'The Return of the King', 1);

insert into book_author values
       (1, 1, 1),
       (2, 1, 1),
       (3, 1, 1),
       (4, 1, 1),
       (5, 2, 1),
       (5, 3, 2);

insert into book_series values
       (1, 1, 1),
       (2, 1, 2),
       (3, 1, 3),
       (4, 1, 4),
       (6, 2, 1),
       (7, 2, 2),
       (8, 2, 3);

insert into readinglists values
       (NULL, 'Fantasy');

insert into readinglist_book values
       (1, 5),
       (1, 6),
       (1, 7),
       (1, 8);

insert into reviews values
       (1, 'Intriguing.', 4.1),
       (2, 'Even more intriguing', 4.4);
