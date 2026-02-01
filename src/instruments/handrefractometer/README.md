# HAND REFRACTOMETER

# Workflow
1. Open lid
2. Calibration
    1. drop aquades
    2. wipes
3. drop water sample
4. close lid
5. peek lense
    1. show meter
6. wipe 
7. calibration

# Docs

# Pseudo Code

```
IF instrument: Hand-refractometer is clicked
    THEN, load hand refracto UI and API
    IF "Open Lid" is clicked
        SET Closed Lid as "false"
        THEN, announce: "..."
    IF "Close Lid" is clicked
        SET Closed Lid as "true"
        THEN, announce: "..."
    IF "Calibration" is clicked
        CHECK if lid is open
            IF valid
                THEN, proceed
            ELSE (or IF lid is still closed)
                THEN, announce: "Lid is still closed"
        SET "Calibrated" as "true"
        SET "Wiped" as "false"
        THEN, announce: "Instrument calibrated succesfully! Value should be back to zero (0)"    
    IF "Wipe" is clicked
        CHECK if lid is open
            IF valid
                THEN, proceed
            ELSE (or IF lid is still closed)
                THEN, announce: "Lid is still closed"
        SET "Wiped" as "true"
        THEN, announce: "Lens wiped!"
    IF "Drop Water Sample" is clicked
        CHECK if "Calibrated" is "true"
            IF valid
                THEN, proceed
            ELSE
                THEN, announce: "Calibrate first!"
        SET "Sampled" as "true"
        SET "Wiped" as "false"
        SET "Calibrated" as "false"
        THEN, announce: "Water sampled!"
    IF "Peek" is clicked
        CHECK if lid is closed (Closed Lid is true)
            IF valid
                THEN, proceed
            ELSE
                THEN, announce: "Lid is still opened"
        CHECK if "Sampled" is "true"
            IF Valid
                THEN, proceed
            ELSE
                THEN, show zero for value
        THEN, show value
            SHOW VALUE
                MOVE image/pixel based on value
            
```

# What Do i Need?

- Template UI

    Jadi tombol2 tinggal buat di sebuah file, dan file utama tinggal pindahin tombol2 tersebut ke tempat yg sudah ada

- Codes that change and check boolean values

    "dont proceed to next step"

- Codes that make some image/pixel move based on value respective on something

