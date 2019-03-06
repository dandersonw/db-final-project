insert into authors values
       (NULL, 'Haruki Murakami'),
       (NULL, 'Terry Pratchett'),
       (NULL, 'Neil Gaiman');

insert into series values (NULL, '1Q84');
insert into series_author values (1, 1);

insert into books values
       (NULL, '1Q84 Volume 1', 1),
       (NULL, '1Q84 Volume 2', 1),
       (NULL, '1Q84 Volume 3', 1),
       (NULL, '1Q84 Volume 4', 1),
       (NULL, 'Good Omens', 1);

insert into book_author values
       (1, 1, 1),
       (2, 1, 1),
       (3, 1, 1),
       (4, 1, 1),
       (5, 2, 1),
       (5, 3, 2);
