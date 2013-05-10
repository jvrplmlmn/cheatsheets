# awk

## Numbering and calculations

#### Precede each line by its line number FOR THAT FILE (left alignment).

**Note:** Using a tab (\t) instead of space will preserve margins.
    awk '{print FNR "\t" $0}' files*

#### Precede each line by its line number FOR ALL FILES TOGETHER, with tab.
**Note:** Using a tab (\t) instead of space will preserve margins.
    awk '{print NR "\t" $0}' files*    
    
#### Count lines ("wc -l")
    awk '{ field = $NF }; END{ print field }'

#### Print the last field of each line
    awk '{ print $NF }'

#### Print the last field of the last line
    awk '{ field = $NF }; END{ print field }'

#### Print every line with more than 5 fields
    awk 'NF > 5'
    
#### Print every line with 3 fields
    awk 'NF == 3'
