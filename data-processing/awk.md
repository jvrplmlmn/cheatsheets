# awk

## Number of calculations

### Print the last field of each line

  awk '{ print $NF }'

### Print the last field of the last line

  awk '{ field = $NF }; END{ print field }'
