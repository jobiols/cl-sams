#!/bin/sh
# correr localmente todos los tests
# ---------------------------------

BASE='/odoo_ar/odoo-13.0e/sams13e'

# restaurar la base de test vacia
cp $BASE/backup_dir/bkp_test/sams13e_test.zip $BASE/backup_dir/
oe --restore -d sams13e_test -c sams13e -f sams13e_test.zip --no-deactivate
rm $BASE/backup_dir/sams13e_test.zip

# correr los tests
sudo docker run --rm -it \
    -v $BASE/config:/opt/odoo/etc/ \
    -v $BASE/data_dir:/opt/odoo/data \
    -v $BASE/sources:/opt/odoo/custom-addons \
   --link pg-sams13e:db \
   jobiols/odoo-ent:13.0e -- --stop-after-init -d sams13e_test \
       -i project_key_improved
       # --test-enable
