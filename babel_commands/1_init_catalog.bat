
set base_dir=wrap_py\transl
set l=ru_RU

if exist %base_dir%\translations\%l%\ (
    echo locale folder %l% exist! Delete first! && goto 1
)

set d=wrap_engine
setup.py init_catalog --domain=%d% --input-file=%base_dir%\%d%.pot --locale=%l% --output-dir=%base_dir%\translations\
set d=wrap_py
setup.py init_catalog --domain=%d% --input-file=%base_dir%\%d%.pot --locale=%l% --output-dir=%base_dir%\translations\

:1