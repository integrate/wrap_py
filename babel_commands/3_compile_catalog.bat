set base_dir=wrap_py\transl
set l=ru_RU

if NOT EXIST %base_dir%\compiled\ (
    mkdir %base_dir%\compiled\
)

if NOT EXIST %base_dir%\compiled\%l% ( mkdir %base_dir%\compiled\%l% )
if NOT EXIST %base_dir%\compiled\%l%\LC_MESSAGES ( mkdir %base_dir%\compiled\%l%\LC_MESSAGES )

set d=wrap_engine
setup.py compile_catalog --domain=%d% --input-file=%base_dir%\translations\%l%\LC_MESSAGES\%d%.po --locale=%l% --directory=%base_dir%\compiled\
set d=wrap_py
setup.py compile_catalog --domain=%d% --input-file=%base_dir%\translations\%l%\LC_MESSAGES\%d%.po --locale=%l% --directory=%base_dir%\compiled\