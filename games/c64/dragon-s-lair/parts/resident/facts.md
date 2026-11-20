# Resident facts

- The high-score shift at `$13E8–$13EA` copies the old fifth row from `$1544–$154E` to `$154F–$1559`. In the controlled insertion probe the descending store began at `$1559`.
- SID pattern termination decrements the repetition counter at `$C127`. With two remaining, stepping the conditional branch reached the pattern-pointer reload at `$C12B`. With one remaining, it reached the cue advance at `$C13E`. The parsed 1,198 note entries from the pattern pointers use indices through `$57`. A read watch fired on the final termination byte at `$CFF0`.
