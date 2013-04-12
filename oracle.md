# Oracle

## Index

### Major Data Dictionary view to manage Index

DBA view describes indexes on all tables in the database.
ALL view describes indexes on all tables accessible to the user.
USER view is restricted to indexes owned by the user.
Some columns in these views contain statistics that are generated by the DBMS_STATS package or ANALYZE statement.

    DBA_INDEXES
    ALL_INDEXES
    USER_INDEXES

These views describe the columns of indexes on tables. Some columns in these views contain statistics that are generated by the `DBMS_STATS` package or `ANALYZE` statement. `DBA_IND_EXPRESSIONS`

    DBA_IND_COLUMNS
    ALL_IND_COLUMNS
    USER_IND_COLUMNS

These views describe the expressions of function-based indexes on tables. `DBA_IND_STATISTICS`

    ALL_IND_EXPRESSIONS
    USER_IND_EXPRESSIONS

These views contain optimizer statistics for indexes.

`INDEX_STATS` Stores information from the last `ANALYZE INDEX…VALIDATE STRUCTURE` statement. `INDEX_HISTOGRAM` Stores information from the last `ANALYZE INDEX…VALIDATE STRUCTURE` statement. `V$OBJECT_USAGE` Contains index usage information produced by the `ALTER INDEX…MONITORING USAGE` functionality.

    ALL_IND_STATISTICS
    USER_IND_STATISTICS

### Identify unusable indexes

  select index_name, status, owner
  from all_indexes
  where status = 'UNUSABLE';

If indexes are partitioned, you might not see any UNUSABLE index, but indexes with a N/A status:

#### Check index status

  select distinct status from dba_indexes;

#### Check index partitions status

  select distinct status from dba_ind_partitions;

#### Check index sub-partitions status

  select distinct status from dba_ind_subpartitions;