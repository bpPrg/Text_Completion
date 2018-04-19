Importing snippets in aText
==============================
```
Open aText
Data > Import data > load_the_given_Latex.csv
  
Caveats:
============
  - Do dot use tab completion, original tab will be disabled, instead use "expand at delimiter". 
  - Do not use built-in dictionary wildy, it may bite you, eg. whic exapands to which, you can never type 'whichever'.
```  
    
## Usage
```bash
Usage:
tba = \boldsymbol{a}
bay = \boldsymbol{\alpha}
xxa = $a$
And so on.
```

**English Alphabet:**
```bash
Text            A               Bold            Dollar
-----------------------------------------------------------
Bold            tba             tba             tbax
Dollar          xxa             xxba            xxa
Script          say             say             sayx

tsb = tau script bold
```

**English Alphabet:**

```bash
Prefixes_y: Angle, Bold, Partial (a.y b.y p.y)
Suffixes  : Bar, Prime, Hat, Star, Tilde (b. p. h. s. t.)


Prefix/Suffix   A               Bold            Dollar         Bold Dollar
---------------------------------------------------------------------------
Angle           aay             aaby            aayx           aabyx
Bold            bay             bay             bayx           bayx    
Partial         pay             paby            payx           pabyx
----------------------------------------------------------------------------
Star            as              asb             asx            asbx
Bar             ab              abb             abx            abbx
dot             ad              adb             adx            adbx
Prime           ap              apb             apx            apbx
Hat             ah              ahb             ahx            ahbx
Tilde           at              atb             atx            atbx
Modulus         am              amb             amx            ambx
zero            a0              a0b             a0x            a0bx
one             a1              a1b             a1x            a1bx
two             a2              a2b             a2x            a2bx
three           a3              a3b             a3x            a3bx
```
    
 ## My configurations
 ![aText](aText.png)
 ![hotkeys](hotkeys.png)

