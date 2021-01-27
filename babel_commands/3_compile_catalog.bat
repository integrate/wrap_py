if NOT EXIST transl\compiled\ (
    mkdir transl\compiled\
)

set l=ru_RU
if NOT EXIST transl\compiled\%l% ( mkdir transl\compiled\%l% )
if NOT EXIST transl\compiled\%l%\LC_MESSAGES ( mkdir transl\compiled\%l%\LC_MESSAGES )

set d=wrap_engine
setup.py compile_catalog --domain=%d% --input-file=transl\translations\%l%\LC_MESSAGES\%d%.po --locale=%l% --directory=transl\compiled\
set d=wrap_py
setup.py compile_catalog --domain=%d% --input-file=transl\translations\%l%\LC_MESSAGES\%d%.po --locale=%l% --directory=transl\compiled\