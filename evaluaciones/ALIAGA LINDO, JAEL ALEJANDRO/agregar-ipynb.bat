for /R "./" %%G in (*) do (
    if "%%~xG"=="" (
        ren "%%G" "%%~nG.ipynb"
    )
)