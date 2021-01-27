set l=ru_RU

if exist transl\translations\%l%\ (
    echo locale folder %l% exist! Delete first! && goto 1
)

set d=wrap_engine
setup.py init_catalog --domain=%d% --input-file=transl\%d%.pot --locale=%l% --output-dir=transl\translations\
set d=wrap_py
setup.py init_catalog --domain=%d% --input-file=transl\%d%.pot --locale=%l% --output-dir=transl\translations\

:1