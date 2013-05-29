-- --------------------------------------
-- Misc stuff about sessions, locks, etc.
-- --------------------------------------
-- References:
-- http://stackoverflow.com/questions/622289/how-to-check-oracle-database-for-long-running-queries



-- Locks
select
  object_name, 
  object_type, 
  session_id, 
  type,   	-- Type or system/user lock
  lmode,    	-- lock mode in which session holds lock
  request, 
  block, 
  ctime 		-- Time since current mode was granted
from
  v$locked_object,
  all_objects,
   v$lock
where
  v$locked_object.object_id = all_objects.object_id AND
  v$lock.id1 = all_objects.object_id AND
  v$lock.sid = v$locked_object.session_id
order by
  session_id, ctime desc, object_name
/


-- List all the waiting sessions
set pages 500 lines 200
col username format a16
col sid for 99999
select
  w.sid,
  s.serial#,
  p.spid,
  s.username,
  w.event,
  w.SECONDS_IN_WAIT,
  w.seq#,
  s.status
from
  v$session_wait w,
  v$session s,
  v$process p
where
  s.sid = w.sid and
  s.username is not null and
  s.paddr = p.addr
order by 6
/


-- Current sql statement associated to a SID (Session ID)
-- Asks for the SID
SELECT
  c.sid,
  d.piece,
  c.serial#,
  c.username,
  d.sql_text
FROM
  v$session c,
  v$sqltext d
WHERE
  c.sql_hash_value = d.hash_value and
  c.sid=&1
ORDER BY
  c.sid, d.piece
/

-- Current sql statement associated to a SPID (System PID)
-- Asks for the PSID
SELECT
  c.sid,
  d.piece,
  c.serial#,
  c.username,
  d.sql_text
FROM
  v$session c,
  v$sqltext d,
  v$process p
WHERE
  c.sql_hash_value = d.hash_value and
  p.addr = c.paddr and
  spid=&1
ORDER BY
  c.sid,
  d.piece
/
