
set base_dir=wrap_py\transl
set l=ru_RU

set d=wrap_engine
setup.py update_catalog --domain=%d% --input-file=%base_dir%\%d%.pot --locale=%l% --output-dir=%base_dir%\translations\

set d=wrap_py
setup.py update_catalog --domain=%d% --input-file=%base_dir%\%d%.pot --locale=%l% --output-dir=%base_dir%\translations\