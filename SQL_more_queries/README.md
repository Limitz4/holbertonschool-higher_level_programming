# SQL: Advanced Queries and Database Permissions

## Overview

This project contains MySQL exercises focused on database users, access permissions, table constraints, relational queries, joins, subqueries, and aggregations. It combines basic database administration with more complex SQL data retrieval.

## Exercises by Topic

### User Accounts and Access Control

| File | Purpose |
| --- | --- |
| `0-privileges.sql` | Display MySQL grants for specified users. |
| `1-create_user.sql` | Create a database user with broad privileges. |
| `2-create_read_user.sql` | Create a user with read-only access to a database. |

### Schema Design and Constraints

| File | Purpose |
| --- | --- |
| `3-force_name.sql` | Create a table with a required name column. |
| `4-never_empty.sql` | Define a column with a default value. |
| `5-unique_id.sql` | Enforce uniqueness through a table constraint. |
| `6-states.sql` | Create a states table with an auto-incrementing primary key. |
| `7-cities.sql` | Create a cities table linked to states. |

### Queries and Data Relationships

| File | Purpose |
| --- | --- |
| `8-cities_of_california_subquery.sql` | Filter cities using a subquery. |
| `9-cities_by_state_join.sql` | Join cities and states to produce combined results. |
| `10-genre_id_by_show.sql` | Retrieve the genre IDs associated with TV shows. |
| `11-genre_id_all_shows.sql` | Include shows without associated genres. |
| `12-no_genre.sql` | Identify shows without a genre relationship. |
| `13-count_shows_by_genre.sql` | Aggregate the number of shows in each genre. |
| `14-my_genres.sql` | Retrieve the genres associated with the show *Dexter*. |
| `15-comedy_only.sql` | Filter shows by the Comedy genre. |
| `16-shows_by_genre.sql` | List shows and their genres using left joins. |

## Technologies

- MySQL 8.x
- SQL (DDL and DML)
- User and privilege management
- Constraints, primary and foreign keys
- Joins, subqueries, filtering, and aggregation

## Example Usage

Import or create the practice databases before running queries that depend on their tables. For the standalone table-creation exercise:

```bash
mysql -u root -p < 6-states.sql
```

For a query that depends on a pre-populated practice database:

```bash
mysql -u root -p hbtn_0d_tvshows < 16-shows_by_genre.sql
```

The second example assumes the TV-show practice database and its tables have already been imported.

## Skills Demonstrated

- Modeling relational data and table constraints.
- Understanding user grants and least-privilege concepts.
- Querying across multiple tables using joins and subqueries.
- Producing aggregate reports from related data.

## Safety Note

Some exercises create users or grant broad database privileges. Execute them only against a local disposable database or an authorized practice instance, never against a production MySQL server.

