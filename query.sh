#!/bin/bash
echo "Running query"
mysql -e "INSERT INTO zeeguu_test.user(id, email) VALUES(1, \"li@la.lo\");" -uroot
mysql -e "INSERT INTO zeeguu_test.session(id, user_id) VALUES(12345, 1);" -uroot
echo "Done running query"
