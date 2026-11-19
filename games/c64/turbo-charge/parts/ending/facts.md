# Turbo Charge — ending sequence

The controller selects file `19-N0S` after the tenth stage. It pushes `$2FFF` before jumping to the loader, which returns to `$3000`. The ending program switches display pages and ultimately loads title file `00-N0S` with synthetic return address `$0EFF` at `$30E0`.
