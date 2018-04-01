#!/bin/bash
echo "Running query"
mysql -e "INSERT INTO zeeguu_test.user(id, email, name, learned_language_id, native_language_id) VALUES(1, \"li@la.lo\", \"la\", 5, 4);" -uroot
mysql -e "INSERT INTO zeeguu_test.session(id, user_id) VALUES(12345, 1);" -uroot
echo "Done running query"
