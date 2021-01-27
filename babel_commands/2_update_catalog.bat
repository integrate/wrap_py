set l=ru_RU

set d=wrap_engine
setup.py update_catalog --domain=%d% --input-file=transl\%d%.pot --locale=%l% --output-dir=transl\translations\

set d=wrap_py
setup.py update_catalog --domain=%d% --input-file=transl\%d%.pot --locale=%l% --output-dir=transl\translations\