# awk

## Numbering and calculations

### Count lines ("wc -l")

    awk '{ field = $NF }; END{ print field }'

### Print the last field of each line

    awk '{ print $NF }'

### Print the last field of the last line

    awk '{ field = $NF }; END{ print field }'

### Print every line with more than 5 fields

    awk 'NF > 5'
    
    
